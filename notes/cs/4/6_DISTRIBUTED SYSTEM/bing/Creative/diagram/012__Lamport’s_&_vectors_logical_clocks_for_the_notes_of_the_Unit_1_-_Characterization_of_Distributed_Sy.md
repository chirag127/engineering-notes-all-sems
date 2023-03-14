Lamport's logical clock and vector clock are two algorithms to determine the order of events in a distributed system. Lamport's logical clock assigns a single integer timestamp to each event, while vector clock assigns a vector of integers, one for each process. The following diagrams illustrate the basic concepts of these algorithms.

Lamport's logical clock:

```
  P1    P2    P3
  |     |     |
  a     |     |
  |     |     |
  |---->b     |
  |     |     |
  |     c     |
  |     |     |
  |     |---->d
  |     |     |
  e     |     |
  |     |     |
  |<----f     |
  |     |     |
  |     |     g
  |     |     |
  |     |<----h
  |     |     |
  i     |     |
  |     |     |
  |     |---->j
  |     |     |
  |     k     |
  |     |     |
  |     |     l
  |     |     |

  Timestamps:

  P1: 1  2  3  4  5  6  7
  P2: 2  3  4  5  6  7  8
  P3: 1  2  3  4  5  6  7
```

Vector clock:

```
  P1    P2    P3
  |     |     |
  a     |     |
  |     |     |
  |---->b     |
  |     |     |
  |     c     |
  |     |     |
  |     |---->d
  |     |     |
  e     |     |
  |     |     |
  |<----f     |
  |     |     |
  |     |     g
  |     |     |
  |     |<----h
  |     |     |
  i     |     |
  |     |     |
  |     |---->j
  |     |     |
  |     k     |
  |     |     |
  |     |     l
  |     |     |

  Timestamps:

  P1: (1,0,0) (1,1,0) (1,2,0) (1,2,1) (2,2,1) (2,3,1) (3,3,1)
  P2: (0,1,0) (0,2,0) (1,2,0) (1,2,1) (1,3,1) (1,3,2) (1,4,2)
  P3: (0,0,1) (0,0,2) (0,1,2) (0,2,2) (0,2,3) (0,2,4) (0,2,5)
```