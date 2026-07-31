Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on Lamport's logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical time.
- A Lamport logical clock is a numerical software counter value maintained in each process. It is incremented whenever a process performs an event, such as sending or receiving a message.
- The basic rules of Lamport's logical clocks are:
  - Each process has a logical clock, initialized to zero.
  - Each time a process performs an internal event, it increments its logical clock by one.
  - Each time a process sends a message, it piggybacks its current logical clock value with the message.
  - Each time a process receives a message, it updates its logical clock to the maximum of its own clock and the received clock value, and then increments it by one.
- Lamport's logical clocks ensure that if event a causally precedes event b, then the logical clock of a is less than the logical clock of b. This is denoted by a -> b.
- However, Lamport's logical clocks do not ensure that if the logical clock of a is less than the logical clock of b, then a causally precedes b. This is because two events may be concurrent, meaning that they are not causally related, but have different logical clock values due to the arbitrary order of message delivery.
- Lamport's logical clocks are also known as scalar clocks, because they use a single integer value to represent the logical time of each event.
- Lamport's logical clocks are widely used in distributed systems to provide a partial ordering of events, and to detect causality violations, such as message overtaking. They are also a basis for more advanced logical clock algorithms, such as vector clocks.