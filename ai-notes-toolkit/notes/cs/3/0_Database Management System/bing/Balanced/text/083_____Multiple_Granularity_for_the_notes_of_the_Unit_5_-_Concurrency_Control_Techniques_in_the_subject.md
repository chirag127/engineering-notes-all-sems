### Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows a tree structure to represent the hierarchy of data items. The root node represents the entire database, and the leaf nodes represent the smallest data items. The intermediate nodes represent the data items of different sizes.
- Multiple granularity locking protocol follows some rules to ensure serializability and avoid deadlock:
  - Follow multi-granularity compatibility function
  - Lock root of tree first, any mode
  - Node Q can be locked by Ti in S or IS only if parent(Q) locked by Ti in IX or IS
  - Node Q can be locked by Ti in X, SIX, IX only if parent(Q) locked by Ti in IX, SIX
  - Ti is two-phase
  - Ti can unlock node Q only if none of Q’s descendants are locked by Ti
- Multiple granularity locking protocol uses the following lock modes:
  - S (Shared): Allows read access to the data item
  - X (Exclusive): Allows read and write access to the data item
  - IS (Intention Shared): Indicates the intention to lock some descendant node in S mode
  - IX (Intention Exclusive): Indicates the intention to lock some descendant node in X mode
  - SIX (Shared Intention Exclusive): Indicates the intention to lock some descendant node in X mode and also allows read access to the current node