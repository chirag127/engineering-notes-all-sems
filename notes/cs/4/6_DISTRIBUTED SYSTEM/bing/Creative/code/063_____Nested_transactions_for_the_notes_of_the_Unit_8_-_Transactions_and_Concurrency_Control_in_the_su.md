### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a sequence of operations that satisfies the ACID properties (atomicity, consistency, isolation, and durability).
- A distributed transaction is a transaction that accesses objects handled by different servers in a distributed system.
- A nested transaction is a transaction that contains subtransactions within it, which can be committed or aborted independently.
- Nested transactions can be used to improve the performance, reliability, and modularity of distributed transactions.
- Nested transactions can be classified into two types: closed nested transactions and open nested transactions.
- Closed nested transactions have the following properties:
  - The commit of a subtransaction is not visible to other transactions until the commit of the parent transaction.
  - The abort of a subtransaction causes the rollback of all its effects and the abort of the parent transaction.
  - The concurrency control and recovery mechanisms are based on the concept of conflict serializability extended to multilevel transactions.
  - The serialization graph testing is used to detect and resolve conflicts among nested transactions.
  - The two-phase commit protocol is used to coordinate the commit or abort of nested transactions across different servers.
- Open nested transactions have the following properties:
  - The commit of a subtransaction is visible to other transactions before the commit of the parent transaction.
  - The abort of a subtransaction does not affect the parent transaction or other subtransactions.
  - The concurrency control and recovery mechanisms are based on the concept of compensating actions, which are used to undo the effects of committed subtransactions in case of abort.
  - The optimistic concurrency control is used to validate the consistency of nested transactions at commit time.
  - The presumed abort protocol is used to coordinate the commit or abort of nested transactions across different servers.