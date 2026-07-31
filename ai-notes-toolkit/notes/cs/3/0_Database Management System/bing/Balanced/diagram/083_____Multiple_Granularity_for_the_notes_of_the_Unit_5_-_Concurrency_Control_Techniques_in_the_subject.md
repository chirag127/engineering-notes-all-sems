### Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock.
- There are three types of lock granularity:
  - Fine granularity: It locks the smallest data item such as a record or a field. It has high concurrency but also high locking overhead.
  - Coarse granularity: It locks the largest data item such as a file or a table. It has low concurrency but also low locking overhead.
  - Medium granularity: It locks the intermediate data item such as a page or a block. It has moderate concurrency and moderate locking overhead.
- Multiple granularity locking protocol is a set of rules that governs how transactions can acquire and release locks on different levels of data granularity.
- Multiple granularity locking protocol uses a compatibility matrix to determine which lock modes are compatible with each other. The lock modes are:
  - Shared (S): The transaction can read the data item but not modify it.
  - Exclusive (X): The transaction can read and modify the data item.
  - Intention Shared (IS): The transaction intends to lock some of the lower level data items in shared mode.
  - Intention Exclusive (IX): The transaction intends to lock some of the lower level data items in exclusive mode.
  - Shared and Intention Exclusive (SIX): The transaction intends to lock some of the lower level data items in exclusive mode and also locks the current data item in shared mode.
- The compatibility matrix is shown below:

|       | S   | X   | IS  | IX  | SIX |
| ----- | --- | --- | --- | --- | --- |
| S     | Yes | No  | Yes | No  | No  |
| X     | No  | No  | No  | No  | No  |
| IS    | Yes | No  | Yes | Yes | No  |
| IX    | No  | No  | Yes | Yes | No  |
| SIX   | No  | No  | No  | No  | No  |

- Multiple granularity locking protocol follows these rules:
  - Lock the root of the tree first, in any mode.
  - Node Q can be locked by Ti in S or IS only if parent(Q) is locked by Ti in IX or IS.
  - Node Q can be locked by Ti in X, SIX, IX only if parent(Q) is locked by Ti in IX or SIX.
  - Ti is two-phase, meaning it acquires all the locks before releasing any lock.
  - Ti can unlock node Q only if none of Q's descendants are locked by Ti.
- An example of multiple granularity locking protocol is shown below:

![Example of multiple granularity locking protocol](https://media.geeksforgeeks.org/wp-content/uploads/20200504161005/Multiple-Granularity-Locking-in-DBMS-1.png)

- In this example, the database is divided into four levels of granularity: database (D), file (F), block (B), and record (R). The transactions T1 and T2 follow the rules of multiple granularity locking protocol to lock and unlock different data items. The lock and unlock operations are shown in the table below:

| Time | T1              | T2              |
| ---- | --------------- | --------------- |
| t1   | lock-S(D)       |                 |
| t2   | lock-S(F1)      |                 |
| t3   | lock-S(B1)      |                 |
| t4   | lock-S(R1)      |                 |
| t5   | read(R1)        |                 |
| t6   | unlock(R1)      |                 |
| t7   | lock-S(R2)      |                 |
| t8   | read(R2)        |                 |
| t9   | unlock(R2)      |                 |
| t10  | unlock(B1)      |                 |
| t11  | lock-S(B2)      |                 |
| t12  | lock-S(R3)      |                 |
| t13  | read(R3)        |                 |
| t14