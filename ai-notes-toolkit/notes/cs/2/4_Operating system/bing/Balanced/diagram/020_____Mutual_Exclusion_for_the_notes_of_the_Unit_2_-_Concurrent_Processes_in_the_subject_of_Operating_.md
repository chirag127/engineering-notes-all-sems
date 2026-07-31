### Mutual Exclusion

- Mutual exclusion is a property of process synchronization which states that “no two processes can exist in the critical section at any given point of time”.
- A critical section is a piece of code that allows processes or threads to access a shared resource, such as a file, a printer, a memory location, etc.
- Mutual exclusion is designed to prevent concurrent access to a shared resource that may result in data inconsistency, corruption, or deadlock .
- Any process synchronization technique being used must satisfy the property of mutual exclusion, without which it would not be possible to get rid of race conditions and ensure data integrity.
- Some of the methods to achieve mutual exclusion are:
  - Hardware-based solutions, such as test-and-set instruction, swap instruction, etc.
  - Software-based solutions, such as Dekker's algorithm, Peterson's algorithm, etc.
  - Operating system-based solutions, such as semaphores, monitors, message passing, etc.
- A successful solution to the mutual exclusion problem must have at least these two properties :
  - It must implement mutual exclusion: only one process can be in the critical section at a time.
  - It must be free of deadlocks: if processes are trying to enter the critical section, one of them must eventually be able to do so.
- Additionally, a desirable solution should also have these properties :
  - It must be free of starvation: every process that wants to enter the critical section should eventually get a chance to do so.
  - It must be fair: processes should be granted access to the critical section in the order of their requests, or at least in a bounded order.
  - It must be efficient: the overhead of entering and exiting the critical section should be minimal, and processes should not waste CPU time by busy waiting.