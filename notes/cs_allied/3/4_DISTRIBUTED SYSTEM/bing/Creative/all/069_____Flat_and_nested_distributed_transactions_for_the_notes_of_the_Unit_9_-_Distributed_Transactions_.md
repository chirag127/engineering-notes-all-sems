# Flat and Nested Distributed Transactions

A distributed transaction is a transaction that accesses objects managed by multiple servers. A distributed transaction must maintain the ACID properties of a transaction, which means that it must be atomic, consistent, isolated, and durable. Atomicity means that either all the changes made by the transaction are committed or none of them are. Consistency means that the transaction preserves the integrity constraints of the data. Isolation means that the transaction does not interfere with other concurrent transactions. Durability means that the committed changes are permanent and survive failures.

There are two ways to structure a distributed transaction: flat or nested.

## Flat Transactions

A flat transaction has a single begin point and a single end point, where it either commits or aborts. A flat transaction is usually simple and short-lived, and it does not have any subtransactions. A flat transaction can be coordinated by a single server, called the transaction manager, which communicates with the other servers involved in the transaction, called the resource managers. The transaction manager uses a two-phase commit protocol to ensure the atomicity of the transaction. The two-phase commit protocol consists of two phases: prepare and commit.

- In the prepare phase, the transaction manager asks each resource manager to vote on whether they are ready to commit the transaction or not. Each resource manager replies with either yes or no. If any resource manager replies with no, the transaction manager aborts the transaction and informs all the resource managers to roll back their changes. If all the resource managers reply with yes, the transaction manager moves to the commit phase.
- In the commit phase, the transaction manager sends a commit message to all the resource managers, instructing them to make their changes permanent. Each resource manager acknowledges the commit message and releases the locks on the objects. The transaction manager then completes the transaction.

## Nested Transactions

A nested transaction is a transaction that has one or more subtransactions, which are transactions themselves. A nested transaction has a hierarchical structure, where the top-level transaction is called the root transaction, and the subtransactions are called the branches. A nested transaction can be coordinated by multiple servers, each of which acts as a transaction manager for its subtransactions. A nested transaction uses a two-phase commit protocol for each subtransaction, and a three-phase commit protocol for the root transaction. The three-phase commit protocol consists of three phases: prepare, pre-commit, and commit.

- In the prepare phase, the root transaction manager asks each branch transaction manager to vote on whether they are ready to commit their subtransactions or not. Each branch transaction manager replies with either yes or no. If any branch transaction manager replies with no, the root transaction manager aborts the root transaction and informs all the branch transaction managers to abort their subtransactions. If all the branch transaction managers reply with yes, the root transaction manager moves to the pre-commit phase.
- In the pre-commit phase, the root transaction manager sends a pre-commit message to all the branch transaction managers, instructing them to prepare to commit their subtransactions. Each branch transaction manager acknowledges the pre-commit message and waits for the final commit message. The root transaction manager then moves to the commit phase.
- In the commit phase, the root transaction manager sends a commit message to all the branch transaction managers, instructing them to commit their subtransactions. Each branch transaction manager acknowledges the commit message and makes their changes permanent. The root transaction manager then completes the root transaction.

## Advantages and Disadvantages of Flat and Nested Transactions

Flat transactions are simpler and faster than nested transactions, as they involve fewer messages and less coordination. However, flat transactions are less flexible and more prone to conflicts and deadlocks, as they lock the objects for the entire duration of the transaction. Flat transactions are suitable for short and simple transactions that do not require much concurrency control.

Nested transactions are more complex and slower than flat transactions, as they involve more messages and more coordination. However, nested transactions are more flexible and more tolerant to failures and partial aborts, as they allow subtransactions to commit or abort independently. Nested transactions are suitable for long and complex transactions that require more concurrency control and fault tolerance.