 Here is the content in markdown format for the topic ## Transaction Control Language(TCL) statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab:

## Transaction Control Language(TCL) statements

- TCL statements are used to manage transactions in a database.
- The main TCL statements are:

1. COMMIT - Finalizes a transaction and makes all changes permanent.
- It releases all locks and resources held by the transaction.
- Used when the transaction is complete and all changes are to be saved.

2. ROLLBACK - Undoes all changes made by the current transaction.
- It releases all locks and resources held by the transaction.
- Used when the transaction is to be aborted and all changes are to be discarded.

3. SAVEPOINT - Sets a savepoint within a transaction.
- It identifies a point in a transaction to which you can later roll back.
- Allows rolling back part of a transaction.

Advantages of TCL:
- Ensures atomicity, consistency, isolation and durability (ACID) properties.
- Allow recovery from failures and undoing unwanted changes.
- Increase concurrency by releasing locks early.

Disadvantages of TCL:
- Additional overheads of resource management and logging.
- May reduce concurrency in case of long transactions due to locks being held for long.

Examples of TCL statements in SQL:
COMMIT;
ROLLBACK;
SAVEPOINT sp_name;
ROLLBACK TO SAVEPOINT sp_name;

Applications of TCL:
- Used in e-commerce and financial applications to maintain integrity.
- Used when distributed transactions are involved to manage failures.
- Used for long queries to save intermediate results in savepoints.

Markdown tables, codes and diagrams can be included if required to enhance the explanations. The content can be expanded with more details and points as needed.