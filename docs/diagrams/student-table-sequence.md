TaskTrack sequence: Add, complete, and reload a task

Participants: Student, TaskTrack UI, Task logic, Input validation, Storage

1. Student opens Add Task.
2. TaskTrack UI shows the task form.
3. Student enters the title, course, due date, and optional details.
4. UI sends the task to Task logic.
5. Task logic asks Input validation to check the required fields and date.

   If the input is invalid:
   - Validation returns errors.
   - UI shows the errors and keeps the form open.

   If the input is valid:
   - Task logic asks Storage to save the task as Pending.
   - If saving fails, UI shows an error and keeps the entered details.
   - If saving succeeds, Task logic sorts tasks by deadline and updates the dashboard.
   - UI shows the saved task in the list.

6. Student marks the task Completed.
7. Task logic saves the new status and recalculates the dashboard counts.
8. UI shows the Completed status and updated counts.

9. Later, Student reopens TaskTrack.
10. TaskTrack loads saved courses and tasks from Storage.
11. Task logic recalculates overdue labels and dashboard counts.
12. UI shows the restored, up-to-date work.