"""Validation and course/assignment/dashboard application services."""
import re
from datetime import date, datetime, time, timezone
from zoneinfo import ZoneInfo

from flask import current_app

from backend.storage import database


class ApiError(Exception):
    def __init__(self, code, message, status=400, fields=None):
        self.code, self.message, self.status = code, message, status
        self.fields = fields or {}


def invalid(field, message):
    raise ApiError("validation_error", "Check the highlighted fields.", fields={field: message})


def payload(data, allowed, required=()):
    if not isinstance(data, dict):
        raise ApiError("invalid_json", "Send a JSON object.")
    for field in data.keys() - set(allowed):
        invalid(field, "Unknown field.")
    for field in required:
        if field not in data:
            invalid(field, "Required field.")
    return data


def text(data, field, maximum, required=False):
    value = data.get(field, "")
    if not isinstance(value, str):
        invalid(field, "Must be text.")
    value = value.strip()
    if required and not value:
        invalid(field, "Required field.")
    if len(value) > maximum:
        invalid(field, f"Use at most {maximum} characters.")
    return value


def record(table, identifier):
    # table is a constant selected by the routes, never request input.
    row = database().execute(f"SELECT * FROM {table} WHERE id = ?", (identifier,)).fetchone()
    if row is None:
        raise ApiError("not_found", "Record no longer exists. Refresh the list.", 404)
    return dict(row)


def course_values(data):
    payload(data, {"name", "code"}, {"name"})
    return text(data, "name", 120, True), text(data, "code", 30)


def create_course(data):
    values = course_values(data)
    db = database()
    with db:
        identifier = db.execute("INSERT INTO courses(name, code) VALUES (?, ?)", values).lastrowid
    return record("courses", identifier)


def update_course(identifier, data):
    record("courses", identifier)
    values = course_values(data)
    db = database()
    with db:
        db.execute("UPDATE courses SET name = ?, code = ? WHERE id = ?", (*values, identifier))
    return record("courses", identifier)


def deadline(data):
    raw_date, raw_time = data.get("due_date"), data.get("due_time")
    try:
        if not isinstance(raw_date, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw_date):
            raise ValueError
        parsed_date = date.fromisoformat(raw_date)
    except ValueError:
        invalid("due_date", "Use a valid calendar date: YYYY-MM-DD.")
    if raw_time is not None and (not isinstance(raw_time, str) or not re.fullmatch(r"\d{2}:\d{2}", raw_time)):
        invalid("due_time", "Use HH:MM or null for 23:59.")
    try:
        parsed_time = time.fromisoformat(raw_time or "23:59")
    except ValueError:
        invalid("due_time", "Use a valid 24-hour time: HH:MM.")
    zone = ZoneInfo(current_app.config["TIMEZONE"])
    local = datetime.combine(parsed_date, parsed_time, zone)
    utc = local.astimezone(timezone.utc)
    if utc.astimezone(zone).replace(tzinfo=None) != local.replace(tzinfo=None):
        invalid("due_time", "This local time does not exist because of a clock change.")
    return utc.isoformat().replace("+00:00", "Z")


def assignment_values(data):
    payload(data, {"title", "course_id", "description", "due_date", "due_time", "task_type"},
            {"title", "course_id", "due_date"})
    title = text(data, "title", 200, True)
    course_id = data["course_id"]
    if type(course_id) is not int or course_id < 1:
        invalid("course_id", "Select an existing course.")
    if database().execute("SELECT id FROM courses WHERE id = ?", (course_id,)).fetchone() is None:
        invalid("course_id", "Select an existing course.")
    deadline(data)
    task_type = data.get("task_type", "Assignment")
    if task_type not in ("Assignment", "Quiz", "Exam"):
        invalid("task_type", "Choose Assignment, Quiz, or Exam.")
    return (course_id, title, text(data, "description", 5000), data["due_date"],
            data.get("due_time"), task_type)


def create_assignment(data):
    values = assignment_values(data)
    db = database()
    with db:
        identifier = db.execute(
            "INSERT INTO assignments(course_id,title,description,due_date,due_time,task_type) "
            "VALUES (?,?,?,?,?,?)", values).lastrowid
    return assignment(identifier)


def update_assignment(identifier, data):
    record("assignments", identifier)
    values = assignment_values(data)
    db = database()
    with db:
        db.execute("UPDATE assignments SET course_id=?,title=?,description=?,due_date=?,due_time=?,task_type=? "
                   "WHERE id=?", (*values, identifier))
    return assignment(identifier)


def now():
    return current_app.config["NOW"]().astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def present(row, evaluated_at):
    row = dict(row)
    row["due_at"] = deadline(row)
    row["overdue"] = row["status"] == "Pending" and datetime.fromisoformat(row["due_at"]) < datetime.fromisoformat(evaluated_at)
    return row


def assignment(identifier):
    row = database().execute(
        "SELECT a.*, c.name AS course_name, c.code AS course_code FROM assignments a "
        "JOIN courses c ON c.id=a.course_id WHERE a.id=?", (identifier,)).fetchone()
    if row is None:
        raise ApiError("not_found", "Assignment no longer exists. Refresh the list.", 404)
    return present(row, now())


def assignments(course_id=None, status=None, evaluated_at=None):
    if status not in (None, "Pending", "Completed", "Overdue"):
        invalid("status", "Choose Pending, Completed, or Overdue.")
    if course_id is not None:
        if not re.fullmatch(r"[1-9]\d*", course_id):
            invalid("course_id", "Use a positive course ID.")
        course_id = int(course_id)
        record("courses", course_id)
    clock = evaluated_at or now()
    rows = database().execute(
        "SELECT a.*, c.name AS course_name, c.code AS course_code FROM assignments a "
        "JOIN courses c ON c.id=a.course_id").fetchall()
    result = [present(row, clock) for row in rows]
    result = [row for row in result if (course_id is None or row["course_id"] == course_id)
              and (status is None or row["status"] == status or (status == "Overdue" and row["overdue"]))]
    return sorted(result, key=lambda row: (row["due_at"], row["title"].casefold(), row["id"]))


def set_status(identifier, data):
    payload(data, {"status"}, {"status"})
    if data["status"] not in ("Pending", "Completed"):
        invalid("status", "Choose Pending or Completed.")
    record("assignments", identifier)
    db = database()
    with db:
        db.execute("UPDATE assignments SET status=? WHERE id=?", (data["status"], identifier))
    return assignment(identifier)


def delete(table, identifier, confirmed):
    if confirmed != "true":
        raise ApiError("confirmation_required", "Confirm deletion before sending confirmed=true.")
    record(table, identifier)
    db = database()
    with db:
        db.execute("BEGIN IMMEDIATE")
        if table == "courses" and db.execute("SELECT 1 FROM assignments WHERE course_id=? LIMIT 1", (identifier,)).fetchone():
            raise ApiError("conflict", "Course still has assignments. Move or delete them first.", 409)
        db.execute(f"DELETE FROM {table} WHERE id=?", (identifier,))


def dashboard():
    clock = now()
    rows = assignments(evaluated_at=clock)
    pending = [row for row in rows if row["status"] == "Pending"]
    return {"pending": len(pending), "completed": len(rows) - len(pending),
            "overdue": sum(row["overdue"] for row in pending),
            "next_due": pending[:5], "evaluated_at": clock,
            "timezone": current_app.config["TIMEZONE"]}
