"""Run with python -m backend.app; local single-user JSON API."""
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

from backend import service, storage


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(
        DATABASE=os.environ.get("TASKTRACK_DATABASE", str(Path(__file__).resolve().parents[1] / "data/tasktrack.sqlite3")),
        TIMEZONE=os.environ.get("TASKTRACK_TIMEZONE", "America/Chicago"),
        NOW=lambda: datetime.now(timezone.utc), MAX_CONTENT_LENGTH=64 * 1024,
    )
    app.config.update(config or {})
    ZoneInfo(app.config["TIMEZONE"])  # Fail startup clearly for an invalid zone.
    storage.initialize(app)

    @app.before_request
    def local_boundary():
        if request.host.split(":")[0] not in ("localhost", "127.0.0.1"):
            raise service.ApiError("invalid_host", "Use the local TaskTrack address.", 403)
        origin = request.headers.get("Origin")
        if origin and origin != request.host_url.rstrip("/"):
            raise service.ApiError("invalid_origin", "Use the same origin as the API.", 403)

    @app.after_request
    def headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Cache-Control"] = "no-store"
        return response

    @app.errorhandler(service.ApiError)
    def api_error(error):
        return jsonify(error={"code": error.code, "message": error.message, "fields": error.fields}), error.status

    @app.errorhandler(sqlite3.DatabaseError)
    def database_error(error):
        app.logger.error("Storage operation failed: %s", error)
        return jsonify(error={"code": "storage_unavailable", "message": "Could not load or save data. Keep your form and retry.", "fields": {}}), 503

    @app.errorhandler(HTTPException)
    def http_error(error):
        return jsonify(error={"code": "http_error", "message": error.description, "fields": {}}), error.code

    @app.get("/api/health")
    def health():
        storage.database().execute("SELECT count(*) FROM users").fetchone()
        return jsonify(data={"status": "ok", "mode": "single-user", "timezone": app.config["TIMEZONE"]})

    @app.route("/api/courses", methods=["GET", "POST"])
    def courses():
        if request.method == "POST":
            return jsonify(data=service.create_course(request.get_json())), 201
        return jsonify(data=[dict(row) for row in storage.database().execute("SELECT * FROM courses ORDER BY name COLLATE NOCASE, id")])

    @app.route("/api/courses/<int:identifier>", methods=["PUT", "DELETE"])
    def course(identifier):
        if request.method == "PUT":
            return jsonify(data=service.update_course(identifier, request.get_json()))
        service.delete("courses", identifier, request.args.get("confirmed"))
        return "", 204

    @app.route("/api/assignments", methods=["GET", "POST"])
    def assignment_list():
        if request.method == "POST":
            return jsonify(data=service.create_assignment(request.get_json())), 201
        unknown = request.args.keys() - {"course_id", "status"}
        if unknown:
            service.invalid(next(iter(unknown)), "Unknown filter.")
        return jsonify(data=service.assignments(request.args.get("course_id"), request.args.get("status")))

    @app.route("/api/assignments/<int:identifier>", methods=["GET", "PUT", "DELETE"])
    def assignment(identifier):
        if request.method == "GET":
            return jsonify(data=service.assignment(identifier))
        if request.method == "PUT":
            return jsonify(data=service.update_assignment(identifier, request.get_json()))
        service.delete("assignments", identifier, request.args.get("confirmed"))
        return "", 204

    @app.patch("/api/assignments/<int:identifier>/status")
    def status(identifier):
        return jsonify(data=service.set_status(identifier, request.get_json()))

    @app.get("/api/dashboard")
    def dashboard():
        return jsonify(data=service.dashboard())

    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=False)
