### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that accesses and possibly modifies data in a database or a system.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- A distributed transaction is a transaction that accesses data from multiple servers or systems that are connected by a network.
- A nested transaction is a transaction that contains other transactions as subtransactions.
- A nested transaction can be used to improve the performance, modularity, and fault tolerance of distributed transactions.
- A nested transaction has the following characteristics :
  - It has a parent transaction and zero or more child transactions.
  - It can commit or abort independently of its parent or child transactions.
  - It can pass data to or receive data from its parent or child transactions.
  - It can be serialized with respect to other transactions using conflict serializability or other criteria.
  - It can be recovered using a two-phase commit protocol or other methods.
- A nested transaction can be classified into two types:
  - Closed nested transaction: A nested transaction that does not share any data with other transactions outside its nesting hierarchy.
  - Open nested transaction: A nested transaction that can share data with other transactions outside its nesting hierarchy.
- A nested transaction can be implemented using different models, such as:
  - Flat model: A nested transaction is treated as a single transaction by the servers or systems involved.
  - Hierarchical model: A nested transaction is treated as a hierarchy of transactions by the servers or systems involved, and each level of the hierarchy has its own coordinator and participants.
  - Multilevel model: A nested transaction is treated as a multilevel transaction by the servers or systems involved, and each level of the hierarchy can have multiple coordinators and participants.