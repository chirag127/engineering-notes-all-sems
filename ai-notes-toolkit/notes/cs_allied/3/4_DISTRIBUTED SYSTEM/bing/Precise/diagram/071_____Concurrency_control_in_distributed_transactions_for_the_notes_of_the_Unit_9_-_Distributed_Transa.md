### Concurrency control in distributed transactions

Concurrency control in distributed transactions refers to the mechanism used to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution. These transactions are performed in a distributed database system where relevant data is hosted by a group of linked data servers.

Some of the methods used for concurrency control in distributed transactions include:

1. **Locking-based concurrency control protocols**: These protocols use the concept of locking data to ensure that only one transaction can access the data at a time.
2. **Timestamp-based concurrency control algorithms**: These algorithms use a transaction’s timestamp to determine the order in which transactions should be executed.
3. **Optimistic concurrency control**: This method assumes that conflicts between transactions are rare and allows transactions to execute concurrently. Conflicts are detected at the end of the transaction and resolved by aborting and restarting one of the conflicting transactions.