## Unit 10 - Replication

Replication is the practice of keeping several copies of data in different places in a distributed system. Replication can enhance the reliability, availability, and throughput of the system, but also introduces challenges such as maintaining consistency, resolving conflicts, and managing network partitions.

Some of the topics covered in this unit are:

- Why do we need replication?
- What are the types of replication?
- What are the consistency models for replication?
- What are the replication protocols and techniques?

### Why do we need replication?

Replication can provide the following benefits for a distributed system:

- **Fault tolerance**: Replication can prevent data loss and system failure when some nodes or replicas are unavailable or damaged. Replication can also improve the recovery time and reduce the impact of failures on the system performance.
- **Load balancing**: Replication can distribute the workload among different replicas and reduce the load on a single node or server. Replication can also improve the response time and latency for the clients by allowing them to access the nearest or the most available replica.
- **Availability**: Replication can ensure that data is accessible for the clients even when some replicas are offline or disconnected. Replication can also cope with network partitions and network failures by allowing the clients to access the local replicas.
- **Scalability**: Replication can increase the system throughput and capacity by adding more replicas and nodes to the system. Replication can also support the growth of the system and the data without affecting the performance or the consistency.

### What are the types of replication?

Replication can be classified into two main types: **active replication** and **passive replication**.

- **Active replication**: In active replication, the client request is sent to all the replicas and each replica executes the request independently. The replicas must agree on the order of the requests to ensure consistency. The client can receive the response from any replica or from a majority of the replicas. Active replication is also known as **state machine replication** or **primary-backup replication**.
- **Passive replication**: In passive replication, the client request is sent to a single replica, called the **primary replica**, and the primary replica executes the request and sends the response to the client. The primary replica also updates the other replicas, called the **backup replicas**, about the changes in the data. The backup replicas only execute the requests when the primary replica fails. Passive replication is also known as **primary-copy replication** or **master-slave replication**.

### What are the consistency models for replication?

Consistency models define the rules and guarantees for the behavior and the results of the operations on the replicated data. Consistency models can be classified into two main categories: **strong consistency models** and **weak consistency models**.

- **Strong consistency models**: Strong consistency models ensure that all the replicas have the same data at all times and that the clients always see the latest updates. Strong consistency models are easier to reason about and program with, but they also require more coordination and communication among the replicas, which can affect the performance and the availability of the system. Examples of strong consistency models are **linearizability**, **sequential consistency**, and **serializability**.
- **Weak consistency models**: Weak consistency models allow some replicas to have stale or divergent data for some time and that the clients may see different or outdated versions of the data. Weak consistency models are more tolerant of network delays and failures, and they can improve the performance and the availability of the system, but they also require more complexity and logic from the clients and the applications. Examples of weak consistency models are **eventual consistency**, **causal consistency**, and **read-your-writes consistency**.

### What are the replication protocols and techniques?

Replication protocols and techniques are the methods and algorithms for implementing and maintaining replication in a distributed system. Replication protocols and techniques can be classified into two main categories: **eager replication** and **lazy replication**.

- **Eager replication**: Eager replication is a replication technique where the updates are propagated to all the replicas as soon as they occur. Eager replication can ensure strong consistency