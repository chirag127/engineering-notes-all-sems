```markdown
## Unit 7 - Transaction Processing Concepts

- A transaction is a logical unit of work that accesses and possibly modifies data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that a transaction either executes all or none of its operations.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it were the only one running on the database.
- Durability means that the effects of a transaction persist even if the system fails.
- A transaction processing system is a system that supports the execution of transactions on a large database with many concurrent users.
- A transaction processing system has three components: a transaction manager, a scheduler, and a recovery manager.
- A transaction manager is responsible for starting, committing, or aborting transactions.
- A scheduler is responsible for controlling the order of execution of operations from different transactions.
- A recovery manager is responsible for restoring the database to a consistent state in case of failures.
- A transaction processing system can use different techniques to ensure the ACID properties of transactions, such as locking, timestamping, logging, and checkpointing.
- A locking protocol is a set of rules that determines when a transaction can acquire or release locks on data items.
- A timestamping protocol is a set of rules that determines the order of execution of transactions based on their assigned timestamps.
- A logging protocol is a set of rules that determines what information is recorded in a log file for each transaction.
- A checkpointing protocol is a set of rules that determines when and how the database and the log file are synchronized.
```