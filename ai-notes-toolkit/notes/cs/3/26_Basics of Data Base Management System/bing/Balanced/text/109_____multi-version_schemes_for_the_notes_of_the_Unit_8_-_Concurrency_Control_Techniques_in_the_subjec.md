### Multi-version schemes for concurrency control

- Multi-version schemes are a type of concurrency control method that allow concurrent access to the database without locking the data.
- Multi-version schemes maintain different versions of data items, each with a version number and a timestamp.
- Each transaction reads the most recent version of a data item that is compatible with its timestamp, and writes a new version of a data item with an incremented version number and its own timestamp.
- Multi-version schemes avoid the problems of locking, such as deadlocks, starvation, and blocking, and improve the performance of database applications in a multiuser environment.
- Multi-version schemes can be classified into two types: optimistic and pessimistic.
- Optimistic multi-version schemes assume that conflicts are rare and allow transactions to execute without checking for concurrency violations until they commit. At commit time, transactions are validated against the versions of data items they have read and written, and are aborted if they violate the serializability property.
- Pessimistic multi-version schemes assume that conflicts are frequent and check for concurrency violations before transactions execute any operation. Transactions are aborted if they try to read or write a data item that has been modified by another transaction with a higher priority or a later timestamp.
- Examples of multi-version schemes are multiversion two-phase locking (MV2PL), multiversion timestamp ordering (MVTO), and snapshot isolation (SI).