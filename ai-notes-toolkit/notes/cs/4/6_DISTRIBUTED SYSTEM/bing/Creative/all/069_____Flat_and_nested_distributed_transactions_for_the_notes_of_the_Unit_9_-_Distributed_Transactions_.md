# Flat and Nested Distributed Transactions

## Introduction

- A **transaction** is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: **atomicity**, **consistency**, **isolation**, and **durability** (ACID).
- A **flat or nested transaction** that accesses objects handled by different servers is referred to as a **distributed transaction**.
- When a distributed transaction reaches its end, in order to maintain the atomicity property of the transaction, it is mandatory that all of the servers involved in the transaction either **commit** the transaction or **abort** it.
- Distributed transactions can be structured in two different ways: **flat transactions** and **nested transactions**.

## Flat Transactions

- A **flat transaction** has a single initiating point (**Begin**) and a single end point (**Commit** or **Abort**) .
- They are usually very simple and are generally used for short activities rather than larger ones .
- A flat transaction can be coordinated by a **two-phase commit protocol** (2PC) or a **three-phase commit protocol** (3PC) .
- The 2PC protocol consists of two phases: a **voting phase** and a **decision phase** .
- In the voting phase, the **coordinator** (the server that initiates the transaction) sends a **prepare** message to all the **participants** (the servers that execute the transaction) and waits for their replies .
- The participants execute the transaction and send either a **yes** vote (if they are ready to commit) or a **no** vote (if they want to abort) to the coordinator .
- In the decision phase, the coordinator decides whether to commit or abort the transaction based on the votes received .
- If the coordinator receives a yes vote from all the participants, it sends a **commit** message to all of them and commits the transaction .
- If the coordinator receives a no vote from any participant, it sends an **abort** message to all of them and aborts the transaction .
- The 3PC protocol is an extension of the 2PC protocol that adds a third phase: a **pre-commit phase** .
- The pre-commit phase is used to avoid blocking in case of failures .
- In the pre-commit phase, the coordinator sends a **pre-commit** message to all the participants after receiving a yes vote from all of them in the voting phase .
- The participants acknowledge the pre-commit message and wait for the final decision from the coordinator .
- In the final decision phase, the coordinator sends either a **commit** or an **abort** message to all the participants based on the outcome of the pre-commit phase .
- If the coordinator receives an acknowledgment from all the participants in the pre-commit phase, it sends a commit message and commits the transaction .
- If the coordinator fails to receive an acknowledgment from any participant in the pre-commit phase, it sends an abort message and aborts the transaction .

## Nested Transactions

- A **nested transaction** is a transaction that contains other transactions as subtransactions .
- A nested transaction has a **root transaction** that initiates the nested transaction and a set of **subtransactions** that are executed by the root transaction or by other subtransactions .
- A nested transaction can be represented by a **transaction tree**, where the nodes are transactions and the edges are parent-child relationships .
- A nested transaction can be coordinated by a **sagas protocol** or a **nested two-phase commit protocol** (N2PC) .
- The sagas protocol is based on the idea of **compensating actions** .
- A compensating action is an action that undoes the effect of a previous action .
- For example, if a subtransaction books a flight, the compensating action is to cancel the flight .
- The sagas protocol works as follows :
  - The root transaction executes the subtransactions in a sequential order and records their compensating actions.
  - If a subtransaction commits successfully, the root transaction proceeds to the next subtransaction.
  - If a subtransaction aborts, the root transaction aborts and executes