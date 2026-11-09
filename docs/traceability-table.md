# TaskTrack Traceability Table

| Legend | Details |
| --- | --- |
| Source documents | Requirement IDs: [Requirements](Requirements.md); use-case IDs: [Use Cases](Use_Case.md) |
| Design and prototype status | Design, implementation, and prototype work have not started. Components and screen names are proposed targets, not completed artifacts. |
| Account access | Optional; not assumed in the first prototype. |
| N/A | No dedicated user-facing screen, or the requirement concerns architecture or project process. |

| Requirement ID | Related use case | Design component | Prototype screen / evidence |
| --- | --- | --- | --- |
| FR-1.1 | None in current scope; account access is optional | Authentication and account management | Registration and login screens (conditional; out of initial prototype scope) |
| FR-1.2 | None in current scope; account access is optional | User-scoped data access | Assignment and course views filtered to the signed-in student (conditional) |
| FR-2.1 | UC-03 | Task form and task data model | Add Assignment form |
| FR-2.2 | UC-03 | Task form validation | Add Assignment form with required-field indicators |
| FR-2.3 | UC-03, UC-04 | Input validation and error display | Add/Edit Assignment form with validation errors |
| FR-2.4 | UC-04 | Task editing flow | Edit Assignment form |
| FR-2.5 | UC-05 | Task deletion operation | Assignment detail/list with Delete action |
| FR-2.6 | UC-05 | Delete confirmation dialog | Delete confirmation dialog |
| FR-2.7 | UC-01, UC-02, UC-03, UC-04, UC-05, UC-07, UC-10 | Persistent course and task storage | Course list, assignment forms, task list, and reloaded saved-work view |
| FR-3.1 | UC-06 | Deadline sorting and task list | Upcoming Assignments list, earliest deadline first |
| FR-3.2 | UC-06 | Task list item | Upcoming Assignments list showing title, course, and due date |
| FR-3.3 | UC-06 | Overdue classification and visual state | Upcoming Assignments list with overdue distinction |
| FR-3.4 | UC-08 | Task detail view | Assignment detail view |
| FR-4.1 | UC-07 | Completion-status control and persistence | Assignment list/detail with Mark Complete action |
| FR-4.2 | UC-07 | Completion-status control and persistence | Assignment list/detail with Reopen or Mark Incomplete action |
| FR-4.3 | UC-07 | Completion-status presentation | Assignment list showing completed and incomplete states |
| FR-4.4 | UC-07 | Dashboard count calculation and state refresh | Dashboard with updated counts after a status change |
| FR-5.1 | UC-03 | Course-to-task association | Add Assignment form with course selector |
| FR-5.2 | UC-09 | Course filter and filtered task list | Assignment list filtered to one course |
| FR-5.3 | UC-01, UC-03 | Course creation and course selector | Add Course form and Add Assignment course selector |
| FR-5.4 | UC-02, UC-09 | Course list and filter controls | Course list and assignment list course filter |
| FR-6.1 | UC-05, UC-08 | Dashboard summary calculation | Dashboard with pending, completed, and overdue counts |
| FR-6.2 | UC-03, UC-04, UC-06, UC-08, UC-10 | Overdue classification based on due date and status | Assignment form, Upcoming list, Dashboard, and reloaded saved-work view |
| FR-6.3 | UC-08 | Dashboard count navigation | Dashboard with count links to matching assignment lists |
| FR-6.4 | UC-08 | Next-due task query and dashboard preview | Dashboard showing the next assignments due |
| NFR-1 | UC-03 | Clear task-entry flow and form labels | Add Assignment form |
| NFR-2 | UC-01, UC-03, UC-04, UC-05, UC-07 | Main navigation and task action controls | Dashboard, assignment list, and task forms |
| NFR-3 | UC-01 through UC-09 | Shared visual design system | Consistent course, assignment, list, and dashboard screens |
| NFR-4 | UC-01, UC-02, UC-03, UC-04, UC-05, UC-07, UC-10 | Data persistence and integrity handling | Course and assignment screens, including saved-work reload evidence |
| NFR-5 | UC-06, UC-09 | Shared deadline-ordering logic | Upcoming and filtered assignment lists |
| NFR-6 | UC-01, UC-02, UC-03, UC-04, UC-05, UC-07, UC-08, UC-10 | Storage error handling and user feedback | Course/task forms, Dashboard, and saved-work view with error states |
| NFR-7 | UC-06, UC-08 | List and dashboard data-loading performance | Upcoming Assignments list and Dashboard |
| NFR-8 | UC-04, UC-07 | Immediate task-state and summary refresh | Edit Assignment form, assignment list, and Dashboard |
| NFR-9 | UC-01 through UC-10 | Cross-browser web UI and compatibility testing | All prototype screens in supported browsers |
| NFR-10 | UC-01 through UC-10 | Responsive layout system | Course, assignment, list, and Dashboard screens at phone/tablet sizes |
| NFR-11 | None in current scope; conditional on implementing accounts | Secure password storage and authentication | Registration and login screens (conditional; out of initial prototype scope) |
| NFR-12 | UC-01, UC-03, UC-04 | Input validation and sanitization | Add/Edit Course and Add/Edit Assignment forms |
| NFR-13 | UC-01 through UC-10 | Front-end, back-end, and data-layer architecture | N/A (architecture evidence, not a screen) |
| NFR-14 | N/A (project process requirement) | Version control and pull-request review workflow | N/A (repository workflow, not a screen) |

## Mapping Guidance

| Item | Guidance |
| --- | --- |
| Functional requirement links | Use-case links follow the references in the current use-case documentation. `None in current scope` means there is no corresponding current use case; it does not introduce a new use-case ID. |
| Non-functional requirement links | These are linked to the user flows they affect. Cross-cutting requirements may apply to several screens. |
| Prototype evidence | Replace proposed screen descriptions with links to actual prototype screens or screenshots when available. |
