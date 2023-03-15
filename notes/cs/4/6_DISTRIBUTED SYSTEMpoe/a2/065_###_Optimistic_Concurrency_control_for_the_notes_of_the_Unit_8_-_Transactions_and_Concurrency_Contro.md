 Here is the content in markdown format for the topic ### Optimistic Concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM:

### Optimistic Concurrency control

- Optimistic concurrency control assumes that concurrent transactions will not conflict with each other, so it allows them to execute without locking data.
- Before committing a transaction, it is validated to check for conflicts. If a conflict is detected, the transaction is aborted and re-executed.
- Advantages:
-- Higher concurrency since no locking is required.
-- Deadlocks are avoided.
- Disadvantages:
-- May have to abort and re-execute transactions, leading to decreased performance.
-- Validation at commit time may be complex.
- Examples:
-- Timestamp ordering - Each transaction gets a timestamp, and the one with the latest timestamp wins in case of a conflict.
-- Multi-version concurrency control (MVCC) - Maintains multiple versions of data, allowing reads to not conflict with writes.

```
/* Mnemonics for remembering pros and cons:
Optimistic - no locking, high concurrency
Validation - may abort and re-execute
*/
```

- Applications: Databases, collaborative editing systems.
- In summary, optimistic concurrency control is useful when conflicts are expected to be rare, and the overhead of validation and occasional transaction re-execution is lower than the overhead of locking.

Does this help? Let me know if you would like me to elaborate on any of the points or add additional details.