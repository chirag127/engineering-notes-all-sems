 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

1. Locks are mechanisms used to restrict access to resources in a system to avoid inconsistent reads and writes.
2. They are used to ensure isolation and consistency in transactions.
3. Two types of locks:
 - Shared lock: Multiple transactions can read a data item concurrently but no transaction can write the data item.
 - Exclusive lock: Only one transaction can access the data item. No other transaction can read or write the data item.
4. Deadlock: When two or more transactions hold locks on resources the other transaction needs and are waiting for the other to release its lock. This leads to a permanent blocking of transactions.
5. Methods to handle deadlocks:
 - Deadlock prevention: Restrict operations that can lead to deadlocks.
 - Deadlock avoidance: Transaction requests for locks in a certain order to avoid deadlocks. The system keeps track of resource allocation and denies lock requests that can lead to deadlocks.
 - Deadlock detection and recovery: Allow deadlocks to occur but detect and resolve them using rollback and other techniques.

The content summarizes the key points around locks, the types of locks, deadlocks that can occur and methods to handle deadlocks. The points are written in a formal tone with no emojis or external links as requested. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.