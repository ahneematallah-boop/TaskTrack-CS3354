# TaskTrack — Student Assignment Management System

[![Docs Review](https://github.com/ahneematallah-boop/TaskTrack-CS3354/actions/workflows/docs-review.yml/badge.svg)](https://github.com/ahneematallah-boop/TaskTrack-CS3354/actions/workflows/docs-review.yml)

CS 3354 Software Engineering · UT Dallas · Fall 2026

Ahmed Neematallah, Ittehadul Karim, Taha Khwaja, Matthew Oksanen, Jacqueline Rodriguez, Vinh Tang

TaskTrack is a web application that keeps a college student's assignments in one place. A student adds assignments with a course and due date, sees them in deadline order, marks them complete, and reads a dashboard of pending, completed, and overdue work.

## Project status

| Phase | State |
|---|---|
| Problem, scope, requirements, use cases, team plan | In repository |
| Design (architecture, data model, UI) | P2 use cases, rationale, and architecture available; shared model/UI integration in progress |
| Implementation | Local course/assignment API and SQLite persistence available on this branch |
| Testing | Backend integration suite and CI available; integrated browser checks pending |

The local backend supports the P2 design with a runnable API. See [Architecture](docs/architecture.md) for setup and [API Contract](docs/api.md) for integration. Frontend prototype screens remain a separate contribution.

## Documentation map

Read the documents in this order. Each one builds on the one before it.

| # | Document | Contents | Owner |
|---|---|---|---|
| 1 | [Problem and Scope](docs/problem-and-scope.md) | Problem statement, stakeholders, feasibility, included and excluded features | Ahmed |
| 2 | [Requirements](docs/Requirements.md) | Functional requirements FR-1.1 to FR-6.4, non-functional requirements NFR-1 to NFR-14, priorities | Taha |
| 3 | [Use Cases](docs/Use_Case.md) | Actors, UC-01 to UC-10 with main, alternate, and exception flows, traceability to requirements | Matthew |
| 4 | [Team Plan](docs/team-plan.md) | Roles, working agreement, milestones, risks | Jackie |
| 5 | [Contributing](CONTRIBUTING.md) | Branch and pull request workflow, review checks | Karim |

## Person 2 — Architecture and backend

- [Architecture, component diagram, and deployment](docs/architecture.md)
- [API contract and smoke workflow](docs/api.md)
- [Frontend integration boundary](frontend/README.md)
- [Backend integration tests](tests/test_backend.py)

## Repository design

```text
TaskTrack-CS3354/
├── README.md                      Project overview and documentation map
├── CONTRIBUTING.md                Branch → pull request → review → merge workflow
├── docs/                          Requirements, use cases, rationale, architecture, API
├── diagrams/                      Architecture PNG and editable SVG
├── frontend/                      Integration guide; screens owned by prototype contributor
├── backend/                       Flask routes, application services, SQLite connections
├── data/schema.sql                Persistent local schema and logical owner
├── tests/test_backend.py          API integration tests using temporary databases
├── scripts/check_traceability.py  Verify cited FR/NFR IDs
├── .github/workflows/             Documentation and backend checks
└── .markdownlint-cli2.jsonc       Lint rules
```

Design rules:

- **One document per section, one owner per document.** Each owner edits their own file, so merge conflicts stay rare and every contribution traces to a commit.
- **Requirements are the source of truth for IDs.** Use cases, test cases, and design documents cite requirement IDs. They never define new ones. The traceability check enforces this.
- **Every change goes through a pull request.** CI runs on the pull request and the final reviewer approves it before merge. This implements NFR-14.
- **Code gets its own top-level directories.** When implementation starts, front-end, back-end, data, and test code each get a separate directory, as NFR-13 requires. The `docs/` tree stays unchanged.

## Review pipeline

Every pull request into `main` runs the **Docs Review** workflow:

| Check | Fails when |
|---|---|
| Markdown lint | Headings, lists, or tables are malformed |
| Relative link check | A link between repository files points to a missing file or heading |
| Requirements traceability | A document cites an FR or NFR ID that `docs/Requirements.md` does not define |

A pull request merges after all three checks pass and the final reviewer approves it. [CONTRIBUTING.md](CONTRIBUTING.md) lists the commands that run the checks locally.

## Team

| Member | Responsibility |
|---|---|
| Ahmed Neematallah | Problem, stakeholders, feasibility, and scope |
| Taha Khwaja | Functional and nonfunctional requirements |
| Matthew Oksanen | Use cases and traceability |
| Jacqueline Rodriguez | Team plan, milestones, and risks |
| Ittehadul Karim | Repository organization and final review |
