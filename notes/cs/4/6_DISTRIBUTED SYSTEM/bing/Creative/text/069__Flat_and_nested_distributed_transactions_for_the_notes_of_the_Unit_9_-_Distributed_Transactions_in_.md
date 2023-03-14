### Flat and nested distributed transactions

- A distributed transaction is a transaction that accesses objects managed by multiple servers .
- A distributed transaction must maintain the ACID properties of atomicity, consistency, isolation and durability.
- A distributed transaction requires a coordinator to control the execution and termination of the transaction.
- A distributed transaction can be structured in two different ways: flat or nested .

#### Flat transactions

- A flat transaction has a single begin point and a single end point (commit or abort) .
- A flat transaction is usually simple and short-lived .
- A flat transaction performs operations on objects in a sequential order.
- A flat transaction can only wait for one object at a time when servers use locking.

#### Nested transactions

- A nested transaction is a transaction that contains subtransactions within it .
- A nested transaction has a hierarchical structure, where the top-level transaction is the parent and the subtransactions are the children .
- A nested transaction can perform operations on objects in parallel.
- A nested transaction can abort a subtransaction without aborting the whole transaction .
- A nested transaction can commit a subtransaction to a local checkpoint, which can be undone if the parent transaction aborts .