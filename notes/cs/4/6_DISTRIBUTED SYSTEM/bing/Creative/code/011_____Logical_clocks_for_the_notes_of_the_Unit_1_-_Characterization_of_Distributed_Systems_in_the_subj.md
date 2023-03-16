### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems  .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock must satisfy the following property: if event A causally precedes event B, then the logical clock value of A must be less than the logical clock value of B  .
- There are different types of logical clocks, such as Lamport timestamps, vector clocks, matrix clocks, etc. Each type has its own advantages and disadvantages in terms of accuracy, complexity, and overhead  .
- Logical clocks are useful in computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress .