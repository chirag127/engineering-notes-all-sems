### Multi-version schemes for concurrency control

- Multi-version schemes are a type of concurrency control method that allow concurrent access to the database without locking the data.
- Multi-version schemes maintain different versions of data items, each with a version number and a timestamp.
- Each transaction reads the most recent version of a data item that is compatible with its timestamp, and writes a new version of a data item with an incremented version number and its own timestamp.
- Multi-version schemes avoid the problems of locking, such as deadlocks, starvation, and blocking, and improve the performance of database applications in a multiuser environment.
- Multi-version schemes can be classified into two types: optimistic and pessimistic.
- Optimistic multi-version schemes assume that conflicts are rare and allow transactions to execute without checking for conflicts until they commit. If a conflict is detected at commit time, the transaction is aborted and restarted.
- Pessimistic multi-version schemes check for conflicts before each read or write operation and abort the transaction if a conflict is detected. This ensures that only serializable schedules are allowed.
- An example of an optimistic multi-version scheme is the multiversion timestamp ordering (MVTO) protocol, which assigns a read timestamp and a write timestamp to each transaction and uses them to order the versions of data items.
- An example of a pessimistic multi-version scheme is the multiversion two-phase locking (MV2PL) protocol, which uses locks to control the access to the versions of data items and ensures that each transaction reads and writes the correct version.