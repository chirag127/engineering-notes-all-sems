### Absence of Global Clock

- In a distributed system, there is no global clock that all nodes can use to synchronize their actions.
- Each node has its own local clock, which may not be synchronized with the clocks of other nodes.
- This can lead to inconsistencies and conflicts when nodes try to coordinate their actions or share data.
- To address this issue, distributed systems use various synchronization algorithms and protocols to achieve a common notion of time among the nodes.
- Some common approaches include using logical clocks, vector clocks, and global time services.
- However, achieving perfect synchronization is difficult, and most distributed systems have to deal with some degree of clock skew and uncertainty.
- The absence of a global clock is one of the fundamental challenges in the design and implementation of distributed systems. It requires careful consideration of timing and synchronization issues to ensure the correct and consistent operation of the system.