# Case Study of Oracle for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

- Oracle is a popular relational database management system that supports concurrent access of data by multiple users and transactions.
- Oracle uses a multiversion concurrency control (MVCC) technique to provide read consistency and isolation levels for queries and transactions.
- Oracle also uses various types of locks to ensure data integrity and prevent conflicts among concurrent updates of the same data.

## Multiversion Concurrency Control

- MVCC is a technique that allows each user to see a consistent snapshot of the database as of a single point in time, regardless of the changes made by other users.
- MVCC avoids locking read operations and reduces the need for locking write operations, thus improving performance and concurrency.
- Oracle implements MVCC by using undo segments, which store the old versions of the data before they are modified by transactions.
- Oracle assigns each transaction a unique system change number (SCN), which is a logical timestamp that indicates the start time of the transaction.
- Oracle also assigns each data block a SCN, which indicates the last time the block was modified.
- When a query is executed, Oracle determines the SCN of the query, which is the highest SCN among all the transactions that have committed at the time the query started.
- Oracle then reads the data blocks that have a SCN less than or equal to the query SCN, and applies the undo information if necessary to reconstruct the consistent snapshot of the data as of the query SCN.
- This ensures that the query sees a consistent view of the data, regardless of the changes made by other transactions after the query started.
- Oracle provides two levels of read consistency: statement-level and transaction-level.
- Statement-level read consistency means that each SQL statement in a transaction sees a consistent snapshot of the data as of the time the statement started.
- Transaction-level read consistency means that all the SQL statements in a transaction see a consistent snapshot of the data as of the time the first statement in the transaction started.
- Oracle always enforces statement-level read consistency, and can optionally provide transaction-level read consistency by setting the isolation level to SERIALIZABLE.

## Locking Mechanisms

- Locking is a technique that prevents concurrent transactions from accessing or modifying the same data in a conflicting way.
- Locking ensures data integrity and consistency, and prevents phenomena such as lost updates, dirty reads, non-repeatable reads, and phantom reads.
- Oracle uses two types of locks: data locks and dictionary locks.
- Data locks are used to protect the data in the database from concurrent modifications. Data locks can be either exclusive or shared.
- Exclusive locks are acquired by transactions that modify data, such as INSERT, UPDATE, or DELETE statements. Exclusive locks prevent other transactions from modifying or locking the same data until the lock is released.
- Shared locks are acquired by transactions that query data, such as SELECT statements. Shared locks allow other transactions to query or lock the same data in shared mode, but prevent them from modifying or locking the data in exclusive mode until the lock is released.
- Oracle automatically acquires and releases data locks as needed, and does not require explicit locking commands from the user.
- Dictionary locks are used to protect the data dictionary, which stores the metadata of the database, such as the definitions of tables, indexes, views, etc. Dictionary locks can be either exclusive or shared.
- Exclusive locks are acquired by transactions that modify the data dictionary, such as CREATE, ALTER, or DROP statements. Exclusive locks prevent other transactions from accessing or modifying the same data dictionary object until the lock is released.
- Shared locks are acquired by transactions that access the data dictionary, such as queries that use the data dictionary views. Shared locks allow other transactions to access the same data dictionary object in shared mode, but prevent them from modifying or locking the object in exclusive mode until the lock is released.
- Oracle automatically acquires and releases dictionary locks as needed, and does not require explicit locking commands from the user.

## Isolation Levels

- Isolation level is a property that determines the degree of isolation or concurrency among transactions.
- Isolation level affects the visibility of the changes made by other transactions, and the possibility of encountering concurrency-related phenomena, such as dirty reads, non-repeatable reads, and phantom reads.
- Oracle supports four isolation levels: READ COMMITTED, SERIALIZABLE, READ ONLY, and READ WRITE.
- READ COMMITTED is the default isolation level in Oracle. It means that each query in a transaction sees the data that was committed before the query started. It prevents dirty reads, but allows non-repeatable reads and phantom reads.
- SERIALIZABLE means that