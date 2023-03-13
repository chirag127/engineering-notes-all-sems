A flat or nested transaction that accesses objects handled by different servers is referred to as a distributed transaction. When a distributed transaction reaches its end, in order to maintain the atomicity property of the transaction, it is mandatory that all of the servers involved in the transaction either commit the transaction or abort it.

Distributed transactions can be structured in two different ways: flat transactions and nested transactions.

A flat transaction has a single initiating point (Begin) and a single end point (Commit or abort). They are usually very simple and are generally used for short activities rather than larger ones.

A nested transaction is a transaction that is composed of a number of subtransactions, each of which may be distributed. A nested transaction has a root transaction and several subtransactions. Each subtransaction may have its own subtransactions, forming a hierarchy. A subtransaction can commit or abort independently, but its effects are not permanent until the root transaction commits.

The following diagram illustrates the basic structure of a flat and a nested distributed transaction using ASCII art:

Flat transaction:

    +-----------------+    +-----------------+    +-----------------+
    | Server 1        |    | Server 2        |    | Server 3        |
    +-----------------+    +-----------------+    +-----------------+
    | Begin           |    | Begin           |    | Begin           |
    |                 |    |                 |    |                 |
    | Do some work    |    | Do some work    |    | Do some work    |
    |                 |    |                 |    |                 |
    | Commit/Abort    |    | Commit/Abort    |    | Commit/Abort    |
    +-----------------+    +-----------------+    +-----------------+
       |                 |    |                 |    |
       +-----------------+----+-----------------+----+
                             |
                             V
    +-----------------+
    | Coordinator     |
    +-----------------+
    | 2PC protocol    |
    +-----------------+

Nested transaction:

    +-----------------+    +-----------------+    +-----------------+
    | Server 1        |    | Server 2        |    | Server 3        |
    +-----------------+    +-----------------+    +-----------------+
    | Begin           |    | Begin           |    | Begin           |
    |                 |    |                 |    |                 |
    | Do some work    |    | Do some work    |    | Do some work    |
    |                 |    |                 |    |                 |
    | Commit/Abort    |    | Commit/Abort    |    | Commit/Abort    |
    +-----------------+    +-----------------+    +-----------------+
       |                 |    |                 |    |
       +-----------------+----+-----------------+----+
                             |
                             V
    +-----------------+    +-----------------+    +-----------------+
    | Subtransaction  |    | Subtransaction  |    | Subtransaction  |
    +-----------------+    +-----------------+    +-----------------+
    | Begin           |    | Begin           |    | Begin           |
    |                 |    |                 |    |                 |
    | Do some work    |    | Do some work    |    | Do some work    |
    |                 |    |                 |    |                 |
    | Commit/Abort    |    | Commit/Abort    |    | Commit/Abort    |
    +-----------------+    +-----------------+    +-----------------+
       |                 |    |                 |    |
       +-----------------+----+-----------------+----+
                             |
                             V
    +-----------------+
    | Root transaction|
    +-----------------+
    | Begin           |
    |                 |
    | Do some work    |
    |                 |
    | Commit/Abort    |
    +-----------------+