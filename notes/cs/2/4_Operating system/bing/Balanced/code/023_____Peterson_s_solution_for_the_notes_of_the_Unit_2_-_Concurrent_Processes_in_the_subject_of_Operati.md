### Peterson's solution for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system

- Peterson's solution is a classic solution to the critical section problem. The critical section problem ensures that no two processes change or modify a resource's value simultaneously .
- Peterson's solution is a software solution that uses only shared memory for communication and does not require strict alternation .
- Peterson's solution follows a simple algorithm and is limited to two processes simultaneously. It can be used to solve other problems like the producer-consumer problem and reader-writer problem.
- Peterson's solution uses two variables: `turn` and `flag`. `turn` indicates whose turn it is to enter the critical section, and `flag` is an array of boolean values that indicate whether a process is ready to enter the critical section .
- Peterson's solution satisfies the three requirements of mutual exclusion, progress, and bounded waiting.
- The algorithm for Peterson's solution is as follows :

```
// P0
flag[0] = true; // P0 is ready
turn = 1; // P1's turn
while (flag[1] && turn == 1) // wait
{
   // busy wait
}
// critical section
...
// end of critical section
flag[0] = false; // P0 is not ready

// P1
flag[1] = true; // P1 is ready
turn = 0; // P0's turn
while (flag[0] && turn == 0) // wait
{
   // busy wait
}
// critical section
...
// end of critical section
flag[1] = false; // P1 is not ready
```