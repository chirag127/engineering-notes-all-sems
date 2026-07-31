### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that accesses and possibly modifies data in a database or a distributed system.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that a transaction either completes all its operations or none of them.
- Consistency means that a transaction preserves the integrity constraints of the data.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

- A nested transaction is a transaction that contains other transactions as subtransactions.
- A nested transaction can be used to divide a complex transaction into smaller and more manageable units.
- A nested transaction can also be used to support partial rollback and recovery, as well as concurrency control and deadlock prevention.
- A nested transaction has a parent transaction and zero or more child transactions.
- A child transaction can also have its own child transactions, forming a hierarchy of transactions.
- A nested transaction can be in one of the following states: active, committed, aborted, or prepared.

- A nested transaction is active when it is executing its operations.
- A nested transaction is committed when it completes all its operations successfully and notifies its parent transaction.
- A nested transaction is aborted when it encounters an error or is aborted by its parent transaction.
- A nested transaction is prepared when it is ready to commit or abort, but waits for the decision of its parent transaction.

- A nested transaction can commit or abort independently of its parent transaction, but its final outcome depends on the outcome of its parent transaction.
- A nested transaction can use one of the following commit protocols: flat, closed, open, or sagas.

- A flat commit protocol treats a nested transaction as a single flat transaction, ignoring the subtransaction boundaries.
- A flat commit protocol is simple and efficient, but does not support partial rollback and recovery, nor concurrency control and deadlock prevention at the subtransaction level.
- A flat commit protocol requires a two-phase commit protocol (2PC) to coordinate the commit or abort of all the servers involved in a distributed transaction.

- A closed commit protocol preserves the subtransaction boundaries and allows a nested transaction to commit or abort its subtransactions independently.
- A closed commit protocol supports partial rollback and recovery, as well as concurrency control and deadlock prevention at the subtransaction level.
- A closed commit protocol requires a nested two-phase commit protocol (N2PC) to coordinate the commit or abort of all the subtransactions and servers involved in a distributed transaction.

- An open commit protocol allows a nested transaction to commit or abort its subtransactions independently, but also allows other transactions to access the data modified by the subtransactions before the parent transaction commits or aborts.
- An open commit protocol supports partial rollback and recovery, as well as concurrency control and deadlock prevention at the subtransaction level, but also improves the performance and availability of the system by reducing the locking time and the blocking of other transactions.
- An open commit protocol requires a multilevel two-phase commit protocol (M2PC) to coordinate the commit or abort of all the subtransactions and servers involved in a distributed transaction, as well as to handle the conflicts and dependencies among the subtransactions and other transactions.

- A sagas commit protocol allows a nested transaction to commit or abort its subtransactions independently, but also allows other transactions to access the data modified by the subtransactions before the parent transaction commits or aborts, and provides a compensation mechanism to undo the effects of the subtransactions in case of abort.
- A sagas commit protocol supports partial rollback and recovery, as well as concurrency control and deadlock prevention at the subtransaction level, but also improves the performance and availability of the system by reducing the locking time and the blocking of other transactions, and by avoiding the need for a global coordinator and a two-phase commit protocol.
- A sagas commit protocol requires each subtransaction to have a compensating transaction that can undo its effects, and a saga manager that can execute the compensating transactions in reverse order in case of abort.

- References:
  -  Nested Transactions in Distributed Systems | IEEE Journals & Magazine
  -  Flat & Nested Distributed Transactions - GeeksforGeeks
  -  Nested Transactions in Distributed Systems | Semantic Scholar