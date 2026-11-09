# Frontend integration boundary

Person 6 owns the dashboard, assignments, courses, assignment form, and screenshots. This directory reserves that layer; screens are not implemented by the backend contribution.

Use the [API contract](../docs/api.md) and [architecture](../docs/architecture.md). For local development, configure the frontend server to proxy `/api` to `http://127.0.0.1:5000`. The browser calls relative `/api/...` URLs; cross-origin requests are rejected by the backend. A standalone page opened as a `file://` URL is not the integrated application.

Render user-entered title, description, and course names as text (`textContent` in vanilla JavaScript). Keep form input after failed saves, disable Save while a write is pending, and show field errors from `error.fields`. Ask for confirmation before DELETE. After each successful mutation, reload the visible assignment list and dashboard; preserve current filters. Refresh on page focus and once per minute to recalculate overdue labels as time passes. A refresh failure must show an error without replacing saved data with an empty view.
