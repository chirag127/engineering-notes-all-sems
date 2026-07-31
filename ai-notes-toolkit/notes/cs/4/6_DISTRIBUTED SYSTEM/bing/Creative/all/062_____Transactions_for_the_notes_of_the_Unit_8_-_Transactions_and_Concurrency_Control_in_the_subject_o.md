# Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

# Distributed Transactions

- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator (DTC) is a component that manages the execution and coordination of distributed transactions.
- A distributed transaction has two phases: prepare and commit.
- In the prepare phase, the DTC sends a prepare message to each data server involved in the transaction, asking them to vote on whether they are ready to commit or abort the transaction.
- In the commit phase, the DTC collects the votes from the data servers and decides whether to commit or abort the transaction. If all the data servers vote to commit, the DTC sends a commit message to each data server, asking them to make the changes permanent. If any data server votes to abort, the DTC sends an abort message to each data server, asking them to undo the changes.

# Distributed Concurrency Control

- Distributed concurrency control is the concurrency control of a system distributed over a computer network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control assumes that conflicts are likely to occur and prevents them by locking the data items accessed by a transaction until it commits or aborts.
- Optimistic concurrency control assumes that conflicts are rare and detects them by validating the read and write sets of a transaction before it commits.
- Some common distributed concurrency control protocols are two-phase locking (2PL), timestamp ordering (TO), and optimistic concurrency control (OCC).