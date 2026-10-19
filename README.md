# TaskTrack — Student Assignment Management System

[![Docs Review](https://github.com/ahneematallah-boop/TaskTrack-CS3354/actions/workflows/docs-review.yml/badge.svg)](https://github.com/ahneematallah-boop/TaskTrack-CS3354/actions/workflows/docs-review.yml)

CS 3354 Software Engineering · UT Dallas · Fall 2026

Ahmed Neematallah, Ittehadul Karim, Taha Khwaja, Matthew Oksanen, Jacqueline Rodriguez

TaskTrack is a web application that keeps a college student's assignments in one place. A student adds assignments with a course and due date, sees them in deadline order, marks them complete, and reads a dashboard of pending, completed, and overdue work.

## Project status

| Phase | State |
|---|---|
| Problem, scope, requirements, use cases, team plan | In repository |
| Design (architecture, data model, UI) | Not started |
| Implementation | Not started |
| Testing | Not started |

This repository holds documentation only. Application code is added in a later phase.

## Documentation map

Read the documents in this order. Each one builds on the one before it.

| # | Document | Contents | Owner |
|---|---|---|---|
| 1 | [Problem and Scope](docs/problem-and-scope.md) | Problem statement, stakeholders, feasibility, included and excluded features | Ahmed |
| 2 | [Requirements](docs/Requirements.md) | Functional requirements FR-1.1 to FR-6.4, non-functional requirements NFR-1 to NFR-14, priorities | Taha |
| 3 | [Use Cases](docs/Use_Case.md) | Actors, UC-01 to UC-10 with main, alternate, and exception flows, traceability to requirements | Matthew |
| 4 | [Team Plan](docs/team-plan.md) | Roles, working agreement, milestones, risks | Jackie |
| 5 | [Contributing](CONTRIBUTING.md) | Branch and pull request workflow, review checks | Karim |

## Repository design

```text
TaskTrack-CS3354/
├── README.md                      Project overview and documentation map
├── CONTRIBUTING.md                Branch → pull request → review → merge workflow
├── docs/                          Every specification document, one file per section
│   ├── problem-and-scope.md
│   ├── Requirements.md
│   ├── Use_Case.md
│   └── team-plan.md
├── scripts/
│   └── check_traceability.py      Verifies every cited FR/NFR ID exists in Requirements.md
├── .github/
│   ├── workflows/docs-review.yml  CI: markdown lint, link check, traceability
│   └── pull_request_template.md   Author and reviewer checklists
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
