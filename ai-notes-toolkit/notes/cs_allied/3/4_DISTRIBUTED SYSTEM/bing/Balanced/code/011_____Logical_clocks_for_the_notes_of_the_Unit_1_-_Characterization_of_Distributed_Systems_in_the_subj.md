### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- Some examples of logical clock algorithms are:
  - Lamport timestamps, which are monotonically increasing software counters that are updated based on the send and receive events of messages .
  - Vector clocks, which are arrays of software counters that are updated based on the send, receive, and local events of processes .
  - Matrix clocks, which are matrices of software counters that are updated based on the send, receive, and local events of processes and also capture the concurrency of events.
- The main properties of logical clocks are:
  - Consistency: If event A causally precedes event B, then the logical clock of A is less than the logical clock of B .
  - Accuracy: If the logical clock of A is less than the logical clock of B, then event A causally precedes event B.
  - Completeness: If the logical clock of A is equal to the logical clock of B, then event A and event B are concurrent.
- The main challenges of logical clocks are:
  - How to synchronize the logical clocks of different processes in a distributed system .
  - How to deal with clock drift, network delays, message losses, and failures in a distributed system .
  - How to minimize the overhead of maintaining and exchanging logical clocks in a distributed system .