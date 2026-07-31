 Here is the content in markdown format without any emojis or external links:

### Concurrency control for the notes of the Unit 8 - Concurrency Control Techniques in the subject of Basics of Data Base Management System.

1. Serializable Schedule: A schedule is serializable if the ordering of any two operations in the schedule is the same as the ordering in some serial execution of those operations. Serializable schedule ensures that there are no conflicts between transactions.
2. Locking: Locking ensures that only one transaction can access the data at a time. There are two types of locks:
- Shared lock: Allows multiple transactions to read the data concurrently.
- Exclusive lock: Allows only one transaction to access the data.
3. Deadlock: When two or more transactions are waiting for each other to release locks, this condition is called deadlock. Deadlocks can be avoided by following protocols such as:
- Request all locks at once: Each transaction requests all the locks it needs at once. This avoids cyclic wait.
- Predefine lock ordering: If all transactions follow a strict lock ordering, deadlocks can be avoided.
4. Timestamp ordering: Each transaction is assigned a timestamp when it begins. Later transactions get higher timestamps. If there is a conflict, the transaction with the earlier timestamp aborts. This ensures serializability.

The content summarizes some key concurrency control techniques like serializable schedule, locking, deadlock handling, and timestamp ordering. The points are written in a formal tone with no emojis or external links as requested. Please let me know if you would like me to explain or add anything further.