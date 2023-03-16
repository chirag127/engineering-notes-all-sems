## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.
- A distributed transaction ensures the ACID (Atomicity, Consistency, Isolation, Durability) properties across multiple hosts, meaning that either all the operations succeed or none of them, the data remains consistent, the concurrent transactions do not interfere with each other, and the effects of the transaction are permanent.
- A distributed transaction faces several challenges, such as network failures, host failures, concurrency control, deadlock detection, and recovery mechanisms.
- A distributed transaction can use different protocols to achieve coordination and consensus, such as two-phase commit, three-phase commit, Paxos, Raft, etc.