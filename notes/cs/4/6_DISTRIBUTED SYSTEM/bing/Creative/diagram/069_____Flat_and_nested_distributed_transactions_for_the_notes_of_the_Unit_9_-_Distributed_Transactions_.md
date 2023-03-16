### Flat and nested distributed transactions

- A **distributed transaction** is a transaction that accesses objects managed by multiple servers .
- A distributed transaction must maintain the **ACID** properties of atomicity, consistency, isolation, and durability across all the servers involved .
- A distributed transaction can be structured in two different ways: **flat** or **nested** .

#### Flat transactions

- A **flat transaction** has a single initiating point (Begin) and a single end point (Commit or Abort) .
- A flat transaction is usually simple and short-lived, and does not allow subtransactions .
- A flat transaction uses a **two-phase commit protocol** (2PC) to coordinate the commit or abort decision among all the servers .
- A flat transaction has the following phases :
  - **Voting phase**: The coordinator asks each server to vote on whether to commit or abort the transaction. Each server replies with a Yes or No vote.
  - **Decision phase**: The coordinator decides to commit the transaction if all the servers voted Yes, or to abort the transaction if any server voted No. The coordinator informs all the servers of the final decision.

#### Nested transactions

- A **nested transaction** is a transaction that can be decomposed into subtransactions, each with its own Begin and End points .
- A nested transaction is usually complex and long-lived, and allows subtransactions to be executed in parallel or sequentially .
- A nested transaction uses a **sagacommunication protocol** (SCP) to coordinate the commit or abort decision among all the servers .
- A nested transaction has the following phases :
  - **Execution phase**: The coordinator executes each subtransaction and collects the results. Each subtransaction can be committed or aborted independently, but the coordinator keeps track of the dependencies among them.
  - **Completion phase**: The coordinator decides to commit the transaction if all the subtransactions committed, or to abort the transaction if any subtransaction aborted. The coordinator informs all the servers of the final decision. If the transaction is aborted, the coordinator invokes the **compensation actions** of the committed subtransactions to undo their effects.