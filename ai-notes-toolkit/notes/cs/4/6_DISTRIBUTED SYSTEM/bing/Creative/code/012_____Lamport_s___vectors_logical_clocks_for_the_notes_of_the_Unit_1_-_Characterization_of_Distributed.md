Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on Lamport's logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Lamport's logical clocks

- Lamport's logical clock (or timestamp) was proposed by Leslie Lamport in the 1970s and widely used in almost all distributed systems since then.
- A Lamport logical clock is a numerical software counter value maintained in each process.
- Conceptually, this logical clock can be thought of as a clock that only has meaning in relation to messages moving between processes.
- When a process receives a message, it re-synchronizes its logical clock with that sender.
- The basic idea of Lamport's logical clock is to assign a logical timestamp to each event in a distributed system, such that if event a causally precedes event b, then the timestamp of a is less than the timestamp of b.
- The logical timestamp of an event is denoted by L(e), and the logical clock of a process is denoted by C(p).
- The algorithm for Lamport's logical clock is as follows:

  - Each process p increments C(p) between any two successive events.
  - If event a is the sending of a message m by process p, then the message m contains a timestamp T(m) = C(p).
  - Upon receiving a message m, process q sets C(q) to be greater than or equal to its present value and greater than T(m).

- The advantage of Lamport's logical clock is that it is simple and easy to implement.
- The disadvantage of Lamport's logical clock is that it does not capture the concurrent events in a distributed system, i.e., two events that are not causally related may have different logical timestamps depending on the order of message delivery.
- To overcome this limitation, vector clocks were introduced by Colin Fidge and Friedemann Mattern in the 1980s.