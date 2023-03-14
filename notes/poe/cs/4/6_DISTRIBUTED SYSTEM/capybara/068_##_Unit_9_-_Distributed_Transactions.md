## Unit 9 - Distributed Transactions

Distributed transactions are transactions that involve multiple resources and are coordinated by a transaction manager. In a distributed system, transactions may involve multiple nodes or systems, each having their own database, and the transaction manager ensures that all the nodes involved in the transaction are in a consistent state. In this unit, we will learn about the concepts and techniques involved in distributed transactions.

### Concepts

1. **Transaction Manager**: A transaction manager is responsible for coordinating distributed transactions. It ensures that all the resources involved in the transaction are in a consistent state and that the transaction is either committed or rolled back as a whole.

2. **Two-Phase Commit Protocol**: The two-phase commit protocol is a distributed algorithm that ensures atomicity of transactions over multiple nodes. In the first phase, the transaction manager asks each resource to prepare for commit. In the second phase, the transaction manager tells each resource to commit or abort the transaction.

3. **Transaction Isolation Levels**: Transaction isolation levels define the degree of isolation between concurrent transactions. The different isolation levels are Read Uncommitted, Read Committed, Repeatable Read, and Serializable.

4. **Deadlocks**: Deadlocks occur when two or more transactions are waiting for each other to release a resource. Distributed transactions are more prone to deadlocks due to the involvement of multiple resources.

### Techniques

1. **Two-Phase Locking**: Two-phase locking is a concurrency control technique used in distributed transactions. It ensures that a transaction acquires all the necessary locks before performing any updates and releases all the locks after the transaction is completed.

2. **Timestamp Ordering**: Timestamp ordering is a concurrency control technique that assigns timestamps to each transaction and orders them based on their timestamps. It ensures that transactions are executed in a serializable order.

3. **Optimistic Concurrency Control**: Optimistic concurrency control is a technique that assumes that conflicts between transactions are rare and allows multiple transactions to access the same resource concurrently. It detects conflicts at commit time and rolls back conflicting transactions.

### Advantages

1. Distributed transactions enable applications to scale horizontally by distributing data across multiple nodes.

2. Distributed transactions allow for fault tolerance, as transactions can be rerouted to other nodes if one node fails.

3. Distributed transactions can improve performance by allowing transactions to be executed concurrently across multiple nodes.

### Disadvantages

1. Distributed transactions can be complex to implement and manage.

2. Distributed transactions can suffer from performance issues, such as increased latency due to the involvement of multiple nodes.

3. Distributed transactions can be prone to deadlocks and other concurrency issues.

### Applications

1. Distributed transactions are commonly used in distributed databases and distributed systems.

2. Distributed transactions are also used in e-commerce applications for processing transactions across multiple nodes.

3. Distributed transactions can be used in financial systems for processing transactions across multiple banks and other financial institutions.

### Learning Tricks

1. Mnemonic: TPC - Two-Phase Commit Protocol
2. Mnemonic: TOM - Two-Phase Locking, Optimistic Concurrency Control, and Timestamp Ordering are the three concurrency control techniques used in distributed transactions.
3. Draw a diagram representing the two-phase commit protocol to better understand the concept. 

```
                    +--------------+
                 /--|  Coordinator |
                /   +--------------+
+-----------+ /
|           |/
|  Resource |\
|           | \
+-----------+  \
                 \   +-----------+
                  \--|  Resource |
                     +-----------+
```
In the diagram, the coordinator initiates the two-phase commit protocol and communicates with the resources involved in the transaction.