# Flat and Nested Distributed Transactions

A distributed transaction is a transaction that accesses objects managed by multiple servers. A distributed transaction must maintain the ACID properties of a transaction, which means that it must be atomic, consistent, isolated, and durable. Atomicity means that either all the servers involved in the transaction commit the transaction or all of them abort the transaction. Consistency means that the transaction preserves the integrity constraints of the data. Isolation means that the transaction does not interfere with other concurrent transactions. Durability means that the effects of the transaction are permanent even in the case of failures.

Distributed transactions can be structured in two different ways: flat transactions and nested transactions.

## Flat Transactions

A flat transaction has a single initiating point (Begin) and a single end point (Commit or Abort). They are usually very simple and are generally used for short activities rather than larger ones. A flat transaction can be coordinated by a single server, called the transaction manager, which is responsible for initiating, committing, or aborting the transaction. The transaction manager communicates with the servers that participate in the transaction using a two-phase commit protocol, which ensures that all the servers agree on the outcome of the transaction.

## Nested Transactions

A nested transaction is a transaction that contains other transactions as subtransactions. A nested transaction has a hierarchical structure, where the top-level transaction is called the root transaction and the subtransactions are called the branches. A nested transaction can be used to decompose a complex transaction into smaller and more manageable units. A nested transaction can also provide more concurrency and fault tolerance than a flat transaction, as the subtransactions can execute in parallel and can be independently committed or aborted.

A nested transaction can be coordinated by a distributed transaction manager, which is a collection of servers that cooperate to manage the transaction. The distributed transaction manager communicates with the servers that participate in the transaction using a nested two-phase commit protocol, which extends the two-phase commit protocol to handle the hierarchical structure of the transaction. The nested two-phase commit protocol ensures that all the servers agree on the outcome of the transaction and that the subtransactions are consistent with the root transaction.