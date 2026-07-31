### Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock.
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows a tree structure to represent the hierarchy of data items, where each node corresponds to a data item and each edge corresponds to a containment relationship.
- Multiple granularity locking protocol uses six types of locks: shared (S), exclusive (X), intention-shared (IS), intention-exclusive (IX), shared-intention-exclusive (SIX), and no lock (NL).
- Multiple granularity locking protocol follows six rules to ensure serializability and avoid deadlocks:
  - Follow multi-granularity compatibility function
  - Lock root of tree first, any mode
  - Node Q can be locked by T iin S or IS only if parent(Q) locked by T iin IX or IS
  - Node Q can be locked by T iin X, SIX, IX only if parent(Q) locked by T iin IX, SIX
  - T iis two-phase
  - T ican unlock node Q only if none of Q’s descendants are locked by T i