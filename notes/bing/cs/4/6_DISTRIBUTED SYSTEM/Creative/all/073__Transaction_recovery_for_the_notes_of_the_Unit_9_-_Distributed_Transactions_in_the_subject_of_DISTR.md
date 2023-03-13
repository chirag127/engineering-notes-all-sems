### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the procedure of restoring the database to a consistent state after a transaction failure.
- Transaction failure can be caused by various reasons, such as system failure, hardware failure, network error, invalid data, application problems, etc.
- Transaction recovery is more difficult in distributed systems than in centralized systems, because of the following challenges:
  - The communication network may be unreliable and prone to failures.
  - The distributed transactions may involve multiple sites and resources, which may have different recovery protocols and policies.
  - The distributed transactions may have dependencies and conflicts with other transactions, which may affect the recovery process.
  - The distributed transactions may have partial or inconsistent information about the global state of the system, which may lead to incorrect recovery decisions.
- Transaction recovery in distributed systems can be achieved by using different techniques, such as:
  - UNDO/REDO: This technique involves undoing the effects of faulty transactions and redoing the effects of committed transactions. This technique requires logging the before and after images of the data items modified by the transactions, and using a two-phase commit protocol to ensure atomicity and durability of the transactions.
  - Compensation: This technique involves applying compensating transactions to reverse the effects of faulty transactions. This technique does not require logging the before images of the data items, but only the after images and the compensation logic. This technique also requires a two-phase commit protocol to ensure atomicity and durability of the transactions.
  - Saga: This technique involves decomposing a long-running transaction into a series of short subtransactions, each of which can be committed or compensated independently. This technique does not require a two-phase commit protocol, but relies on the application logic to coordinate the subtransactions and handle failures. This technique is suitable for transactions that involve heterogeneous data sources or services.
- Transaction recovery in distributed systems can be evaluated by using different criteria, such as:
  - Consistency: The degree to which the recovery technique preserves the consistency of the database and the application logic.
  - Availability: The degree to which the recovery technique minimizes the downtime and the blocking of the system resources.
  - Performance: The degree to which the recovery technique reduces the overhead and the latency of the transaction processing.
  - Scalability: The degree to which the recovery technique can handle the increasing number of transactions and sites in the system.
  - Simplicity: The degree to which the recovery technique is easy to implement and understand.
- Transaction recovery in distributed systems is an important and challenging topic that requires careful design and implementation of the recovery techniques and protocols. It is also a topic that has many trade-offs and variations depending on the application requirements and the system characteristics.