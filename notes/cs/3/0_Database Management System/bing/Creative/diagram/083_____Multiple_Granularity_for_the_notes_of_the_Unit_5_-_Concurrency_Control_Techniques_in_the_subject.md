### Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock.
- There are three types of lock granularity:
  - Tuple level locking: Locking a single tuple or record in a table.
  - Page level locking: Locking a page or block of tuples in a table.
  - Table level locking: Locking the entire table or relation.
- Multiple granularity locking protocol is a variant of two-phase locking protocol that uses a compatibility matrix to determine the lock modes that can coexist on the same data item.
- The lock modes are:
  - Shared (S): Allows read access to the data item.
  - Exclusive (X): Allows read and write access to the data item.
  - Intention Shared (IS): Indicates the intention to lock some of the lower level items in shared mode.
  - Intention Exclusive (IX): Indicates the intention to lock some of the lower level items in exclusive mode.
  - Shared and Intention Exclusive (SIX): Indicates the intention to lock some of the lower level items in exclusive mode and also allows read access to the current level item.
- The compatibility matrix is:

|     | S  | X  | IS | IX | SIX |
|-----|----|----|----|----|-----|
| S   | Y  | N  | Y  | N  | N   |
| X   | N  | N  | N  | N  | N   |
| IS  | Y  | N  | Y  | Y  | N   |
| IX  | N  | N  | Y  | Y  | N   |
| SIX | N  | N  | N  | N  | N   |

- Y means compatible and N means incompatible.
- Multiple granularity locking protocol follows these rules:
  - Follow multi-granularity compatibility function.
  - Lock root of tree first, any mode.
  - Node Q can be locked by T iin S or IS only if parent(Q) locked by T iin IX or IS.
  - Node Q can be locked by T iin X, SIX, IX only if parent(Q) locked by T iin IX, SIX.
  - T iis two-phase.
  - T ican unlock node Q only if none of Q’s descendants are locked by T i.
- An example of multiple granularity locking protocol is:

![Example of multiple granularity locking protocol](https://media.geeksforgeeks.org/wp-content/uploads/20200220190704/Untitled-Diagram-2020-02-20T190657.771.png)

- In this example, the database is divided into four levels: database, file, block and record. The transactions T1 and T2 lock and unlock the nodes according to the protocol rules. For instance, T1 locks the root node in IS mode, then locks file A in IX mode, then locks block A1 in IX mode, then locks record A11 in X mode, and so on. T2 locks the root node in IS mode, then locks file B in S mode, then locks block B2 in S mode, and so on. The locks are compatible according to the matrix. The transactions follow the two-phase locking protocol and release the locks in the reverse order of acquiring them.