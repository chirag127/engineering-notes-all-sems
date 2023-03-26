 Here is the content in Markdown format without any emojis or external links and in formal tone:

### Theoretical Foundation for Distributed System

1. Shared Nothing Architecture: In this architecture, each node has its own memory and storage. Nodes do not share memory or storage. Communication happens via message passing. Examples: Database sharding, Distributed caching.
2. Replication: Keeping copies of same data on multiple machines to increase data availability and access latency. However, it introduces complexity of synchronization. Examples: DNS, Peer to peer file sharing.
3. Eventual Consistency: In distributed systems, consistency can take time to propagate across all nodes. The system reaches a consistent state eventually. Example: Replication across data centers.
4. CAP Theorem: States that it is impossible for a distributed system to simultaneously provide all three of the following guarantees: Consistency, Availability, and Partition Tolerance. According to the theorem, a distributed system can satisfy at most two of these guarantees at any given time.
5. Consensus: Achieving agreement on a single data value among distributed processes. It is a fundamental problem in distributed systems. Examples: Leader election, Ordering/sequencing of events.
6. Fault Tolerance: Ability of a system to continue operating properly in the event of the failure of one or more components. Redundancy and Replication can be used to achieve fault tolerance.
7. Consistency Models: Defining the degree of consistency that a system provides. Some models are strong consistency, causal consistency, eventual consistency, sequential consistency, etc. The model used depends on the requirements and constraints of the system.