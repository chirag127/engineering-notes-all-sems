
### Recovery from Deadlock

1. Deadlock is a situation in which two or more processes are blocked forever, waiting for each other to finish.

2. Deadlock can be avoided by using proper synchronization techniques, such as semaphores and monitors.

3. Deadlock can be detected using resource allocation graphs, which represent the resources and processes in the system.

4. Recovery from deadlock can be achieved by using one of the following methods:

- Preemptive Recovery: This method involves preempting one of the processes involved in the deadlock.

- Rollback Recovery: This method involves rolling back the state of the system to a point before the deadlock occurred.

- Wait-Die Recovery: This method involves allowing processes with higher priority to proceed and delaying processes with lower priority.

- Banker's Algorithm: This method involves allocating resources to processes in a way that ensures that the system will never enter a deadlock state.