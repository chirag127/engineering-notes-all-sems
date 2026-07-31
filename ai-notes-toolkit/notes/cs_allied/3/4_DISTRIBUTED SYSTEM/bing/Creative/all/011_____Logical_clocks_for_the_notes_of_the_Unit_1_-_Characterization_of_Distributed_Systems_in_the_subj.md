# Logical Clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- Some examples of logical clock algorithms are:
  - Lamport timestamps, which are monotonically increasing software counters that are updated based on the send and receive events of messages .
  - Vector clocks, which are arrays of software counters that are updated based on the send and receive events of messages and the causal dependencies among them  .
  - Matrix clocks, which are matrices of software counters that are updated based on the send and receive events of messages and the causal and concurrent dependencies among them.
- A logical clock must satisfy the following property: if event A causally precedes event B, then the logical clock value of A is less than the logical clock value of B  .
- A logical clock may not satisfy the following property: if event A and event B are concurrent, then the logical clock values of A and B are incomparable  .
- A logical clock may not reflect the real-time order of events, as different processes may have different clock rates and delays .
- A logical clock can be implemented by using message passing protocols, synchronization algorithms, or consensus algorithms  .