### Lamport’s & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Lamport's logical clock is a procedure to determine the order of events occurring in a distributed system. It provides a basis for the more advanced vector clock algorithm. Due to the absence of a global clock in a distributed system, Lamport logical clock is needed. 

A vector clock is a data structure used for determining the partial ordering of events in a distributed system and detecting causality violations. It is an extension of Lamport's logical clock that can capture the concurrency of events. 

#### Lamport's logical clock algorithm

The algorithm is named after its creator, Leslie Lamport. It is based on the concept of a happened-before relation, denoted by `->`, which means that one event causally precedes another event. For example, if process A sends a message to process B, then the send event happens before the receive event. The algorithm assigns a numerical value, called a timestamp, to each event that occurs in the system, such that the timestamps respect the happened-before relation. 

The criteria for the logical clocks are:

- [C1]: If `a -> b` within the same process, then `C(a) < C(b)`, where `C(x)` is the timestamp of event `x`.
- [C2]: If `a -> b` by sending a message from process A to process B, then `C(a) < C(b)`.

The implementation rules are:

- [IR1]: Each process increments its own logical clock by one before each event it executes.
- [IR2]: When a process sends a message, it piggybacks its current logical clock value with the message.
- [IR3]: When a process receives a message, it updates its own logical clock to be the maximum of its current value and the received value, and then increments it by one.

For example, consider the following scenario with two processes and a disk:

![Lamport example](https://media.geeksforgeeks.org/wp-content/uploads/20190117175913/Lamport-Logical-Clock-1.png)

The timestamps of the events are computed as follows:

- `e11 = 1`, `e21 = 1`: The initial events have timestamp 1 by rule [IR1].
- `e12 = 2`, `e13 = 3`, `e14 = 4`, `e15 = 5`, `e16 = 6`: The subsequent events within the same process have timestamps incremented by one by rule [IR1].
- `e22 = 2`, `e24 = 4`, `e26 = 7`: The subsequent events within the same process have timestamps incremented by one by rule [IR1].
- `e17 = 7`: The receive event has timestamp equal to the maximum of the current value (6) and the received value (5) plus one by rule [IR3].
- `e23 = 3`: The receive event has timestamp equal to the maximum of the current value (2) and the received value (2) plus one by rule [IR3].
- `e25 = 6`: The receive event has timestamp equal to the maximum of the current value (4) and the received value (5) plus one by rule [IR3].

The limitation of Lamport's logical clock is that it does not capture the concurrency of events. For example, `e13` and `e22` are concurrent events, meaning that they are not causally related, but their timestamps do not reflect that. In fact, `C(e13) < C(e22)`, which implies that `e13 -> e22`, which is false. 

#### Vector clock algorithm

The vector clock algorithm is an extension of Lamport's logical clock algorithm that can capture the concurrency of events. It is based on the idea of maintaining a vector of logical clocks, one for each process in the system, and updating the vector according to the happened-before relation. 

The criteria for the vector clocks are:

- [C1]: If `a -> b` within the same process, then `VC(a)[i] < VC(b)[i]`, where `VC(x)[i]` is the `i`-th element of the vector clock of event `x`.
- [C2]: If `a -> b` by sending a message from process A to process B, then `VC(a