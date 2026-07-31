# Multi-Version Schemes

Multi-version schemes are a type of concurrency control technique used in database management systems. These schemes allow multiple versions of data to coexist, providing increased concurrency and isolation between transactions.

Here are some key points to remember about multi-version schemes:

1. Multi-version schemes maintain multiple versions of data items to increase concurrency and isolation between transactions.
2. Each version of a data item is associated with a timestamp, indicating the time at which the version was created.
3. Transactions read the version of a data item that was current at the time the transaction started.
4. When a transaction wants to write to a data item, it creates a new version of the data item with a timestamp equal to the transaction's start time.
5. Older versions of data items are eventually removed by a process called garbage collection.
