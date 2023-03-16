# Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it were the only one in the system, without interference from other transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.

# Concurrency Control

- Concurrency control is the process of managing simultaneous execution of transactions in a shared database, to ensure the serializability and correctness of the transactions.
- Serializability is the property that the concurrent execution of a set of transactions is equivalent to some serial execution of the same transactions.
- Concurrency control can be achieved by using locking protocols, timestamp ordering, or optimistic methods.

# Distributed Transactions and Distributed Concurrency Control

- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator is a component that coordinates the execution and commitment of distributed transactions across multiple data servers.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be based on centralized, decentralized, or hierarchical approaches.
- Centralized approach uses a single coordinator to control the locking and commitment of all subtransactions in a distributed transaction.
- Decentralized approach uses a peer-to-peer communication among data servers to reach a consensus on the locking and commitment of subtransactions.
- Hierarchical approach uses a tree structure of coordinators to propagate the locking and commitment requests and responses among data servers.