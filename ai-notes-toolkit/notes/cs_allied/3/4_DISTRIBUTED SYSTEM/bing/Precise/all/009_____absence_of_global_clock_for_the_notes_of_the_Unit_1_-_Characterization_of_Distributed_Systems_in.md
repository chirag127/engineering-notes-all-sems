# Absence of Global Clock

- In a distributed system, there is no global clock that all nodes can use to synchronize their actions.
- Each node has its own local clock, which may not be synchronized with the clocks of other nodes.
- This can lead to inconsistencies and conflicts when nodes try to coordinate their actions or share data.
- To address this issue, distributed systems use various synchronization algorithms and protocols to achieve a common notion of time among the nodes.
- Some common synchronization techniques include the use of logical clocks, vector clocks, and global time services.
- Despite these efforts, the absence of a global clock remains a fundamental challenge in the design and implementation of distributed systems.
