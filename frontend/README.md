# TaskTrack frontend prototype

Owner: Taha Khwaja (Person 6). Plain HTML, CSS, and JavaScript with no build step. It calls the [API contract](../docs/api.md) through relative `/api` URLs; see [architecture](../docs/architecture.md) for the backend.

## Run it

Use two terminals from the repository root.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r backend/requirements.txt
python -m backend.app
```

```sh
python3 frontend/dev_server.py
```

Open `http://localhost:5173`. The dev server serves this folder and proxies `/api` to `http://127.0.0.1:5000`. It rewrites `Host` and `Origin` because the backend rejects any other origin. Opening `index.html` as a `file://` page does not work.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Page structure: dashboard, assignments, courses, and dialogs |
| `style.css` | Responsive layout with light and dark themes |
| `app.js` | API calls, rendering, forms, filters, and refresh logic |
| `dev_server.py` | Local static server and `/api` proxy |

## Screens and use cases

| Screen | Use cases | Requirements | Evidence |
| --- | --- | --- | --- |
| Dashboard | UC-08, UC-06 | FR-6.1, FR-6.3, FR-6.4 | [Dashboard](../docs/screenshots/01-dashboard.png) |
| Assignment list | UC-06, UC-07, UC-09 | FR-3.1, FR-3.2, FR-3.3, FR-4.3 | [List](../docs/screenshots/02-assignment-list.png) |
| Add and edit assignment form | UC-03, UC-04 | FR-2.1, FR-2.2, FR-2.3, FR-2.4, FR-5.1 | [Form](../docs/screenshots/03-add-assignment-form.png) |
| Validation errors | UC-03, UC-04 | FR-2.3, NFR-12 | [Errors](../docs/screenshots/04-validation-error.png) |
| Delete confirmation | UC-05 | FR-2.5, FR-2.6 | [Confirm](../docs/screenshots/05-delete-confirm.png) |
| Course management | UC-01, UC-02 | FR-5.3, FR-5.4 | [Courses](../docs/screenshots/06-course-management.png) |
| Course and status filters | UC-09 | FR-5.2 | [Filters](../docs/screenshots/07-filters.png) |
| Saved work after backend restart | UC-10 | FR-2.7 | [Persistence](../docs/screenshots/08-after-restart.png) |

Mark complete and Reopen (UC-07, FR-4.1 to FR-4.4) appear on every assignment row.

## Integration behavior

- Student text is rendered with `textContent`, never `innerHTML`.
- Forms keep their input after a failed save and show `error.fields` under each field.
- Save buttons are disabled while a write is pending.
- Delete always asks for confirmation before sending `?confirmed=true`.
- After each successful write, the list and dashboard reload and keep the current filters.
- The app refreshes on page focus and once per minute. A failed refresh shows a banner and keeps the data already on screen.
- A stale course filter (404) resets to "All courses".

## Scope and testing status

Single local student; no login. FR-1.1 and FR-1.2 are **deferred**, matching [architecture](../docs/architecture.md).

| Area | Status |
| --- | --- |
| Manual walkthrough of every screen in Chromium against the real backend | Done |
| Backend integration tests | `python -m unittest discover -s tests -v` |
| Automated browser tests | Not implemented |
| Firefox, Safari, and phone-size testing (NFR-9, NFR-10) | Not completed |
