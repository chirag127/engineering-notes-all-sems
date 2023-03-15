### Peterson's solution for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system

- Peterson's solution is a **concurrent programming algorithm** for mutual exclusion that allows two or more processes to share a single-use resource without conflict, using only shared memory for communication.
- Peterson's solution is a **classic solution** to the critical section problem, which ensures that no two processes change or modify a resource's value simultaneously .
- Peterson's solution follows a **simple algorithm** and is limited to two processes simultaneously. It can be implemented in any programming language, and it can be used to solve other problems like the producer-consumer problem and reader-writer problem.
- Peterson's solution uses two **shared variables**: `turn` and `flag`. `turn` indicates whose turn it is to enter the critical section, and `flag` is an array of boolean values that indicate whether a process is ready to enter the critical section.
- Peterson's solution works as follows:
  - Initially, `turn` is set to either 0 or 1, and `flag` is set to false for both processes.
  - When a process wants to enter the critical section, it sets its `flag` to true and assigns the `turn` to the other process.
  - Then, it waits until either the other process's `flag` is false or the `turn` is its own.
  - After exiting the critical section, it sets its `flag` to false.
- Peterson's solution satisfies the three requirements of mutual exclusion, progress, and bounded waiting :
  - Mutual exclusion: Only one process can enter the critical section at a time, as the other process will be waiting for either the `flag` or the `turn` condition to be true.
  - Progress: A process that is not in the critical section cannot prevent another process from entering the critical section, as the `turn` variable ensures that both processes have a fair chance to enter.
  - Bounded waiting: There is a bound on the number of times a process can be bypassed by another process before entering the critical section, as the `turn` variable alternates between the two processes.