# Data Independence and Database Language and Interfaces

## Data Independence

- Data independence is a property of DBMS that allows the database schema to be changed at one level without affecting the schema at the next higher level.
- Data independence helps to keep the data separated from the programs that use it, which increases the flexibility, maintainability and adaptability of the database system.
- Data independence can be achieved by using the three-schema architecture, which consists of three levels of abstraction: external, conceptual and internal.
- There are two types of data independence: logical and physical .

### Logical Data Independence

- Logical data independence is the ability to change the conceptual schema without affecting the external schemas or the application programs .
- Logical data independence allows the database administrator to modify the structure or organization of the data, such as adding, deleting or renaming tables, columns, views or relationships, without changing the way the data is accessed by the users or programs .
- Logical data independence is important for evolving the database to meet changing requirements or business rules, without affecting the existing applications or users .

### Physical Data Independence

- Physical data independence is the ability to change the internal schema without affecting the conceptual schema or the external schemas .
- Physical data independence allows the database administrator to modify the physical storage or implementation of the data, such as changing the file organization, indexing, compression, encryption or partitioning, without changing the logical structure or organization of the data .
- Physical data independence is important for improving the performance, security, reliability or availability of the database, without affecting the logical meaning or interpretation of the data .

## Database Language and Interfaces

- Database language and interfaces are the means of communication between the users or programs and the DBMS.
- Database language and interfaces provide different levels of functionality, abstraction and ease of use for different categories of users or programs.
- There are three main types of database language and interfaces: data definition language (DDL), data manipulation language (DML) and data query language (DQL).

### Data Definition Language (DDL)

- Data definition language (DDL) is a database language that is used to define the database schema, such as creating, altering or dropping tables, columns, views, indexes, constraints or triggers.
- Data definition language (DDL) is used by the database administrator or the database designer to specify the logical and physical structure of the data.
- Data definition language (DDL) statements are executed by the DBMS and stored in the data dictionary, which is a special database that contains the metadata or information about the database schema.

### Data Manipulation Language (DML)

- Data manipulation language (DML) is a database language that is used to manipulate the data in the database, such as inserting, updating, deleting or retrieving data.
- Data manipulation language (DML) is used by the end users or the application programs to perform various operations on the data.
- Data manipulation language (DML) statements are executed by the DBMS and may affect the data in the database or the data in the buffer cache, which is a temporary memory area that stores the most frequently accessed data.

### Data Query Language (DQL)

- Data query language (DQL) is a database language that is used to query the data in the database, such as selecting, filtering, sorting, grouping, aggregating or joining data.
- Data query language (DQL) is used by the end users or the application programs to retrieve the data that satisfies certain criteria or conditions.
- Data query language (DQL) statements are executed by the DBMS and may involve the data in the database or the data in the buffer cache, which is a temporary memory area that stores the most frequently accessed data.
- Data query language (DQL) is often a subset or a part of data manipulation language (DML), such as the SELECT statement in SQL.