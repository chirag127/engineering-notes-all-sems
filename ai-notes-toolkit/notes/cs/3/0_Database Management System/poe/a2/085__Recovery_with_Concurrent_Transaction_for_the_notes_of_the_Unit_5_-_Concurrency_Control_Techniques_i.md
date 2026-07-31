 Here is the markdown content for the given topic:

### Recovery with Concurrent Transaction

1. When multiple transactions are executing concurrently, it may happen that some transactions commit while others abort. This can leave the database in an inconsistent state.
2. To handle such situations, we need to have a recovery procedure that undoes the effects of all transactions that were executing but did not commit at the time of failure.
3. The recovery manager uses the log records to undo the uncommitted transactions. It goes through the log in reverse chronological order, undoing the effects of each uncommitted transaction.
4. Once all such transactions have been undone, the recovery manager then goes forward through the log again, this time redo-ing the effects of all committed transactions to restore the database to a consistent state reflecting all committed updates.
5. This process of rolling back uncommitted transactions and then redoing committed transactions is known as rollback/recovery or undo/redo processing. The end result is to recover the database to a state that reflects only the changes due to transactions that committed successfully.
6. With recovery, the ACID properties of transactions can be guaranteed, even in the presence of failures. Recovery is what ensures durability of transaction updates - that committed changes persist even after failures.

The content is written in points and in markdown format without any emojis or external links as instructed. The tone is formal and no feelings are shown as directed. Please let me know if you would like me to modify or expand the content in any way.