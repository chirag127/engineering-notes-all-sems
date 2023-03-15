### Distributed Database for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A distributed database is a collection of databases that are physically distributed over different locations and connected by a network.
- A distributed transaction is a database transaction that involves two or more network hosts, each providing transactional resources such as data, locks, or logs.
- A transaction manager is responsible for creating and managing a global transaction that encompasses all operations against such resources.
- A distributed transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that the transaction preserves the integrity constraints of the database.
- Isolation means that the transaction does not interfere with other concurrent transactions.
- Durability means that the effects of the transaction are permanent and survive failures.
- A distributed transaction can be executed using a two-phase commit protocol, which consists of two phases: prepare and commit.
- In the prepare phase, the transaction manager asks each participant to vote on whether to commit or abort the transaction, based on their local operations and resources.
- In the commit phase, the transaction manager decides whether to commit or abort the transaction, based on the votes received from the participants, and informs them of the decision.
- A transaction becomes in-doubt if the two-phase commit protocol fails, due to network or system failures, and the transaction manager or some participants do not know the final outcome of the transaction.
- An in-doubt transaction must be resolved by either committing or aborting it, based on the available information and recovery mechanisms.