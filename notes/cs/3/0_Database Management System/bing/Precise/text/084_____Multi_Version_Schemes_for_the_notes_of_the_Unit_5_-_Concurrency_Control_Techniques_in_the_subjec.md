### Multi Version Schemes

Multi Version Schemes are a type of concurrency control technique used in Database Management Systems. These schemes allow multiple versions of the same data item to exist simultaneously, enabling transactions to access the version of the data that was current at the time the transaction started.

Some key points to note about Multi Version Schemes are:

1. Multi Version Schemes can improve the performance of a database system by reducing the number of conflicts between transactions.
2. These schemes can also improve the availability of data, as transactions can continue to access older versions of data even if the current version is locked by another transaction.
3. Multi Version Schemes can be implemented using various techniques, such as timestamp ordering or multi-version concurrency control (MVCC).
4. These schemes can be used in both centralized and distributed database systems.
5. Multi Version Schemes can add complexity to a database system, as the system must manage multiple versions of the same data item.

Overall, Multi Version Schemes are a powerful tool for managing concurrency in a database system, allowing transactions to access data in a consistent and efficient manner. However, the use of these schemes must be carefully considered, as they can add complexity to the system.