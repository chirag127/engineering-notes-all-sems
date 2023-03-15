### Multi Version Schemes

Multi Version Schemes are a type of concurrency control technique used in Database Management Systems. These schemes allow multiple versions of data items to coexist in the database, providing increased concurrency and isolation between transactions.

Some key points to note about Multi Version Schemes are:

1. Each transaction operates on its own snapshot of the database, which is created at the start of the transaction.
2. Transactions can read data items from their snapshot without acquiring locks, which reduces contention and increases concurrency.
3. When a transaction wants to write to a data item, it creates a new version of the item and writes to that version. This new version is only visible to the transaction that created it and any transactions that start after it.
4. When a transaction commits, its changes are made permanent and become visible to other transactions.
5. Multi Version Schemes use a mechanism such as timestamps or version numbers to determine which version of a data item a transaction should read or write to.
6. These schemes can provide high levels of isolation between transactions, including serializability, snapshot isolation, and repeatable read.

Multi Version Schemes can be an effective way to increase concurrency and isolation in a Database Management System, but they do require additional storage space to maintain multiple versions of data items. It is important to carefully consider the trade-offs when deciding whether to use a Multi Version Scheme in a particular system.