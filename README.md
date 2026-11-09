
# TaskTrack — Student Assignment Management System

[![Docs Review](https://github.com/ahneematallah-boop/TaskTrack-CS3354/actions/workflows/docs-review.yml/badge.svg)](https://github.com/ahneematallah-boop/TaskTrack-CS3354/actions/workflows/docs-review.yml)

**Course:** CS 3354 — Software Engineering  
**University:** University of Texas at Dallas  
**Semester:** Fall 2026

**Team Members:**
- Ahmed Neematallah
- Ittehadul Karim
- Matthew Oksanen
- Jacqueline Rodriguez
- Vinh Tang
- Taha Khwaja

## Project Overview

TaskTrack is a web application designed to help college students organize their courses, assignments, exams, and deadlines in one place.

Students can add courses and assignments, set due dates, view upcoming work, and mark assignments as completed. The application also provides a dashboard showing pending, completed, and overdue assignments.

Our goal is to make it easier for students to manage their schoolwork without constantly switching between course platforms or keeping separate to-do lists.

This repository contains our work for Project 1 (Proposal and Requirements) and Project 2 (Analysis and High-Level Design).

## Project Status

| Phase | Status |
| --- | --- |
| Project 1 — Proposal and Requirements | Completed |
| Project 2 — Analysis and High-Level Design | Main deliverables added to repository |
| Use-case analysis | Completed |
| Architecture and high-level design | Completed |
| Design rationale | Completed |
| Models and traceability | Completed |
| Frontend prototype | Implemented with backend integration |
| Backend | Flask API with SQLite persistence |
| Testing | Backend integration tests available; additional browser testing pending |

Project 2 builds on the requirements and use cases from Project 1. We are continuing with the same TaskTrack application instead of starting a separate project.

---

## Project 1 — Proposal and Requirements

Project 1 focused on identifying the problem, defining the scope, gathering requirements, and explaining how students would interact with TaskTrack.

### Project 1 Documentation

| Document | Description | Owner |
| --- | --- | --- |
| [Problem and Scope](docs/problem-and-scope.md) | Problem statement, stakeholders, feasibility, and scope | Ahmed |
| [Requirements](docs/Requirements.md) | Functional and nonfunctional requirements | Taha |
| [Use Cases](docs/Use_Case.md) | Ten use cases with main, alternate, and exception flows | Matthew |
| [Team Plan](docs/team-plan.md) | Team responsibilities, milestones, and risks | Jackie |
| [Contributing Guidelines](CONTRIBUTING.md) | GitHub workflow and repository organization | Karim |

### Project 1 Feedback

Our Project 1 submission received 30/40 points.

The professor highlighted our repository organization, documentation structure, contribution tracking, and detailed use cases as strengths.

The feedback also identified areas for improvement:

- Add acceptance criteria to functional requirements.
- Make nonfunctional requirements measurable.
- Provide stronger evidence for stakeholder needs and feasibility.
- Improve team planning and risk management.
- Clarify whether account requirements FR-1.1 and FR-1.2 are included or deferred.
- Maintain traceability between requirements and design documents.

We used this feedback to guide our Project 2 design and documentation.

### Project 1 — Team Responsibilities

| Team Member | Responsibility |
| --- | --- |
| Ahmed Neematallah | Problem, stakeholders, feasibility, and scope |
| Taha Khwaja | Functional and nonfunctional requirements |
| Matthew Oksanen | Use cases and traceability |
| Jacqueline Rodriguez | Team planning, milestones, and risks |
| Ittehadul Karim | Repository organization and final review |
| Vinh Tang | Models and sequence diagram |

---

## Project 2 — Analysis and High-Level Design

Project 2 focuses on explaining how TaskTrack works, how its components interact, and how the design supports the original requirements.

Our Project 2 deliverables include:

- Use-case analysis and diagrams.
- System architecture and interfaces.
- High-level design and database models.
- Design rationale and quality trade-offs.
- Sequence diagrams and requirements traceability.
- Frontend prototype and integration.
- Individual contribution evidence.

### Project 2 — Team Responsibilities

| Person | Team Member | Responsibility |
| --- | --- | --- |
| Person 1 | Ahmed Neematallah | Use-case analysis and use-case diagram |
| Person 2 | Ittehadul Karim | System architecture, backend, and interfaces |
| Person 3 | Matthew Oksanen | High-level design, class diagram, and data model |
| Person 4 | Jacqueline Rodriguez | Design rationale and quality trade-offs |
| Person 5 | Vinh Tang | Models, sequence diagram, and requirements traceability |
| Person 6 | Taha Khwaja | Prototype and integration |

Each member was responsible for completing their assigned section and contributing to the project through GitHub.

### Project 2 Documentation

| Section | Document | Description |
| --- | --- | --- |
| Use-Case Analysis | [P2 Use-Case Analysis](docs/p2-use-case-analysis.md) | Main flows, alternate flows, and exceptions |
| Use-Case Diagram | [Use-Case Diagram](docs/diagrams/tasktrack-use-cases.png) | Student interactions with the system |
| Architecture | [Architecture](docs/architecture.md) | System components, interfaces, and deployment |
| Architecture Diagram | [Architecture Diagram](diagrams/architecture.png) | Overview of system layers |
| High-Level Design | [High-Level Design](docs/high-level-design.md) | Class structure and data model |
| Class Diagram | [Class Diagram](docs/diagrams/class-diagram.png) | Classes and relationships |
| ER Diagram | [ER Diagram](docs/diagrams/er-diagram.png) | Database entities and relationships |
| Design Rationale | [Design Rationale](docs/design-rationale.md) | Design decisions and trade-offs |
| Sequence Diagram | [Sequence Diagram](docs/diagrams/student-use-cases-sequence.svg) | Student and system interactions |
| Traceability | [Traceability Table](docs/traceability-table.md) | Requirements, use cases, design, and prototype mappings |
| API | [API Contract](docs/api.md) | Backend API endpoints |
| Prototype | [Frontend Prototype](frontend/README.md) | Frontend implementation, setup, and screen coverage |

---

## 1. Use-Case Analysis

**Contributor: Ahmed Neematallah**

The primary actor in TaskTrack is the student.

We continued using the ten use cases established in Project 1.

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

The use-case analysis describes each interaction, including the main flow, alternate flows, input validation, and error handling.

It also connects the use cases to their related Project 1 requirements.

**Deliverables:**
- [Use-Case Analysis](docs/p2-use-case-analysis.md)
- [Use-Case Diagram](docs/diagrams/tasktrack-use-cases.png)

**Contribution Evidence:**
- [Ahmed's Pull Request #2](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pull/2)

---

## 2. System Architecture and Backend

**Contributor: Ittehadul Karim**

TaskTrack uses a layered architecture separating the user interface, application logic, and data storage.

The main components include:

**Frontend:** Allows students to interact with the dashboard, courses, and assignments.

**Application Logic:** Handles input validation, assignment operations, due-date calculations, and dashboard updates.

**Database:** Stores courses, assignments, deadlines, and completion statuses.

The backend uses Flask and SQLite for local development.

An API contract describes the communication between the frontend and backend.

The architecture also defines component responsibilities and deployment assumptions.

**Deliverables:**
- [Architecture Document](docs/architecture.md)
- [Architecture Diagram](diagrams/architecture.png)
- [API Contract](docs/api.md)
- [Backend Tests](tests/test_backend.py)
- [Person 2 Contribution Record](docs/person-2-contribution.md)

**Contribution Evidence:**
- [Karim's Pull Request #8](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pull/8)
- [Karim's Issue #7](https://github.com/ahneematallah-boop/TaskTrack-CS3354/issues/7)

---

## 3. High-Level Design

**Contributor: Matthew Oksanen**

The high-level design explains TaskTrack's main objects, responsibilities, and relationships.

The system is organized around courses and assignments.

A course can contain multiple assignments. Each assignment includes information such as its title, description, due date, and completion status.

The high-level design uses class and entity-relationship diagrams to show how the system is structured.

These models help connect the functional requirements to the proposed implementation.

**Deliverables:**
- [High-Level Design](docs/high-level-design.md)
- [Class Diagram](docs/diagrams/class-diagram.png)
- [ER Diagram](docs/diagrams/er-diagram.png)

**Contribution Evidence:**
- [High-Level Design Pull Request #6](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pull/6)

---

## 4. Design Rationale and Quality Trade-offs

**Contributor: Jacqueline Rodriguez**

This section explains the major design decisions made for TaskTrack and why certain approaches were selected.

The main design decisions include:

- Using a layered architecture.
- Providing a dashboard for upcoming assignments.
- Calculating overdue status automatically.
- Validating assignment information before saving.
- Requiring confirmation before deleting assignments.
- Using persistent storage.

We compared different approaches and considered their advantages and disadvantages.

The design decisions focus on usability, reliability, maintainability, security, and simplicity.

We also included proposed measurable quality targets based on the Project 1 requirements.

**Deliverable:**
- [Design Rationale](docs/design-rationale.md)

**Contribution Evidence:**
- [Jackie's Pull Request #5](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pull/5)
- [Jackie's Issue #4](https://github.com/ahneematallah-boop/TaskTrack-CS3354/issues/4)

---

## 5. Models and Requirements Traceability

**Contributor: Vinh Tang**

This section connects TaskTrack's requirements to its use cases, design components, and prototype.

The sequence diagram describes how the student interacts with the system when adding assignments, updating completion status, and returning to saved work.

The traceability table connects:

1. Project 1 functional and nonfunctional requirements.
2. Related use cases.
3. Design components.
4. Prototype screens or expected evidence.

The table helps verify that important requirements are represented in the proposed design.

**Deliverables:**
- [Sequence Diagram](docs/diagrams/student-use-cases-sequence.svg)
- [Sequence Description](docs/diagrams/student-table-sequence.md)
- [Traceability Table](docs/traceability-table.md)

**Contribution Evidence:**
- [Vinh's Pull Request #3](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pull/3)

---

## 6. Prototype and Integration

**Contributor: Taha Khwaja**

The frontend prototype demonstrates how a student can interact with TaskTrack.

The prototype includes:

- A dashboard showing assignment status counts.
- Course management.
- Assignment creation and editing.
- Upcoming assignment lists.
- Completion status controls.
- Course and status filters.
- Assignment deletion confirmation.
- Validation and error messages.

The frontend uses HTML, CSS, and JavaScript.

It communicates with the Flask backend using the documented API.

The prototype includes a local development server that serves the frontend and forwards API requests to the backend.

### Prototype Files

| File | Purpose |
| --- | --- |
| [index.html](frontend/index.html) | Main interface and page structure |
| [style.css](frontend/style.css) | Styling and responsive layouts |
| [app.js](frontend/app.js) | Application interactions and API requests |
| [dev_server.py](frontend/dev_server.py) | Local frontend server and API proxy |
| [Frontend README](frontend/README.md) | Setup instructions and screen coverage |

### Prototype Evidence

The frontend documentation references screenshots for the following interactions:

| Screen | Related Use Cases |
| --- | --- |
| Dashboard | UC-06, UC-08 |
| Assignment List | UC-06, UC-07, UC-09 |
| Add/Edit Assignment | UC-03, UC-04 |
| Validation Errors | UC-03, UC-04 |
| Delete Confirmation | UC-05 |
| Course Management | UC-01, UC-02 |
| Course and Status Filters | UC-09 |
| Saved Work After Restart | UC-10 |

**Prototype Documentation:**
- [Frontend Guide and Screenshot Links](frontend/README.md)
- [Person 6 Contribution Record](docs/Person%206%20Contribution)

The contribution record describes manual browser verification of the main screens and interactions.

Automated browser testing and complete cross-browser testing remain future work.

---

## 7. Account Access and Project Scope

Project 1 included optional account requirements FR-1.1 and FR-1.2.

For the current single-user prototype, account registration and login are deferred.

This allows the team to focus on assignment management, course organization, dashboard functionality, and data persistence.

Authentication and private multi-user accounts can be considered in a future version.

The deferred account functionality should not be presented as an implemented feature.

---

## 8. Individual Contribution Evidence

We use GitHub issues, branches, commits, and pull requests to document team contributions.

The following table identifies the main Project 2 responsibilities and available GitHub evidence.

| Member | P2 Responsibility | Evidence |
| --- | --- | --- |
| Ahmed Neematallah | Use-case analysis | [PR #2](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pull/2) |
| Ittehadul Karim | Architecture and backend | [PR #8](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pull/8) |
| Matthew Oksanen | High-level design | [PR #6](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pull/6) |
| Jacqueline Rodriguez | Design rationale | [PR #5](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pull/5) |
| Vinh Tang | Models and traceability | [PR #3](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pull/3) |
| Taha Khwaja | Prototype and integration | [Contribution Record](docs/Person%206%20Contribution) |

Additional contribution history can be found through:

- [Commit History](https://github.com/ahneematallah-boop/TaskTrack-CS3354/commits/main/)
- [All Pull Requests](https://github.com/ahneematallah-boop/TaskTrack-CS3354/pulls?q=is%3Apr)
- [GitHub Issues](https://github.com/ahneematallah-boop/TaskTrack-CS3354/issues)

These records show the work contributed to the repository and help document individual responsibilities.

---

## 9. Repository Structure

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
│   ├── Person 6 Contribution
│   ├── screenshots/
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
│   ├── README.md
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── dev_server.py
├── backend/
├── data/
├── tests/
├── scripts/
│   └── check_traceability.py
└── .github/
    └── workflows/
```

The repository separates documentation, diagrams, application code, and testing files to make the project easier to navigate and maintain.

---

## 10. Running the Prototype

The frontend and backend run locally.

### Backend Setup

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r backend/requirements.txt
python -m backend.app
```

### Frontend Setup

Open another terminal in the repository root and run:

```bash
python3 frontend/dev_server.py
```

Open the application at:

http://localhost:5173

The frontend development server forwards API requests to the backend running on port 5000.

For additional details, see:

- [Frontend Setup](frontend/README.md)
- [Backend Architecture](docs/architecture.md)
- [API Documentation](docs/api.md)

---

## 11. Testing and Verification

TaskTrack includes backend integration tests and automated documentation checks.

### Backend Testing

The repository includes integration tests for the backend API.

These tests help verify core course and assignment operations.

Run the tests using:

```bash
python -m unittest discover -s tests -v
```

### Requirements Traceability

The repository includes a script that checks references to requirement IDs.

Run:

```bash
python scripts/check_traceability.py
```

### Frontend Verification

The prototype contribution documentation describes manual checks of:

- Dashboard navigation.
- Course and assignment management.
- Validation errors.
- Delete confirmation.
- Status changes and filtering.
- Data persistence after reopening the application.

Cross-browser testing, phone-size testing, and automated browser tests are not fully completed.

---

## 12. GitHub Workflow

Our team uses GitHub to organize work and track contributions.

The general workflow is:

1. Create or claim an issue.
2. Create a branch for the assigned work.
3. Add or update the necessary files.
4. Commit the changes.
5. Push the branch to GitHub.
6. Open a pull request.
7. Review the changes and automated checks.
8. Merge the approved changes into `main`.

The repository also includes automated documentation checks.

| Check | Purpose |
| --- | --- |
| Markdown lint | Detect documentation formatting errors |
| Relative link check | Verify links between repository files |
| Requirements traceability | Detect references to undefined requirement IDs |

All Project 2 documents should use the requirement IDs already defined in `docs/Requirements.md`.

See [CONTRIBUTING.md](CONTRIBUTING.md) for additional workflow instructions.

---

## 13. AI-Use Declaration

Our team used **ChatGPT (OpenAI)** and **Claude (Anthropic)** as AI-assisted tools during work on TaskTrack.

These tools were used to assist with project documentation, writing and revision, explaining software engineering concepts, and reviewing project materials. AI assistance also supported parts of the design and development process.

AI-generated suggestions were treated as supporting material rather than automatically accepted as final work. Team members were responsible for reviewing the content, making necessary corrections, and checking that it matched the project requirements and our intended design.

We used our Project 1 requirements, use cases, professor feedback, and Project 2 grading rubric to guide the final deliverables.

We acknowledge the use of ChatGPT and Claude and the importance of checking AI-assisted work for accuracy and consistency.

---

## 14. Project 2 Submission

**Project:** TaskTrack — Student Assignment Management System  
**Course:** CS 3354 — Software Engineering  
**Milestone:** Project 2 — Analysis and High-Level Design  
**Due Date:** November 8, 2026, at 11:59 PM CT

**Submission Requirement:** One team PDF containing the repository URL.

**GitHub Repository:**

https://github.com/ahneematallah-boop/TaskTrack-CS3354

The repository contains the Project 1 and Project 2 documentation, design diagrams, implementation files, prototype, and available individual contribution evidence.

---

## Conclusion

TaskTrack is intended to provide students with a simple way to manage their courses, assignments, and deadlines.

Project 1 established the problem, requirements, and use cases. Project 2 builds on that foundation through system architecture, high-level design, sequence diagrams, requirements traceability, design rationale, and prototype development.

The team will continue using these documents to guide implementation, testing, and future improvements.
