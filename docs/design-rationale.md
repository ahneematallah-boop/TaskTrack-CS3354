# TaskTrack — P2 Design Rationale

**Course:** CS 3354 – Software Engineering  
**Project:** TaskTrack – Student Assignment Management System  
**Contributor:** Jacqueline Rodriguez  
**Milestone:** Project 2 – Analysis and High-Level Design

## 1. Purpose

TaskTrack is intended to facilitate organization of the student's courses, assignments, exams, deadlines in one system. Design considerations for this system include: usability, maintainability, reliability, security and simplicity.

In order to decide upon an implementation for this task, we took into account the requirements developed in the Project 1 and the use cases from Project 2.

## 2. Design Decisions and Alternatives

### 2.1 Application Structure

We propose to separate the user interface, application logic and data storage.

User interface provides the possibility for the student to manage his assignments and courses. The application logic takes care of validating the entered data, manipulating the statuses of the assignments, calculating the due date and counting the dashboard totals. The data storage preserves the information of the student.

Two options can be considered here:

- **Option A: Layered design.** The user interface, application logic and data storage are separated from each other.
- **Option B: Tightly coupled design.** The same component contains more responsibilities.

We recommend the Option A as it improves maintainability of TaskTrack. For example, the change of how overdue status of assignments is calculated does not have to affect dashboard.

The trade-off consists of the extra initial organization required for a layered design.

**Related use cases:** UC-03, UC-06, UC-07, UC-08, UC-10.

### 2.2 Dashboard and Assignment Organization

Students have to find out about deadlines in the upcoming weeks without opening all the courses.

We considered two ways of doing this task:

- **Option A:** Provide students with a dashboard which includes the list of upcoming assignments and dashboard totals.
- **Option B:** Provide the student with a course-only view requiring the opening of each course.

We propose the Option A which provides faster access for students.

The dashboard must include numbers of pending, completed and overdue assignments and allow filtering the assignments according to their course and/or status.

The possible trade-off of this design is the information overload which can be avoided by providing the most important information first.

**Related use cases:** UC-06, UC-08, UC-09.

### 2.3 Assignment Status and Overdue Calculation

It has to be possible for TaskTrack to differentiate pending, completed and overdue assignments.

We considered two possible ways:

- **Option A:** Save Pending
**Option B:** Enable saving and deleting immediately without further checks.

We recommend Option A as it allows avoiding user errors.

For instance, TaskTrack should verify that the assignment has a proper title, course, and due date. Prior to deleting an assignment, TaskTrack should ask user to confirm his/her intention.

In case the user fails to save or delete his/her task, TaskTrack should notify the user about the failure and keep the previously saved information.

On the other hand, validation and confirmation increase the number of actions.

**Related use cases:** UC-01, UC-02, UC-03, UC-04, UC-05.

### 2.5 Data Storage and Reliability

Students must have ability to close TaskTrack and use it again at some point in time without any problems.

There are two possible approaches here:

**Option A:** Persistently stored information about courses, assignments and completion statuses.

**Option B:** Temporarily stored information only until current session ends.

We recommend Option A since students need access to previously saved information.

In case it is impossible to load information, TaskTrack should notify user about error and show him/her information about empty list of assignments instead of an incorrect view.

Persistently stored information requires more error handling, however it is necessary to implement the core goal of the application.

**Related use case:** UC-10.

## 3. Quality Attributes

| Quality Attribute | Design Approach | Benefit |
| --- | --- | --- |
| Usability | Dashboard, filters, and simple forms | Students can manage assignments easily |
| Maintainability | Separation of responsibilities | Easier to update and test |
| Reliability | Validation, error handling, and persistent storage | Reduces incorrect or lost information |
| Data consistency | Calculated overdue status and dashboard totals | Keeps displayed information accurate |
| Security | Input validation and appropriate access controls | Helps prevent unauthorized changes |
| Simplicity | Focus on courses, assignments, and deadlines | Avoids unnecessary complexity |

## 4. Security Considerations

TaskTrack should verify the information prior to saving the changes as well as protect the student information.

In Project 1 it is stated that making account registration optional. If accounts are used, the design should support authentication and access only to specific student data. Also passwords must be safely hashed and not stored in plain text format.

In case the team decides to use single-user prototype, multi-user authentication must be recognized as out-of-scope requirement.

This approach allows focusing on prototype development and taking into account security considerations in the future.

## 5. Overall Trade-offs

| Design Decision | Recommended Approach | Advantage | Trade-off |
| --- | --- | --- | --- |
| Application structure | Layered design | Easier maintenance | More initial organization |
| Assignment display | Dashboard with filters | Faster access to deadlines | May become crowded |
| Assignment status | Calculate overdue dynamically | More consistent data | Requires date calculations |
| Saving and deletion | Validation and confirmation | Prevents accidental mistakes | Additional steps |
| Data storage | Persistent storage | Preserves student information | Requires error handling |

## 6. Conclusion

The presented design ensures the simplicity, reliability, and effectiveness of TaskTrack.

Recommendation is to separate functionality, use dashboard, validate the input information of assignments, calculate deadline of them dynamically, and use persistent storage for saved assignments.

These approaches meet the Project 1 specifications and use cases from Project 2.

Further technical decisions must be verified with the Architecture and Prototype Team.
