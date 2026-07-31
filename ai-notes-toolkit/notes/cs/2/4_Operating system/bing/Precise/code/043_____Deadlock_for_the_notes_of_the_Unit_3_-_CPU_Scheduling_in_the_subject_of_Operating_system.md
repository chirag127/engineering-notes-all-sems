### Deadlock

Deadlock is a situation that occurs in a computer system when two or more processes are unable to continue executing because they are waiting for each other to release resources. This results in the system being in a state of indefinite waiting, and no progress can be made.

Here are some key points to remember about deadlock:

1. Deadlock occurs when there is a circular wait condition, where each process in the cycle is waiting for a resource held by the next process in the cycle.
2. There are four necessary conditions for deadlock to occur: mutual exclusion, hold and wait, no preemption, and circular wait.
3. Deadlock can be prevented by ensuring that at least one of the necessary conditions is not met.
4. Deadlock can be avoided by using resource allocation algorithms that ensure that the system will never enter an unsafe state.
5. Deadlock can be detected by using algorithms that check for cycles in the resource allocation graph.
6. Once deadlock is detected, it can be resolved by either terminating one or more processes or by preempting resources from processes.
