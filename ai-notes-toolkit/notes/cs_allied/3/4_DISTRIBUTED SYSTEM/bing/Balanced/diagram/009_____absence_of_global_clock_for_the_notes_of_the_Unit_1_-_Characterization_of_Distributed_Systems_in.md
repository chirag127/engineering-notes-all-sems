Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of absence of global clock for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Absence of global clock

- A global clock is a hypothetical clock that can synchronize all the processes in a distributed system.
- A global clock would allow the processes to agree on a common notion of time and order events according to their timestamps.
- However, a global clock is impossible to implement in a distributed system due to the following reasons:
  - Physical limitations: The speed of light and the propagation delays of messages prevent the processes from having a consistent view of the global clock at any given instant.
  - Logical limitations: The processes may have different clock rates and drifts, and the clock synchronization algorithms may introduce errors and uncertainties in the clock values.
  - Fault tolerance: The global clock may fail or be corrupted by malicious processes, and the system may need to cope with clock failures and recoveries.
- Therefore, a distributed system has to deal with the absence of global clock and use other methods to coordinate and order events, such as logical clocks, vector clocks, causal ordering, etc.