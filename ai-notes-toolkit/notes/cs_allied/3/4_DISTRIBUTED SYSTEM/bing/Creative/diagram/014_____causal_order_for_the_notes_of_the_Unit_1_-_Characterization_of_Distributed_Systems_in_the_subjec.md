### Causal order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or global clocks.
- Causal order ensures that if an event e1 causally precedes another event e2, then e1 is observed before e2 by all processes in the system.
- Causal order is important for maintaining consistency and correctness in distributed systems, especially for applications that rely on causal dependencies, such as collaborative editing, social media, or online gaming.
- Causal order can be defined formally using the concept of Lamport's happened-before relation, denoted by ->, which is a partial order on the set of events in a distributed system.
- The happened-before relation -> satisfies the following properties:
  - If e1 and e2 are events in the same process, and e1 occurs before e2, then e1 -> e2.
  - If e1 is the sending of a message by one process and e2 is the receipt of the same message by another process, then e1 -> e2.
  - If e1 -> e2 and e2 -> e3, then e1 -> e3 (transitivity).
- Two events e1 and e2 are said to be concurrent, denoted by e1 || e2, if neither e1 -> e2 nor e2 -> e1 holds.
- Causal order can be implemented in distributed systems using various algorithms, such as vector clocks, causal broadcast, or causal delivery.
- Vector clocks are an extension of Lamport's logical clocks, which assign a scalar timestamp to each event in a distributed system. Vector clocks assign a vector of timestamps to each event, where each element of the vector represents the logical clock of a process in the system.
- Vector clocks can be used to determine the causal order of events by comparing their vectors element-wise. If the vector of e1 is less than or equal to the vector of e2 in every element, then e1 -> e2. If the vectors are incomparable, then e1 || e2.
- Causal broadcast is a communication primitive that guarantees that messages are delivered to all processes in the system in causal order. Causal broadcast can be implemented using vector clocks, by piggybacking the vector clock of the sender with each message, and buffering the messages at the receiver until their causal dependencies are satisfied.
- Causal delivery is a weaker property than causal broadcast, which only guarantees that messages are delivered to each process in causal order, but not necessarily to all processes. Causal delivery can be implemented using vector clocks, by piggybacking the vector clock of the sender with each message, and delivering the messages at the receiver in the order of their vector clocks.