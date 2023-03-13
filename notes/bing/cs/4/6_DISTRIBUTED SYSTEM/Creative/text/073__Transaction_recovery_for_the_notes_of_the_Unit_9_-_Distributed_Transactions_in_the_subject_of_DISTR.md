### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring the consistency and correctness of a distributed database after a transaction failure or an abort.
- Transaction recovery is based on the following principles:
  - Atomicity: A transaction must either commit or abort as a whole, and no partial effects of a transaction should be visible to other transactions.
  - Durability: The effects of a committed transaction must be persistent and survive any system failures.
  - Isolation: A transaction must execute in isolation from other concurrent transactions, and no interference or conflicts should occur among them.
  - Consistency: A transaction must preserve the consistency constraints of the database, and the database must be in a consistent state before and after the transaction execution.
- Transaction recovery involves the following steps:
  - Detection: The system must detect the occurrence of a transaction failure or an abort, and identify the affected transactions and data items.
  - Classification: The system must classify the transactions into two categories: committed and aborted. Committed transactions are those that have successfully completed their execution and have received a commit decision from the coordinator. Aborted transactions are those that have either failed during their execution or have received an abort decision from the coordinator.
  - Compensation: The system must compensate for the effects of the aborted transactions by undoing their changes to the database. This can be done by using the undo log records that store the previous values of the data items modified by the transactions. The system must also ensure that the compensation actions are idempotent, meaning that they can be repeated without changing the outcome.
  - Redo: The system must redo the effects of the committed transactions by applying their changes to the database. This can be done by using the redo log records that store the new values of the data items modified by the transactions. The system must also ensure that the redo actions are idempotent, meaning that they can be repeated without changing the outcome.
  - Notification: The system must notify the participants of the final outcome of the transaction recovery, and release any locks or resources held by the transactions. The system must also update the transaction status to either committed or aborted, and delete the log records of the completed transactions.