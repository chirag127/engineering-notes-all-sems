# Dekker's solution

Dekker's solution is a mutual exclusion algorithm that allows two processes to share a critical section without conflict, using only shared memory for communication. It was the first provably-correct solution to the critical section problem, and one of the first mutual exclusion algorithms to be invented  .

The algorithm works as follows:

- Each process has a boolean flag that indicates whether it wants to enter the critical section or not.
- Each process also has a turn variable that indicates whose turn it is to enter the critical section.
- Initially, both flags are false and the turn is arbitrary.
- When a process wants to enter the critical section, it sets its flag to true and checks the other process's flag.
- If the other process's flag is false, it means that the other process is not interested in the critical section, so the current process can enter it.
- If the other process's flag is true, it means that the other process is also interested in the critical section, so the current process has to wait until its turn.
- When a process exits the critical section, it sets its flag to false and gives the turn to the other process.

The algorithm can be expressed in pseudocode as follows:

```
// Process 0
flag[0] = false
turn = 0 or 1

while (true) {
  // Non-critical section
  flag[0] = true // I want to enter the critical section
  while (flag[1]) { // The other process also wants to enter
    if (turn != 0) { // It's not my turn
      flag[0] = false // I give up
      while (turn != 0) {} // I wait until my turn
      flag[0] = true // I try again
    }
  }
  // Critical section
  // ...
  turn = 1 // I give the turn to the other process
  flag[0] = false // I exit the critical section
}
```

```
// Process 1
flag[1] = false
turn = 0 or 1

while (true) {
  // Non-critical section
  flag[1] = true // I want to enter the critical section
  while (flag[0]) { // The other process also wants to enter
    if (turn != 1) { // It's not my turn
      flag[1] = false // I give up
      while (turn != 1) {} // I wait until my turn
      flag[1] = true // I try again
    }
  }
  // Critical section
  // ...
  turn = 0 // I give the turn to the other process
  flag[1] = false // I exit the critical section
}
```

The algorithm satisfies the following properties:

- Mutual exclusion: Only one process can enter the critical section at a time, because the other process will either have its flag set to false or will wait until its turn.
- Progress: If both processes want to enter the critical section, the one whose turn it is will eventually enter it, because the other process will give up and wait until its turn.
- Bounded waiting: There is a bound on the number of times that a process can be denied access to the critical section after it has indicated its interest, because the turn will eventually be given to it by the other process.

The algorithm can be generalized to more than two processes, but it becomes more complex and less efficient. There are other algorithms that achieve mutual exclusion with better performance and scalability, such as Peterson's algorithm, Lamport's bakery algorithm, and spin locks.