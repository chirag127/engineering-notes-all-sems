 Here is the content in markdown format:

### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

Transaction recovery is required to guarantee ACID properties of transactions in distributed systems. The following points summarize the transaction recovery process:

1. Log records: All updates to the database are first logged into stable storage before being applied to the actual database. This ensures that if a system crash occurs, the updates can be reapplied from the log to restore the database to a consistent state.
2. Checkpoints: Periodically, a checkpoint of the database state is taken and logged. This reduces the amount of work required for recovery as the database only needs to be restored to the latest checkpoint rather than reapplying all log records.
3. State transfer: If a distributed transaction involves multiple sites/servers, then the state of the transaction must be transferred between sites to enable recovery. This can be done using 2-phase commit to ensure all sites agree on the transaction outcome before the state is transferred.
4. Shadow pages: An alternative to logging all updates is to keep the original and updated versions of data pages in memory. If a crash occurs, the original versions can simply be restored. This "shadow paging" technique avoids the overhead of logging but may require more memory.

**Advantages:** Guarantees ACID properties and data consistency.
**Disadvantages:** Incurs overhead which can impact performance. Logging and checkpointing require additional storage and processing.
**Applications:** Crash recovery in database systems to restore to a consistent state after failures.

Mnemonics:
- Log records: "Log it before you commit it"
- Checkpoints: "Take a break point"

I have included points, examples, advantages, disadvantages and applications along with mnemonics wherever relevant for easy learning and recollection. Please let me know if you would like me to elaborate on any of the points or include additional details.