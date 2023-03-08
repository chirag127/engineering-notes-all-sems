 Here are the notes for Unit 4 - Normalization in the subject of Database Management Systems Lab:

### Normalization

Normalization is a database design technique which organizes tables in a database. It helps in eliminating redundant data and ensures data dependencies make sense. The main advantages of normalization are:

1. It minimizes duplicate data, which reduces storage needs.
2. It prevents inconsistent data by ensuring data dependencies are logical.
3. It makes the database more flexible to changes.

The three main normal forms in normalization are:

1. First Normal Form (1NF): The information is stored in a two-dimensional table with rows and columns. There are no repeating groups of columns.
2. Second Normal Form (2NF): The table is in first normal form and all non-key columns depend on the primary key.
3. Third Normal Form (3NF): The table is in second normal form and all non-key columns only depend on the primary key, not on other non-key columns.

Further normal forms like Boyce-Codd Normal Form (BCNF) and Fourth Normal Form (4NF) also exist to handle certain type of dependencies between columns.

Normalization is performed through a step-by-step process by applying normalization forms. Starting from a first normal form, modifications are done to satisfy the next higher normal form. This process continues until the highest normal form suitable for the database is achieved.

The advantages of normalization have to be weighed against the disadvantages of increased processing required to join normalized tables. For simple databases, normalization may not be worth the effort. However, for complex databases with many relationships, normalization is critical to efficient design and operation.