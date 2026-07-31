### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a sequence of operations that satisfies the ACID properties (Atomicity, Consistency, Isolation, Durability).
- A distributed transaction is a transaction that accesses objects handled by different servers in a distributed system.
- A nested transaction is a transaction that contains subtransactions within it, each with its own begin and end points.
- Nested transactions can be used to improve the performance, reliability, and modularity of distributed transactions.
- Nested transactions have the following characteristics:
  - A subtransaction can commit or abort independently of its parent transaction, but its effects are not visible to other transactions until the parent transaction commits.
  - A subtransaction can inherit the locks and resources of its parent transaction, or it can acquire its own locks and resources.
  - A subtransaction can be retried or compensated in case of failure, without affecting the rest of the parent transaction.
  - A subtransaction can be nested within another subtransaction, forming a hierarchy of transactions.
- Nested transactions can be classified into two types: closed nested transactions and open nested transactions.
  - Closed nested transactions are those that follow the strict two-phase locking protocol, which ensures serializability and recoverability of transactions. They are also called flat transactions or subtransactions.
  - Open nested transactions are those that allow subtransactions to release their locks and resources before the parent transaction commits, which improves concurrency and availability of transactions. They are also called sagas or compensating transactions.