# Timestamp Ordering

Timestamp ordering is a concurrency control protocol used in distributed systems to ensure serializability of transactions. It assigns a unique timestamp to each transaction, which represents the order in which the transactions are to be executed. The protocol ensures that conflicting operations are executed in the order of their timestamps.

Here are some key points to remember about timestamp ordering:

1. Each transaction is assigned a unique timestamp when it enters the system.
2. The timestamps are used to determine the order in which conflicting operations are executed.
3. If a transaction T1 has an earlier timestamp than transaction T2, then any conflicting operations in T1 must be executed before the corresponding operations in T2.
4. If a transaction T1 has a later timestamp than transaction T2, and T1 issues a read or write operation that conflicts with an operation in T2, then T1 is rolled back and restarted with a new timestamp.
5. Timestamp ordering ensures serializability, but it may result in a high rate of transaction rollbacks if there are many conflicts.
