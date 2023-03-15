### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique that prevents priority inversion and deadlock in real-time systems that use shared resources .
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a resource needed by the high-priority task.
- Deadlock occurs when two or more tasks are waiting for each other to release a resource, resulting in a circular dependency.
- In priority-ceiling protocol, each resource is assigned a priority ceiling, which is the highest priority of any task that can access that resource .
- A task can lock a resource only if its current priority is higher than the priority ceiling of all the resources currently locked by other tasks .
- This ensures that a task cannot be blocked by a lower-priority task, and that a task cannot cause a deadlock by locking a resource that is needed by a higher-priority task .
- In dynamic priority systems, the priorities of the tasks may change over time, depending on factors such as deadlines, arrival times, or execution times.
- This means that the priority ceilings of the resources may also change over time, depending on the current priorities of the tasks that can access them.
- Therefore, in dynamic priority systems, the priority-ceiling protocol requires updating the priority ceilings of the resources and the system each time the task priorities change.
- The system priority ceiling is the highest priority ceiling of all the resources in the system .
- A task can preempt another task only if its current priority is higher than the system priority ceiling .
- This ensures that a task cannot preempt another task that is holding a resource that is needed by a higher-priority task .
- An example of a dynamic priority system is a deadline-driven system, where the priorities of the tasks are inversely proportional to their deadlines.
- In such a system, the priority of a task may increase or decrease as its deadline approaches or recedes.
- Consider a system with two tasks T1 (2, 0.9) and T2 (5, 2.3), where the first number is the period and the second number is the execution time.
- Assume that both tasks share a resource X, and that T1 has higher priority than T2 at time 0.
- The priority ceiling of X is initially 1, which is the priority of T1.
- The system priority ceiling is also 1.
- At time 0, T1 starts executing and locks X.
- At time 2, T2 arrives and preempts T1, since its priority is higher than the system priority ceiling.
- At time 4, T1's deadline is closer than T2's, so T1's priority becomes higher than T2's.
- The priority ceiling of X also becomes 2, which is the new priority of T1.
- The system priority ceiling also becomes 2.
- T1 preempts T2 and resumes execution, since its priority is higher than the system priority ceiling.
- T1 unlocks X and finishes execution at time 4.9.
- T2 resumes execution and finishes at time 5.2.
- Both tasks meet their deadlines and no priority inversion or deadlock occurs.

: Priority ceiling protocol - Wikipedia
: Priority Ceiling Protocol - GeeksforGeeks
: Use of Priority Ceiling Protocol in Dynamic Priority Systems: - Benchpartner.com