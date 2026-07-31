 Here is the content written in a formal tone without any emojis or external links in Markdown format with points on the given topic:

### Recovery from Transaction Failures

1. Transaction failure: When a transaction is unable to complete its execution successfully, it is said to have failed. This can happen due to system crashes, network failures, etc.
2. Need for recovery: When a transaction fails, the database may be left in an inconsistent state. To maintain consistency, it is necessary to undo the changes made by the failed transaction and redo the changes of committed transactions that were affected by the failed one. This process of restoring consistency is called recovery.
3. Recovery techniques: The most common techniques for recovery are:
- Rollback: The changes made by the failed transaction are undone to restore the database to its state before the transaction began.
- Rollforward: The changes made by committed transactions that were affected by the failed transaction are redone. This is done using transaction logs that store the changes made by committed transactions.
- Combination of rollforward and rollback: This technique first rolls back changes of the failed transaction and then rolls forward changes of committed transactions to restore consistency and recover the database.

The above points cover the key details about recovery from transaction failures for the given topic in a formal tone with no emojis or external links as required. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.