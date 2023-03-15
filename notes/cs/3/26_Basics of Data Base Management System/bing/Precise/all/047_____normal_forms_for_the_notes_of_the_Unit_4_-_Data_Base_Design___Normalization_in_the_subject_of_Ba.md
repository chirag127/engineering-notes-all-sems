# Normal Forms

Normal forms are a set of rules that a database must follow to minimize data redundancy and prevent data anomalies. These rules are used in the process of database normalization, which involves organizing the data in a database into tables and establishing relationships between the tables.

There are several normal forms, including:

1. **First Normal Form (1NF):** This normal form requires that each table in the database has a primary key and that all data in each column is atomic, meaning that it cannot be further subdivided.
2. **Second Normal Form (2NF):** This normal form requires that all non-key attributes in a table are dependent on the entire primary key. This means that there should be no partial dependencies, where an attribute is dependent on only part of the primary key.
3. **Third Normal Form (3NF):** This normal form requires that all non-key attributes in a table are not only dependent on the primary key, but also on non-key attributes. This means that there should be no transitive dependencies, where an attribute is dependent on another attribute that is dependent on the primary key.
4. **Boyce-Codd Normal Form (BCNF):** This normal form is a stronger version of 3NF that requires that all determinants in a table be candidate keys. This means that there should be no non-trivial functional dependencies where the determinant is not a candidate key.
5. **Fourth Normal Form (4NF):** This normal form requires that a table has no multi-valued dependencies, where an attribute is dependent on another attribute, but not on the key of the table.
6. **Fifth Normal Form (5NF):** This normal form, also known as Project-Join Normal Form (PJNF), requires that a table cannot be decomposed into smaller tables without losing information.

These normal forms provide a framework for designing a well-structured database that minimizes data redundancy and prevents data anomalies. It is important to note that not all databases need to be normalized to the highest normal form, and that the level of normalization should be determined based on the specific needs of the database and its intended use.