### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is a technique to distribute data across multiple servers or locations, so that users can access data relevant to their activities without interfering with the work of others, and to improve availability, performance, and fault-tolerance of the system.
- Transactions with replicated data are transactions that involve data items that are replicated on different servers or locations, and need to be synchronized and consistent after the transaction.
- Transactions with replicated data pose several challenges for distributed systems, such as:
  - How to ensure atomicity and durability of transactions that span multiple servers or locations?
  - How to ensure consistency and isolation of transactions that access or update replicated data items?
  - How to handle concurrency, conflicts, and failures of transactions with replicated data?
  - How to balance the trade-offs between performance, availability, and consistency of transactions with replicated data?
- There are different approaches to handle transactions with replicated data, such as:
  - Two-phase commit protocol (2PC): A distributed protocol that ensures atomicity and durability of transactions that span multiple servers or locations, by using a coordinator and participants to agree on the outcome of the transaction (commit or abort) in two phases: prepare and commit/abort.
  - Quorum-based protocols: A distributed protocol that ensures consistency and availability of transactions that access or update replicated data items, by using a quorum (a subset of replicas) to perform read or write operations, and to resolve conflicts or failures.
  - Optimistic replication: A distributed protocol that allows transactions to access or update replicated data items without coordination or locking, and to detect and resolve conflicts or inconsistencies later, by using versioning, validation, and reconciliation techniques.
  - Elastic database transactions: A distributed protocol that enables transactions across cloud databases that are part of the same logical group, by using .NET libraries that ensure two-phase commit where necessary to ensure atomicity.