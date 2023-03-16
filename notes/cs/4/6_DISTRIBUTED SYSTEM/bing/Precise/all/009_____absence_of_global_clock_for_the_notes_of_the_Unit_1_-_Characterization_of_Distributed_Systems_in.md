# Absence of Global Clock

- In a distributed system, there is no global clock that all nodes can use to synchronize their actions.
- Each node has its own clock, and the clocks of different nodes may not be synchronized.
- This can lead to problems when coordinating actions between nodes, as it is difficult to determine the order of events.
- To address this issue, distributed systems use logical clocks, which assign a logical timestamp to each event.
- These timestamps can be used to determine the order of events, even if the physical clocks of the nodes are not synchronized.
- Vector clocks and Lamport timestamps are two common types of logical clocks used in distributed systems.
- Another approach to dealing with the absence of a global clock is to use a time synchronization protocol, such as the Network Time Protocol (NTP), to synchronize the clocks of the nodes.
- However, even with time synchronization, it is still possible for the clocks of different nodes to drift apart over time, so logical clocks are still necessary to determine the order of events.