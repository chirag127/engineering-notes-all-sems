### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that accesses and possibly modifies data in a database or a system.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- A distributed transaction is a transaction that accesses data from multiple servers or systems that are connected by a network.
- A nested transaction is a transaction that contains other transactions as subtransactions.
- Nested transactions can be used to improve the modularity, concurrency, and fault tolerance of distributed systems.
- Nested transactions have the following characteristics:
  - A nested transaction can commit or abort independently of its parent transaction.
  - A nested transaction can see the effects of its parent and sibling transactions, but not of its children transactions.
  - A nested transaction can be partially committed, meaning that its effects are visible to its parent transaction, but not to other transactions.
  - A nested transaction can be flattened, meaning that its effects are merged with its parent transaction and treated as a single transaction.
- Nested transactions can be classified into two types: closed nested transactions and open nested transactions.
  - A closed nested transaction is a nested transaction that follows the strict two-phase locking protocol, meaning that it acquires all the locks before releasing any of them.
  - A closed nested transaction guarantees serializability, but may suffer from high locking overhead and deadlock.
  - A closed nested transaction can be implemented using the two-phase commit protocol, which ensures atomicity and durability of distributed transactions.
  - A open nested transaction is a nested transaction that relaxes the strict two-phase locking protocol, meaning that it can release some locks before acquiring others.
  - A open nested transaction may improve concurrency and performance, but may violate serializability and consistency.
  - A open nested transaction can be implemented using the compensating transactions technique, which uses undo and redo operations to restore consistency in case of failure or abort.