```markdown
# Flat and Nested Distributed Transactions

## Introduction

- A **distributed transaction** is a flat or nested transaction that accesses objects managed by multiple servers .
- A **flat transaction** has a single begin point and a single end point (commit or abort). It is usually simple and short-lived.
- A **nested transaction** has a hierarchical structure of subtransactions, each with its own begin and end points. It is usually complex and long-lived.
- Both flat and nested transactions require atomicity, consistency, isolation and durability (ACID) properties to be maintained across multiple servers .

## Flat Transactions

- A flat transaction can be implemented using a **two-phase commit protocol (2PC)**  .
- In 2PC, there is a **coordinator** that initiates the transaction and collects the votes from the **participants** (servers) that execute the transaction  .
- The coordinator sends a **prepare** message to all the participants, asking them to prepare to commit or abort the transaction  .
- The participants reply with a **vote** message, either **yes** (ready to commit) or **no** (ready to abort)  .
- If the coordinator receives a **yes** vote from all the participants, it sends a **commit** message to all of them, asking them to commit the transaction  .
- If the coordinator receives a **no** vote from any participant, or a timeout occurs, it sends an **abort** message to all the participants, asking them to abort the transaction  .
- The participants acknowledge the coordinator's message and release the resources held by the transaction  .
- The coordinator records the outcome of the transaction in a **log**  .

## Nested Transactions

- A nested transaction can be implemented using a **sagas** protocol .
- In sagas, a complex transaction is decomposed into a sequence of **compensatable subtransactions** .
- Each subtransaction has a **compensation action** that can undo its effects in case of a failure .
- The subtransactions are executed in a **forward** direction, committing their local effects as they go .
- If a subtransaction fails, the saga is aborted and the **backward** direction is taken, executing the compensation actions of the previous subtransactions in reverse order .
- The saga maintains the consistency of the system by ensuring that either all the subtransactions are executed or none of them are .
- The saga allows for more concurrency and flexibility than the flat transaction, as it does not require locking the resources for the entire duration of the transaction .
```