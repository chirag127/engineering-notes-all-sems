### Case Study of Oracle for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

- Oracle is a relational database management system that supports concurrent access of data by multiple users and transactions.
- Oracle uses a multiversion concurrency control (MVCC) model to provide read consistency and avoid locking conflicts.
- Oracle also uses various types of locks to ensure data integrity and consistency among transactions.
- Oracle supports different isolation levels to control the degree of concurrency and consistency for transactions.

#### Multiversion Concurrency Control

- Oracle automatically provides read consistency to a query so that all the data that the query sees comes from a single point in time (statement-level read consistency)   .
- Oracle can also provide read consistency to all of the queries in a transaction (transaction-level read consistency)  .
- Oracle achieves read consistency by using undo segments, which store the old versions of the data before they are modified by transactions  .
- Oracle assigns each transaction a system change number (SCN), which is a logical timestamp that indicates the commit order of transactions  .
- Oracle uses the SCN to determine which version of the data to show to a query, based on the query's start time or the transaction's start time  .
- Oracle's MVCC model allows queries to read data without locking or blocking other transactions, and also allows transactions to modify data without overwriting other transactions' changes   .

#### Locking Mechanisms

- Oracle maintains data integrity and consistency among transactions by using various types of locks, such as data locks, dictionary locks, and internal locks .
- Data locks are used to protect data from concurrent modification by different transactions. Data locks can be exclusive or shared, depending on the type of operation performed on the data .
- Dictionary locks are used to protect the data dictionary, which stores the metadata of the database objects, such as tables, indexes, and views. Dictionary locks can be exclusive or shared, depending on the type of operation performed on the data dictionary .
- Internal locks are used to protect the internal structures of the database, such as control files, redo log files, and data files. Internal locks are managed automatically by Oracle and are not visible to users .
- Locking occurs automatically and requires no user action. Oracle uses a lock manager to coordinate the acquisition and release of locks among transactions .

#### Isolation Levels

- Oracle supports different isolation levels to control the degree of concurrency and consistency for transactions. Isolation levels determine how transactions see the changes made by other transactions  .
- Oracle supports four isolation levels: read committed, serializable, read only, and snapshot  .
- Read committed is the default isolation level in Oracle. It ensures that transactions see only the changes that have been committed by other transactions at the time of the query  .
- Serializable is the highest isolation level in Oracle. It ensures that transactions see a consistent snapshot of the database as of the start of the transaction, and also prevents any concurrent transactions from modifying the data that the transaction has read or modified  .
- Read only is similar to serializable, except that it does not allow the transaction to modify any data. It ensures that transactions see a consistent snapshot of the database as of the start of the transaction  .
- Snapshot is a user-defined isolation level that allows transactions to see a consistent snapshot of the database as of a specified SCN or time. It is useful for applications that need to perform historical analysis or reporting on the database  .

#### References

: Data Concurrency and Consistency - Oracle
: Data Concurrency - Oracle
: Concurrency (Multi-User access) and Locking - Oracle - SS64.com
: Data Concurrency and Consistency - Oracle Help Center
: Locking and Concurrency Control - Oracle Help Center