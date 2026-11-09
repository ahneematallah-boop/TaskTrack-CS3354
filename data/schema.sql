PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    display_name TEXT NOT NULL
);
INSERT OR IGNORE INTO users (id, display_name) VALUES (1, 'Local student');
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL DEFAULT 1 REFERENCES users(id) ON DELETE RESTRICT,
    name TEXT NOT NULL CHECK(length(trim(name)) BETWEEN 1 AND 120),
    code TEXT NOT NULL DEFAULT '' CHECK(length(code) <= 30)
);
CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE RESTRICT,
    title TEXT NOT NULL CHECK(length(trim(title)) BETWEEN 1 AND 200),
    description TEXT NOT NULL DEFAULT '' CHECK(length(description) <= 5000),
    due_date TEXT NOT NULL,
    due_time TEXT,
    task_type TEXT NOT NULL DEFAULT 'Assignment'
        CHECK(task_type IN ('Assignment', 'Quiz', 'Exam')),
    status TEXT NOT NULL DEFAULT 'Pending' CHECK(status IN ('Pending', 'Completed'))
);
CREATE INDEX IF NOT EXISTS assignments_course_id ON assignments(course_id);
