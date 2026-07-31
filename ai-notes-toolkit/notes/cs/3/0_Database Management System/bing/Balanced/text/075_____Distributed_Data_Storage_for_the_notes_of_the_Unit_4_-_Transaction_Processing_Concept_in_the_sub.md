### Distributed Data Storage for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A distributed database is a database that is stored across multiple computers or sites that are connected by a network .
- A distributed database management system (DDBMS) is a centralized software system that manages a distributed database in a manner as if it were all stored in a single location .
- A distributed database incorporates transaction processing, which is a program including a collection of one or more database operations.
- Transaction processing is an atomic process that is either entirely executed or not at all.
- In a distributed database system, transaction processing can be challenging because of the following issues:
  - Concurrency control: ensuring that concurrent transactions do not interfere with each other and maintain data consistency.
  - Distributed commit: ensuring that a transaction that spans multiple sites is either committed or aborted at all sites.
  - Failure recovery: ensuring that the system can recover from partial or total failures of sites or network links.
  - Data replication: ensuring that copies of data at different sites are consistent and up-to-date.
- To address these issues, distributed database systems use various techniques, such as:
  - Two-phase locking: a protocol that acquires and releases locks on data items to prevent conflicts among concurrent transactions.
  - Two-phase commit: a protocol that coordinates the commit or abort decision of a distributed transaction among all the sites involved.
  - Distributed snapshots: a method of capturing the global state of a distributed system at a certain point in time.
  - Quorum consensus: a method of ensuring data consistency among replicated copies by requiring a minimum number of sites to agree on a data value.
  - Timestamp ordering: a method of ordering transactions based on their logical timestamps to ensure serializability.