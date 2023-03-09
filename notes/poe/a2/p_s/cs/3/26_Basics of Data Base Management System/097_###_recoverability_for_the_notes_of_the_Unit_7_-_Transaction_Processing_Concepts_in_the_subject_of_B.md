 Here is the content in markdown format for the topic ### recoverability for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System:

### Recoverability

- Recoverability refers to the ability of a database system to recover from failures and return to a consistent state.
- If a failure occurs, the partial effects of incomplete transactions must be undone, and the database must be restored to a state that is consistent with the effects of completed transactions.
- For recoverability, the database system must keep logs of all changes made to the database. The log entries are made before the actual changes occur to the database.
- In the event of a failure, the database can be restored to a consistent state by undoing the effects of incomplete transactions using the log entries and redoing the effects of completed transactions.
- The following properties are required for recoverable databases:

1. Logical atomicity: The effects of a transaction must be either completely present in the database or completely absent. There are no intermediate states.
2. Physical atomicity: Database changes must be made in units that can either be completely implemented or completely reversed.
3. Persistence: Once a transaction commits, its effects must persist even in the event of a failure. The log entries can be used to redo the transaction's effects during recovery.
4. Durability: The effects of a committed transaction must not be lost, even in the event of a failure. The log is critical for ensuring durability.

- The key techniques for ensuring recoverability are:

1. Logging: Maintaining a log of all changes to the database. The log entries are made before the actual changes occur.
2. Checkpointing: Periodically saving the state of the database to nonvolatile storage. This limits the amount of work required during recovery.
3. Shadow paging: Maintaining old and new versions of data pages in memory. If a transaction aborts, the old versions can be used to undo changes.

- The ability to recover from failures is critical to ensuring data integrity and availability in database systems. Careful logging, checkpointing, and other techniques are essential to achieving recoverability.