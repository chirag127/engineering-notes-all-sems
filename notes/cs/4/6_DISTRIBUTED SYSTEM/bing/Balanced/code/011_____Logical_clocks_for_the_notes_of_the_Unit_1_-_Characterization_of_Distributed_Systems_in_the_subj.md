### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- There are different types of logical clocks, such as Lamport timestamps, vector clocks, matrix clocks, etc., each with different properties and applications  .
- A logical clock must satisfy the following property: if event A causally precedes event B, then the logical clock value of A must be less than the logical clock value of B .
- A logical clock does not necessarily reflect the real time or the physical order of events, but only the logical order and causality  .