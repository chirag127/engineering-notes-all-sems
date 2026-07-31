## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.  
- A distributed transaction has the same ACID properties as a local transaction, which are atomicity, consistency, isolation, and durability. However, achieving these properties in a distributed environment is more challenging and requires additional protocols and mechanisms. 
- Some of the challenges and issues in distributed transactions are:
  - Network failures and partitions, which may cause communication problems between the transaction manager and the transactional resources, or among the transactional resources themselves. 
  - Concurrency and locking, which may cause deadlocks or conflicts when multiple transactions access the same data across different hosts. 
  - Data replication and consistency, which may cause data inconsistency or divergence when multiple copies of the same data are stored on different hosts and updated by different transactions. 
  - Performance and scalability, which may degrade as the number of hosts and transactions increases, due to the overhead of coordination and communication. 
- Some of the common protocols and mechanisms for distributed transactions are:
  - Two-phase commit (2PC), which is a protocol that ensures atomicity and durability of a distributed transaction by using a coordinator (usually the transaction manager) and a set of participants (usually the transactional resources) to vote and commit on the outcome of the transaction.  
  - Three-phase commit (3PC), which is a protocol that improves the availability and fault-tolerance of 2PC by introducing a third phase of pre-commit, which allows the participants to recover from network failures or partitions without blocking or aborting the transaction.  
  - Saga, which is a mechanism that relaxes the atomicity and isolation of a distributed transaction by allowing partial commits and compensating actions, which are used to undo the effects of a failed or aborted transaction. 
  - Eventual consistency, which is a mechanism that relaxes the consistency and isolation of a distributed transaction by allowing temporary data inconsistency or divergence, which is resolved over time by applying updates or reconciling conflicts.