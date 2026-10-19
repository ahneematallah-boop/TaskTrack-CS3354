# TaskTrack – Use Cases

TaskTrack is a website that helps college students keep track of their assignments, exams, and deadlines. The use cases below explain how a student would use the main features of the application.

## Actors

The **student** is the main user of TaskTrack. Students add their own courses and schoolwork, check what's due, and update assignments as they finish them. Professors provide assignments and due dates, but they do not use TaskTrack directly.

## Use Case Summary

| Use Case | Description | Related Requirements |
| --- | --- | --- |
| UC-01 | Add a course | FR-5.3, FR-2.7 |
| UC-02 | Edit or delete a course | FR-5.4, FR-2.7 |
| UC-03 | Add an assignment or exam | FR-2.1, FR-2.2, FR-2.3, FR-2.7, FR-5.1, FR-5.3, FR-6.2 |
| UC-04 | Edit an assignment or exam | FR-2.4, FR-2.3, FR-2.7, FR-6.2 |
| UC-05 | Delete an assignment or exam | FR-2.5, FR-2.6, FR-2.7, FR-6.1 |
| UC-06 | View upcoming assignments | FR-3.1, FR-3.2, FR-3.3, FR-6.2 |
| UC-07 | Mark an assignment complete or incomplete | FR-4.1, FR-4.2, FR-4.3, FR-4.4, FR-2.7 |
| UC-08 | View dashboard | FR-6.1, FR-6.2, FR-6.3, FR-6.4, FR-3.4 |
| UC-09 | Filter assignments by course or status | FR-5.2, FR-5.4 |
| UC-10 | Return to saved assignments | FR-2.7, FR-6.2, NFR-6 |

## Detailed Use Cases

### UC-01: Add a Course

**Actor:** Student  
**Goal:** Add a new class to organize related academic tasks.  
**Preconditions:** TaskTrack is open.  
**Trigger:** Student selects **Add Course**.  
**Main success scenario:**

1. Student opens the Add Course form.
2. TaskTrack asks for a course name and optional course code.
3. Student enters a name such as `Software Engineering` and selects Save.
4. TaskTrack validates the submitted fields.
5. TaskTrack stores the new course and displays it in the course list and task course selector.
**Alternate and exception flows:** A1 (step 4): Blank/whitespace-only course name -> show inline validation error; do not save. A2 (step 3): Student cancels -> close form; do not save. E1 (step 5): Storage error -> show an actionable error; keep entered fields available for retry.  
**Success postcondition:** Exactly one course has been added and can be selected when creating tasks.  
**Trace:** FR-5.3, FR-2.7; tests TC-01, TC-09.

### UC-02: Edit or Delete a Course

**Actor:** Student  
**Goal:** Correct a course name or remove an unused course.  
**Preconditions:** At least one course exists.  
**Trigger:** Student chooses Edit or Delete on a course.  
**Main success scenario (edit):**

1. Student selects the course and chooses Edit.
2. TaskTrack fills the form with current course information.
3. Student changes the name and saves.
4. TaskTrack validates and persists the name change.
5. All tasks previously linked to the course display its updated name.
**Alternate and exception flows:** A1 (step 3): Blank name -> reject; keep the prior saved name. A2: Student selects Delete on a course with no linked tasks -> request confirmation, then remove only if confirmed. A3: Student selects Delete on a course that has tasks -> block deletion and explain that tasks must be reassigned or removed first. A4: Student cancels -> leave course unchanged. E1: Storage failure -> keep prior data unchanged.  
**Success postcondition:** Rename retains task associations; safe delete removes only an empty course.  
**Trace:** FR-5.4, FR-2.7; TC-02, TC-13.

### UC-03: Add an Assignment or Exam

**Actor:** Student  
**Goal:** Record a deadline for an assignment, quiz, or exam.  
**Preconditions:** At least one course exists.  
**Trigger:** Student selects **Add Task**.  
**Main success scenario:**

1. TaskTrack presents fields for title, course, due date, optional due time, description, and optional type.
2. Student enters `Requirements worksheet`, selects `CS 3354`, and sets a due date.
3. Student selects Save.
4. TaskTrack validates required fields and applies the documented default time when omitted.
5. TaskTrack saves the task as Pending and shows it in the list at the correct deadline position.
**Alternate and exception flows:** A1 (step 1): No course exists -> direct student to UC-01, without losing the intent to add a task. A2 (step 4): Missing title/course/date or invalid date -> show field errors; do not persist. A3 (step 3): Cancel -> do not create a task. A4 (step 2): Due date is in the past -> allow save and display Overdue if status is Pending. E1 (step 5): Save fails -> no duplicate/partial task; keep the form available.  
**Success postcondition:** One Pending task is persisted with a course association and deadline.  
**Trace:** FR-2.1, FR-2.2, FR-2.3, FR-2.7, FR-5.1, FR-5.3, FR-6.2; TC-03, TC-10, TC-12.

### UC-04: Edit an Assignment or Exam

**Actor:** Student  
**Goal:** Correct a recorded deadline or task detail.  
**Preconditions:** Task already exists.  
**Trigger:** Student selects Edit on a task.  
**Main success scenario:**

1. TaskTrack displays the task's existing values.
2. Student changes title, course, deadline, description, or type.
3. Student selects Save.
4. TaskTrack validates the update, saves it to the existing task record, and updates all relevant views.
**Alternate and exception flows:** A1: Required field removed -> show validation message without saving. A2: Cancel -> keep original record. A3: Deadline changed from future to past -> overdue classification recalculates if Pending. E1: Save error -> original version remains; edited fields remain available.  
**Success postcondition:** The existing task is updated, not duplicated.  
**Trace:** FR-2.4, FR-2.3, FR-2.7, FR-6.2; TC-04.

### UC-05: Delete an Assignment or Exam

**Actor:** Student  
**Goal:** Remove a task entered accidentally or no longer relevant.  
**Preconditions:** Task exists.  
**Trigger:** Student selects Delete.  
**Main success scenario:**

1. TaskTrack displays a confirmation with the selected task title.
2. Student confirms deletion.
3. TaskTrack deletes only that task.
4. TaskTrack refreshes list and dashboard counts.
**Alternate and exception flows:** A1 (step 2): Cancel -> task remains. E1 (step 3): Storage error -> task remains and an error is shown.  
**Success postcondition:** The confirmed task no longer appears and is not restored on reload.  
**Trace:** FR-2.5, FR-2.6, FR-2.7, FR-6.1; TC-05.

### UC-06: View Upcoming Assignments

**Actor:** Student  
**Goal:** Determine what to work on next.  
**Preconditions:** App is open; task list may be empty.  
**Trigger:** Student selects Upcoming or opens the task list.  
**Main success scenario:**

1. TaskTrack loads Pending tasks.
2. TaskTrack evaluates each due timestamp against the current time.
3. TaskTrack sorts Pending tasks from earliest deadline to latest; ties use title.
4. Student reviews sorted tasks with course, due time, and Overdue label where applicable.
**Alternate and exception flows:** A1: No Pending tasks -> show empty-state text and an Add Task action. A2: Two tasks share a due timestamp -> sort deterministically by title. E1: Read error -> show error instead of incorrect zero counts.  
**Success postcondition:** Student sees an accurate ordered list of Pending work.  
**Trace:** FR-3.1, FR-3.2, FR-3.3, FR-6.2; TC-06, TC-10.

### UC-07: Mark an Assignment Complete or Incomplete

**Actor:** Student  
**Goal:** Track finished work and correct completion mistakes.  
**Preconditions:** Task exists.  
**Trigger:** Student selects its status control.  
**Main success scenario:**

1. Student marks a Pending task Completed.
2. TaskTrack saves Completed status.
3. TaskTrack removes the task from the Pending/Overdue totals and adds it to Completed total.
4. Student can reopen the task by selecting Pending.
5. TaskTrack restores it to Pending and recalculates whether its deadline has passed.
**Alternate and exception flows:** A1: Task is already Completed -> present Reopen option, not duplicate the record. E1: Status save fails -> original state remains visible with an error.  
**Success postcondition:** Task status and summaries agree and survive reload.  
**Trace:** FR-4.1, FR-4.2, FR-4.3, FR-4.4, FR-2.7; TC-07, TC-08.

### UC-08: View the Dashboard

**Actor:** Student  
**Goal:** Check overall workload at a glance.  
**Preconditions:** App is open.  
**Trigger:** Student visits Dashboard.  
**Main success scenario:**

1. TaskTrack loads tasks from storage.
2. TaskTrack computes Pending, Completed, and Overdue counts using defined status rules.
3. TaskTrack shows a short list of next-due Pending tasks.
4. Student selects a task to view its details or opens the complete task list.
**Alternate and exception flows:** A1: No tasks -> show three zero counts and a useful empty-state message. A2: A past-due task is Completed -> count it in Completed, not Overdue. E1: Load fails -> show an error, not invented zeros.  
**Success postcondition:** Counts and preview are consistent with the underlying task list.  
**Trace:** FR-6.1, FR-6.2, FR-6.3, FR-6.4, FR-3.4; TC-08.

### UC-09: Filter Assignments

**Actor:** Student  
**Goal:** Focus on work for one course or completion state.  
**Preconditions:** At least one task exists.  
**Trigger:** Student changes a filter.  
**Main success scenario:**

1. Student selects one course or All Courses.
2. Student selects Pending, Completed, or All Statuses.
3. TaskTrack displays tasks matching both filters, retaining due-date ordering where applicable.
4. Student clears filters to return to the full list.
**Alternate and exception flows:** A1: No matching tasks -> show `No matching tasks` and option to clear filters. A2: Previously selected course is removed -> reset to All Courses.  
**Success postcondition:** Filters restrict only the view, never delete tasks.  
**Trace:** FR-5.2, FR-5.4; TC-11.

### UC-10: Return to Saved Assignments

**Actor:** Student  
**Goal:** Continue tracking work without re-entering it.  
**Preconditions:** Student previously created at least one course and task and saved a completion status.  
**Trigger:** Student reloads or reopens TaskTrack in the same configured workspace.  
**Main success scenario:**

1. Student reopens the application.
2. TaskTrack reads persisted courses and tasks.
3. TaskTrack reconstructs the list, associations, statuses, and dashboard counts.
4. TaskTrack re-evaluates overdue deadlines using the current time.
**Alternate and exception flows:** A1: Saved dataset is empty -> show an intentional empty state. E1: Storage unavailable/corrupt -> display a recovery error without silently overwriting stored data.  
**Success postcondition:** Previously saved valid records reappear with correct current deadline labels.  
**Trace:** FR-2.7, FR-6.2, NFR-6; TC-09, TC-10.

## Requirements Traceability

The use case summary above links each use case to the requirements it supports. Requirement IDs refer to [Requirements](Requirements.md); the Docs Review traceability check verifies every ID on each pull request.
