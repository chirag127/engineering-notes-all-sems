 Here is the content in markdown format:

### Detection & Resolution for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

* Detection: Some of the techniques used for detecting distributed deadlocks are:

1. Time-out: Each transaction is assigned a maximum time that it can hold locks. If this time is exceeded, the transaction releases all its locks and aborts. This ensures that deadlocks are avoided. However, the chosen time-out value is critical. If it is too small, transactions may abort unnecessarily. If it is too large, deadlocks may occur.

2. Locking hierarchy: A partial ordering is defined among different types of locks and transactions must obtain locks in the defined order. This method ensures freedom from deadlock but may reduce concurrency.

3. Detection and recovery: The state of the system is constantly monitored to detect deadlocks. If a deadlock is detected, one or more transactions are aborted to break the deadlock. The aborted transactions are rescheduled. This method maximizes concurrency but may reduce performance due to overhead of deadlock detection.

* Resolution: Some of the common approaches to resolve distributed deadlocks are:

1. Abort all transactions: Abort all the transactions that are involved in the deadlock. This ensures that the deadlock is resolved but leads to wasted work.

2. Selectively abort transactions: Examine the transactions involved in the deadlock and abort the transaction that has acquired the minimum number of locks. This leads to less wasted work but may not always resolve the deadlock.

3. Preempt resources: The lock manager may preempt locks from transactions to resolve the deadlock. This method minimizes wasted work but may reduce concurrency.

4. Ignore deadlock: The system may choose to ignore the deadlock in the hope that the deadlock may resolve on its own after some time due toTransaction completion or lock release. However, this may not always happen and lead to system freeze.

[Diagrams and examples can be included here if helpful.]