# Student, P1 use cases, and design components

This sequence diagram traces the Student actor through the Project 1 use cases and the proposed TaskTrack design components. The UI, use-case controller, services, validators, and repositories are logical design components; they describe responsibilities, not existing implementation classes.

The **Student table** is conditional: P1 makes accounts optional. When account access is out of scope, the app uses a single-user context and does not need to read or write a Student table. In account mode, the active student ID scopes course and assignment operations. The table lifelines below represent conceptual storage, not a finalized database schema.

```mermaid
sequenceDiagram
    actor Student
    participant UI as TaskTrack UI
    participant UC as Use-case controller
    participant Auth as Account service
    participant Validator as Input validator
    participant CourseSvc as Course service
    participant TaskSvc as Assignment service
    participant Dashboard as Dashboard service
    participant StudentRepo as Student repository
    participant CourseRepo as Course repository
    participant TaskRepo as Assignment repository
    participant StudentDB as Student table (optional)
    participant CourseDB as Course table
    participant TaskDB as Assignment table

    opt Account mode enabled — FR-1.1, FR-1.2
        Student->>UI: Register or log in
        UI->>UC: Submit credentials
        UC->>Auth: Authenticate or register
        Auth->>StudentRepo: Find or create student
        StudentRepo->>StudentDB: Read/write student record
        StudentDB-->>StudentRepo: Student ID and account result
        StudentRepo-->>Auth: Account result
        Auth-->>UC: Active student context
        UC-->>UI: Show the student's TaskTrack
    end

    rect rgb(238, 246, 255)
        Note over Student,CourseDB: UC-01 Add course — FR-5.3, FR-2.7
        Student->>UI: Enter course details and save
        UI->>UC: Add course request
        UC->>Validator: Check course name
        Validator-->>UC: Valid or field errors
        alt Valid course
            UC->>CourseSvc: Create course for active student
            CourseSvc->>CourseRepo: Insert course
            CourseRepo->>CourseDB: Save course
            CourseDB-->>CourseRepo: Saved course
            CourseRepo-->>CourseSvc: Course
            CourseSvc-->>UC: Course created
            UC-->>UI: Show course in list and selector
        else Invalid course or storage error
            UC-->>UI: Show error; keep form values
        end
    end

    rect rgb(238, 255, 242)
        Note over Student,TaskDB: UC-03 Add assignment — FR-2.1, FR-2.2, FR-2.3, FR-2.7, FR-5.1, FR-5.3, FR-6.2
        Student->>UI: Enter title, course, due date, optional details
        UI->>UC: Add assignment request
        UC->>Validator: Check required fields and date
        Validator-->>UC: Valid or field errors
        alt Valid assignment
            UC->>TaskSvc: Create Pending assignment
            TaskSvc->>CourseRepo: Confirm selected course
            CourseRepo->>CourseDB: Read course
            CourseDB-->>CourseRepo: Course and owner
            CourseRepo-->>TaskSvc: Course is available
            TaskSvc->>TaskRepo: Insert assignment and course link
            TaskRepo->>TaskDB: Save assignment
            TaskDB-->>TaskRepo: Saved assignment
            TaskRepo-->>TaskSvc: Assignment
            TaskSvc-->>UC: Assignment saved; calculate overdue state
            UC-->>UI: Show saved assignment in due-date order
        else Invalid input or save failure
            UC-->>UI: Show error; do not show a successful save
        end
    end

    rect rgb(255, 248, 232)
        Note over Student,TaskDB: UC-04 Edit assignment — FR-2.4, FR-2.3, FR-2.7, FR-6.2
        Student->>UI: Edit assignment fields and save
        UI->>UC: Update request
        UC->>Validator: Validate changed fields
        Validator-->>UC: Valid or field errors
        UC->>TaskSvc: Update existing assignment
        TaskSvc->>TaskRepo: Update assignment by ID
        TaskRepo->>TaskDB: Save changed fields
        TaskDB-->>TaskRepo: Updated assignment
        TaskRepo-->>TaskSvc: Updated assignment
        TaskSvc-->>UC: Recalculate overdue state
        UC-->>UI: Refresh assignment and dashboard
    end

    rect rgb(255, 238, 238)
        Note over Student,TaskDB: UC-05 Delete assignment — FR-2.5, FR-2.6, FR-2.7, FR-6.1
        Student->>UI: Select Delete
        UI-->>Student: Ask for confirmation
        alt Student confirms
            Student->>UI: Confirm deletion
            UI->>UC: Delete request
            UC->>TaskSvc: Delete assignment
            TaskSvc->>TaskRepo: Delete assignment by ID
            TaskRepo->>TaskDB: Remove assignment
            TaskDB-->>TaskRepo: Delete result
            TaskRepo-->>TaskSvc: Delete result
            TaskSvc-->>UC: Refresh dashboard data
            UC-->>UI: Remove task and update counts
        else Student cancels
            Student->>UI: Cancel
            UI-->>Student: Keep assignment
        end
    end

    rect rgb(246, 238, 255)
        Note over Student,TaskDB: UC-06 Upcoming, UC-07 Completion, UC-08 Dashboard, UC-09 Filter — FR-3.1–FR-3.4, FR-4.1–FR-4.4, FR-5.2, FR-5.4, FR-6.1–FR-6.4
        Student->>UI: Open upcoming list/dashboard or choose a filter
        UI->>UC: Request tasks and dashboard data
        UC->>TaskSvc: Load tasks for active student and filter
        TaskSvc->>TaskRepo: Query matching tasks
        TaskRepo->>TaskDB: Read tasks ordered by due date
        TaskDB-->>TaskRepo: Matching assignments
        TaskRepo-->>TaskSvc: Assignments
        TaskSvc-->>UC: Sorted tasks and computed overdue states
        UC->>Dashboard: Calculate pending/completed/overdue counts
        Dashboard-->>UC: Counts and next due assignments
        UC-->>UI: Display list, details, filter results, and dashboard
        UI-->>Student: Show current assignments and counts
        opt Student marks a task complete or incomplete
            Student->>UI: Change completion status
            UI->>UC: Update status
            UC->>TaskSvc: Save status and recompute overdue state
            TaskSvc->>TaskRepo: Update assignment status
            TaskRepo->>TaskDB: Persist status
            TaskDB-->>TaskRepo: Updated assignment
            TaskRepo-->>TaskSvc: Updated assignment
            TaskSvc-->>UC: Refresh dashboard counts
            UC->>Dashboard: Recalculate counts
            Dashboard-->>UC: Updated counts
            UC-->>UI: Show status and updated counts
        end
    end

    rect rgb(235, 250, 250)
        Note over Student,TaskDB: UC-10 Return to saved assignments — FR-2.7, FR-6.2, NFR-6
        Student->>UI: Reopen TaskTrack
        UI->>UC: Load saved data
        UC->>CourseSvc: Load courses for active student
        CourseSvc->>CourseRepo: Read courses
        CourseRepo->>CourseDB: Query saved courses
        CourseDB-->>CourseRepo: Courses
        CourseRepo-->>CourseSvc: Courses
        UC->>TaskSvc: Load assignments for active student
        TaskSvc->>TaskRepo: Read saved assignments
        TaskRepo->>TaskDB: Query saved assignments
        TaskDB-->>TaskRepo: Assignments
        TaskRepo-->>TaskSvc: Assignments
        TaskSvc-->>UC: Recalculate overdue states
        UC->>Dashboard: Recalculate current counts
        Dashboard-->>UC: Counts and next due assignments
        UC-->>UI: Restore saved courses, tasks, and dashboard
        UI-->>Student: Show restored data or a load error
    end

    Note over CourseSvc,TaskDB: UC-02 Edit/delete course — FR-5.4, FR-2.7: validate and persist edits; block deletion while assignments are linked.
```

### Requirement and design trace

| Project 1 use case | Main design path |
| --- | --- |
| UC-01 Add course | UI → use-case controller → input validator → course service/repository → Course table |
| UC-02 Edit/delete course | UI → use-case controller → course service/repository; check assignment links before delete |
| UC-03 Add assignment | UI → use-case controller → input validator → assignment service → course/assignment repositories |
| UC-04 Edit assignment | UI → use-case controller → input validator → assignment service/repository |
| UC-05 Delete assignment | UI confirmation → use-case controller → assignment service/repository |
| UC-06 Upcoming assignments | UI → use-case controller → assignment service/repository → deadline-ordered list |
| UC-07 Completion status | UI → use-case controller → assignment service/repository → dashboard service |
| UC-08 Dashboard | UI → use-case controller → assignment repository → dashboard service |
| UC-09 Filter assignments | UI → use-case controller → assignment service/repository |
| UC-10 Return to saved assignments | UI → use-case controller → course and assignment services/repositories |
| Optional account access | UI → use-case controller → account service → student repository → Student table |

This is a proposed interaction design based on P1 requirements; it does not claim these components or tables have already been implemented.
