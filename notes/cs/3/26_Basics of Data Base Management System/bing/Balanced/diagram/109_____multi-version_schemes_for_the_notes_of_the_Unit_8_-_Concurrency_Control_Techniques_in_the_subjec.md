### Multi-version Schemes of Concurrency Control

- Multi-version concurrency control (MVCC) is a technique that allows concurrent access to the database without locking the data.
- MVCC creates multiple versions of each data item and assigns them timestamps to indicate their validity .
- MVCC allows transactions to read the most recent committed version of a data item that is compatible with their timestamp, without blocking or waiting for other transactions .
- MVCC also allows transactions to write a new version of a data item, without overwriting the existing versions, and increment its version number .
- MVCC ensures serializability and consistency by validating the transactions at commit time, using their timestamps and version numbers .
- MVCC has several advantages, such as:
  - Reducing the locking overhead and improving the concurrency level .
  - Avoiding the phantom problem and the lost update problem .
  - Supporting snapshot isolation and repeatable read isolation levels .
  - Enhancing the performance and scalability of database systems .
- MVCC has some disadvantages, such as:
  - Increasing the storage space and the garbage collection cost for maintaining multiple versions .
  - Introducing the write skew problem and the read skew problem .
  - Requiring the timestamp synchronization and the version management mechanisms .
- MVCC is widely used by many database management systems, such as PostgreSQL, Oracle, MySQL, MongoDB, and CouchDB .