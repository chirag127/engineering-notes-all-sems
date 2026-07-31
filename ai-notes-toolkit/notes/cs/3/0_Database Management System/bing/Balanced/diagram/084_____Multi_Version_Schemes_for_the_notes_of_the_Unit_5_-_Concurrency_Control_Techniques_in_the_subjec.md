### Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that allow multiple versions of data objects to exist in the database at the same time.
- The main idea of multi version schemes is to grant an appropriate version of a data object to each read request, while write requests operate on a copy of the data object, not the original one.
- This way, read requests do not have to wait for write requests to finish, and write requests do not have to lock the data object for exclusive access.
- The benefits of multi version schemes are increased concurrency, reduced blocking, and improved performance.
- The challenges of multi version schemes are maintaining consistency, avoiding conflicts, and managing storage space.

#### How Multi Version Schemes Work

- While different database systems may implement multi version schemes in their own ways, the general steps are as follows:
  - Every data object has a version number that indicates its freshness and validity.
  - Concurrent read requests happen against the data object with the highest version number that is compatible with the transaction's isolation level.
  - Write requests operate on a copy of the data object, not the original one. The copy is assigned a new version number that is higher than the previous one.
  - Other users continue to read the older version of the data object while the copy is updated.
  - After the write request is successful, the version number is incremented and the copy becomes the new version of the data object.
  - Subsequent concurrent read requests use the updated version of the data object.
- An example of a multi version scheme is the timestamp ordering protocol, which assigns a timestamp to each transaction and uses it to determine the order of execution and the version of the data object to access.