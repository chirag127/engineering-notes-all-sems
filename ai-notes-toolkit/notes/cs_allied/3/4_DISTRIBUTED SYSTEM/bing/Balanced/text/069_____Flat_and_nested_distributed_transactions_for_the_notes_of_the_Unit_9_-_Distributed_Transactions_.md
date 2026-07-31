### Flat and Nested Distributed Transactions

- A **flat or nested transaction** that accesses objects handled by different servers is referred to as a **distributed transaction** .
- When a distributed transaction reaches its end, in order to maintain the **atomicity property** of the transaction, it is mandatory that all of the servers involved in the transaction either **commit** the transaction or **abort** it .
- Distributed transactions can be structured in two different ways: **flat transactions** and **nested transactions** .
- A **flat transaction** has a single initiating point (**Begin**) and a single end point (**Commit** or **Abort**). They are usually very simple and are generally used for short activities rather than larger ones .
- A **nested transaction** is a transaction that consists of several subtransactions, each of which may be distributed. A nested transaction has a **root transaction** and several **subtransactions**. Each subtransaction may have its own subtransactions, forming a **tree structure** .
- A nested transaction has the following properties:
  - **Atomicity**: If the root transaction commits, then all the subtransactions commit. If the root transaction aborts, then all the subtransactions abort.
  - **Consistency**: Each subtransaction preserves the consistency of the data it accesses.
  - **Isolation**: The effects of a subtransaction are not visible to other subtransactions until the root transaction commits.
  - **Durability**: The effects of a committed subtransaction are persistent and not lost due to failures.
- A nested transaction allows more **flexibility** and **concurrency** than a flat transaction, as it can handle partial failures and independent recoveries of subtransactions. It also allows more **modularity** and **reuse** of subtransactions, as they can be composed into larger transactions.