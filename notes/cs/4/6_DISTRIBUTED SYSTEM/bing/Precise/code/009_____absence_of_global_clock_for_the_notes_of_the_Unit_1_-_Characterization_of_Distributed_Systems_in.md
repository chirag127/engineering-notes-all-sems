### Absence of Global Clock

- In a distributed system, there is no single, global clock that all processes can access.
- Instead, each process has its own local clock, which may not be synchronized with the clocks of other processes.
- This can lead to inconsistencies and difficulties in coordinating actions between processes.
- To address this issue, distributed systems often use logical clocks or vector clocks to establish a partial ordering of events.
- These clocks allow processes to determine the relative order of events, even in the absence of a global clock.
- However, the absence of a global clock can still lead to challenges in achieving consistency and coordination in a distributed system.