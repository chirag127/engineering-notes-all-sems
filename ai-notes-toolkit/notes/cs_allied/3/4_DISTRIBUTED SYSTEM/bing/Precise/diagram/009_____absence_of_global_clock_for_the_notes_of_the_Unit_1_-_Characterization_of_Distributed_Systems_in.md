### Absence of Global Clock

- In a distributed system, there is no global clock that all nodes can refer to.
- Each node has its own local clock, which may not be synchronized with the clocks of other nodes.
- This can lead to inconsistencies and difficulties in coordinating actions between nodes.
- To address this issue, various algorithms and protocols have been developed to synchronize clocks or to provide a logical notion of time.
- Examples of such algorithms and protocols include the Lamport timestamps, vector clocks, and the Network Time Protocol (NTP).
- Despite these efforts, the absence of a global clock remains a fundamental characteristic of distributed systems and must be taken into account when designing and implementing such systems.
