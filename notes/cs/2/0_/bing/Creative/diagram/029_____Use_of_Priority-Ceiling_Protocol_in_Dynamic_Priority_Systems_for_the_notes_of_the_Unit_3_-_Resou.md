### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique that prevents priority inversion and deadlock in real-time systems that share resources among tasks.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a resource needed by the high-priority task.
- Deadlock occurs when two or more tasks are waiting for each other to release a resource, resulting in a circular dependency.
- In priority-ceiling protocol, each resource is assigned a priority ceiling, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the current priority ceiling of the system, which is the maximum of the priority ceilings of all the locked resources.
- If a task is blocked by a lower-priority task that holds a resource, the blocked task inherits the priority of the blocking task, thus avoiding priority inversion.
- In dynamic priority systems, the priorities of the tasks may change over time, depending on factors such as deadlines, arrival times, or execution times.
- Therefore, the priority ceilings of the resources may also change over time, depending on the current priorities of the tasks that can access them.
- To use priority-ceiling protocol in dynamic priority systems, the priority ceilings of the resources and the system must be updated each time the task priorities change.
- This ensures that the resource access control is consistent with the current task priorities and prevents priority inversion and deadlock.
- For example, consider a system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in a deadline-driven system, where the first number is the period and the second number is the execution time.
- Assume that both tasks share a resource X, and T1 has higher priority than T2 at time 0.
- The priority ceiling of X is initially 1, which is the priority of T1.
- At time 0, T1 locks X and starts executing.
- At time 2, T2 arrives and requests X, but is blocked by T1.
- At time 4, T1 releases X and finishes its execution.
- At this point, the priority of T2 becomes higher than T1, because T2 has a shorter deadline than T1.
- Therefore, the priority ceiling of X is updated to 2, which is the priority of T2.
- T2 locks X and starts executing.
- At time 5, T1 arrives again and requests X, but is blocked by T2.
- T1 inherits the priority of T2, thus avoiding priority inversion.
- At time 6.3, T2 releases X and finishes its execution.
- T1 locks X and resumes its execution.
- At time 7, T2 arrives again and requests X, but is blocked by T1.
- T2 inherits the priority of T1, thus avoiding priority inversion.
- At time 7.9, T1 releases X and finishes its execution.
- T2 locks X and resumes its execution.
- At time 9.6, T2 releases X and finishes its execution.
- The system is free of priority inversion and deadlock, thanks to the use of priority-ceiling protocol and the dynamic update of the priority ceilings.

: Use of Priority Ceiling Protocol in Dynamic Priority Systems: https://benchpartner.com/use-of-priority-ceiling-protocol-in-dynamic-priority-systems
: Priority ceiling protocol - Wikipedia: https://en.wikipedia.org/wiki/Priority_ceiling_protocol
: Priority Ceiling Protocol - GeeksforGeeks: https://www.geeksforgeeks.org/priority-ceiling-protocol/