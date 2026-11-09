
# TaskTrack — Student Assignment Management System

[![Docs Review](https://github.com/ahneematallah-boop/TaskTrack-CS3354/actions/workflows/docs-review.yml/badge.svg)](https://github.com/ahneematallah-boop/TaskTrack-CS3354/actions/workflows/docs-review.yml)

**CS 3354 — Software Engineering**  
**University of Texas at Dallas | Fall 2026**

**Team Members:** Ahmed Neematallah, Ittehadul Karim, Taha Khwaja, Matthew Oksanen, Jacqueline Rodriguez, and Vinh Tang

## Project Overview

TaskTrack is a web application designed to help college students manage their courses, assignments, exams, and deadlines in one place.

Students can add courses and assignments, set due dates, view upcoming deadlines, and mark assignments as completed. TaskTrack also provides a dashboard displaying pending, completed, and overdue assignments.

Our goal is to make it easier for students to keep track of their schoolwork without constantly checking multiple course platforms or managing separate to-do lists.

This repository contains our work for both Project 1 (Proposal and Requirements) and Project 2 (Analysis and High-Level Design).

## Project Status

| Phase | Status |
| --- | --- |
| Project 1 — Proposal and Requirements | Completed |
| Project 2 — Analysis and High-Level Design | Documentation available; final integration in progress |
| Backend implementation | Local API and SQLite persistence available |
| Frontend prototype | Integration and evidence being finalized |
| Testing | Backend integration tests available; full browser testing pending |

Project 2 builds on the requirements and use cases established during Project 1. We are continuing with the same TaskTrack application rather than creating a separate project.

---

## Project 1 — Proposal and Requirements

Project 1 focused on defining the problem, identifying stakeholders, establishing system requirements, and explaining how students would interact with TaskTrack.

### Project 1 Documentation

| Document | Description | Owner |
| --- | --- | --- |
| [Problem and Scope](docs/problem-and-scope.md) | Problem statement, stakeholders, feasibility, and scope | Ahmed |
| [Requirements](docs/Requirements.md) | Functional and nonfunctional requirements and priorities | Taha |
| [Use Cases](docs/Use_Case.md) | Ten use cases with main, alternate, and exception flows | Matthew |
| [Team Plan](docs/team-plan.md) | Team responsibilities, milestones, and risks | Jackie |
| [Contributing Guidelines](CONTRIBUTING.md) | Repository organization and GitHub workflow | Karim |

### Project 1 Feedback

Our Project 1 submission received 30/40 points.

The professor highlighted the repository organization, documentation structure, contribution tracking, and detailed use cases as strengths.

The feedback also identified several areas for improvement:

- Add acceptance criteria to functional requirements.
- Make nonfunctional requirements measurable.
- Provide stronger evidence for stakeholder needs and feasibility.
- Improve the team plan with clear decision rules, milestones, and risk owners.
- Clarify whether account requirements FR-1.1 and FR-1.2 are included or deferred.
- Maintain traceability between requirements and design documents.

We are using this feedback to guide Project 2 and the remaining development work.

### Project 1 — Team Responsibilities

| Team Member | Responsibility |
| --- | --- |
| Ahmed Neematallah | Problem, stakeholders, feasibility, and scope |
| Taha Khwaja | Functional and nonfunctional requirements |
| Matthew Oksanen | Use cases and traceability |
| Jacqueline Rodriguez | Team planning, milestones, and risks |
| Ittehadul Karim | Repository organization and final review |
| Vinh Tang | Joined the team for Project 2; no P1 contribution recorded |

---

## Project 2 — Analysis and High-Level Design

Project 2 focuses on explaining how TaskTrack will work before completing the final implementation.

This includes use-case analysis, system architecture, high-level design, design rationale, models, requirements traceability, and prototype evidence.

We are keeping the same TaskTrack project and building on our existing Project 1 documentation.

### Project 2 — Team Responsibilities

| Person | Team Member | Responsibility |
| --- | --- | --- |
| Person 1 | Ahmed Neematallah | Use-case analysis and use-case diagram |
| Person 2 | Ittehadul Karim | System architecture, backend, and interfaces |
| Person 3 | Matthew Oksanen | High-level design, class diagram, and data model |
| Person 4 | Jacqueline Rodriguez | Design rationale and quality trade-offs |
| Person 5 | Vinh Tang | Models, sequence diagram, and requirements traceability |
| Person 6 | Taha Khwaja | Prototype and integration |

Each member is responsible for completing their assigned section, committing their changes, and participating in the GitHub review process.

### Project 2 Documentation

| Section | Document | Description |
| --- | --- | --- |
| Use-Case Analysis | [P2 Use-Case Analysis](docs/p2-use-case-analysis.md) | Main flows, alternate flows, exceptions, and system interactions |
| Use-Case Diagram | [Use-Case Diagram](docs/diagrams/tasktrack-use-cases.png) | Visual representation of student interactions |
| Architecture | [Architecture and Deployment](docs/architecture.md) | Components, interfaces, and deployment assumptions |
| High-Level Design | [High-Level Design](docs/high-level-design.md) | System classes, data model, and design structure |
| Class Diagram | [Class Diagram](docs/diagrams/class-diagram.png) | Main system classes and relationships |
| ER Diagram | [ER Diagram](docs/diagrams/er-diagram.png) | Database entities and relationships |
| Design Rationale | [Design Rationale](docs/design-rationale.md) | Design decisions, alternatives, and trade-offs |
| Sequence Diagram | [Sequence Diagram](docs/diagrams/student-use-cases-sequence.svg) | Student interactions with system components |
| Traceability | [Requirements Traceability Table](docs/traceability-table.md) | Connections between requirements, use cases, design, and prototype |
| API Design | [API Contract](docs/api.md) | Backend endpoints and frontend integration |
| Prototype | [Frontend Integration Guide](frontend/README.md) | Frontend integration and prototype expectations |

### 1. Use-Case Analysis

**Owner: Ahmed Neematallah**

The main actor in TaskTrack is the student.

Project 2 builds on the ten use cases defined in Project 1.

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

The use-case analysis describes the student's goals, system responsibilities, main interactions, alternate flows, and error handling.

It also connects the use cases to the functional requirements from Project 1.

**Documents:**

- [P2 Use-Case Analysis](docs/p2-use-case-analysis.md)
- [Use-Case Diagram](docs/diagrams/tasktrack-use-cases.png)

### 2. System Architecture and Backend

**Owner: Ittehadul Karim**

TaskTrack uses a layered design that separates the frontend, application logic, and data storage.

The main components are:

**Frontend:** Allows students to manage courses, assignments, deadlines, and completion status.

**Application Logic:** Handles input validation, assignment management, deadline calculations, and dashboard updates.

**Data Storage:** Stores courses, assignments, due dates, and completion statuses.

The repository includes a Flask-based backend, SQLite database support, and an API contract for frontend integration.

The layered structure keeps responsibilities separate and makes the application easier to maintain and test.

**Documents:**

- [Architecture and Deployment](docs/architecture.md)
- [Architecture Diagram](diagrams/architecture.png)
- [API Contract](docs/api.md)
- [Backend Integration Tests](tests/test_backend.py)
- [Person 2 Contribution Evidence](docs/person-2-contribution.md)

### 3. High-Level Design

**Owner: Matthew Oksanen**

The high-level design explains the main system objects, their responsibilities, and how they relate to each other.

TaskTrack's main data concepts include students, courses, and assignments.

A course organizes assignments, while each assignment contains information such as its title, description, due date, and completion status.

The high-level design includes class and entity-relationship diagrams to show the proposed system structure.

**Documents:**

- [High-Level Design](docs/high-level-design.md)
- [Class Diagram](docs/diagrams/class-diagram.png)
- [ER Diagram](docs/diagrams/er-diagram.png)

### 4. Design Rationale and Quality Trade-offs

**Owner: Jacqueline Rodriguez**

This section explains why we selected our proposed design approaches and what alternatives we considered.

Our main design decisions include:

- Using a layered architecture instead of combining all functionality into one component.
- Providing a dashboard so students can view deadlines in one place.
- Calculating overdue status based on due dates and completion status.
- Validating information before saving assignments.
- Requiring confirmation before permanently deleting assignments.
- Using persistent storage so students do not lose their saved work.

These decisions focus on usability, reliability, maintainability, security, and simplicity.

The design rationale also discusses trade-offs, including extra development work, additional validation, and the complexity of maintaining consistent information.

The proposed quality targets are connected to our Project 1 requirements.

**Document:**

- [Design Rationale and Quality Trade-offs](docs/design-rationale.md)

### 5. Models and Requirements Traceability

**Owner: Vinh Tang**

This section explains how TaskTrack's requirements relate to use cases, system components, and the proposed prototype.

The sequence diagram shows how the student interacts with the TaskTrack interface, application logic, validation, and data storage.

It covers important actions such as adding assignments, changing completion status, and reopening the application to view saved work.

The requirements traceability table connects:

1. Project 1 functional and nonfunctional requirements.
2. Related use cases.
3. Proposed design components.
4. Prototype screens and expected evidence.

This helps the team verify that the proposed design supports the original requirements.

**Documents:**

- [Sequence Diagram](docs/diagrams/student-use-cases-sequence.svg)
- [Sequence Description](docs/diagrams/student-table-sequence.md)
- [Requirements Traceability Table](docs/traceability-table.md)

### 6. Prototype and Integration

**Owner: Taha Khwaja**

The prototype is intended to demonstrate how students will interact with TaskTrack.

The planned interface includes:

- Dashboard with pending, completed, and overdue assignments.
- Course management.
- Add and edit assignment forms.
- Upcoming assignments list.
- Completion status controls.
- Course and status filters.

The frontend should follow the use-case analysis and connect to the backend through the documented API.

Prototype screenshots and evidence will be linked once the team's frontend contribution is finalized.

**Documents:**

- [Frontend Integration Guide](frontend/README.md)
- [API Contract](docs/api.md)

### Account Access and Scope

Project 1 included optional account requirements FR-1.1 and FR-1.2.

The team must confirm whether account registration and authentication are included in the current implementation or deferred to a future version.

If the prototype is single-user, those requirements should be explicitly marked as deferred rather than presented as completed features.

The architecture, traceability table, and prototype should reflect the same decision.

---

## Individual Contribution Evidence

We use GitHub issues, branches, commits, and pull requests to track each member's work.

Each contributor should have evidence showing:

- Their assigned task.
- Files or diagrams they created or updated.
- Commits made under their GitHub account.
- Pull requests and reviews.
- A short explanation of their individual contribution.

Relevant GitHub links:

- [Commit History](https://github.com/ahneematallah-boop/TaskTrack-CS3354/commits/main/)
- [Pull Requests](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pulls?q=is%3Apr)
- [Issues](https://github.com/ahneematallah-boop/TaskTrack-CS3354/issues)
- [Person 2 Contribution Record](docs/person-2-contribution.md)

The final Project 2 contribution record should summarize the actual work completed by all six members.

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

The repository keeps documentation, diagrams, source code, and testing files organized in separate directories.

---

## Development and Testing

The repository includes backend functionality supporting course and assignment management.

The backend uses Flask and SQLite for local development.

The API contract describes how the frontend and backend communicate.

Backend integration tests are available to check core API functionality.

Complete frontend and browser integration testing remains part of the remaining work.

For setup and testing information, see:

- [Architecture and Setup](docs/architecture.md)
- [API Contract](docs/api.md)
- [Frontend Integration Guide](frontend/README.md)
- [Backend Tests](tests/test_backend.py)

---

## GitHub Workflow

Our team uses GitHub branches and pull requests to organize contributions.

The general workflow is:

1. Create or claim an issue for the assigned work.
2. Create a separate branch.
3. Add or update the relevant files.
4. Commit changes with a descriptive message.
5. Push the branch to GitHub.
6. Open a pull request.
7. Review the changes and automated checks.
8. Merge approved changes into the main branch.

This workflow allows us to track individual contributions and reduces conflicts between team members.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.

## Automated Documentation Checks

The repository uses GitHub Actions to help check documentation changes.

The Docs Review workflow includes:

| Check | Purpose |
| --- | --- |
| Markdown lint | Detect formatting problems |
| Relative link check | Check links between repository documents |
| Requirements traceability | Detect references to undefined requirement IDs |

All Project 2 documents should use requirement IDs already defined in `docs/Requirements.md`.

The automated checks help prevent documentation problems, but team review is still needed to confirm that the content is complete and consistent.

---

## AI-Use Declaration

Project 2 requires the team to document any use of AI tools.

The final declaration should accurately describe which tools were used, how they assisted with the work, and how the team reviewed or verified the results.

Any AI-assisted writing, coding, diagram creation, or documentation work should be disclosed as applicable.

The team must complete and confirm this declaration before final submission.

---

## Project 2 Submission

**Milestone:** Analysis and High-Level Design  
**Due Date:** November 8, 2026, at 11:59 PM CT  
**Submission Type:** One team PDF containing the GitHub repository URL

**Repository:**

https://github.com/ahneematallah-boop/TaskTrack-CS3354

The repository contains the documentation, diagrams, design decisions, and development work for TaskTrack.

The final submission should reference the Project 2 deliverables, prototype evidence, and individual contributions.

---

## Conclusion

TaskTrack is designed to provide a simple and organized way for college students to manage their assignments and deadlines.

Project 1 established the requirements and use cases. Project 2 builds on that foundation by defining the architecture, system interactions, design decisions, data models, and requirements traceability.

The team will continue using these documents as a reference for implementation, testing, and future improvements.
