### Multiple Granularity for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows the multi-granularity compatibility function, which defines the compatibility of different lock modes on different levels of the hierarchy .
- The lock modes are: Shared (S), Exclusive (X), Intention Shared (IS), Intention Exclusive (IX), and Shared with Intention Exclusive (SIX) .
- The compatibility function is shown in the following table :

|     | S  | X  | IS | IX | SIX |
|-----|----|----|----|----|-----|
| S   | Y  | N  | Y  | N  | N   |
| X   | N  | N  | N  | N  | N   |
| IS  | Y  | N  | Y  | Y  | Y   |
| IX  | N  | N  | Y  | Y  | N   |
| SIX | N  | N  | Y  | N  | N   |

- The multi-granularity locking protocol follows these rules :
  - Lock the root of the tree first, in any mode.
  - Node Q can be locked by Ti in S or IS only if parent(Q) is locked by Ti in IX or IS.
  - Node Q can be locked by Ti in X, SIX, IX only if parent(Q) is locked by Ti in IX or SIX.
  - Ti is two-phase, meaning it acquires all the locks before releasing any lock.
  - Ti can unlock node Q only if none of Q's descendants are locked by Ti.
- An example of a multi-granularity locking hierarchy is shown in the following figure:

![Figure 1: An example of a multi-granularity locking hierarchy](https://media.geeksforgeeks.org/wp-content/uploads/20200226194704/Untitled-Diagram-2020-02-26T194602.993.png)

- In this figure, the database is divided into four levels: database (D), file (F), page (P), and record (R). Each level has a different granularity and can be locked by different transactions in different modes. For example, T1 has locked the entire database in IS mode, meaning it intends to read some of the files. T2 has locked file F1 in IX mode, meaning it intends to update some of the pages in F1. T3 has locked page P1 in S mode, meaning it wants to read P1. T4 has locked record R1 in X mode, meaning it wants to update R1. T5 has locked record R2 in S mode, meaning it wants to read R2. These locks are compatible according to the compatibility function and the protocol rules.