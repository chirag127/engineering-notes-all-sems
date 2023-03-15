### Validation Based Protocol

Validation-based protocol, also known as optimistic concurrency control, is a concurrency control technique used in database management systems. It is based on the assumption that conflicts between transactions are rare and that it is more efficient to allow transactions to execute concurrently and then check for conflicts before committing the changes.

Here are the key points to remember about validation-based protocol:

1. Transactions are allowed to execute concurrently without any locking or synchronization.
2. Before committing the changes, each transaction must go through a validation phase to check for conflicts with other transactions.
3. If a conflict is detected, the transaction is rolled back and must be restarted.
4. The validation phase can be implemented using timestamps or other techniques to determine the order of transactions and detect conflicts.
5. Validation-based protocol can improve performance in systems where conflicts are rare, but it can also increase the overhead of checking for conflicts and rolling back transactions.

This is a brief overview of validation-based protocol in the context of concurrency control techniques in database management systems. It is important to understand this concept when studying the subject of Basics of Database Management System, particularly in Unit 8 - Concurrency Control Techniques.