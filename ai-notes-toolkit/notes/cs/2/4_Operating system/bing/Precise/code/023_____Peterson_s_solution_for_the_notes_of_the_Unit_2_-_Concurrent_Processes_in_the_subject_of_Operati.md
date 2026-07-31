### Peterson’s solution for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system

Peterson's solution is a concurrent programming algorithm for mutual exclusion that allows two or more processes to share a single-use resource without conflict, using only shared memory for communication.

1. It was formulated by Gary L. Peterson in 1981.
2. It is a software-based solution to the critical section problem.
3. The algorithm uses two variables, a boolean array `flag` and an integer `turn`.
4. The `flag` array indicates if a process is ready to enter the critical section.
5. The `turn` variable indicates which process has priority to enter the critical section.
6. The algorithm works by having each process follow a specific protocol before entering the critical section.
7. The protocol involves setting the `flag` variable to indicate readiness, then checking the `turn` variable to see if the process has priority.
8. If the process has priority, it enters the critical section, otherwise, it waits until it has priority.
9. After leaving the critical section, the process resets its `flag` variable and updates the `turn` variable to give priority to the other process.
10. Peterson's solution is a simple and effective algorithm for mutual exclusion in shared-memory systems.
