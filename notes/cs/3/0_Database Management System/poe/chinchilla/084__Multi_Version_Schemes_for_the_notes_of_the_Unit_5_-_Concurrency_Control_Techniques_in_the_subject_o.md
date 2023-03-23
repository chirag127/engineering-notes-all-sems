### Multi Version Schemes for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

Multi Version Schemes are used in Database Management Systems to allow for concurrency control of data access. In these schemes, multiple versions of a data item can exist simultaneously, with each version representing a different state of the data item at a particular point in time. Here are some important points to understand about Multi Version Schemes:

1. **Versions of Data Items:** In Multi Version Schemes, each data item is associated with multiple versions. Each version represents a different state of the data item at a particular point in time. Thus, an operation that modifies a data item creates a new version of the item, rather than modifying the existing version.

2. **Read Operations:** In Multi Version Schemes, read operations can access any version of a data item. The version that is accessed depends on the transaction's read timestamp, which determines the point in time at which the transaction started.

3. **Write Operations:** Write operations in Multi Version Schemes can create a new version of a data item, but only if the transaction's write timestamp is greater than the timestamps of all existing versions of the item. This ensures that the new version is the most recent version of the item.

4. **Garbage Collection:** In Multi Version Schemes, it is important to periodically remove old versions of data items. This is done through a process called garbage collection. Garbage collection removes versions of data items that are no longer needed for any active transaction.

5. **Snapshot Isolation:** Snapshot isolation is a type of Multi Version Scheme that provides repeatable reads and allows for high concurrency. In snapshot isolation, each transaction operates on a snapshot of the database as it existed at the beginning of the transaction. This ensures that the transaction sees a consistent view of the database, even if other transactions modify the same data.

6. **Serializable Snapshot Isolation:** Serializable snapshot isolation is a stricter form of snapshot isolation that ensures serializability of transactions. This is achieved by ensuring that transactions are ordered based on their read and write dependencies. Serializable snapshot isolation is the most strict form of Multi Version Scheme, but it can lead to lower concurrency and higher overhead.

In conclusion, Multi Version Schemes are an important technique for achieving concurrency control in Database Management Systems. By allowing multiple versions of data items to exist simultaneously, Multi Version Schemes enable transactions to access consistent views of the database while minimizing conflicts and ensuring high concurrency.