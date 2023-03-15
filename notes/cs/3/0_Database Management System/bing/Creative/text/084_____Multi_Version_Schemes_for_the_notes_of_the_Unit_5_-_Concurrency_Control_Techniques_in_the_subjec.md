### Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that allow multiple versions of data objects to exist in the database at the same time.
- The main idea of multi version schemes is to grant an appropriate version of a data object to each read request, while write requests operate on a copy of the data object, not the original one.
- This way, read requests do not have to wait for write requests to finish, and write requests do not have to lock the data objects they modify.
- The benefits of multi version schemes are increased concurrency, reduced locking overhead, and improved performance.
- The challenges of multi version schemes are maintaining consistency, avoiding conflicts, and managing storage space for multiple versions.

#### How Multi Version Schemes Work

- While different database management systems may implement multi version schemes in their own ways, a general algorithm for multi version schemes is as follows:

  1. Every data object has a version number that indicates its freshness and validity.
  2. When a transaction wants to read a data object, it is granted the version with the highest version number that is lower than or equal to the transaction's start time. This ensures that the transaction reads a consistent snapshot of the database.
  3. When a transaction wants to write a data object, it creates a copy of the data object with a new version number that is higher than the transaction's start time. The original data object is not modified.
  4. Other transactions can continue to read the older version of the data object while the copy is being updated.
  5. After the write operation is successful, the version number of the copy is incremented and the copy becomes the current version of the data object.
  6. Subsequent read requests use the updated version of the data object.

#### Example of Multi Version Schemes

- Suppose we have a data object X with a version number 1 and a value 10. We also have two transactions T1 and T2 that start at time 1 and 2 respectively. The following table shows the operations performed by the transactions and the versions of X they access.

| Transaction | Operation | Version of X | Value of X |
| ----------- | --------- | ------------ | ---------- |
| T1          | Read X    | 1            | 10         |
| T2          | Write X   | 2            | 20         |
| T1          | Write X   | 3            | 30         |
| T2          | Read X    | 2            | 20         |
| T1          | Commit    | 3            | 30         |
| T2          | Commit    | 2            | 20         |

- As we can see, T1 and T2 read and write different versions of X, and do not interfere with each other. T1 reads the initial version of X, while T2 reads the version created by its own write operation. T1 writes a new version of X, which becomes the current version after T1 commits. T2 writes another version of X, which is discarded after T2 commits, since it is older than the current version.