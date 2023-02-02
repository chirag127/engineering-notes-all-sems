### Priority Driven Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System
Priority Driven Approach: 
- A real-time scheduling algorithm that assigns priorities to tasks based on their criticality.
- Tasks with higher priority are given more CPU time compared to lower priority tasks.
- Preemptive scheduling: Higher priority task can interrupt a lower priority task.
- Non-preemptive scheduling: Once a task starts execution, it continues until completion.
- Priority inversion: When a lower priority task holds a resource needed by a higher priority task, leading to the higher priority task being blocked.
- Priority inheritance: A technique to prevent priority inversion by temporarily boosting the priority of the task holding the resource.
- Rate Monotonic: A priority assignment algorithm where tasks with shorter periods are assigned higher priority.
- Earliest Deadline First: A priority assignment algorithm where tasks with earlier deadlines are assigned higher priority.
