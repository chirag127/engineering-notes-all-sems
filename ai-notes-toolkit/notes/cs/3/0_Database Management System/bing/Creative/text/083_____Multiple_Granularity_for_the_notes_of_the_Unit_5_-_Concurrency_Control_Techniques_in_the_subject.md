### Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- Multiple granularity locking protocol increases concurrency and decreases overhead especially when there is a combination of short transactions with a few accesses and transactions that last for a long time accessing a large number of objects such as audit transactions that access every item in the database.
- Multiple granularity locking protocol follows a multi-granularity compatibility function that defines the compatibility of different lock modes on different levels of granularity .
- Multiple granularity locking protocol also follows a set of rules to ensure serializability and avoid deadlock:
  - Lock the root of the tree first, any mode
  - Node Q can be locked by T iin S or IS only if parent(Q) locked by T iin IX or IS
  - Node Q can be locked by T iin X, SIX, IX only if parent(Q) locked by T iin IX, SIX
  - T iis two-phase
  - T ican unlock node Q only if none of Q’s descendants are locked by T i
- Multiple granularity locking protocol can be represented graphically as a tree, where each node represents a data item of a certain granularity and each edge represents the nesting relationship between data items. For example, consider the following tree, which consists of four levels of nodes:

```
          Database
            /  \
           /    \
          /      \
         /        \
        /          \
       /            \
      /              \
     /                \
    /                  \
   /                    \
  /                      \
 /                        \
A                          B
/ \                        / \
/   \                      /   \
/     \                    /     \
/       \                  /       \
/         \                /         \
/           \              /           \
/             \            /             \
/               \          /               \
/                 \        /                 \
/                   \      /                   \
/                     \    /                     \
A1                      A2 B1                      B2
/ \                    / \ / \                    / \
/   \                  /   /   \                  /   \
/     \                /   /     \                /     \
/       \              /   /       \              /       \
/         \            /   /         \            /         \
/           \          /   /           \          /           \
/             \        /   /             \        /             \
/               \      /   /               \      /               \
/                 \    /   /                 \    /                 \
/                   \  /   /                   \  /                   \
/                     \/   /                     \/                     \
A11                      A12 B11                      B12 B21                      B22
```