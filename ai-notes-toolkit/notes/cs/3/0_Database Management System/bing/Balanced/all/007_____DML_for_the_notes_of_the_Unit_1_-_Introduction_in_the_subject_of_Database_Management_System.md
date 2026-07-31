# DML

DML stands for Data Manipulation Language. It is a subset of SQL statements that are used to manipulate data in a database. DML includes the following operations:

- **INSERT**: This operation is used to insert new data into a table or view.
- **SELECT**: This operation is used to retrieve data from one or more tables or views.
- **UPDATE**: This operation is used to modify existing data in a table or view.
- **DELETE**: This operation is used to remove existing data from a table or view.

DML statements can be executed directly by the user or by a program that interacts with the database. DML statements can also be triggered by certain events that affect the data, such as insertions, updates, or deletions. These events can be handled by special stored procedures called DML triggers.

DML is mainly concerned with the performance and efficiency of the database, as well as the consistency and integrity of the data. DML utilizes the append-only nature of the Hadoop Distributed File System (HDFS) storage, which means that data can only be added to the end of a file, not modified or deleted.

Some of the characteristics of DML are:

- It is a declarative language, which means that the user specifies what data to manipulate, not how to manipulate it.
- It is a set-oriented language, which means that it operates on sets of data, not individual records.
- It supports various data types, such as numeric, string, date, time, etc.
- It supports various operators, such as arithmetic, logical, comparison, etc.
- It supports various functions, such as aggregate, scalar, window, etc.
- It supports various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, etc.
- It supports various joins, such as inner, outer, cross, etc.
- It supports various subqueries, such as correlated, uncorrelated, etc.
- It supports various expressions, such as case, coalesce, nullif, etc.