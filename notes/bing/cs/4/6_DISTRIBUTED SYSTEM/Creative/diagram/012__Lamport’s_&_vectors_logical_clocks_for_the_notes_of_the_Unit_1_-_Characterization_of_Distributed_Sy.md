Lamport's logical clock and vector clock are both methods to order events in a distributed system based on causality, without relying on a global physical clock. They are both logical clocks, meaning that they are numerical values that are assigned to events by the processes that generate or receive them.

Lamport's logical clock is a scalar value that is incremented by one whenever a process performs an internal event or sends a message, and is updated to the maximum of its current value and the timestamp of the received message plus one whenever a process receives a message. Lamport's logical clock ensures that if event A causally precedes event B, then the timestamp of A is less than the timestamp of B. However, it does not ensure the converse, meaning that two events with different timestamps may be concurrent (not causally related).

Vector clock is an array of scalar values, one for each process in the system. Each process maintains its own local vector clock, which is incremented by one in its own entry whenever it performs an internal event or sends a message, and is updated to the element-wise maximum of its current value and the vector clock of the received message whenever it receives a message. Vector clock ensures that if event A causally precedes event B, then the vector clock of A is less than the vector clock of B in the partial order defined by element-wise comparison. It also ensures the converse, meaning that two events are concurrent if and only if their vector clocks are incomparable.

The following diagram illustrates the basic architecture of a distributed system with three processes (P1, P2, P3) and the logical clocks (Lamport's and vector) of the events that occur in them. The arrows represent the messages sent and received by the processes, and the numbers in parentheses represent the logical clocks of the events.

```
    P1                  P2                  P3
    |                   |                   |
a1 (1)                  |                   |
    |------------------>|                   |
    |               b1 (2)                  |
    |                   |------------------>|
    |                   |               c1 (3)
a2 (2)                  |                   |
    |                   |<------------------|
    |               b2 (4)                  |
    |<------------------|                   |
a3 (5)              b3 (5)                  |
    |                   |                   |
    |-------------------------------------->|
    |                   |               c2 (6)
a4 (6)                  |                   |
    |                   |                   |
```

Lamport's logical clock:

```
    P1                  P2                  P3
    |                   |                   |
a1 (1)                  |                   |
    |------------------>|                   |
    |               b1 (2)                  |
    |                   |------------------>|
    |                   |               c1 (3)
a2 (3)                  |                   |
    |                   |<------------------|
    |               b2 (4)                  |
    |<------------------|                   |
a3 (5)              b3 (5)                  |
    |                   |                   |
    |-------------------------------------->|
    |                   |               c2 (6)
a4 (6)                  |                   |
    |                   |                   |
```

Vector clock:

```
    P1                  P2                  P3
    |                   |                   |
a1 (1,0,0)              |                   |
    |------------------>|                   |
    |               b1 (1,1,0)              |
    |                   |------------------>|
    |                   |               c1 (1,1,1)
a2 (2,1,0)              |                   |
    |                   |<------------------|
    |               b2 (2,2,1)              |
    |<------------------|                   |
a3 (3,2,1)          b3 (3,3,1)              |
    |                   |                   |
    |-------------------------------------->|
    |                   |               c2 (3,3,2)
a4 (4,3,2)              |                   |
    |                   |                   |
```