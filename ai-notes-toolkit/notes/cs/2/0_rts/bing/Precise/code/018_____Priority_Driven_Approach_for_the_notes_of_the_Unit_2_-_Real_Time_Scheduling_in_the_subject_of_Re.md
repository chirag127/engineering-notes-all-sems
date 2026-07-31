### Priority Driven Approach

Priority-driven scheduling is a method used in real-time systems to schedule tasks based on their priority levels. In this approach, tasks with higher priority are executed before tasks with lower priority. The priority of a task can be determined by various factors such as deadline, criticality, or importance.

Some key points to note about priority-driven scheduling are:

1. Tasks are assigned priorities based on their importance or urgency.
2. The scheduler selects the highest priority task for execution.
3. If two tasks have the same priority, the scheduler may use other criteria such as the earliest deadline first to determine which task to execute.
4. Priority-driven scheduling can be either preemptive or non-preemptive.
5. In preemptive scheduling, a higher priority task can interrupt a lower priority task that is currently executing.
6. In non-preemptive scheduling, a lower priority task that is currently executing will not be interrupted by a higher priority task.
7. Priority inversion can occur when a lower priority task holds a resource needed by a higher priority task.
