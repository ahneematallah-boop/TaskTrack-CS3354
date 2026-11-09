
# TaskTrack — Student Assignment Management System

[![Docs Review](https://github.com/ahneematallah-boop/TaskTrack-CS3354/actions/workflows/docs-review.yml/badge.svg)](https://github.com/ahneematallah-boop/TaskTrack-CS3354/actions/workflows/docs-review.yml)

**CS 3354 — Software Engineering**  
**University of Texas at Dallas | Fall 2026**

**Team Members:** Ahmed Neematallah, Ittehadul Karim, Taha Khwaja, Matthew Oksanen, Jacqueline Rodriguez, and Vinh Tang

## Project Overview

TaskTrack is a student assignment management system designed to help college students organize their coursework and deadlines in one place.

Students can add courses and assignments, set due dates, view upcoming deadlines, and mark assignments as completed. The system also includes a dashboard that displays pending, completed, and overdue assignments.

Our goal is to make it easier for students to keep track of their schoolwork without having to check multiple course platforms or maintain separate lists.

This repository contains our work for Project 1 (Proposal and Requirements) and Project 2 (Analysis and High-Level Design).

## Project Status

| Phase | Status |
| --- | --- |
| Project 1 — Proposal and Requirements | Completed |
| Project 2 — Analysis and High-Level Design | Documentation available; final integration in progress |
| Backend implementation | Local API and SQLite persistence available |
| Frontend prototype | Integration and evidence being finalized |
| Testing | Backend integration tests available; full browser testing pending |

Project 2 builds directly on the requirements and use cases developed in Project 1. We are continuing with the same TaskTrack system rather than creating a separate project.

---

## Project 1 — Proposal and Requirements

The first phase focused on defining the problem, identifying the intended users, establishing requirements, and describing how students would interact with TaskTrack.

### Project 1 Documentation

| Document | Description | Owner |
| --- | --- | --- |
| [Problem and Scope](docs/problem-and-scope.md) | Problem statement, stakeholders, feasibility, and project scope | Ahmed |
| [Requirements](docs/Requirements.md) | Functional and nonfunctional requirements, priorities, and system expectations | Taha |
| [Use Cases](docs/Use_Case.md) | Ten use cases with main, alternate, and exception flows | Matthew |
| [Team Plan](docs/team-plan.md) | Team responsibilities, milestones, and project risks | Jackie |
| [Contributing Guidelines](CONTRIBUTING.md) | Repository organization, branches, pull requests, and reviews | Karim |

### Project 1 Feedback

Our Project 1 submission received 30/40 points.

The feedback highlighted our repository organization, documentation structure, GitHub workflow, and detailed use cases as strengths.

The professor also identified areas for improvement:

- Add testable acceptance criteria to functional requirements.
- Make nonfunctional requirements measurable.
- Provide evidence supporting stakeholder needs and feasibility.
- Improve team planning and risk management.
- Clarify whether account registration is included or deferred.
- Maintain clear traceability between requirements and design decisions.

We are using this feedback to guide Project 2 and the remaining development work.

---

## Project 2 — Analysis and High-Level Design

Project 2 focuses on explaining how TaskTrack will work before completing the final implementation.

This includes analyzing system interactions, defining the architecture, designing the data model, comparing design alternatives, and connecting requirements to the proposed prototype.

We are keeping the same requirements and use cases established during Project 1.

### Project 2 Documentation

| Section | Document | Description |
| --- | --- | --- |
| Use-Case Analysis | [P2 Use-Case Analysis](docs/p2-use-case-analysis.md) | Detailed system interactions, main flows, alternate flows, and error handling |
| Use-Case Diagram | [Use-Case Diagram](docs/diagrams/tasktrack-use-cases.png) | Visual representation of student interactions with TaskTrack |
| Architecture | [Architecture and Deployment](docs/architecture.md) | System components, responsibilities, interfaces, and deployment assumptions |
| High-Level Design | [High-Level Design](docs/high-level-design.md) | Main classes, entities, relationships, and design structure |
| Class Diagram | [Class Diagram](docs/diagrams/class-diagram.png) | Main system classes and their relationships |
| ER Diagram | [ER Diagram](docs/diagrams/er-diagram.png) | Database entities and relationships |
| Design Rationale | [Design Rationale](docs/design-rationale.md) | Design choices, alternatives, quality attributes, and trade-offs |
| Sequence Diagram | [Student Sequence Diagram](docs/diagrams/student-use-cases-sequence.svg) | Student interactions with the interface, application logic, and storage |
| Traceability | [Requirements Traceability Table](docs/traceability-table.md) | Mapping between P1 requirements, use cases, design components, and proposed prototype screens |
| API Design | [API Contract](docs/api.md) | Proposed API endpoints and frontend/backend interactions |
| Prototype Integration | [Frontend Integration Guide](frontend/README.md) | Frontend integration expectations and implementation boundary |

These documents are intended to describe the same system and use the requirement IDs defined in `docs/Requirements.md`.

### 1. Use-Case Analysis

The primary actor in TaskTrack is the student.

The analysis builds on the ten use cases from Project 1:

| ID | Use Case |
| --- | --- |
| UC-01 | Add a course |
| UC-02 | Edit or delete a course |
| UC-03 | Add an assignment or exam |
| UC-04 | Edit an assignment or exam |
| UC-05 | Delete an assignment or exam |
| UC-06 | View upcoming assignments |
| UC-07 | Mark an assignment complete or incomplete |
| UC-08 | View dashboard |
| UC-09 | Filter assignments by course or status |
| UC-10 | Return to saved assignments |

Each use case describes the student's goal, the steps involved, and how the system should respond to alternate situations or errors.

The analysis also connects use cases to the existing functional requirements.

**Documents:**
- [P2 Use-Case Analysis](docs/p2-use-case-analysis.md)
- [Use-Case Diagram](docs/diagrams/tasktrack-use-cases.png)

### 2. Architecture and High-Level Design

TaskTrack uses a layered design that separates the user interface, application logic, and data storage.

The main parts are:

**Frontend:** Allows students to manage courses and assignments, update completion status, and view their dashboard.

**Application logic:** Handles validation, assignment operations, due-date calculations, and dashboard information.

**Data storage:** Preserves courses, assignments, due dates, and completion statuses between sessions.

This separation makes the application easier to maintain and allows team members to work on different components independently.

The repository also contains a Flask-based backend, API documentation, and SQLite database support for local development.

**Documents:**
- [Architecture](docs/architecture.md)
- [High-Level Design](docs/high-level-design.md)
- [Architecture Diagram](diagrams/architecture.png)
- [Class Diagram](docs/diagrams/class-diagram.png)
- [ER Diagram](docs/diagrams/er-diagram.png)
- [API Contract](docs/api.md)

### 3. Design Rationale and Quality Trade-offs

We considered different approaches before selecting the proposed design.

Our main decisions include:

- Using a layered structure instead of combining all functionality into one component.
- Providing a dashboard so students can view deadlines without opening every course.
- Calculating overdue status from due dates and completion status.
- Validating assignment information before saving.
- Requiring confirmation before deleting assignments.
- Using persistent storage to preserve saved information.

These decisions were chosen based on usability, maintainability, reliability, security, and simplicity.

We also considered the disadvantages of each approach, including additional development work, more validation logic, and possible dashboard complexity.

The quality targets are based on the existing Project 1 requirements and proposed acceptance measures. They are not presented as completed test results.

**Document:** [Design Rationale and Quality Trade-offs](docs/design-rationale.md)

### 4. Models and Requirements Traceability

The models help explain how TaskTrack's components interact and how data moves through the system.

The sequence diagram covers important student workflows, including creating assignments, updating completion status, and loading previously saved information.

The traceability table connects:

1. Project 1 requirements.
2. Related use cases.
3. Proposed design components.
4. Prototype screens or expected evidence.

This helps the team check that important requirements are reflected in the system design.

**Documents:**
- [Sequence Diagram](docs/diagrams/student-use-cases-sequence.svg)
- [Sequence Description](docs/diagrams/student-table-sequence.md)
- [Traceability Table](docs/traceability-table.md)

### 5. Prototype and Integration

The prototype is intended to demonstrate how students will interact with TaskTrack.

The planned screens and interactions include:

- Dashboard with pending, completed, and overdue assignments.
- Course management.
- Add and edit assignment forms.
- Assignment list with deadlines.
- Completion status controls.
- Course and status filtering.

The frontend should follow the use-case analysis and connect to the backend through the documented API.

Prototype screenshots and links should be added to the repository when the team's frontend contribution is finalized.

**Integration Guide:** [Frontend README](frontend/README.md)

### 6. Scope and Account Access

The main focus of TaskTrack is course and assignment management.

Project 1 also included optional account requirements, FR-1.1 and FR-1.2.

The team must confirm whether account registration and authentication will be included in the current implementation or explicitly deferred.

The architecture and traceability documents identify these requirements as conditional. The final prototype and documentation should consistently reflect the team's decision.

---

## Team Responsibilities

### Project 1

| Team Member | Responsibility |
| --- | --- |
| Ahmed Neematallah | Problem, stakeholders, feasibility, and scope |
| Taha Khwaja | Functional and nonfunctional requirements |
| Matthew Oksanen | Use cases and traceability |
| Jacqueline Rodriguez | Team planning, milestones, and risks |
| Ittehadul Karim | Repository organization and final review |

### Project 2

| Team Member | Responsibility |
| --- | --- |
| Ahmed Neematallah | Use-case analysis and use-case diagram |
| Ittehadul Karim | System architecture, backend, and interfaces |
| Taha Khwaja | High-level design, class diagram, and data model |
| Jacqueline Rodriguez | Design rationale and quality trade-offs |
| Vinh Tang | Models, sequence diagram, and requirements traceability |
| Matthew Oksanen | Prototype and integration |

Each member is responsible for documenting their work, committing changes, and participating in the review process.

---

## Individual Contribution Evidence

We use GitHub branches, commits, issues, and pull requests to track individual work.

Each contributor should provide evidence of:

- Their assigned responsibilities.
- Files or diagrams they created or updated.
- Commits associated with their work.
- Pull requests and reviews.
- An explanation of their contribution.

Relevant links:

- [All Commits](https://github.com/ahneematallah-boop/TaskTrack-CS3354/commits/main/)
- [Pull Requests](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pulls?q=is%3Apr)
- [Project Issues](https://github.com/ahneematallah-boop/TaskTrack-CS3354/issues)
- [Person 2 Contribution Record](docs/person-2-contribution.md)

The final P2 contribution record should summarize all six members' actual work and reference their GitHub evidence.

---

## Repository Structure

```text
TaskTrack-CS3354/
├── README.md
├── CONTRIBUTING.md
├── docs/
│   ├── problem-and-scope.md
│   ├── Requirements.md
│   ├── Use_Case.md
│   ├── team-plan.md
│   ├── p2-use-case-analysis.md
│   ├── architecture.md
│   ├── high-level-design.md
│   ├── design-rationale.md
│   ├── traceability-table.md
│   ├── api.md
│   ├── person-2-contribution.md
│   └── diagrams/
│       ├── tasktrack-use-cases.png
│       ├── tasktrack-use-cases.dot
│       ├── class-diagram.png
│       ├── er-diagram.png
│       ├── student-use-cases-sequence.svg
│       └── student-table-sequence.md
├── diagrams/
│   ├── architecture.png
│   └── architecture.svg
├── frontend/
│   └── README.md
├── backend/
├── data/
├── tests/
├── scripts/
│   └── check_traceability.py
└── .github/
    └── workflows/
```

The repository keeps documentation, diagrams, source code, and tests organized in separate locations.

---

## Development and Testing

The repository includes backend functionality supporting course and assignment management.

The backend uses Flask and SQLite for local development.

The API contract describes how the frontend and backend communicate.

Backend integration tests are available to check core API functionality. Complete frontend and browser integration testing remains part of the ongoing work.

For setup and implementation information, see:

- [Architecture and Setup](docs/architecture.md)
- [API Contract](docs/api.md)
- [Frontend Integration Guide](frontend/README.md)
- [Backend Tests](tests/test_backend.py)

---

## GitHub Workflow

We use a branch-based workflow so team members can work on their sections without directly changing the main branch.

The general process is:

1. Create or claim a GitHub issue.
2. Create a separate branch for the assigned work.
3. Add or update the relevant files.
4. Commit changes with a descriptive message.
5. Push the branch to GitHub.
6. Open a pull request.
7. Review the changes and automated checks.
8. Merge approved changes into `main`.

Each team member's contributions remain visible through GitHub history.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.

## Automated Documentation Checks

The repository uses GitHub Actions to check documentation changes.

The Docs Review workflow includes:

| Check | Purpose |
| --- | --- |
| Markdown lint | Detect formatting problems |
| Relative link check | Check links to repository documents |
| Requirements traceability | Detect references to undefined requirement IDs |

All requirement IDs used in Project 2 should already exist in `docs/Requirements.md`.

These checks help prevent documentation errors, but team review is still needed to confirm that the design documents are complete and consistent.

---

## AI-Use Declaration

Project 2 requires the team to document any use of AI tools.

The final declaration should identify which tools were used, what they assisted with, and how team members reviewed or verified the resulting work.

AI-assisted writing, coding, diagram preparation, or documentation changes should be disclosed accurately where applicable.

The final team declaration must be completed and agreed upon before submission.

---

## Project 2 Submission

**Milestone:** Analysis and High-Level Design  
**Due Date:** November 8, 2026, at 11:59 PM CT  
**Submission:** One team PDF containing the repository URL

**Repository URL:**  
https://github.com/ahneematallah-boop/TaskTrack-CS3354

The repository contains the documentation and development work for TaskTrack. The final submission should reference the relevant Project 2 documents, diagrams, prototype evidence, and individual contributions.

---

## Conclusion

TaskTrack is intended to provide a simple way for students to manage courses, assignments, and deadlines.

Project 1 established the requirements and main use cases. Project 2 builds on that foundation by defining the system's structure, interactions, design decisions, and traceability.

The project will continue to use these documents as a reference for implementation, testing, and future improvements.
