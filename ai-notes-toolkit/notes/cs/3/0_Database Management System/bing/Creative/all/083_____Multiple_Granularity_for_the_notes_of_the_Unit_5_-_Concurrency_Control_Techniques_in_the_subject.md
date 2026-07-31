# Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock.
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity means hierarchically breaking up the database into blocks that can be locked and can be tracked needs what needs to lock and in what fashion. Such a hierarchy can be represented graphically as a tree.
- For example, consider the following tree, which consists of four levels of nodes:

![tree](https://media.geeksforgeeks.org/wp-content/uploads/20200519151803/Multiple-Granularity-Locking-in-DBMS-1.png)

- The root node represents the entire database, the second level nodes represent the files, the third level nodes represent the pages, and the fourth level nodes represent the records.
- There are three types of lock granularity: record level, page level, and file level.
- Record level locking is the finest granularity, where each record can be locked individually. This allows the highest degree of concurrency, but also the highest lock overhead and the highest risk of deadlock.
- Page level locking is the intermediate granularity, where each page (a collection of records) can be locked. This reduces the lock overhead and the risk of deadlock, but also reduces the concurrency.
- File level locking is the coarsest granularity, where each file (a collection of pages) can be locked. This minimizes the lock overhead and the risk of deadlock, but also minimizes the concurrency.
- To implement multiple granularity locking, a compatibility matrix is used to determine which locks are compatible with each other at different levels of the hierarchy.
- The compatibility matrix is as follows:

![matrix](https://media.geeksforgeeks.org/wp-content/uploads/20200519151803/Multiple-Granularity-Locking-in-DBMS-2.png)

- The lock modes are: shared (S), exclusive (X), intention shared (IS), intention exclusive (IX), and shared with intention exclusive (SIX).
- A shared lock (S) allows a transaction to read a data item, but not to write or modify it. A shared lock is compatible with another shared lock, but not with an exclusive lock.
- An exclusive lock (X) allows a transaction to read and write a data item, but not to share it with any other transaction. An exclusive lock is not compatible with any other lock.
- An intention shared lock (IS) indicates that a transaction intends to acquire a shared lock on some data item in the lower level of the hierarchy. An intention shared lock is compatible with another intention shared lock, a shared lock, or a shared with intention exclusive lock, but not with an exclusive lock or an intention exclusive lock.
- An intention exclusive lock (IX) indicates that a transaction intends to acquire an exclusive lock on some data item in the lower level of the hierarchy. An intention exclusive lock is compatible with another intention shared lock or an intention exclusive lock, but not with a shared lock, an exclusive lock, or a shared with intention exclusive lock.
- A shared with intention exclusive lock (SIX) indicates that a transaction has a shared lock on a data item and intends to acquire an exclusive lock on some data item in the lower level of the hierarchy. A shared with intention exclusive lock is compatible with another intention shared lock or a shared lock, but not with an exclusive lock, an intention exclusive lock, or a shared with intention exclusive lock.
- To ensure correctness and consistency, the multiple granularity locking protocol follows these rules:
  - Follow the multi-granularity compatibility function as shown in the matrix.
  - Lock the root of the tree first, in any mode.
  - Node Q can be locked by transaction T in S or IS mode only if the parent of Q is locked by T in IX or IS mode.
  - Node Q can be locked by transaction T in X, SIX