### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system.
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems.
- A logical clock assigns a unique timestamp to each event in the system, determined by a logical time function that takes into account the events that have occurred in the past.
- A logical clock satisfies the following property: if event A causally precedes event B, then the timestamp of A is less than the timestamp of B.
- A logical clock does not need to synchronize with the real time, it only needs to agree on the order in which events occur.
- One example of a logical clock is the Lamport timestamp, which is based on the following rules :
  - Each process maintains a counter that is incremented before each event in that process.
  - When a process sends a message, it attaches its current counter value to the message.
  - When a process receives a message, it updates its counter to the maximum of its own value and the received value, and then increments it by one.
- Another example of a logical clock is the vector clock, which is based on the following rules:
  - Each process maintains a vector of counters, one for each process in the system.
  - When a process executes an event, it increments its own counter in the vector.
  - When a process sends a message, it attaches its current vector to the message.
  - When a process receives a message, it updates each element in its vector to the maximum of its own value and the received value.
- Logical clocks are useful for ordering events in distributed systems, such as detecting concurrency, consistency, causality, and synchronization.
- Logical clocks have some limitations, such as:
  - They do not reflect the real time of events, only their relative order.
  - They do not provide a total order on events, only a partial order based on causality.
  - They may assign different timestamps to concurrent events, which may lead to ambiguity or inconsistency.
- A possible mnemonic to remember the concept of logical clocks is: **L**ogical clocks **L**ink events by **L**amport or **L**ist.
- A possible learning trick to understand the concept of logical clocks is to draw a diagram of the events and messages in a distributed system, and label them with their logical timestamps according to the rules of the logical clock algorithm. For example, the following diagram shows a distributed system with three processes and Lamport timestamps:

```
  P1   P2   P3
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    |<---(2,0,0)
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
(1,0,0)---->|    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |<---(2,1,0)
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |---->(2,1