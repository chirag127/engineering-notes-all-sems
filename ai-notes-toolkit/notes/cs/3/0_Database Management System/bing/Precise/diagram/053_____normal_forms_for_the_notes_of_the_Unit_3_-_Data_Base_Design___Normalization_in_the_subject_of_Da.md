### Normal Forms

Normal forms are a set of rules used in database design to reduce data redundancy and improve data integrity. Normalization is the process of organizing data in a database according to these rules. There are several normal forms, including:

1. **First Normal Form (1NF):** This normal form requires that each column in a table contains only atomic values, meaning that each value in a column is indivisible. It also requires that each column contains values of the same data type and that there are no repeating groups or arrays within a column.

2. **Second Normal Form (2NF):** This normal form requires that a table is in 1NF and that all non-key columns are dependent on the entire primary key. This means that if a table has a composite primary key (a primary key made up of more than one column), then all non-key columns must be dependent on all columns of the primary key.

3. **Third Normal Form (3NF):** This normal form requires that a table is in 2NF and that there are no transitive dependencies between non-key columns. A transitive dependency occurs when a non-key column is dependent on another non-key column, which is in turn dependent on the primary key.

4. **Boyce-Codd Normal Form (BCNF):** This normal form is a stronger version of 3NF. It requires that a table is in 3NF and that for every non-trivial functional dependency, the determinant is a superkey. A superkey is a set of columns that uniquely identifies a row in a table.

5. **Fourth Normal Form (4NF):** This normal form requires that a table is in BCNF and that there are no multi-valued dependencies. A multi-valued dependency occurs when a column is dependent on another column, but not on the primary key.

6. **Fifth Normal Form (5NF):** This normal form, also known as Project-Join Normal Form (PJNF), requires that a table is in 4NF and that there are no join dependencies that are not implied by the candidate keys. A join dependency occurs when a table can be decomposed into two or more smaller tables, and the original table can be reconstructed by taking the natural join of the smaller tables.

These normal forms provide a framework for designing a database that is free of data redundancy and that maintains data integrity. It is important to note that normalization is not always necessary or desirable, and that denormalization (the process of introducing redundancy into a database) can sometimes improve performance. However, normalization is a useful tool for database designers and should be considered when designing a database.