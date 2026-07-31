# Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction is not affected by the concurrent execution of other transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

# Distributed Transactions

- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator (DTC) is a component that manages the coordination and execution of distributed transactions.
- A distributed transaction has two phases: the prepare phase and the commit phase.
- In the prepare phase, the DTC sends a prepare message to each data server involved in the transaction, asking them to vote on whether they are ready to commit or abort the transaction.
- In the commit phase, the DTC collects the votes from the data servers and decides whether to commit or abort the transaction. If all the data servers vote to commit, the DTC sends a commit message to each data server, asking them to make the changes permanent. If any data server votes to abort, the DTC sends an abort message to each data server, asking them to undo the changes.

# Distributed Concurrency Control

- Distributed concurrency control is the concurrency control of a system distributed over a computer network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be classified into two categories: centralized and decentralized.
- Centralized concurrency control relies on a single coordinator to manage the concurrency control of all the data servers. This approach simplifies the design and implementation, but introduces a single point of failure and a performance bottleneck.
- Decentralized concurrency control distributes the responsibility of concurrency control among the data servers. This approach improves the availability and scalability, but increases the complexity and communication overhead.
- Distributed concurrency control can use various techniques to ensure serializability, such as locking, timestamping, validation, and multiversioning.