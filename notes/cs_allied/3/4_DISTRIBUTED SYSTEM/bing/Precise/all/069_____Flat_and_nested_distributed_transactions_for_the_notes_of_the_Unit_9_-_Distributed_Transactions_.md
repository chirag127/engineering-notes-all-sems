### Flat and Nested Distributed Transactions

A flat or nested transaction that accesses objects handled by different servers is referred to as a distributed transaction. When a distributed transaction reaches its end, in order to maintain the atomicity property of the transaction, it is mandatory that all of the servers involved in the transaction either commit the transaction or abort it.

Distributed transactions can be structured in two different ways: Flat transactions and Nested transactions.

#### Flat Transactions
A flat transaction has a single initiating point (Begin) and a single end point (Commit or abort). They are usually very simple and are generally used for short activities rather than larger ones.

#### Nested Transactions
Nested transactions offer a finer granularity of control over transactions. They take a top-down approach to decompose a complex transaction into subtransactions. Distributed transactions provided global integrity constraints over multiple resources. These resources soon started to be heterogeneous as well.

However, it is important to note that while flat transactions are the most prevalent model and are supported by most commercial database systems, nested transactions are supported by far fewer commercial database systems.