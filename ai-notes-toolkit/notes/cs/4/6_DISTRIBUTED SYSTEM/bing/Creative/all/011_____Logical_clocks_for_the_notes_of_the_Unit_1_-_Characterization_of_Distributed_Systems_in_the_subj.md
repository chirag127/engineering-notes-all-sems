# Logical Clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems  .
- A logical clock is not a physical device, but a protocol that assigns logical timestamps to events based on some rules .
- A logical clock can be implemented using different algorithms, such as Lamport's clocks, vector clocks, or matrix clocks  .
- A logical clock must satisfy the following property: if event a causally precedes event b, then the logical timestamp of a is less than the logical timestamp of b  .
- A logical clock can provide a total order or a partial order on events, depending on the algorithm used  .
- A logical clock can help in solving problems such as mutual exclusion, deadlock detection, distributed snapshots, and distributed debugging in a distributed system  .