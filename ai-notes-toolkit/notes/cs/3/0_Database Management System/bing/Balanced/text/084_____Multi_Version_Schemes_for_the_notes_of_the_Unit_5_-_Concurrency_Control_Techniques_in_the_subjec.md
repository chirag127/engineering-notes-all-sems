### Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that allow multiple versions of data items to coexist in the database.
- The main idea is to grant an appropriate version of a data item to each read request, while write requests operate on a copy of the data item, not the original one.
- This way, read requests do not have to wait for write requests to finish, and write requests do not have to lock the data item from other transactions.
- The benefits of multi version schemes are increased concurrency, reduced locking overhead, and improved performance.
- The challenges of multi version schemes are maintaining consistency, avoiding conflicts, and managing storage space for multiple versions.
- There are different types of multi version schemes, such as timestamp-based, validation-based, and snapshot-based, that use different criteria to determine which version of a data item to read or write.
- Timestamp-based schemes assign a unique timestamp to each transaction and each version of a data item, and use the timestamps to order the transactions and the versions.
- Validation-based schemes allow transactions to read and write any version of a data item, but validate the transactions at commit time to ensure serializability.
- Snapshot-based schemes create a snapshot of the database for each transaction, and allow transactions to read and write only the versions of the data items in their snapshot.