A flat or nested transaction that accesses objects handled by different servers is referred to as a distributed transaction. When a distributed transaction reaches its end, in order to maintain the atomicity property of the transaction, it is mandatory that all of the servers involved in the transaction either commit the transaction or abort it .

Distributed transactions can be structured in two different ways: flat transactions and nested transactions .

A flat transaction has a single initiating point (Begin) and a single end point (Commit or abort) . They are usually very simple and are generally used for short activities rather than larger ones. A client makes requests to multiple servers in a flat transaction. Before moving on to the next request, a flat client transaction completes the previous one. As a result, each transaction visits the server object in order.

A nested transaction is a transaction that contains one or more subtransactions . Each subtransaction has its own begin and end points, and can be committed or aborted independently . A nested transaction can be either distributed or local, depending on whether it accesses objects on multiple servers or not. A nested transaction can also be either top-level or nested, depending on whether it is initiated by a client or by another transaction.

The following diagram illustrates the basic architecture of a flat and nested distributed transaction using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Server X     |     |    Server Y     |     |    Server Z     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Client A     |     |    Client B     |     |    Client C     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |                      +-----------------+
       |                      |                      |                      |                 |
       |                      |                      |                      |    Client D     |
       |                      |                      |                      |                 |
       |                      |                      |                      +-----------------+
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|  Coordinator A  |     |  Coordinator B  |     |  Coordinator C  |     |  Coordinator D  |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       +