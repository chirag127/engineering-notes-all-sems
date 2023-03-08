 Here is the content in markdown format for the topic ### Controlling Concurrent Accesses to Data Objects for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System:

## Controlling Concurrent Accesses to Data Objects

- When multiple processes access and modify shared data objects concurrently, the consistency of data can be compromised due to race conditions and unpredictable results.
- Hence, concurrency control mechanisms are required to coordinate the access of shared data objects.
- Some popular concurrency control techniques are:
    - Mutual Exclusion - Allows only one process to access the critical section (shared data) at a time. Others have to wait.
    - Semaphores - Generalize the mutual exclusion concept. Acts as a counter for shared resources. Allows multiple processes to access the shared resource simultaneously if count allows.
    - Monitors - Allow a process to access a shared data object only if it has acquired the monitor associated with the object. The monitor allows only one process at a time to execute within the monitor.
- Advantages: Prevents race conditions and inconsistent data. Ensures predictable results.
- Disadvantages: Can lead to deadlocks and starvation. Reduces parallelism and affects performance.
- Examples: Implementing locks, semaphores in operating systems. Database transactions use concurrency control.
- Applications: Multiprocessing systems, databases, file systems, etc.

[Detailed diagrams and code samples can be added here to aid understanding]

The content is written in points in a formal tone with headings and formatting as requested. Let me know if you would like me to elaborate on any of the points or add more details.