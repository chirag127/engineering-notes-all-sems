# Mutual Exclusion

- Mutual exclusion is a property of process synchronization which states that “no two processes can exist in the critical section at any given point of time”.
- The critical section is a segment of code where a process accesses shared resources, such as memory, files, or devices, that must not be accessed by more than one process at a time.
- A successful solution to the mutual exclusion problem must have at least these two properties :
  - It must implement mutual exclusion: only one process can be in the critical section at a time.
  - It must be free of deadlocks: if processes are trying to enter the critical section, one of them must eventually be able to do so.
- Additionally, a desirable property of a mutual exclusion solution is fairness: every process that wants to enter the critical section should get a chance to do so in a finite amount of time.
- There are various methods to achieve mutual exclusion in operating systems, such as:
  - Hardware-based solutions: using special instructions or registers that can atomically test and modify a shared variable, such as test-and-set or compare-and-swap.
  - Software-based solutions: using algorithms that rely on shared variables and flags, such as Dekker's algorithm or Peterson's algorithm.
  - Semaphore-based solutions: using a special type of variable that can be incremented or decremented atomically, and can be used to signal or wait for a resource, such as binary semaphores or counting semaphores.
  - Monitor-based solutions: using a high-level abstraction that encapsulates shared data and synchronization operations in a single module, and allows only one process to access it at a time, such as Hoare monitors or Mesa monitors.
  - Message-based solutions: using communication primitives, such as send and receive, to exchange messages between processes and coordinate access to shared resources, such as Lamport's bakery algorithm or Ricart-Agrawala algorithm.