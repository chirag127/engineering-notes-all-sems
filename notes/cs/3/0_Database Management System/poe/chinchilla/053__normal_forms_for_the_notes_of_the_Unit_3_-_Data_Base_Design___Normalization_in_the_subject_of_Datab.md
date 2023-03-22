### Normal Forms for the Notes of Unit 3 - Database Design & Normalization

In the field of database management, normalization is a crucial process that helps in designing a database schema that is both efficient and effective. Normalization involves the process of breaking down a large and complex database into smaller, more manageable parts, which are easier to maintain and query. The process of normalization is guided by a set of rules called normal forms, which are discussed below.

1. First Normal Form (1NF)
The first normal form requires that a table should have a primary key, and every column in the table should be atomic, which means that it contains only one value. The table should also have no repeating groups or arrays.

2. Second Normal Form (2NF)
The second normal form requires that a table should be in 1NF and should have no partial dependencies. This means that every non-key column in the table must be dependent on the primary key. If a non-key column is dependent on only a part of the primary key, it should be moved to a separate table.

3. Third Normal Form (3NF)
The third normal form requires that a table should be in 2NF and should have no transitive dependencies. This means that if a non-key column is dependent on another non-key column, it should be moved to a separate table.

4. Boyce-Codd Normal Form (BCNF)
The Boyce-Codd Normal Form requires that a table should be in 3NF and should have no non-trivial functional dependencies. This means that every determinant should be a candidate key.

5. Fourth Normal Form (4NF)
The fourth normal form requires that a table should be in BCNF and should have no multi-valued dependencies. This means that a table should not have non-key attributes that depend on other non-key attributes.

6. Fifth Normal Form (5NF)
The fifth normal form requires that a table should be in 4NF and should have no join dependencies. This means that a table should not have any non-trivial dependencies on combinations of its candidate keys.

In conclusion, the process of normalization is essential for database design, and it helps in ensuring that the database schema is efficient, effective, and easy to maintain. The normal forms provide a set of rules that guide the normalization process, and it is essential to ensure that a database is in the highest possible normal form to avoid data anomalies and inconsistencies.