"""SQLite connections and transaction boundary; no browser access to the file."""
import sqlite3
from pathlib import Path

from flask import current_app, g


def database():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"], timeout=5)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def initialize(app):
    path = Path(app.config["DATABASE"])
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as connection:
        connection.executescript(
            (Path(__file__).resolve().parents[1] / "data/schema.sql").read_text()
        )

    @app.teardown_appcontext
    def close_database(_error):
        connection = g.pop("db", None)
        if connection is not None:
            connection.close()
