### Dynamic voting protocols

- Dynamic voting protocols are techniques for maintaining consistency and availability of replicated data in distributed systems.
- The basic idea is to assign weights or votes to each replica of a data item, and to require a majority of votes to access or update the data item.
- Dynamic voting protocols can adapt to changes in the system state, such as site failures, network partitions, or load balancing, by reassigning votes to different replicas.
- Dynamic voting protocols can be classified into two categories: quorum-based and topology-based.
- Quorum-based protocols use a fixed or variable quorum size to determine the majority of votes. A quorum is a subset of replicas that satisfies some condition, such as having a minimum number of votes or being connected by a spanning tree.
- Topology-based protocols use the network topology to determine the majority of votes. A topology is a graph that represents the connectivity and reachability of the sites in the system. A topology can be static or dynamic, depending on whether it changes with the system state or not.
- Some examples of dynamic voting protocols are:

  - The dynamic weighted voting scheme  , which assigns weights to replicas based on their availability and reliability, and adjusts the quorum size according to the system state.
  - The protocols for dynamic vote reassignment, which reassign votes to different replicas upon node or link failures, to maintain a majority of votes in each partition of the system.
  - The efficient dynamic voting algorithms, which use a dynamic topology to determine the majority of votes, and perform better than other voting algorithms when two or more replicas reside in the same non-partitionable group.