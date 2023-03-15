### Multiple Granularity for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows a tree structure to represent the hierarchy of data items, where each node corresponds to a data item and each edge corresponds to a containment relationship.
- Multiple granularity locking protocol uses six types of locks: shared (S), exclusive (X), intention shared (IS), intention exclusive (IX), shared intention exclusive (SIX), and no lock (NL).
- Multiple granularity locking protocol follows six rules to ensure serializability and avoid deadlock:
  1. Follow multi-granularity compatibility function, which defines which lock modes are compatible with each other at the same node.
  2. Lock the root of the tree first, in any mode.
  3. Node Q can be locked by transaction Ti in S or IS only if parent(Q) is locked by Ti in IX or IS.
  4. Node Q can be locked by transaction Ti in X, SIX, IX only if parent(Q) is locked by Ti in IX or SIX.
  5. Ti is two-phase, meaning it acquires all the locks before releasing any lock.
  6. Ti can unlock node Q only if none of Q's descendants are locked by Ti.