### Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- There are three types of lock granularity:
  - Fine-grained locking: Locking individual data items such as records or fields. This allows high concurrency but also high locking overhead and potential deadlock.
  - Coarse-grained locking: Locking large data items such as files or tables. This reduces locking overhead and deadlock possibility but also reduces concurrency and may cause unnecessary blocking.
  - Medium-grained locking: Locking intermediate data items such as pages or blocks. This is a compromise between fine-grained and coarse-grained locking that balances concurrency and overhead.
- Multiple granularity locking protocol is a set of rules that governs how transactions can acquire and release locks on different levels of data granularity . The protocol uses a compatibility matrix to determine which lock modes are compatible with each other. The lock modes are :
  - Shared (S): Allows reading but not writing the data item. Compatible with other S locks but not with X, SIX, or IX locks.
  - Exclusive (X): Allows reading and writing the data item. Not compatible with any other lock mode.
  - Intention Shared (IS): Indicates the intention to lock some descendant node in S mode. Compatible with other IS or IX locks but not with X or SIX locks.
  - Intention Exclusive (IX): Indicates the intention to lock some descendant node in X mode. Compatible with other IS or IX locks but not with S, X, or SIX locks.
  - Shared and Intention Exclusive (SIX): Indicates the intention to lock some descendant node in X mode and also lock the current node in S mode. Not compatible with any other lock mode except IS.
- The protocol also uses a tree structure to represent the hierarchy of data granularity, where the root node is the entire database and the leaf nodes are the individual data items . For example, consider the following tree, which consists of four levels of nodes:

```
    D
   / \
  F1  F2
 / \  / \
R1 R2 R3 R4
```

- The protocol follows these rules :
  - The root node (D) must be locked first, in any mode.
  - A node (Q) can be locked by a transaction (Ti) in S or IS mode only if the parent of Q is locked by Ti in IX or IS mode.
  - A node (Q) can be locked by a transaction (Ti) in X, SIX, or IX mode only if the parent of Q is locked by Ti in IX or SIX mode.
  - A transaction (Ti) must follow the two-phase locking protocol, that is, it cannot acquire any new locks after releasing any lock.
  - A transaction (Ti) can unlock a node (Q) only if none of Q's descendants are locked by Ti.
- The protocol ensures that if a transaction (Ti) locks a node (Q) in a certain mode, then no other transaction (Tj) can lock Q or any of its ancestors in a conflicting mode . This prevents the lost update, unrepeatable read, and phantom read problems. However, the protocol does not prevent deadlock, so a deadlock detection or prevention mechanism is still needed.