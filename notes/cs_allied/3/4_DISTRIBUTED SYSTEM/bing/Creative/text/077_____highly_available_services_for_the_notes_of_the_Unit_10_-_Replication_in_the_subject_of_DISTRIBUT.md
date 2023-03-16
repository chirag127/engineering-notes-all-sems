### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- One of the potential benefits of distributed systems is their use in providing **highly-available services** that are likely to be usable when needed.
- **Availability** is the probability that a service is operational at a given time.
- **Replication** is the technique of maintaining multiple copies of data or services on different nodes in a distributed system, to increase availability, reliability, and performance.
- Replication can be classified into two types: **eager replication** and **lazy replication**.
  - **Eager replication** ensures that all replicas are updated synchronously, as soon as an update occurs. This guarantees **strong consistency** among replicas, but it is expensive and may introduce delays or failures.
  - **Lazy replication** allows replicas to be updated asynchronously, after an update occurs. This improves **availability** and **performance**, but it may lead to **inconsistency** among replicas, which needs to be resolved later.
- There are different methods to implement replication in distributed systems, such as **primary copy**, **quorum-based**, **gossip-based**, and **operational transformation**     .
  - **Primary copy** assigns a single replica as the primary, which receives all update requests and propagates them to other replicas. This ensures **consistency**, but it introduces a **single point of failure** and a **performance bottleneck** .
  - **Quorum-based** requires a minimum number of replicas to agree on an update before it is committed. This allows **fault tolerance** and **load balancing**, but it may increase **communication overhead** and **latency**.
  - **Gossip-based** disseminates updates randomly among replicas, using a probabilistic protocol. This achieves **scalability** and **robustness**, but it may result in **eventual consistency** and **redundant messages**.
  - **Operational transformation** applies updates as operations that can be transformed to maintain **consistency** and **convergence** among replicas, even if they are applied in different orders. This enables **collaboration** and **conflict resolution**, but it may require **complex algorithms** and **metadata** .