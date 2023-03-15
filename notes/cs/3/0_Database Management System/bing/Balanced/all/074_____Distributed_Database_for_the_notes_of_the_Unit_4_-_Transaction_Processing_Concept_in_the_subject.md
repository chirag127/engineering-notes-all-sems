# Distributed Database

A distributed database is a collection of databases that are physically stored on different network hosts and logically appear as a single database to the user. A distributed database can improve performance, reliability, availability, and scalability of data management.

# Transaction Processing Concept

A transaction is a logical unit of work that consists of one or more database operations, such as queries, updates, or inserts. A transaction has the following properties:

- Atomicity: A transaction must either complete all of its operations or none of them.
- Consistency: A transaction must preserve the consistency of the database state by obeying the integrity constraints.
- Isolation: A transaction must not interfere with other concurrent transactions. Each transaction should execute as if it is the only one in the system.
- Durability: A transaction must ensure that the changes it made to the database persist even in the case of system failures.

## Distributed Transaction

A distributed transaction is a transaction that involves two or more network hosts that provide transactional resources, such as databases, message queues, or files. A distributed transaction requires a transaction manager that is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources. A distributed transaction must also satisfy the ACID properties, but it faces additional challenges, such as:

- Network failures: The communication between the hosts may be disrupted or delayed, causing the transaction to fail or become in-doubt.
- Host failures: One or more hosts may crash or become unavailable, causing the transaction to fail or become in-doubt.
- Data inconsistency: The data on different hosts may be inconsistent or outdated, causing the transaction to violate the integrity constraints or produce incorrect results.
- Concurrency control: The transaction must coordinate with other concurrent transactions on different hosts to ensure the isolation and consistency of the data.
- Deadlocks: The transaction may encounter circular dependencies on the locks or resources on different hosts, causing the transaction to wait indefinitely or abort.

## Two-Phase Commit Protocol

The two-phase commit protocol is a common technique for ensuring the atomicity and durability of distributed transactions. The protocol involves two phases:

- Prepare phase: The transaction manager asks each host involved in the transaction to prepare to commit or abort the transaction. Each host executes the operations of the transaction and locks the resources involved. If the host is ready to commit, it sends a prepared message to the transaction manager. If the host encounters any error or failure, it sends an abort message to the transaction manager and releases the locks.
- Commit phase: The transaction manager decides whether to commit or abort the transaction based on the messages received from the hosts. If all the hosts are prepared, the transaction manager sends a commit message to each host and commits the transaction. If any host has aborted, the transaction manager sends an abort message to each host and aborts the transaction. Each host then releases the locks and acknowledges the transaction manager.

The two-phase commit protocol ensures that either all the hosts commit the transaction or none of them do. However, the protocol also has some drawbacks, such as:

- Blocking: The protocol blocks the hosts from executing other transactions until the transaction manager decides the outcome of the transaction. This reduces the concurrency and availability of the system.
- In-doubt transactions: If the transaction manager or any host fails or loses communication during the protocol, the transaction may become in-doubt, meaning that its outcome is unknown. The in-doubt transactions may hold the locks and resources indefinitely, causing other transactions to wait or fail. The in-doubt transactions must be resolved manually or automatically by using a timeout mechanism or a voting protocol.
- Single point of failure: The transaction manager is a critical component of the protocol. If the transaction manager fails, the protocol cannot proceed and the transactions may become in-doubt. The transaction manager must be reliable and fault-tolerant to avoid this problem.