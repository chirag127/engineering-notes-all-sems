# Distributed Database for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A distributed database is a collection of databases that are physically distributed over different locations and connected by a network.
- A distributed transaction is a database transaction that involves two or more network hosts, each providing transactional resources such as data, locks, or logs.
- A transaction manager is a component that is responsible for creating and managing a global transaction that encompasses all operations against the distributed resources.
- A global transaction is a logical unit of work that ensures the atomicity, consistency, isolation, and durability (ACID) properties of a distributed transaction across all the involved hosts.
- A two-phase commit protocol is a mechanism that coordinates the commit or rollback of a global transaction by communicating with all the involved hosts and ensuring that they reach a consistent outcome.
- A transaction becomes in-doubt if the two-phase commit protocol fails due to network or system failures, leaving some hosts uncertain about the final outcome of the global transaction.
- A transaction recovery process is a procedure that resolves the in-doubt transactions by either committing or rolling back the changes on all the involved hosts, based on the available information and the predefined policies.