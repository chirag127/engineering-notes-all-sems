### Flat and nested distributed transactions

- A **distributed transaction** is a flat or nested transaction that accesses objects managed by multiple servers .
- A distributed transaction must maintain the **atomicity** property, which means that either all of the servers involved in the transaction commit the transaction or all of them abort it .
- Distributed transactions can be structured in two different ways: **flat transactions** and **nested transactions** .

#### Flat transactions
- A **flat transaction** has a single initiating point (Begin) and a single end point (Commit or abort) .
- Flat transactions are usually simple and short-lived, and are suitable for activities that do not require complex coordination or recovery .
- Flat transactions use a **two-phase commit protocol** (2PC) to ensure atomicity across multiple servers .
- The 2PC protocol involves a **coordinator** and a set of **participants**. The coordinator initiates the transaction and sends requests to the participants. The participants execute the requests and send their votes (commit or abort) to the coordinator. The coordinator collects the votes and decides the outcome of the transaction. The coordinator then sends the decision (commit or abort) to the participants, who finalize the transaction accordingly .
- The 2PC protocol has some drawbacks, such as blocking, single point of failure, and lack of concurrency .

#### Nested transactions
- A **nested transaction** is a transaction that consists of a number of subtransactions, each of which may have its own Begin and Commit or abort points .
- Nested transactions are more complex and long-lived, and are suitable for activities that require modularization, fault isolation, or concurrency control .
- Nested transactions use a **sag
as protocol** to ensure atomicity across multiple servers.
- The sagas protocol involves breaking a transaction into a sequence of **compensatable** subtransactions. Each subtransaction can be committed independently, but if a subtransaction fails or aborts, then all the previous subtransactions must be **compensated** by executing some undo operations.
- The sagas protocol has some advantages, such as non-blocking, fault tolerance, and concurrency.