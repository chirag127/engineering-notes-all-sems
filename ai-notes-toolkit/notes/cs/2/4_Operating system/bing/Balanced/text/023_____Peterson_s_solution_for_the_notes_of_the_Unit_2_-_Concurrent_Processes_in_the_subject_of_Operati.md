### Peterson's solution for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system

- Peterson's solution is a classic solution to the critical section problem, which ensures that no two processes change or modify a resource's value simultaneously .
- The critical section problem arises when multiple processes need to access a shared resource, such as a file, a printer, or a variable, and they may interfere with each other's operations.
- The solution requires two processes to cooperate by using two variables: a boolean array `flag` and an integer `turn`.
- The `flag` array indicates whether a process is ready to enter the critical section. The `turn` variable indicates whose turn it is to enter the critical section.
- The algorithm works as follows   :
  - Before entering the critical section, process `i` sets `flag[i]` to `true` and `turn` to the other process's number `j`.
  - Then, it checks if `flag[j]` is `true` and `turn` is `j`. If both conditions are true, it means that the other process is also ready and has priority, so process `i` waits until either `flag[j]` becomes `false` or `turn` becomes `i`.
  - After exiting the critical section, process `i` sets `flag[i]` to `false` to indicate that it is done with the resource.
- The algorithm satisfies the three requirements of mutual exclusion, progress, and bounded waiting   :
  - Mutual exclusion: Only one process can enter the critical section at a time, because the other process will be waiting in the while loop until the first process sets its `flag` to `false` or gives up its `turn`.
  - Progress: If both processes are ready to enter the critical section, the one whose `turn` it is will enter first. The other process will not block the first process from entering or exiting the critical section.
  - Bounded waiting: There is a bound on the number of times that a process can be bypassed by another process. The bound is one, because after a process gives up its `turn`, it will not give it up again until it enters and exits the critical section.
- The algorithm can be implemented in any programming language, and it can be used to solve other problems like the producer-consumer problem and reader-writer problem.
- The algorithm is limited to two processes and requires busy waiting, which wastes CPU cycles   .