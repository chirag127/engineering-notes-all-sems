### Concurrency control in distributed transactions

Concurrency control in distributed transactions refers to the mechanism used to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution. These transactions are performed in a distributed database system where relevant data is hosted by a group of linked data servers.

There are several approaches to achieving concurrency control in distributed transactions, including:

1. **Locking-based concurrency control protocols**: These protocols use the concept of locking data to prevent multiple transactions from accessing the same data simultaneously.
2. **Timestamp-based concurrency control algorithms**: These algorithms use a transaction’s timestamp to determine the order in which transactions should be executed.
3. **Optimistic concurrency control**: This approach assumes that conflicts between transactions are rare and allows transactions to execute concurrently. Conflicts are detected at commit time, and the transaction is rolled back if a conflict is detected.

One example of a distributed transaction control protocol is 2PC*, which is an optimized protocol based on the traditional 2PC. It can extract more concurrent processing capabilities under high-intensity competitive workloads than previous approaches for a multi-microservice.