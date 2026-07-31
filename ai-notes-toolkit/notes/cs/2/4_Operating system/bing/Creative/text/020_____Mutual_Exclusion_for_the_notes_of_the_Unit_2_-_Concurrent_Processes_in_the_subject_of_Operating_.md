### Mutual Exclusion

- Mutual exclusion is a property of process synchronization which states that “no two processes can exist in the critical section at any given point of time”.
- A critical section is a piece of code that allows processes or threads to access a shared resource, such as a file, a variable, or a device.
- Mutual exclusion is designed so that when a write operation is in progress, another thread is not granted to use the same object before the first one has done writing and releases the object.
- Mutual exclusion is required to prevent data inconsistency, race conditions, and corruption of shared resources .
- Mutual exclusion can be implemented by using various techniques, such as locks, semaphores, monitors, message passing, etc .
- A successful solution to the mutual exclusion problem must have at least these two properties :
  - It must implement mutual exclusion: only one process can be in the critical section at a time.
  - It must be free of deadlocks: if processes are trying to enter the critical section, one of them must eventually be able to do so.
- Additionally, a desirable solution should also have these properties :
  - It must be free of starvation: every process that wants to enter the critical section should eventually get a chance.
  - It must be fair: processes should get access to the critical section in the order of their requests.
  - It must be efficient: the overhead of entering and exiting the critical section should be minimal.