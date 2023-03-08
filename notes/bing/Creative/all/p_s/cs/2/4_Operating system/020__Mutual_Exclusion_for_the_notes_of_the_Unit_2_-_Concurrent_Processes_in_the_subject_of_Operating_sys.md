### Mutual Exclusion

- Mutual exclusion is a property of process synchronization which states that “no two processes can exist in the critical section at any given point of time”.
- A critical section is a piece of code that allows processes or threads to access a shared resource, such as a file, a printer, a memory location, etc.
- Mutual exclusion is designed so that when a write operation is in progress, then another thread is not granted to use the same object before the first one has done writing and releases the object.
- Mutual exclusion is required to prevent data inconsistency, race conditions, and deadlock situations in concurrent processes.
- Mutual exclusion can be implemented by using various techniques, such as locks, semaphores, monitors, message passing, etc.
- Some of the desirable properties of a mutual exclusion algorithm are:
  - Safety: No two processes can be in the critical section at the same time.
  - Liveness: If a process requests to enter the critical section, it will eventually be granted.
  - Fairness: No process is indefinitely postponed or starved while waiting to enter the critical section.
  - Efficiency: The algorithm should minimize the overhead and the waiting time for the processes.

- An example of mutual exclusion using locks is:

```c
// Assume that lock is a shared variable initialized to 0
// lock = 0 means the critical section is free
// lock = 1 means the critical section is occupied

void enter_critical_section(int pid) {
  while (lock == 1); // busy wait until the lock is free
  lock = 1; // acquire the lock
  printf("Process %d entered the critical section\n", pid);
}

void exit_critical_section(int pid) {
  printf("Process %d exited the critical section\n", pid);
  lock = 0; // release the lock
}
```

Some possible mnemonics and learning tricks for the topic are:

- To remember the four properties of a mutual exclusion algorithm, you can use the acronym **SELF**:
  - **S**afety: No two processes can be in the critical section at the same time.
  - **E**fficiency: The algorithm should minimize the overhead and the waiting time for the processes.
  - **L**iveness: If a process requests to enter the critical section, it will eventually be granted.
  - **F**airness: No process is indefinitely postponed or starved while waiting to enter the critical section.

- To remember the difference between busy waiting and blocking, you can use the analogy of a restaurant:
  - Busy waiting is like standing in a queue and constantly checking if a table is available.
  - Blocking is like giving your name to the host and waiting for them to call you when a table is available.

- To remember the difference between locks and semaphores, you can use the analogy of a bathroom:
  - A lock is like a key that only allows one person to enter the bathroom at a time.
  - A semaphore is like a counter that allows a limited number of people to enter the bathroom at a time.