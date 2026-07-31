# Distributed Database

A distributed database is a collection of databases that are physically stored on different network hosts and logically appear as a single database to the user. A distributed database can improve performance, reliability, availability, and scalability of data management.

# Transaction Processing Concept

A transaction is a logical unit of work that consists of one or more SQL statements executed by a single user. A transaction has the following properties:

- Atomicity: A transaction either commits or aborts as a whole. Partial changes are not visible to other users.
- Consistency: A transaction preserves the consistency of the database by ensuring that it satisfies all the integrity constraints.
- Isolation: A transaction is isolated from other concurrent transactions. The intermediate states of a transaction are not visible to other users.
- Durability: The effects of a committed transaction are permanent and survive any system failures.

# Distributed Transaction

A distributed transaction is a transaction that involves two or more network hosts that provide transactional resources, such as databases, message queues, or files. A distributed transaction requires a transaction manager that coordinates the execution and completion of the transaction across all the involved hosts.

# Two-Phase Commit Protocol

The two-phase commit protocol is a mechanism that ensures the atomicity and consistency of a distributed transaction. The protocol involves two phases:

- Prepare phase: The transaction manager asks all the involved hosts to prepare to commit the transaction. Each host executes the transaction locally and sends a reply indicating whether it is ready to commit or not.
- Commit phase: The transaction manager decides whether to commit or abort the transaction based on the replies from all the hosts. If all the hosts are ready to commit, the transaction manager sends a commit message to all the hosts. Otherwise, it sends an abort message. Each host then commits or aborts the transaction accordingly.

# In-Doubt Transactions

A transaction becomes in-doubt if the two-phase commit protocol fails due to a network or system failure. For example, if the transaction manager crashes after sending the prepare message, some hosts may not receive the commit or abort message and remain in a prepared state. In this case, the transaction is in-doubt and its final outcome is unknown.

# Recovery of In-Doubt Transactions

To recover from in-doubt transactions, the transaction manager and the hosts use a mechanism called presumed abort or presumed commit. In this mechanism, each host maintains a log of the prepared transactions and their outcomes. The transaction manager also maintains a log of the committed transactions. When a failure occurs, the transaction manager and the hosts communicate with each other to resolve the in-doubt transactions. The transaction manager can either query the hosts for the status of the prepared transactions, or broadcast the list of the committed transactions. The hosts can then commit or abort the in-doubt transactions based on the information from the transaction manager.