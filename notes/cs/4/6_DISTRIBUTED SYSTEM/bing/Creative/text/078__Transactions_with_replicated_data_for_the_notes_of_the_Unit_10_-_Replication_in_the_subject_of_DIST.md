### Transactions with replicated data

- Transactions are a sequence of operations that are executed as a single logical unit of work.
- Transactions ensure the ACID properties of atomicity, consistency, isolation, and durability.
- Transactions are essential for maintaining data integrity and consistency in distributed systems.
- Transactions with replicated data involve executing operations on multiple copies of the same data that are stored on different nodes in a distributed system.
- Transactions with replicated data aim to achieve the following goals:
  - Availability: The data should be accessible to the users even if some nodes fail or become disconnected.
  - Performance: The data should be located close to the users to reduce latency and network traffic.
  - Consistency: The data should be synchronized across all the replicas to ensure a single view of the data.
- Transactions with replicated data face the following challenges:
  - Concurrency control: The system should prevent conflicting or concurrent updates to the same data by different transactions.
  - Failure recovery: The system should ensure that the data is restored to a consistent state after a node or network failure.
  - Replication management: The system should coordinate the replication of data across the nodes and handle the issues of replication lag, replication conflict, and replication topology.
- Transactions with replicated data can use different replication types and schemes to achieve different trade-offs between availability, performance, and consistency.
  - Replication types can be synchronous or asynchronous, depending on whether the data is updated on all the replicas at the same time or not.
  - Replication schemes can be active or passive, depending on whether the replicas can accept updates from any node or only from a designated primary node.
  - Replication schemes can also be based on the server model, such as master-slave, peer-to-peer, or multi-master, depending on how the replicas are organized and synchronized.
- Transactions with replicated data can use different replication models to define the rules and protocols for replication, such as snapshot, transactional, or merge replication.
  - Snapshot replication copies a snapshot of the data at a given point in time and does not track the changes to the data.
  - Transactional replication copies the data and the changes to the data in the order of transactions and ensures consistency.
  - Merge replication combines the data and the changes from multiple sources and resolves any conflicts.
- Transactions with replicated data can have different levels of consistency, such as strong, weak, or eventual, depending on how fast and how often the replicas are synchronized.
  - Strong consistency guarantees that all the replicas have the same data at all times and any read operation returns the latest write operation.
  - Weak consistency allows some replicas to have stale or outdated data and some read operations to return old values.
  - Eventual consistency ensures that all the replicas will eventually have the same data if no new updates occur.
- Transactions with replicated data can use different techniques and tools to implement replication, such as replication middleware, database replication, or data replication platforms  .
  - Replication middleware is a software layer that provides replication services and hides the details of replication from the application layer.
  - Database replication is a feature of some database management systems that allows replicating data across multiple database servers.
  - Data replication platforms are specialized tools that enable data replication across different data sources, formats, and destinations.

: Data Replication in Distributed Systems: The Best Guide 101. https://hevodata.com/learn/data-replication-in-distributed-system/
: Data Replication {Replication Types and Schemes Explained}. https://phoenixnap.com/kb/data-replication
: Distributed Transactions. https://people.cs.rutgers.edu/~pxk/417/notes/transactions.html
: Data Replication in DBMS. https://www.geeksforgeeks.org/data-replication-in-dbms/