### Normal Forms

Normal forms are a set of rules that a database must follow to minimize data redundancy and prevent data anomalies. There are several normal forms, including:

1. **First Normal Form (1NF):** This normal form requires that each column in a table must contain only atomic values, meaning that each value in a column must be indivisible. Additionally, each column must have a unique name, and the order in which data is stored does not matter.

2. **Second Normal Form (2NF):** This normal form requires that a table be in 1NF and that all non-key columns be dependent on the entire primary key. This means that if a table has a composite primary key, all non-key columns must be dependent on all parts of the primary key.

3. **Third Normal Form (3NF):** This normal form requires that a table be in 2NF and that there be no transitive dependencies between non-key columns. This means that if a non-key column is dependent on another non-key column, that column must be dependent on the primary key.

4. **Boyce-Codd Normal Form (BCNF):** This normal form is a stronger version of 3NF. It requires that a table be in 3NF and that for every non-trivial functional dependency, the determinant must be a candidate key.

5. **Fourth Normal Form (4NF):** This normal form requires that a table be in BCNF and that there be no multi-valued dependencies. This means that if a column can have multiple values for a single row, those values must be stored in a separate table.

6. **Fifth Normal Form (5NF):** This normal form requires that a table be in 4NF and that there be no join dependencies that are not implied by the candidate keys. This means that if a table can be decomposed into multiple tables, those tables must be able to be joined back together using only the candidate keys.

These normal forms provide a framework for designing a database that is free of data redundancy and data anomalies. By following these rules, a database designer can create a database that is efficient and easy to maintain.