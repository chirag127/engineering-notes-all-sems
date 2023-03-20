 Here are the notes on Deadlock for the topic CPU Scheduling in Operating System:

### Deadlock

- Deadlock refers to a situation where two or more processes are waiting indefinitely for an event that can be caused by the other process.
- It occurs due to resource starvation and is a common problem in multiprocessing systems.
- Four conditions must be met for a deadlock to occur:

1. Mutual exclusion: Only one process can use a resource at a time.
2. Hold and wait: A process holding one resource requests additional resources.
3. No preemption: Resources cannot be forcibly removed from a process.
4. Circular wait: There is a set {P0, P1, ..., Pn} of waiting processes such that P0 is waiting for a resource held by P1, P1 is waiting for a resource held by P2, ..., Pn−1 is waiting for a resource held by Pn, and Pn is waiting for a resource held by P0.

- Methods to handle deadlocks:

1. Prevent deadlocks by denying one of the four conditions.
2. Detect and recover using deadlock detection and recovery algorithms.
3. Ignore deadlocks and reboot the system if they occur.

- Common deadlock prevention techniques:

1. Lock ordering: Acquire locks in a fixed order to avoid cycles.
2. Resource reservation: Reserve all resources before starting processes.
3. Preemption: Allow resources to be forcibly removed.
4. Limiting the number of instances of a resource type.

- That's all for the notes on Deadlock. Let me know if you would like me to explain anything in particular.