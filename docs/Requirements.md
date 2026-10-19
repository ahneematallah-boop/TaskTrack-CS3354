# TaskTrack – Requirements

> Student Assignment Management System · Version 1.0

## Contents

- [Priority Key](#priority-key)
- [1. Functional Requirements (FR)](#1-functional-requirements-fr)
  - [1.1 Account Access](#11-account-access)
  - [1.2 Assignment Management](#12-assignment-management)
  - [1.3 Upcoming Assignments View](#13-upcoming-assignments-view)
  - [1.4 Completion Status](#14-completion-status)
  - [1.5 Course Organization](#15-course-organization)
  - [1.6 Dashboard](#16-dashboard)
- [2. Non-Functional Requirements (NFR)](#2-non-functional-requirements-nfr)
  - [2.1 Usability](#21-usability)
  - [2.2 Reliability and Data Integrity](#22-reliability-and-data-integrity)
  - [2.3 Performance](#23-performance)
  - [2.4 Compatibility and Responsiveness](#24-compatibility-and-responsiveness)
  - [2.5 Security and Privacy](#25-security-and-privacy)
  - [2.6 Maintainability](#26-maintainability)

---

## Priority Key

| Priority | Meaning |
| :------- | :------ |
| **High** | Must have for version 1.0 |
| **Medium** | Should have |
| **Low** | Nice to have |

---

## 1. Functional Requirements (FR)

### 1.1 Account Access

| ID | Requirement | Priority |
| :-- | :---------- | :------- |
| FR-1.1 | The system shall allow a student to register and log in so that their assignments are stored privately. *(May be simplified to single-user mode if the team decides accounts are out of scope.)* | Medium |
| FR-1.2 | The system shall show a student only their own assignments and courses. | Medium |

### 1.2 Assignment Management

| ID | Requirement | Priority |
| :-- | :---------- | :------- |
| FR-2.1 | The system shall allow a student to create an assignment with a title, course name, description, and due date. | High |
| FR-2.2 | The system shall require a title, course, and due date, and shall allow the description to be left blank. | High |
| FR-2.3 | The system shall reject invalid input (for example, an empty title or an incorrectly formatted date) and display a clear error message. | High |
| FR-2.4 | The system shall allow a student to edit any field of an existing assignment. | High |
| FR-2.5 | The system shall allow a student to delete an assignment. | High |
| FR-2.6 | The system shall ask the student to confirm before an assignment is permanently deleted. | High |
| FR-2.7 | The system shall save all assignment changes so they are still present after the student closes and reopens the application. | High |

### 1.3 Upcoming Assignments View

| ID | Requirement | Priority |
| :-- | :---------- | :------- |
| FR-3.1 | The system shall display assignments sorted by due date, with the earliest deadline first. | High |
| FR-3.2 | The system shall show each assignment's title, course, and due date in the list. | High |
| FR-3.3 | The system shall visually distinguish overdue assignments from other assignments. | High |
| FR-3.4 | The system shall show the full details of an assignment when the student selects it. | High |

### 1.4 Completion Status

| ID | Requirement | Priority |
| :-- | :---------- | :------- |
| FR-4.1 | The system shall allow a student to mark an assignment as completed. | High |
| FR-4.2 | The system shall allow a student to change a completed assignment back to incomplete. | High |
| FR-4.3 | The system shall visually distinguish completed assignments from incomplete ones. | High |
| FR-4.4 | The system shall update dashboard counts immediately when an assignment's status changes. | High |

### 1.5 Course Organization

| ID | Requirement | Priority |
| :-- | :---------- | :------- |
| FR-5.1 | The system shall allow a student to assign each assignment to a course. | High |
| FR-5.2 | The system shall allow a student to view the assignments for a single selected course. | High |
| FR-5.3 | The system shall allow a student to add a new course while creating an assignment or from a course list. | High |
| FR-5.4 | The system shall list all of the student's courses and allow the student to filter by any one of them. | High |

### 1.6 Dashboard

| ID | Requirement | Priority |
| :-- | :---------- | :------- |
| FR-6.1 | The system shall provide a dashboard showing the number of pending, completed, and overdue assignments. | High |
| FR-6.2 | The system shall classify an assignment as overdue when its due date has passed and it is not completed. | High |
| FR-6.3 | The system shall allow the student to open the list of assignments behind each dashboard count. | High |
| FR-6.4 | The dashboard shall show the next assignment(s) due so the student can see what to work on next. | High |

---

## 2. Non-Functional Requirements (NFR)

### 2.1 Usability

| ID | Requirement |
| :-- | :---------- |
| NFR-1 | A first-time student shall be able to add an assignment without instructions or training. |
| NFR-2 | Core actions (add, edit, delete, mark complete) shall be reachable within two clicks or taps from the main screen. |
| NFR-3 | The interface shall use consistent layouts, labels, and colors throughout. |

### 2.2 Reliability and Data Integrity

| ID | Requirement |
| :-- | :---------- |
| NFR-4 | Saved assignment data shall not be lost or altered incorrectly during normal use. |
| NFR-5 | Assignments shall always be displayed in the correct deadline order. |
| NFR-6 | The system shall show an error message, rather than failing silently, if saving or loading data fails. |

### 2.3 Performance

| ID | Requirement |
| :-- | :---------- |
| NFR-7 | Pages and list views shall load within 3 seconds under normal conditions for a typical student (up to about 200 assignments). |
| NFR-8 | Adding, editing, or completing an assignment shall be reflected on screen within 1 second. |

### 2.4 Compatibility and Responsiveness

| ID | Requirement |
| :-- | :---------- |
| NFR-9 | The application shall work correctly in the latest versions of Chrome, Firefox, Safari, and Edge. |
| NFR-10 | The layout shall adapt to different screen sizes, including phones and tablets, through the browser (no native mobile app). |

### 2.5 Security and Privacy

| ID | Requirement |
| :-- | :---------- |
| NFR-11 | If accounts are implemented, passwords shall be stored securely (hashed, never as plain text). |
| NFR-12 | User input shall be validated and sanitized to prevent common attacks such as script injection. |

### 2.6 Maintainability

| ID | Requirement |
| :-- | :---------- |
| NFR-13 | Code shall be organized into clear front-end, back-end, and data layers and documented well enough for any team member to work on it. |
| NFR-14 | The team shall use version control and review changes before merging. |
