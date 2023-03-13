### Transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that consists of one or more operations on a database or a distributed system .
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID)   .
  - Atomicity: A transaction either commits all its changes or aborts and leaves the system in its initial state   .
  - Consistency: A transaction preserves the integrity constraints of the system, such as unique keys, referential integrity, etc.   .
  - Isolation: A transaction executes as if it is the only one in the system, and does not interfere with other concurrent transactions   .
  - Durability: The changes made by a committed transaction are permanent and survive system failures   .
- A distributed transaction is a transaction that affects several resources, such as multiple databases, files, or services, that are distributed across different nodes in a network  .
- A distributed transaction requires a distributed commit protocol to ensure that all the participants agree on the outcome of the transaction, either commit or abort  .
- A distributed commit protocol can be either synchronous or asynchronous .
  - Synchronous: The coordinator waits for the acknowledgments from all the participants before deciding the outcome of the transaction .
  - Asynchronous: The coordinator decides the outcome of the transaction based on a timeout or a quorum of participants .
- A distributed transaction can be structured in two different ways: flat or nested .
  - Flat: A flat transaction has a single begin and a single end point, and is usually used for short and simple activities .
  - Nested: A nested transaction is composed of subtransactions that can be committed or aborted independently, and is usually used for long and complex activities .
- A distributed transaction can face several challenges, such as network failures, concurrency conflicts, deadlock detection, and recovery management   .
- A distributed transaction can benefit from several techniques, such as concurrency control protocols, locking mechanisms, timestamp ordering, optimistic methods, and replication strategies   .