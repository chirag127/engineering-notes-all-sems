### Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock.
- There are three types of lock granularity:
  - Tuple level locking: Locking a single tuple or record in a table.
  - Page level locking: Locking a page or block of tuples in a table.
  - Table level locking: Locking the entire table or relation.
- Multiple granularity locking protocol uses a tree structure to represent the hierarchy of data items and their locks. The root of the tree is the entire database, and the leaves are the smallest data items (such as tuples or attributes).
- The protocol uses six types of locks:
  - Shared (S): Allows read access to a data item.
  - Exclusive (X): Allows read and write access to a data item.
  - Intention Shared (IS): Indicates the intention to lock some descendant node in shared mode.
  - Intention Exclusive (IX): Indicates the intention to lock some descendant node in exclusive mode.
  - Shared and Intention Exclusive (SIX): Indicates the intention to lock some descendant node in exclusive mode and also allows read access to the current node.
  - Shared and Intention Shared (SIS): Indicates the intention to lock some descendant node in shared mode and also allows read access to the current node.
- The protocol follows the multi-granularity compatibility function, which defines the compatibility of different lock modes on the same or different nodes.
- The protocol also follows the multi-granularity 2PL rules, which are:
  1. Follow multi-granularity compatibility function.
  2. Lock root of tree first, any mode.
  3. Node Q can be locked by T<sub>i</sub> in S or IS only if parent(Q) locked by T<sub>i</sub> in IX or IS.
  4. Node Q can be locked by T<sub>i</sub> in X, SIX, IX only if parent(Q) locked by T<sub>i</sub> in IX, SIX.
  5. T<sub>i</sub> is two-phase.
  6. T<sub>i</sub> can unlock node Q only if none of Q’s descendants are locked by T<sub>i</sub>.
- An example of multiple granularity locking protocol is:

```
T1: lock-S(root), lock-S(A), lock-S(A1), read(A1), unlock(A1), unlock(A), unlock(root)
T2: lock-X(root), lock-X(B), lock-X(B1), write(B1), unlock(B1), unlock(B), unlock(root)
T3: lock-IS(root), lock-IS(A), lock-S(A2), read(A2), unlock(A2), unlock(A), unlock(root)
```

- The tree structure for the above example is:

```
          root
         /    \
        A      B
       / \    / \
      A1 A2  B1 B2
```