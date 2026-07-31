### Basic Priority-Inheritance and Priority-Ceiling Protocols for Resources Sharing in Real Time System

- **Priority inheritance protocol** and **priority ceiling protocol** are two protocols belonging to the priority inheritance protocols class.
- Both protocols solve the uncontrolled priority inversion problem.
- The priority ceiling protocol solves this uncontrolled priority inversion problem particularly well; it reduces the worst-case task-blocking time to at most the duration of execution of a single critical section of a lower-priority task.
- This protocol also prevents the formation of deadlocks.
- Sufficient conditions under which a set of periodic tasks using this protocol may be scheduled is derived.
- Priority Ceiling Protocol is a job task synchronization protocol in a real-time system that is better than Priority inheritance protocol in many ways.
- Real-Time Systems are multitasking systems that involve the use of semaphore variables, signals, and events for job synchronization.
- In real-time computing, the priority ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority Inheritance protocols are greedy while Priority Ceiling protocols are not.
- The allocation rule of priority inheritance protocol lets the requesting job have a resource whenever the resource is free but in case of priority ceiling protocol, a job may be denied its requested resource even when the resource is free at the time.