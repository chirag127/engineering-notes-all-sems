### Multi Version Schemes

Multi-version concurrency control (MVCC) is a technique used in database management systems to provide concurrent access to the database and to detect conflicts between transactions. It is commonly used in database systems that support high levels of concurrency.

Here are some key points to remember about multi-version schemes:

1. MVCC allows multiple versions of a data item to exist at the same time.
2. Each version of a data item is associated with a timestamp, which indicates when the version was created.
3. Transactions read the version of the data item that was current at the time the transaction started.
4. When a transaction wants to modify a data item, it creates a new version of the data item with a new timestamp.
5. The old version of the data item is not deleted, but is kept for other transactions that may need to read it.
6. Conflicts between transactions are detected by comparing the timestamps of the versions of the data items they want to read or write.
7. MVCC provides a high level of concurrency, as transactions can read and write data items without locking them.
8. However, it can also lead to increased storage requirements, as multiple versions of data items need to be stored.
