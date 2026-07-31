### Flat and nested distributed transactions

- A **distributed transaction** is a transaction that accesses objects managed by multiple servers .
- A distributed transaction must maintain the **ACID** properties of atomicity, consistency, isolation, and durability across all the servers involved .
- A distributed transaction can be structured in two different ways: **flat** or **nested** .

#### Flat transactions

- A **flat transaction** has a single initiating point (**Begin**) and a single end point (**Commit** or **Abort**) .
- A flat transaction is usually simple and short-lived, and does not allow any subtransactions .
- A flat transaction uses a **two-phase commit protocol** (2PC) to coordinate the commit or abort decision among all the servers .
- A flat transaction has the following drawbacks :
  - It may cause long blocking times and high resource consumption on the servers.
  - It may suffer from failures and inconsistencies due to network or server crashes.
  - It may not support complex or long-running activities that require multiple steps or interactions.

#### Nested transactions

- A **nested transaction** is a transaction that can be decomposed into smaller subtransactions  .
- A nested transaction has a single initiating point (**Begin**) and a single end point (**Commit** or **Abort**), but also allows intermediate points (**Partial Commit** or **Partial Abort**) for the subtransactions  .
- A nested transaction is usually complex and long-lived, and supports hierarchical and modular decomposition of a transaction  .
- A nested transaction uses a **saga protocol** or a **compensation protocol** to coordinate the commit or abort decision among all the servers  .
- A nested transaction has the following advantages  :
  - It reduces the blocking times and resource consumption on the servers by committing or aborting subtransactions independently.
  - It tolerates failures and inconsistencies by using compensating actions or undo logs to restore the previous state of the servers.
  - It supports complex or long-running activities that require multiple steps or interactions by allowing partial results and flexible control.