# Transaction Recovery for the Notes of the Unit 9 - Distributed Transactions in the Subject of Distributed System

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has the properties of atomicity, consistency, isolation, and durability (ACID).
- A distributed transaction is a transaction that spans multiple sites or nodes in a distributed system.
- A distributed transaction may fail due to various reasons, such as network failures, site failures, communication failures, or concurrency conflicts.
- Transaction recovery is the process of restoring the database to a consistent state after a transaction failure.
- Transaction recovery in a distributed system is more complex than in a centralized system, because it involves coordinating the recovery actions of multiple sites or nodes.
- Transaction recovery in a distributed system can be classified into two types: backward recovery and forward recovery.
- Backward recovery is the process of undoing the effects of a failed transaction by restoring the previous values of the data items that were modified by the transaction.
- Forward recovery is the process of redoing the effects of a committed transaction by applying the new values of the data items that were modified by the transaction.
- Transaction recovery in a distributed system can be implemented using various techniques, such as logging, shadow versions, two-phase commit protocol, three-phase commit protocol, or consensus protocols.
- Logging is a technique that records the changes made by a transaction in a log file, which can be used to undo or redo the transaction in case of a failure.
- Shadow versions is a technique that maintains multiple versions of the data items, and switches to the appropriate version depending on the outcome of the transaction.
- Two-phase commit protocol is a protocol that ensures the atomicity of a distributed transaction by coordinating the commit or abort decision of all the sites or nodes involved in the transaction.
- Three-phase commit protocol is a protocol that improves the availability of a distributed transaction by avoiding blocking situations in case of network partitions or site failures.
- Consensus protocols are protocols that enable a group of sites or nodes to agree on a common value or decision, such as the commit or abort of a distributed transaction.