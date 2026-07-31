### Recovery in Concurrent Systems

- Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while preserving the effects of concurrent transactions that did not cause the failure.
- Recovery in concurrent systems is challenging because of the interleaving of operations from different transactions, which may affect the same data items or resources.
- Recovery in concurrent systems requires coordination between the concurrency control and the recovery mechanisms, to ensure that the system maintains the ACID properties of transactions (atomicity, consistency, isolation, and durability).
- Recovery in concurrent systems can be classified into two main categories: backward recovery and forward recovery.

#### Backward Recovery

- Backward recovery is the technique of undoing the effects of erroneous or incomplete transactions, and restoring the system to a previous consistent state.
- Backward recovery relies on logging the operations and data values of transactions, so that they can be reversed in case of a failure.
- Backward recovery can be done in different ways, depending on the concurrency control scheme used, such as:
  - Interaction with concurrency control: The recovery scheme depends on the concurrency control scheme, such as locking, timestamp ordering, or optimistic concurrency control, to determine which transactions need to be undone and in what order.
  - Transaction rollback: The recovery scheme aborts and undoes the transactions that are affected by the failure, either partially or completely, and restarts them later.
  - Checkpoints: The recovery scheme periodically saves the state of the system and the transactions, so that in case of a failure, it can undo the transactions that occurred after the last checkpoint, and resume from there.
  - Restart recovery: The recovery scheme restarts the system after a failure, and uses the log to undo the transactions that were not committed before the failure, and redo the transactions that were committed but not reflected in the database.

#### Forward Recovery

- Forward recovery is the technique of correcting the effects of erroneous or incomplete transactions, and advancing the system to a new consistent state.
- Forward recovery relies on detecting and resolving the errors or inconsistencies in the system, without undoing the transactions that caused them.
- Forward recovery can be done in different ways, such as:
  - Compensation: The recovery scheme applies compensating operations to reverse the effects of erroneous transactions, without aborting them.
  - Majority consensus: The recovery scheme uses a voting protocol to determine the correct value of a data item or a resource, based on the majority of the replicas or participants in the system.
  - Error masking: The recovery scheme uses redundancy or fault tolerance techniques to mask the errors or inconsistencies in the system, and continue the normal operation.