### Unit 4 - Normalization

Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It involves breaking down a table into smaller, more manageable tables that are linked together through relationships.

#### First Normal Form (1NF)

- Each column in a table must have atomic values, meaning each value can't be further broken down into smaller values. 
- There should be no repeating groups of data in a table. 
- Each table should have a primary key that uniquely identifies each row.

#### Second Normal Form (2NF)

- A table is in 2NF if it is in 1NF and every non-key column is dependent on the entire primary key.
- If a table has a composite primary key, then each non-key column should be dependent on the entire composite key, not just part of it.

#### Third Normal Form (3NF)

- A table is in 3NF if it is in 2NF and every non-key column is dependent only on the primary key and not on any other non-key column.
- This eliminates transitive dependencies, where a non-key column is dependent on another non-key column.

#### Boyce-Codd Normal Form (BCNF)

- A table is in BCNF if it is in 3NF and every determinant (a column or set of columns that uniquely determines another column) is a candidate key.
- BCNF is stricter than 3NF and ensures that there are no overlapping candidate keys.

#### Fourth Normal Form (4NF)

- A table is in 4NF if it is in BCNF and has no multi-valued dependencies.
- Multi-valued dependencies occur when a non-key column has multiple values associated with a single value in another column.

#### Fifth Normal Form (5NF)

- A table is in 5NF if it is in 4NF and there are no join dependencies.
- Join dependencies occur when a table can be further broken down into smaller tables without losing any information.

In conclusion, normalization helps to prevent data inconsistencies and anomalies by breaking down a table into smaller, more manageable tables. The normalization process follows a set of rules to ensure that tables are organized efficiently and effectively.