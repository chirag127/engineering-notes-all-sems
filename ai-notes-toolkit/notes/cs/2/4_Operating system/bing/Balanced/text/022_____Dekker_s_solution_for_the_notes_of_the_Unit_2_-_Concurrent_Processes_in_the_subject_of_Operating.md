### Dekker's solution

- Dekker's solution is the first known correct solution to the mutual exclusion problem in concurrent programming .
- The mutual exclusion problem is the problem of ensuring that at most one process can enter a critical section (a section of code that accesses a shared resource) at a time .
- Dekker's solution allows two processes to share a single-use resource without conflict, using only shared memory for communication .
- Dekker's solution avoids the strict alternation of a naive turn-taking algorithm, and was one of the first mutual exclusion algorithms to be invented .
- Dekker's solution works as follows :
  - Each process has a boolean flag that indicates its intention to enter the critical section.
  - Each process also has a turn variable that indicates whose turn it is to enter the critical section.
  - Initially, both flags are false and the turn is arbitrary.
  - When a process wants to enter the critical section, it sets its flag to true and checks the other process's flag.
  - If the other process's flag is false, it means that the other process is not interested in the critical section, so the current process can enter it.
  - If the other process's flag is true, it means that the other process is also interested in the critical section, so the current process has to check the turn variable.
  - If the turn variable is equal to the current process's id, it means that the current process has priority to enter the critical section, so it can enter it.
  - If the turn variable is not equal to the current process's id, it means that the other process has priority to enter the critical section, so the current process has to wait until the turn variable changes or the other process's flag becomes false.
  - After exiting the critical section, the current process sets its flag to false and gives the turn to the other process.
- Dekker's solution guarantees mutual exclusion, progress, and bounded waiting .
  - Mutual exclusion: Only one process can enter the critical section at a time, because the flag and turn variables prevent both processes from entering it simultaneously.
  - Progress: If both processes want to enter the critical section, the turn variable decides which one can enter it first, and the other one has to wait until the turn variable changes or the flag variable becomes false. This ensures that no process is starved or blocked indefinitely.
  - Bounded waiting: There is a bound on the number of times that a process can be bypassed by another process before it can enter the critical section, because the turn variable alternates between the two processes after each exit from the critical section. This ensures that no process has to wait too long to enter the critical section.