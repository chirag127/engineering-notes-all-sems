### Multiple Granularity for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows the following rules :
  - Follow multi-granularity compatibility function
  - Lock root of tree first, any mode
  - Node Q can be locked by T i in S or IS only if parent(Q) locked by T i in IX or IS
  - Node Q can be locked by T i in X, SIX, IX only if parent(Q) locked by T i in IX, SIX
  - T i is two-phase
  - T i can unlock node Q only if none of Q’s descendants are locked by T i
- Multiple granularity locking protocol uses the following types of locks :
  - Shared (S): Allows a transaction to read a data item
  - Exclusive (X): Allows a transaction to read and write a data item
  - Intention Shared (IS): Indicates that a transaction intends to lock some of the descendants of a node in shared mode
  - Intention Exclusive (IX): Indicates that a transaction intends to lock some of the descendants of a node in exclusive mode
  - Shared and Intention Exclusive (SIX): Indicates that a transaction intends to lock some of the descendants of a node in exclusive mode and also wants to read the node itself
- Multiple granularity locking protocol can be represented graphically as a tree, where each node corresponds to a data item or a set of data items, and the root node represents the entire database. For example, consider the following tree, which consists of four levels of nodes:

```
    A
   / \
  B   C
 / \ / \
D  E F  G
```

- In this tree, A represents the entire database, B and C represent two relations, D, E, F, and G represent four tuples, and the edges represent the parent-child relationship. A transaction can lock any node in the tree according to the rules and types of locks mentioned above. For example, a transaction T1 can lock node B in IX mode and node D in X mode, indicating that it intends to write tuple D in relation B. Another transaction T2 can lock node A in IS mode and node C in S mode, indicating that it intends to read relation C in the database. These locks are compatible and do not cause any conflict. However, if a transaction T3 tries to lock node A in X mode, it will conflict with both T1 and T2 and will have to wait until they release their locks.