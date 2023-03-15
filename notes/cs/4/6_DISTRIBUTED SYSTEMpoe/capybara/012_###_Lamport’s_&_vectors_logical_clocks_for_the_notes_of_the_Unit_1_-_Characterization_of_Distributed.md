### Lamport’s & Vectors Logical Clocks

In a distributed system, it is essential to have a mechanism to maintain the order of events that occur across different nodes. Logical clocks are used to keep track of the order of events in a distributed system.

Lamport’s Logical Clocks:
- Proposed by Leslie Lamport in 1978.
- It is a simple algorithm to maintain the order of events in a distributed system using a logical clock.
- Every process in the system has a logical clock, which is a counter that increases whenever an event occurs.
- When a process sends a message, it includes its current logical clock value.
- When a process receives a message, it updates its logical clock value to the maximum of its current value and the value received in the message, plus one.
- This ensures that events are ordered based on their logical clock values.

Mnemonic: Think of Lamport's Logical Clocks as a stopwatch that counts the events in order.

Vectors Logical Clocks:
- Proposed by Colin Fidge in 1988.
- It is an extension of Lamport’s Logical Clocks to handle the causality of events in a distributed system.
- Every process in the system has a vector clock, which is a list of logical clocks (one for each process).
- When a process sends a message, it includes its current vector clock value.
- When a process receives a message, it updates its vector clock value by taking the maximum value of each element in its own vector clock and the received vector clock, plus one for its own process.
- This ensures that events are ordered based on their causality.

Mnemonic: Think of Vectors Logical Clocks as a scoreboard that keeps track of the events and their causality.

Advantages of Logical Clocks:
- Simple to implement and understand.
- Useful for maintaining the order of events in a distributed system.

Disadvantages of Logical Clocks:
- Cannot handle events that are concurrent or have a partial ordering.

Example:
Consider a distributed system with three processes P1, P2, and P3. The following events occur:
- P1 sends a message to P2.
- P2 receives the message from P1.
- P2 sends a message to P3.
- P1 receives the message from P2.

Using Lamport’s Logical Clocks, the order of events is:
- P1 sends a message to P2 (LC: 1).
- P2 receives the message from P1 (LC: 2).
- P2 sends a message to P3 (LC: 3).
- P1 receives the message from P2 (LC: 4).

Using Vectors Logical Clocks, the order of events is:
- P1 sends a message to P2 (VC: [1,0,0]).
- P2 receives the message from P1 (VC: [2,1,0]).
- P2 sends a message to P3 (VC: [2,1,0]).
- P1 receives the message from P2 (VC: [2,2,0]).

Applications:
- Useful in distributed systems that require ordering of events, such as databases, messaging systems, etc.