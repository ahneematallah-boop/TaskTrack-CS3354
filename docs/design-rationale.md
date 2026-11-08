# TaskTrack — P2 Design Rationale

**Course:** CS 3354 – Software Engineering
**Project:** TaskTrack – Student Assignment Management System
**Contributor:** Jacqueline Rodriguez
**Milestone:** Project 2 – Analysis and High-Level Design

## 1. Purpose

TaskTrack is designed to help students organize their courses, assignments, exams, and deadlines in one place. The goal is to make it easier for students to see what they need to finish and keep track of their progress.

For Project 2, we considered different ways to design the system while keeping the requirements from Project 1 in mind. Our main priorities are usability, reliability, maintainability, security, and simplicity.

This document explains the design decisions we recommend, the alternatives we considered, and the trade-offs involved.

## 2. Design Decisions and Alternatives

### 2.1 Application Structure

We propose separating TaskTrack into three main layers: the user interface, application logic, and data storage.

The user interface allows students to add courses, manage assignments, and view their dashboard. The application logic handles input validation, assignment status, due dates, and dashboard calculations. The data layer stores courses and assignments.

We considered two options:

- **Option A: Layered design.** Keep the interface, logic, and storage responsibilities separate.
- **Option B: Tightly coupled design.** Put most of the functionality together in fewer components.

We recommend Option A because it makes the system easier to maintain and test. For example, changing how overdue assignments are calculated should not require rewriting the dashboard interface.

The trade-off is that a layered design requires more initial planning and organization.

**Related requirements:** NFR-13, NFR-14.
**Related use cases:** UC-03, UC-06, UC-07, UC-08, UC-10.

### 2.2 Dashboard and Assignment Organization

Students need a quick way to see upcoming deadlines without opening each course individually.

We considered two options:

- **Option A: Dashboard with upcoming assignments, status counts, and filters.**
- **Option B: Course-only view where students open each course to see its assignments.**

We recommend Option A because students can see their most important deadlines in one place.

The dashboard should show pending, completed, and overdue assignment counts. Students should also be able to filter assignments by course and status.

The trade-off is that showing too much information can make the dashboard crowded. We can reduce this problem by displaying the most important information first and keeping the layout simple.

**Related requirements:** FR-3.1, FR-3.2, FR-5.2, FR-5.4, FR-6.1, FR-6.3, FR-6.4, NFR-1, NFR-2.
**Related use cases:** UC-06, UC-08, UC-09.

### 2.3 Assignment Status and Overdue Calculation

TaskTrack needs to distinguish between pending, completed, and overdue assignments.

We considered two options:

- **Option A: Calculate overdue status using the assignment's due date and completion status.**
- **Option B: Store overdue status as a separate value that must be updated whenever an assignment changes.**

We recommend Option A. When an incomplete assignment passes its deadline, TaskTrack can classify it as overdue automatically. A completed assignment should not be considered overdue.

This approach avoids storing outdated overdue information. It also makes the dashboard more consistent when a student changes an assignment's due date or completion status.

The trade-off is that the system must recalculate overdue status when displaying assignments or updating dashboard totals.

**Related requirements:** FR-3.3, FR-4.1, FR-4.2, FR-4.3, FR-4.4, FR-6.1, FR-6.2.
**Related use cases:** UC-06, UC-07, UC-08.

### 2.4 Input Validation and Deletion Confirmation

Students may accidentally enter incorrect assignment information or delete something they still need.

We considered two options:

- **Option A: Validate assignment information and confirm deletion before removing saved data.**
- **Option B: Save or delete information immediately without validation or confirmation.**

We recommend Option A because it helps prevent avoidable mistakes.

TaskTrack should require an assignment title, course, and valid due date. If the student enters invalid information, the system should display an error and allow the student to correct it.

Before permanently deleting an assignment, TaskTrack should request confirmation. If the student cancels, the assignment should remain unchanged.

The trade-off is that validation and confirmation require extra interactions, but these steps help protect the student's information.

**Related requirements:** FR-2.1, FR-2.2, FR-2.3, FR-2.4, FR-2.5, FR-2.6, NFR-6.
**Related use cases:** UC-03, UC-04, UC-05.

### 2.5 Data Storage and Reliability

Students need their saved assignments to remain available after closing and reopening TaskTrack.

We considered two options:

- **Option A: Persistent storage for courses, assignments, due dates, and completion statuses.**
- **Option B: Temporary storage that only lasts during the current session.**

We recommend Option A because keeping assignments between sessions is one of TaskTrack's main requirements.

When a student saves an assignment, the system should preserve the information and load it again when the application is reopened.

If saving or loading fails, TaskTrack should display an error rather than silently losing information. The interface should also avoid presenting a failed load as an intentionally empty assignment list.

Persistent storage requires additional error handling, but it is necessary for TaskTrack to be useful.

**Related requirements:** FR-2.7, NFR-4, NFR-5, NFR-6.
**Related use cases:** UC-01, UC-03, UC-04, UC-05, UC-07, UC-10.

## 3. Quality Attributes

The following quality attributes explain what the design should support and how the team can evaluate it.

The measurable targets below are proposed design and acceptance targets, not completed test results. They should be confirmed with the team and checked during implementation and testing.

| Quality Attribute | Design Approach | Proposed Measure or Target |
| --- | --- | --- |
| Usability | Simple forms, dashboard, and clear labels | A first-time student should be able to add an assignment without instructions. Core actions should be accessible within two clicks or taps from the main screen. |
| Performance | Keep assignment loading and calculations efficient | Pages and lists should load within 3 seconds with up to 200 assignments under normal test conditions. |
| Responsiveness | Update views after assignment changes | Assignment changes should appear on screen within 1 second. |
| Reliability | Persistent storage and error handling | Saved assignments should remain available after reopening the application. Failed saves and loads should show an error. |
| Data consistency | Calculate overdue status from deadlines and completion | Dashboard counts and assignment statuses should match the stored data after each successful change. |
| Security | Validate input and restrict access if accounts are supported | Invalid input should be rejected, and passwords must never be stored in plain text if accounts are implemented. |
| Maintainability | Separate the interface, application logic, and data storage | Code should have clear responsibilities and changes should be reviewed before merging. |
| Compatibility | Responsive browser-based interface | The application should work in current versions of Chrome, Firefox, Safari, and Edge, including mobile-sized layouts. |

**Related requirements:** NFR-1 through NFR-14.

The team can evaluate these targets using basic functional tests, timing checks, browser testing, and review of the implementation.

## 4. Security Considerations

TaskTrack should validate user input before saving data and avoid exposing student information unnecessarily.

Project 1 includes optional account requirements, FR-1.1 and FR-1.2. The team must decide whether account registration and login are part of the current implementation.

If accounts are implemented, TaskTrack should authenticate users, restrict access to their own information, and store passwords using secure password hashing.

If the team chooses a single-user prototype, FR-1.1 and FR-1.2 should be explicitly marked as deferred. They should not be presented as completed features.

Input validation is still important in either design. It helps prevent invalid information from being stored and supports safer data handling.

**Related requirements:** FR-1.1, FR-1.2, FR-2.3, NFR-11, NFR-12.

## 5. Overall Trade-offs

| Design Decision | Recommended Approach | Advantage | Trade-off |
| --- | --- | --- | --- |
| Application structure | Layered design | Easier maintenance and testing | More initial organization |
| Assignment display | Dashboard with filters | Faster access to deadlines | Can become crowded |
| Assignment status | Calculate overdue dynamically | More consistent information | Requires repeated date calculations |
| Input validation | Validate before saving | Reduces incorrect entries | Adds validation logic |
| Assignment deletion | Require confirmation | Helps prevent accidental deletion | Adds an extra step |
| Data storage | Persistent storage | Preserves assignments between sessions | Requires error handling |
| Account access | Confirm scope before implementation | Avoids unnecessary prototype complexity | Single-user mode does not provide private multi-user accounts |

These decisions focus on making TaskTrack practical for students without adding unnecessary complexity.

## 6. Connection to Project 1 Requirements

The design decisions were selected to support the requirements and use cases already documented in Project 1.

| Design Decision | P1 Requirements | Related Use Cases |
| --- | --- | --- |
| Layered architecture | NFR-13, NFR-14 | UC-03, UC-06, UC-07, UC-08, UC-10 |
| Dashboard and filters | FR-3.1, FR-5.2, FR-5.4, FR-6.1, FR-6.3, FR-6.4 | UC-06, UC-08, UC-09 |
| Dynamic overdue calculation | FR-3.3, FR-4.4, FR-6.2 | UC-06, UC-07, UC-08 |
| Input validation | FR-2.1, FR-2.2, FR-2.3 | UC-03, UC-04 |
| Deletion confirmation | FR-2.5, FR-2.6 | UC-05 |
| Persistent storage | FR-2.7, NFR-4, NFR-6 | UC-03, UC-04, UC-07, UC-10 |
| Optional account access | FR-1.1, FR-1.2, NFR-11 | Requires a team decision |

These connections should remain consistent with the architecture, models, and prototype developed by the other team members.

## 7. Conclusion

For TaskTrack, we recommend a layered design, a dashboard with assignment filters, automatic overdue calculations, input validation, deletion confirmation, and persistent storage.

These decisions support the main requirements from Project 1 while keeping the application manageable for the team.

The main trade-off is that some features require additional logic and planning, but they help make TaskTrack more reliable and easier to use.

The final implementation details, account scope, and proposed quality targets should be confirmed with the architecture and prototype team before the project moves into development.
