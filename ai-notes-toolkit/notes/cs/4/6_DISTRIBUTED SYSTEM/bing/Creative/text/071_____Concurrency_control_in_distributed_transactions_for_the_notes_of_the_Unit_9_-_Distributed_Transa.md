### Concurrency control in distributed transactions

- Concurrency control is the process of managing the concurrent execution of transactions in a distributed database system, such that the ACID properties are preserved.
- Concurrency control aims to ensure the correctness, consistency, and isolation of transactions, while also maximizing the degree of concurrency and minimizing the overhead of synchronization.
- Concurrency control can be classified into two main categories: pessimistic and optimistic.
  - Pessimistic concurrency control assumes that conflicts are likely to occur and uses locking mechanisms to prevent them. Locking-based protocols require transactions to acquire locks on the data items they access, and release them when they are done. Locks can be shared or exclusive, depending on the operation (read or write) performed by the transaction. Locking-based protocols can be centralized, decentralized, or distributed .
  - Optimistic concurrency control assumes that conflicts are rare and allows transactions to execute without locking. However, before committing, transactions have to validate their read and write sets against other concurrent transactions. If a conflict is detected, the transaction is aborted and restarted. Optimistic concurrency control can be based on timestamps, validation numbers, or versions .
- Concurrency control in distributed transactions faces several challenges, such as:
  - Network latency and communication costs, which can affect the performance and scalability of the protocols.
  - Network failures and partitions, which can cause inconsistency and unavailability of the data.
  - Data replication and consistency, which require additional mechanisms to ensure that copies of the same data item are synchronized across different servers.
  - Deadlocks and livelocks, which can occur when transactions wait for each other to release locks or validate their operations .
- Concurrency control in distributed transactions can be improved by using various techniques, such as:
  - Adaptive concurrency control, which adjusts the level of concurrency and the type of protocol based on the workload characteristics and the system state.
  - Semantic concurrency control, which exploits the application semantics and the data dependencies to allow more concurrency and reduce conflicts.
  - Distributed commit protocols, which coordinate the final outcome of a distributed transaction across multiple servers. The most common protocol is the two-phase commit (2PC), which consists of a prepare phase and a commit phase. However, 2PC is blocking, meaning that if a server fails, the transaction cannot proceed. Therefore, variants of 2PC have been proposed, such as 3PC, 2PC*, and Paxos commit .
  - Compensation and sagas, which allow transactions to undo their effects in case of failures or conflicts, by executing compensating actions or reversing the sequence of operations.