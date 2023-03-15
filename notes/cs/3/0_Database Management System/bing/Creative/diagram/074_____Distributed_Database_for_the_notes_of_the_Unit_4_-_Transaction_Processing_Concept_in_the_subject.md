### Distributed Database

A distributed database is a collection of databases that are physically stored on different network hosts and logically appear as a single database to the user. A distributed database can improve performance, reliability, availability, and scalability of data management.

### Transaction Processing Concept

A transaction is a logical unit of work that consists of one or more database operations, such as queries, updates, inserts, or deletes. A transaction has the following properties:

- Atomicity: A transaction must either complete all of its operations or none of them. If any operation fails, the transaction is aborted and the database is restored to its previous state.
- Consistency: A transaction must preserve the integrity constraints of the database. If the database is consistent before the transaction, it must be consistent after the transaction.
- Isolation: A transaction must not interfere with other concurrent transactions. The intermediate results of a transaction are not visible to other transactions until the transaction commits.
- Durability: A transaction must ensure that the changes it makes to the database are permanent and not lost due to system failures.

### Transaction Processing in a Distributed Database

A distributed transaction is a transaction that involves two or more network hosts that provide transactional resources, such as databases, message queues, or files. A distributed transaction requires a transaction manager that is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources. A distributed transaction must satisfy the same properties as a local transaction, but it also faces additional challenges, such as:

- Network failures: The communication between the transaction manager and the transactional resources may be disrupted or delayed, causing uncertainty about the status of the transaction.
- Resource failures: The transactional resources may crash or become unavailable during the transaction, causing inconsistency or data loss.
- Concurrency conflicts: The transactional resources may have different concurrency control mechanisms or isolation levels, causing potential conflicts or deadlocks among the transactions.
- Data replication: The transactional resources may have different copies or versions of the same data, causing potential inconsistency or divergence among the replicas.

To overcome these challenges, a distributed transaction typically uses a two-phase commit protocol, which consists of the following phases:

- Prepare phase: The transaction manager asks each transactional resource to prepare to commit the transaction. Each transactional resource performs its local operations, locks the data, and writes the undo and redo logs. If the transactional resource is ready to commit, it sends a prepared message to the transaction manager. If the transactional resource encounters any error or aborts the transaction, it sends an abort message to the transaction manager.
- Commit phase: The transaction manager collects the responses from all the transactional resources. If all the responses are prepared, the transaction manager decides to commit the transaction and sends a commit message to all the transactional resources. If any response is abort, the transaction manager decides to abort the transaction and sends an abort message to all the transactional resources. Each transactional resource follows the decision of the transaction manager and either commits or aborts the transaction, releases the locks, and deletes the logs.

The two-phase commit protocol ensures the atomicity and consistency of the distributed transaction, but it also introduces some drawbacks, such as:

- Blocking: The transactional resources are blocked until they receive the final decision from the transaction manager. If the transaction manager or the network fails, the transactional resources may remain blocked indefinitely, reducing the availability and performance of the system.
- Scalability: The transaction manager must coordinate with all the transactional resources involved in the transaction, increasing the network traffic and the response time of the transaction. The more transactional resources are involved, the more overhead and latency are incurred.
- Data freshness: The transactional resources must lock the data until the transaction commits or aborts, preventing other transactions from accessing or updating the data. This reduces the concurrency and freshness of the data, especially for long-running transactions.

To mitigate these drawbacks, some alternative protocols or techniques have been proposed, such as:

- Three-phase commit protocol: This protocol adds a pre-commit phase between the prepare and commit phases, in which the transaction manager sends a pre-commit message to all the transactional resources after receiving all the prepared responses. The transactional resources acknowledge the pre-commit message and wait for the final commit message. This protocol reduces the blocking problem by allowing the transactional resources to decide the outcome of the transaction independently if the transaction manager fails after the pre-commit phase.
- Optimistic replication: This technique allows the transactional resources to update their local copies of the data without locking or coordinating with other replicas. The transaction manager only needs to coordinate with one replica to commit the transaction. The other replicas are asynchronously updated and reconciled later.