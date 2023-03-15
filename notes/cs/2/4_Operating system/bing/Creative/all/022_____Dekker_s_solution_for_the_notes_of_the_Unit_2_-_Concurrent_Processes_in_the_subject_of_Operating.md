# Dekker's solution

Dekker's solution is a software-based algorithm for achieving mutual exclusion between two concurrent processes that share a common resource. Mutual exclusion means that only one process can access the resource at a time, while the other process has to wait. Mutual exclusion is necessary to avoid race conditions, where the outcome of the computation depends on the order of execution of the processes.

Some of the properties that a mutual exclusion algorithm should satisfy are:

- **Safety**: No two processes can enter the critical section (the part of the code that accesses the resource) at the same time.
- **Liveness**: Every process that wants to enter the critical section eventually gets a chance to do so.
- **Fairness**: No process is starved or indefinitely postponed from entering the critical section.
- **Efficiency**: The algorithm should not consume too much time or space, and should not rely on assumptions about the speed or number of the processes.

Dekker's solution was the first algorithm to achieve mutual exclusion using only shared memory for communication between the processes, without relying on hardware support or operating system primitives. It was proposed by Dutch mathematician Th. J. Dekker in the 1960s, and later popularized by Edsger W. Dijkstra in his writings on concurrent programming.

The algorithm works as follows:

- Assume that there are two processes, P0 and P1, that want to access a shared resource.
- Each process has a boolean variable, `flag[i]`, that indicates whether it wants to enter the critical section or not. Initially, both flags are false.
- Each process also has an integer variable, `turn`, that indicates whose turn it is to enter the critical section. Initially, the turn can be either 0 or 1.
- The algorithm consists of three parts: entry section, critical section, and exit section.
- In the entry section, a process sets its flag to true, indicating that it wants to enter the critical section. Then, it checks the flag of the other process. If the other process also wants to enter the critical section, then the process checks the turn variable. If the turn is not in its favor, then the process sets its flag to false and waits until the turn changes. Otherwise, the process proceeds to the critical section.
- In the critical section, the process accesses the shared resource and performs its computation.
- In the exit section, the process sets its flag to false, indicating that it is done with the critical section. Then, it sets the turn to the other process, giving it a chance to enter the critical section.

The pseudocode for the algorithm is given below:

```
// Process P0
flag[0] = false; // initially, P0 does not want to enter the critical section
flag[1] = false; // initially, P1 does not want to enter the critical section
turn = 0 or 1; // initially, the turn can be either 0 or 1

// Entry section
flag[0] = true; // P0 wants to enter the critical section
while (flag[1]) { // while P1 also wants to enter the critical section
  if (turn != 0) { // if the turn is not in P0's favor
    flag[0] = false; // P0 sets its flag to false and waits
    while (turn != 0); // until the turn changes
    flag[0] = true; // P0 sets its flag to true again and tries to enter the critical section
  }
}

// Critical section
// P0 accesses the shared resource and performs its computation

// Exit section
flag[0] = false; // P0 sets its flag to false and leaves the critical section
turn = 1; // P0 gives the turn to P1
```

```
// Process P1
flag[0] = false; // initially, P0 does not want to enter the critical section
flag[1] = false; // initially, P1 does not want to enter the critical section
turn = 0 or 1; // initially, the turn can be either 0 or 1

// Entry section
flag[1] = true; // P1 wants to enter the critical section
while (flag[0]) { // while P0 also wants to enter the critical section
  if (turn != 1) { // if the turn is not in P1's favor
    flag[1] = false; // P1 sets its flag to false and waits
    while (turn !=