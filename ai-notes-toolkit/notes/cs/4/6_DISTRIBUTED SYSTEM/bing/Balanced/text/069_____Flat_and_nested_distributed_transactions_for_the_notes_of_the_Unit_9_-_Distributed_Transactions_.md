### Flat and Nested Distributed Transactions

- A **distributed transaction** is a flat or nested transaction that accesses objects managed by multiple servers .
- A **flat transaction** has a single begin point and a single end point (commit or abort). It is usually simple and short-lived .
- A **nested transaction** has a hierarchical structure of subtransactions, each with its own begin and end points. It is usually complex and long-lived .
- A **flat distributed transaction** can be coordinated by a single transaction manager that communicates with all the servers involved in the transaction.
- A **nested distributed transaction** can be coordinated by a hierarchy of transaction managers, each responsible for a subtransaction and its children.
- The advantages of nested distributed transactions over flat distributed transactions are:
  - They allow partial commits, which means that some subtransactions can commit even if others abort, thus reducing the amount of work to be redone.
  - They allow concurrency control and recovery to be done locally, which means that each subtransaction can use its own locking and logging mechanisms, thus reducing the overhead and complexity of global coordination.
  - They allow better fault tolerance, which means that each subtransaction can handle its own failures and restarts, thus reducing the impact of failures on other subtransactions.