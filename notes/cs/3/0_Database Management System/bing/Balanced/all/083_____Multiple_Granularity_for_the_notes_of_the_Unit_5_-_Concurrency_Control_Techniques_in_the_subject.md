# Multiple Granularity

- Multiple granularity is a database locking technique that allows various data items of different sizes and set locks on them and also defines the hierarchy of data granularity where small granularities are nested within the larger granularity.
- Multiple granularity breaks the database into a number of blocks that can be locked to increase the concurrency and decrease the lock overhead. It also makes it easy to decide which segment or part of data to lock or which one to unlock .
- There are three types of lock granularity:
  - Fine granularity: It locks the smallest data items such as records or fields. It provides high concurrency but also high locking overhead.
  - Coarse granularity: It locks the largest data items such as files or tables. It provides low concurrency but also low locking overhead.
  - Medium granularity: It locks the intermediate data items such as pages or blocks. It provides a balance between concurrency and locking overhead.
- Multiple granularity locking protocol uses a tree structure to represent the hierarchy of data granularities and the compatibility matrix to determine the lock modes that can be applied on each node .
- The tree structure consists of four levels of nodes:
  - Database (D): The root node that represents the entire database.
  - File (F): The child nodes of D that represent the files in the database.
  - Page (P): The child nodes of F that represent the pages in the files.
  - Record (R): The child nodes of P that represent the records in the pages.
- The compatibility matrix defines six lock modes that can be applied on each node :
  - Shared (S): Allows read access to the node and its descendants.
  - Exclusive (X): Allows read and write access to the node and its descendants.
  - Intention Shared (IS): Indicates the intention to lock some of the descendants of the node in S mode.
  - Intention Exclusive (IX): Indicates the intention to lock some of the descendants of the node in X mode.
  - Shared and Intention Exclusive (SIX): Allows read access to the node and indicates the intention to lock some of the descendants of the node in X mode.
  - No lock (NL): No access to the node or its descendants.
- The compatibility function determines whether a transaction can lock a node in a given mode based on the existing locks on the node by other transactions. The function is shown in the table below:

|       | NL | IS | IX | S  | SIX | X  |
| ----- | -- | -- | -- | -- | --- | -- |
| NL    | Y  | Y  | Y  | Y  | Y   | Y  |
| IS    | Y  | Y  | Y  | Y  | Y   | N  |
| IX    | Y  | Y  | Y  | N  | N   | N  |
| S     | Y  | Y  | N  | Y  | N   | N  |
| SIX   | Y  | Y  | N  | N  | N   | N  |
| X     | Y  | N  | N  | N  | N   | N  |

- Y means compatible and N means incompatible.
- Multiple granularity locking protocol follows these rules:
  - Lock the root node of the tree first, in any mode.
  - Node Q can be locked by transaction T in S or IS mode only if the parent of Q is locked by T in IX or IS mode.
  - Node Q can be locked by transaction T in X, SIX, or IX mode only if the parent of Q is locked by T in IX or SIX mode.
  - Transaction T is two-phase, meaning it acquires all the locks before releasing any lock.
  - Transaction T can unlock node Q only if none of Q's descendants are locked by T.