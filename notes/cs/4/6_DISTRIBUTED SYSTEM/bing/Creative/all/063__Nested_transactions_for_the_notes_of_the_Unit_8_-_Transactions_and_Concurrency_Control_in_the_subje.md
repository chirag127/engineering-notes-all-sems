### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A nested transaction is a transaction that consists of subtransactions, each of which may have its own begin and end points.
- Nested transactions allow for more concurrency and fault tolerance in distributed systems, as subtransactions can be committed or aborted independently of each other and of the parent transaction.
- Nested transactions can be classified into two types: **flat** and **nested**.
- Flat transactions have a single begin and end point, and are usually simple and short-lived. They are suitable for accessing objects on a single server or a small number of servers.
- Nested transactions have multiple begin and end points, and can span across multiple servers and objects. They are suitable for complex and long-lived activities that involve multiple subtasks and resources.
- Nested transactions have the following properties:
  - **Atomicity**: A nested transaction is either committed or aborted as a whole. If a subtransaction aborts, it does not affect the outcome of the parent transaction or other subtransactions.
  - **Consistency**: A nested transaction preserves the consistency of the data and the system state. If a subtransaction violates a consistency constraint, it is aborted and the violation is reported to the parent transaction.
  - **Isolation**: A nested transaction is isolated from other concurrent transactions. The effects of a subtransaction are not visible to other transactions until the parent transaction commits.
  - **Durability**: The effects of a committed nested transaction are persistent and survive failures.
- Nested transactions can be implemented using various protocols, such as the **two-phase commit protocol** or the **sagas protocol**.
- The two-phase commit protocol ensures that all the servers involved in a distributed transaction agree on the outcome of the transaction, either commit or abort. It consists of two phases: **prepare** and **commit**. In the prepare phase, the coordinator asks each server to vote on whether to commit or abort the transaction. In the commit phase, the coordinator decides the final outcome based on the votes and informs each server to commit or abort accordingly.
- The sagas protocol allows for partial rollback of nested transactions in case of failures or aborts. It consists of a sequence of subtransactions, each of which has a compensating action that can undo its effects. If a subtransaction fails or aborts, the saga executes the compensating actions of the previous subtransactions in reverse order, restoring the system to a consistent state.