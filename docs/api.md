# TaskTrack — Local API Contract

**Owner:** Ittehadul Karim (Person 2).  
**Base URL:** `http://127.0.0.1:5000/api`.  
**Mode:** Single local student; no login. See [architecture and deployment](architecture.md).

## Request and response conventions

Send `Content-Type: application/json` for POST, PUT, and PATCH. A JSON object is required. Unknown body fields are rejected; request bodies are limited to 64 KiB. IDs are positive integers. Success bodies use `{"data": ...}`; lists return arrays, including `[]` when intentionally empty. DELETE success is 204 with no body.

Errors use a stable envelope:

```json
{
  "error": {
    "code": "validation_error",
    "message": "Check the highlighted fields.",
    "fields": {"title": "Required field."}
  }
}
```

| HTTP status | Meaning | Frontend response |
| --- | --- | --- |
| 400 | Invalid fields, filters, JSON, or missing delete confirmation | Keep form; show fields/message |
| 403 | Invalid local Host or cross-origin request | Use the local frontend proxy/origin |
| 404 | Missing route/record/course filter | Refresh stale selections; explain missing record |
| 405 | Method unsupported | Correct the integration request |
| 409 | Course still contains assignments | Keep course; ask student to move/delete assignments first |
| 413 | Request exceeds 64 KiB | Reduce form payload |
| 415 | Write body is not JSON | Send JSON Content-Type |
| 503 | Database read/write failed | Keep current view/form and offer retry |

## Endpoints

| Method | Path under `/api` | Body or filters | Success |
| --- | --- | --- | --- |
| GET | `/health` | None | 200, status/mode/timezone; checks DB access |
| GET | `/courses` | None | 200, courses ordered by name then ID |
| POST | `/courses` | Required `name`; optional `code` | 201, course |
| PUT | `/courses/{id}` | Required `name`; optional `code` | 200, updated course |
| DELETE | `/courses/{id}?confirmed=true` | Confirm first in UI | 204; 409 if assignments remain |
| GET | `/assignments` | Optional `course_id`, `status` | 200, filtered deadline-ordered list |
| POST | `/assignments` | Assignment fields below | 201, created Pending assignment |
| GET | `/assignments/{id}` | None | 200, full assignment details |
| PUT | `/assignments/{id}` | Assignment fields below | 200, updated assignment, same ID/status |
| PATCH | `/assignments/{id}/status` | `{"status":"Completed"}` or `{"status":"Pending"}` | 200, saved assignment |
| DELETE | `/assignments/{id}?confirmed=true` | Confirm first in UI | 204 |
| GET | `/dashboard` | None | 200, counts, next five Pending items, evaluation time/zone |

PUT replaces editable fields: omitted optional course code becomes empty; omitted description becomes empty; omitted due time becomes null; omitted task type becomes Assignment. Assignment PUT preserves completion status; use PATCH to change status. Status PATCH is idempotent. POST requests create new records and are not idempotent: disable repeated Save while a write is pending. If a response is lost after a write, reload the list before retrying to avoid duplicates. No automatic POST retries or idempotency-key support is implemented.

## Fields and derived values

| Input | Constraint |
| --- | --- |
| Course `name` | Required nonblank text, at most 120 characters |
| Course `code` | Optional text, at most 30 characters; default empty |
| Assignment `title` | Required nonblank text, at most 200 characters |
| Assignment `course_id` | Required positive integer referencing an existing course |
| Assignment `due_date` | Required real calendar date, `YYYY-MM-DD` |
| Assignment `due_time` | Optional `HH:MM` or null; null/omitted resolves to 23:59 workspace time |
| Assignment `description` | Optional text, at most 5,000 characters; default empty |
| Assignment `task_type` | Optional Assignment, Quiz, or Exam; default Assignment |
| Status PATCH `status` | Exactly Pending or Completed; Overdue is derived |

Text is trimmed at the boundary. Student text is stored as text; the frontend must render it with escaping/`textContent`. Null is accepted for due time only. Past due dates are valid. Workspace time defaults to America/Chicago; see the [deadline policy](architecture.md#6-deadline-and-count-policy) for daylight-saving behavior.

Course responses include `id`, `user_id`, `name`, and `code`. Assignment responses include the stored assignment fields plus `id`, `status`, `course_name`, `course_code`, UTC `due_at`, and Boolean `overdue`:

```json
{
  "data": {
    "id": 1,
    "course_id": 1,
    "title": "Architecture report",
    "description": "Component diagram and API contract",
    "due_date": "2026-11-20",
    "due_time": null,
    "task_type": "Assignment",
    "status": "Pending",
    "course_name": "Software Engineering",
    "course_code": "CS3354",
    "due_at": "2026-11-21T05:59:00Z",
    "overdue": false
  }
}
```

The example assumes a request before the deadline. Dates/counts in examples are illustrative. GET assignments accepts `status=Pending`, `Completed`, or `Overdue`; omit status to include all. Pending includes overdue assignments. Combine a status and course filter with `&`. An unknown filter key is rejected. A nonexistent course filter returns 404 so the UI can reset a stale selection. Ordering is UTC deadline, case-insensitive title, then ID.

Dashboard response fields are `pending`, `completed`, `overdue`, `next_due` (assignment array), `evaluated_at` (UTC), and `timezone`. Overdue is a subset of pending. Completed work is excluded from overdue and next due. Counts come from the same read/evaluation time. The browser refreshes list/dashboard after successful writes and as time passes.

## Local smoke workflow

Start the backend as described in the architecture document. These commands write demo records into the selected local database; use a separate `TASKTRACK_DATABASE` file for experiments. On an empty database, the created IDs are 1; otherwise use IDs from the returned responses.

```sh
curl -s http://127.0.0.1:5000/api/health
curl -s -X POST http://127.0.0.1:5000/api/courses \
  -H 'Content-Type: application/json' \
  -d '{"name":"Software Engineering","code":"CS3354"}'
curl -s -X POST http://127.0.0.1:5000/api/assignments \
  -H 'Content-Type: application/json' \
  -d '{"title":"Architecture report","course_id":1,"due_date":"2026-11-20"}'
curl -s 'http://127.0.0.1:5000/api/assignments?status=Pending&course_id=1'
curl -s -X PATCH http://127.0.0.1:5000/api/assignments/1/status \
  -H 'Content-Type: application/json' -d '{"status":"Completed"}'
curl -s http://127.0.0.1:5000/api/dashboard
```

Stop and restart the backend with the same database path, then GET assignments again to check persistence. A form's Cancel action sends no request. Only send DELETE after the student confirms the selected title; `confirmed=true` records the client workflow decision and is not authentication or proof of a human click.
