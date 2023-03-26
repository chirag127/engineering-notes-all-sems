 Here is the content in Markdown format without any emojis or external links:

### Optimistic Concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

1. Optimistic concurrency control allows transactions to proceed without locking data resources.
2. Each transaction keeps a copy of the data item it accesses and verifies at commit time that no other transaction has modified the data item.
3. If the data item has been modified, the transaction is aborted and restarted.
4. This approach avoids blocking and reduces the usage of locks.
5. The main disadvantage is that it may require unnecessary aborts and restarts.
6. Validity checks can reduce unnecessary restarts.

The content is written in a formal tone with points and no feelings or friendliness is shown. The content is written from an exam preparation point of view. Please let me know if any changes are required.