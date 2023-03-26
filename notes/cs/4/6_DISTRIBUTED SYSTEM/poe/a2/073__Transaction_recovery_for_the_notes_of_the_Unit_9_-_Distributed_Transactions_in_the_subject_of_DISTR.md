 Here is the content in Markdown format without any emojis or external links:

### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM:

1. Transaction recovery is required to ensure ACID properties in case of failures.
2. Log-based recovery: The state of a transaction is logged before it is committed. In case of failure, the transaction state is recovered from the log. This ensures atomicity.
3. Checkpoint-based recovery: The system state is checkpointed at intervals. In case of failure, the system rolls back to the latest checkpoint and re-executes the transactions after that point. This may lead to loss of some completed transactions.
4. Deferred update: Updates are not applied to the database immediately. They are buffered and applied later. In case of failure, the updates in the buffer are discarded. This may lead to loss of some completed transaction updates.
5. Forward recovery: The system state is recovered by re-executing transactions from logged/checkpointed state. This may lead to duplication of some transaction effects.
6. Backward recovery: The system rolls back incomplete transactions and undoes the effects of committed transactions to recover to a previous correct state. This may lead to loss of some committed transaction updates.

The content is written in a formal tone with points and without any emojis or external links as per the given instructions. Please let me know if you would like me to modify or add any other content.