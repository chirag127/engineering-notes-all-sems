# Multiple Granularity for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- There are three types of lock granularity:
  - Fine granularity: It locks the smallest data items, such as records or fields. It has high concurrency but also high locking overhead and high probability of deadlock.
  - Coarse granularity: It locks the largest data items, such as files or tables. It has low concurrency but also low locking overhead and low probability of deadlock.
  - Medium granularity: It locks the intermediate data items, such as pages or blocks. It has moderate concurrency and moderate locking overhead and deadlock probability.
- Multiple granularity locking protocol is a set of rules that governs how transactions can acquire and release locks on different levels of data granularity . It uses a compatibility matrix to determine which lock modes are compatible with each other. The lock modes are :
  - Shared (S): It allows a transaction to read a data item.
  - Exclusive (X): It allows a transaction to read and write a data item.
  - Intention Shared (IS): It indicates that a transaction intends to lock some of the lower level data items in shared mode.
  - Intention Exclusive (IX): It indicates that a transaction intends to lock some of the lower level data items in exclusive mode.
  - Shared and Intention Exclusive (SIX): It indicates that a transaction intends to lock some of the lower level data items in exclusive mode and also locks the current data item in shared mode.
- The compatibility matrix is as follows :

|     | S | X | IS | IX | SIX |
|-----|---|---|----|----|-----|
| S   | Y | N | Y  | N  | N   |
| X   | N | N | N  | N  | N   |
| IS  | Y | N | Y  | Y  | N   |
| IX  | N | N | Y  | Y  | N   |
| SIX | N | N | N  | N  | N   |

- Y means compatible and N means incompatible.
- Multiple granularity locking protocol follows these rules :
  - Follow the compatibility matrix for locking data items.
  - Lock the root of the tree first, in any mode.
  - Node Q can be locked by transaction T in S or IS mode only if the parent of Q is locked by T in IX or IS mode.
  - Node Q can be locked by transaction T in X, SIX, or IX mode only if the parent of Q is locked by T in IX or SIX mode.
  - Transaction T is two-phase, meaning it acquires all the locks before releasing any lock.
  - Transaction T can unlock node Q only if none of Q's descendants are locked by T.
- An example of multiple granularity locking protocol is shown below:

![A tree representing the hierarchy of data granularity, with four levels of nodes: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P. A is the root node, B and C are its children, D, E, F, G are the children of B, and H, I, J, K, L, M, N, O, P are the children of C. The nodes represent different data items, such as files, pages, records, or fields.](https://media.geeksforgeeks.org/wp-content/uploads/20200121125318/Multiple-Granularity-Locking-in-DBMS-1.png)

- Suppose there are two transactions, T1 and T2, that want to access some of the data items in the tree. The sequence of locking and unlocking operations is as follows:

| Transaction | Operation | Lock Mode | Node |
|-------------|-----------|-----------|------|
| T1          | Lock      | IS        | A    |
|