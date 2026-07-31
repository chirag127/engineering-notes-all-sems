## Unit 8 - Concurrency Control Techniques:

Concurrency control techniques are employed to maintain the consistency and integrity of the database in a multi-user environment where multiple transactions can access the same data concurrently. Here are some of the common concurrency control techniques:

1. Locking: 
   - Locking is a technique in which a transaction acquires a lock on a data item before accessing it. 
   - This ensures that only one transaction can access the data item at a time, preventing data inconsistencies.
   - Types of locks include shared locks and exclusive locks.

2. Timestamp Ordering:
   - Timestamp ordering is a technique in which each transaction is assigned a unique timestamp.
   - Transactions are executed based on their timestamp order, with earlier transactions executing first.
   - This technique ensures that transactions are executed in a serializable order, preventing conflicts and inconsistencies.

3. Optimistic Concurrency Control:
   - Optimistic concurrency control is a technique in which the system assumes that conflicts between transactions are rare.
   - Transactions are allowed to execute concurrently without acquiring locks on data items.
   - Before committing, the system checks for conflicts between transactions and resolves any conflicts that exist.

4. Multi-Version Concurrency Control:
   - Multi-version concurrency control is a technique in which multiple versions of a data item are maintained simultaneously.
   - Each transaction reads a specific version of a data item, depending on the transaction's timestamp.
   - This technique allows for high concurrency and reduces the need for locking.

5. Two-Phase Locking:
   - Two-phase locking is a technique in which transactions acquire locks in two phases.
   - In the first phase, locks are acquired on data items as they are accessed.
   - In the second phase, locks are released as the transaction is committed or rolled back.
   - This technique ensures serializability and prevents conflicts between transactions.

In conclusion, concurrency control techniques are essential for maintaining the consistency and integrity of a database in a multi-user environment. Each technique has its benefits and drawbacks, and the selection of a technique depends on the specific requirements of the system.