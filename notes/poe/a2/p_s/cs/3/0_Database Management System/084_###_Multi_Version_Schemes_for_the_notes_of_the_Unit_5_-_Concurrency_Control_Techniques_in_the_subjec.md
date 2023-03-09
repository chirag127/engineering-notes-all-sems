 Here is the content in markdown format for the topic -

### Multi Version Schemes

Multi version schemes are concurrency control techniques that allow multiple transactions to access and modify the database simultaneously by maintaining multiple versions of data items. The key idea is to allow transactions to read data based on its committed state at the start of the transaction while allowing concurrently executing transactions to modify their own private versions of data. This avoids read-write conflicts since readers always access committed data and writers access private versions. The different versions are eventually reconciled when transactions commit.

There are two common multi version schemes -

1. Timestamp ordering - Each data item has a timestamp that indicates the transaction that last modified it. Transactions are ordered based on their timestamps - a read operation can only see data modified by transactions that committed before it started and a write operation conflicts with other writes that have larger timestamps. This ensures serializability. The overhead is maintaining and updating timestamps with each data access.

2. Snapshot isolation - Each transaction reads data based on a snapshot of the database at a point in time. This avoids the overhead of maintaining and updating timestamps but can lead to an anomaly called "snapshot isolation anomaly" where a transaction reads data that is subsequently modified by another transaction and rolled back leading to an inconsistent read. Additional logic is required to detect and resolve such anomalies.

Advantages -
- Avoid read-write conflicts and allow high concurrency.
- Simplicity of not dealing with intricate locking mechanisms.

Disadvantages -
- Extra space and time overhead for maintaining multiple versions.
- Complexity of reconciling different versions when transactions commit.
- Handling of anomalies in snapshot isolation.

Applications -
- Databases that require very high concurrency.
- When conflicts are difficult to deal with using other techniques.
- Optimistic concurrency control.

Hope this helps! Let me know if you would like me to explain or add anything further.