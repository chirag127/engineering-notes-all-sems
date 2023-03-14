 Here is the content in markdown format for the topic ### Concurrency control in distributed transactions for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM:

### Concurrency control in distributed transactions

- Concurrency control ensures correctness of data when multiple transactions access and update shared data concurrently. It is challenging in distributed systems due to lack of global clock and different transaction executions at different sites.
- Following are the concurrency control techniques for distributed transactions:

1. Two-phase locking (2PL):
- Data items are locked by transactions before use.
- Locks are released in two phases:
    - Growing phase: Transactions acquire all locks needed.
    - Shrinking phase: Transactions release all locks.
- Prevents deadlock through lock ordering and detection.
- Prone to reduced concurrency due to early locking.

2. Optimistic concurrency control:
- Transactions execute without acquiring locks, assuming no conflicts.
- Before committing, each transaction validates that no other transaction has modified its read data (using timestamp/version numbers).
- If conflict is detected, transaction is aborted and re-executed.
- Improves concurrency but may suffer from excessive aborts and re-executions.

3. Timestamp ordering:
- Each transaction is assigned a unique timestamp on start.
- Transaction T2 can only commit if its timestamp is greater than the commit timestamp of all transactions T1 that have modified data read by T2.
- Ensures serializability but suffers from reduced concurrency.

**Mnemonics:**

- 2PL: Grow (acquire locks), Shrink (release locks)
- Optimistic: Assume no conflict, then validate and re-execute if conflict
- Timestamp: Greater timestamp wins

**Advantages:**

- 2PL: Prevents deadlock, less aborts
- Optimistic: High concurrency
- Timestamp: Ensures serializability

**Disadvantages:**

- 2PL: Low concurrency due to early locking
- Optimistic: Excessive aborts and re-executions
- Timestamp: Low concurrency