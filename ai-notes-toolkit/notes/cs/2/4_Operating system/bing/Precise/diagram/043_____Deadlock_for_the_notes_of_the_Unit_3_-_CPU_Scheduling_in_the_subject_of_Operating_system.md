### Deadlock

Deadlock is a situation in a computer system where two or more processes are unable to proceed because they are waiting for each other to release resources. This results in a circular wait where each process is waiting for the other to release resources, but none of them do, causing the system to be stuck in a state of deadlock.

Some key points to remember about deadlock are:

- Deadlock can occur when there are limited resources and multiple processes competing for them.
- A set of processes is in a deadlock state when every process in the set is waiting for an event that can only be caused by another process in the set.
- There are four necessary conditions for deadlock to occur: mutual exclusion, hold and wait, no preemption, and circular wait.
- Deadlock prevention and avoidance are two strategies used to handle deadlock. Deadlock prevention aims to prevent deadlock by ensuring that at least one of the necessary conditions for deadlock does not hold. Deadlock avoidance, on the other hand, allows the system to enter a deadlock state but provides a mechanism to detect and recover from it.
- Another approach to handling deadlock is deadlock detection and recovery. This involves periodically checking the system for deadlock and taking appropriate action to recover from it, such as terminating one or more processes or releasing resources.
