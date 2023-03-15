### Multiple Granularity for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows the multi-granularity compatibility function, which defines the compatibility of different lock modes on different levels of the hierarchy .
- The lock modes are: shared (S), exclusive (X), intention shared (IS), intention exclusive (IX), and shared with intention exclusive (SIX). The compatibility function is shown in the table below .

|     | S  | X  | IS | IX | SIX |
|-----|----|----|----|----|-----|
| S   | Y  | N  | Y  | N  | N   |
| X   | N  | N  | N  | N  | N   |
| IS  | Y  | N  | Y  | Y  | Y   |
| IX  | N  | N  | Y  | Y  | N   |
| SIX | N  | N  | Y  | N  | N   |

- The rules for multiple granularity locking protocol are:
  - Lock the root of the tree first, any mode.
  - Node Q can be locked by Ti in S or IS only if parent(Q) locked by Ti in IX or IS.
  - Node Q can be locked by Ti in X, SIX, IX only if parent(Q) locked by Ti in IX, SIX.
  - Ti is two-phase.
  - Ti can unlock node Q only if none of Q’s descendants are locked by Ti.
- An example of multiple granularity locking protocol is shown in the figure below. The hierarchy consists of four levels of nodes: database (D), file (F), page (P), and record (R). The transactions T1 and T2 lock and unlock different nodes according to the rules and the compatibility function.

![Multiple granularity locking example](https://media.geeksforgeeks.org/wp-content/uploads/20200220141401/Multiple-Granularity-Locking-in-DBMS.png)