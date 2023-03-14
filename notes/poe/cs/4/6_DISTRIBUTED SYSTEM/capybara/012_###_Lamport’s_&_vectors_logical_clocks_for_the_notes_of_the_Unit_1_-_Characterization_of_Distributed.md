### Lamport’s & Vectors Logical Clocks

In a distributed system, it becomes important to maintain a notion of time across different processes. This is where the concept of logical clocks comes in. Logical clocks assign a time value to each event in a distributed system, which can be used for debugging, consistency checking, and other purposes.

There are two types of logical clocks commonly used in distributed systems: Lamport’s logical clocks and vector clocks.

#### Lamport’s Logical Clocks

Lamport’s logical clocks were introduced by Leslie Lamport in 1978. The idea behind these clocks is simple: each process maintains a counter that is incremented whenever an event occurs.

The Lamport clock value of an event is the value of the counter at the time the event occurred. If event A happened before event B, then the Lamport clock value of A will be less than the Lamport clock value of B.

Lamport’s logical clocks have a few important properties:

- They are simple to implement and do not require any communication between processes.
- They provide a partial ordering of events in a distributed system.
- They can be used to detect causality violations, where one event appears to happen before another event that it should not precede.

#### Vectors Logical Clocks

Vector clocks were introduced by Colin Fidge and Alan Jones in 1988. The idea behind these clocks is that each process maintains a vector of counters, one for each process in the system.

When an event occurs, the process increments its own counter and sends its vector clock to all other processes. When a process receives a vector clock, it updates its own vector clock by taking the maximum of each corresponding counter in the received vector clock and its own vector clock.

The vector clock value of an event is the vector clock at the time the event occurred. Vector clocks have several important properties:

- They provide a total ordering of events in a distributed system.
- They can be used to detect causality violations, just like Lamport’s clocks.
- They can be used to detect concurrent events, where two events occur at the same time in different processes.

#### Mnemonics and Learning Tricks

For Lamport’s logical clocks, a simple mnemonic to remember is that the clock value is simply the number of events that have occurred. For example, if three events have occurred, the clock value is three.

For vector clocks, a useful trick is to think of each process’s vector clock as a row in a matrix. When a process sends its vector clock to another process, it is simply sending one row of the matrix. When a process receives a vector clock, it updates its own matrix by taking the maximum of each corresponding row in the received matrix and its own matrix.