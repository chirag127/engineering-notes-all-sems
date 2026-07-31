### Mutual Exclusion

- Mutual exclusion is a property of process synchronization which states that “no two processes can exist in the critical section at any given point of time”.
- A critical section is a piece of code that allows processes or threads to access a shared resource, such as a file, a printer, a memory location, etc.
- Mutual exclusion is necessary to prevent race conditions, where the outcome of the execution depends on the order or timing of the processes or threads accessing the shared resource.
- A race condition can lead to inconsistency, corruption, or loss of data, or violation of the intended logic of the program.
- To achieve mutual exclusion, a process or thread must acquire a lock or a mutex (mutual exclusion object) before entering the critical section, and release it after exiting the critical section .
- A lock or a mutex is a program object that prevents simultaneous access to a shared resource by different processes or threads.
- A process or thread that wants to enter the critical section must check the status of the lock or mutex, and wait until it is available or free .
- A process or thread that exits the critical section must signal or notify the other processes or threads that the lock or mutex is available or free .
- A solution to the mutual exclusion problem must have at least these two properties :
  - It must implement mutual exclusion: only one process can be in the critical section at a time.
  - It must be free of deadlocks: if processes are trying to enter the critical section, one of them must eventually be able to do so.
- A solution to the mutual exclusion problem may also have these desirable properties :
  - It must be free of starvation: every process that wants to enter the critical section must eventually be able to do so.
  - It must be fair: every process that wants to enter the critical section must get a chance to do so in a reasonable amount of time.
  - It must be efficient: the overhead of acquiring and releasing the lock or mutex must be minimal.