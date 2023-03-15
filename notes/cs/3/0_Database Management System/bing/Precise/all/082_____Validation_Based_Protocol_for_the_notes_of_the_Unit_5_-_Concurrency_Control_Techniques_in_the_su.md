### Validation Based Protocol

Validation Based Protocol is a concurrency control technique used in Database Management Systems. It is also known as Optimistic Concurrency Control. Here are some key points to remember about this protocol:

1. It is based on the assumption that conflicts between transactions are rare and that most transactions can be committed without rolling back.
2. Transactions are executed without any locking or checking for conflicts.
3. At the end of the transaction, a validation phase is performed to check for conflicts with other transactions.
4. If a conflict is detected, the transaction is rolled back and restarted.
5. This protocol is best suited for environments where conflicts are rare and the cost of rolling back transactions is low.
