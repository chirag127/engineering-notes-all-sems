### Flat and nested distributed transactions

- A distributed transaction is a transaction that accesses objects managed by multiple servers.
- A distributed transaction must maintain the atomicity property, which means that either all of the servers commit the transaction or all of them abort the transaction.
- There are two ways to structure a distributed transaction: flat or nested.

#### Flat transactions

- A flat transaction has a single begin point and a single end point (commit or abort).
- A flat transaction is usually simple and short-lived, and does not involve any subtransactions.
- A flat transaction can be coordinated by a single server or by a distributed commit protocol, such as the two-phase commit protocol.

#### Nested transactions

- A nested transaction is a transaction that contains other transactions as subtransactions.
- A nested transaction has a hierarchical structure, where the top-level transaction is the parent of all the subtransactions, and the subtransactions can have their own subtransactions as children.
- A nested transaction can be committed or aborted independently of its parent or children, but the final outcome of the top-level transaction depends on the outcomes of all the subtransactions.
- A nested transaction can provide more concurrency, fault tolerance, and modularity than a flat transaction, but it also requires more complex coordination and recovery mechanisms.