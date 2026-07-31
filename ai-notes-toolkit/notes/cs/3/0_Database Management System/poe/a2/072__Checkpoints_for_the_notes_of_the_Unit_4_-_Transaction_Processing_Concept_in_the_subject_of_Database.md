 Here are the notes for Unit 4 - Transaction Processing Concept in Database Management System:

### Checkpoints for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System:

1. Transaction: A transaction is a single logical operation of a database application that accesses and possibly modifies the contents of a database.

2. Transaction Processing: Transaction processing refers to the execution of transactions in a database system. The main goals of transaction processing are performance, reliability, and data integrity.

3. ACID Properties: The four properties that a database system must guarantee for each transaction to ensures data integrity are:

A - Atomicity: Either all actions of a transaction complete successfully or none do.
C - Consistency: A transaction moves data from one consistent state to another.
I - Isolation: Transactions execute independently and separately.
D - Durability: Once a transaction completes, its effects persist, even if there is a system failure.

4. Schedule: The order in which transactions are executed in the system is called a schedule. Schedules can be serial or concurrent. Serial schedules execute one transaction at a time. Concurrent schedules execute transactions in an interleaved fashion.

5. Conflicts and Recoverability: Conflicts occur when two transactions access the same data and at least one of them modifies it. A conflict can cause one transaction to overwrite the other's changes, leading to incorrect results or data corruption. A schedule is recoverable if it can be undone in the reverse order in the event of a system failure. Not all schedules are recoverable.

6. Serializability: A schedule is serializable if its end result is equivalent to some serial schedule. Serializability is the key correctness criterion for transaction processing. Not all serializable schedules are conflict serializable or view serializable. Conflict and view serializability are stronger and more restrictive correctness criteria.