## Unit 2 - Consensus

Consensus is an essential concept in distributed systems, where a group of nodes needs to agree on a common state despite failures and network delays. In this unit, we'll explore the following topics:

1. Consensus algorithms: Consensus algorithms are used to reach an agreement on a shared value in a distributed system. Some of the popular consensus algorithms are:
    * Paxos: Paxos is a protocol for distributed consensus invented by Leslie Lamport in 1989. It has three phases: prepare, promise, and accept. Paxos ensures that a single value is chosen, even if nodes fail or messages are lost.
    * Raft: Raft is a distributed consensus algorithm that was designed to be more understandable than Paxos. It is based on the idea of a leader who is responsible for managing the consensus process. Raft has two phases: leader election and log replication.
    * Byzantine fault tolerance: Byzantine fault tolerance is a property of a distributed system that allows it to continue operating even if some of the nodes fail or behave maliciously. Byzantine fault tolerance algorithms are designed to deal with Byzantine failures, which are more severe than crash failures.

2. Fault tolerance: Fault tolerance is the ability of a system to continue operating in the presence of faults, such as node failures or network partitions. Some of the techniques used to achieve fault tolerance in distributed systems are:
    * Replication: Replication is the process of copying data across multiple nodes in a distributed system. By replicating data, we can ensure that there is no single point of failure in the system.
    * Redundancy: Redundancy is the process of adding extra nodes to a system to increase its fault tolerance. Redundancy can be achieved by adding extra replicas of data or by adding extra nodes to the system.
    
3. Consistency models: Consistency models define the guarantees provided by a distributed system regarding the ordering of operations. Some of the popular consistency models are:
    * Strong consistency: Strong consistency guarantees that all nodes in the system see the same data at the same time. In other words, strong consistency ensures that all operations are ordered and that all nodes agree on the order.
    * Eventual consistency: Eventual consistency is a weaker consistency model that allows nodes to diverge temporarily. The system eventually converges to a consistent state, but it may take some time.
    
4. Byzantine fault tolerance: Byzantine fault tolerance is a property of a distributed system that allows it to continue operating even if some of the nodes fail or behave maliciously. Byzantine fault tolerance algorithms are designed to deal with Byzantine failures, which are more severe than crash failures.

Mnemonics and learning tricks for these concepts are not easy to remember. It is recommended to read and understand the concepts thoroughly and practice solving problems related to consensus algorithms, fault tolerance, and consistency models to gain a better understanding of these topics.