### Entity Integrity

- Entity integrity is a rule that ensures that each row or record in a relational table is uniquely identified by a primary key.
- A primary key is a column or a combination of columns that can uniquely distinguish each row in a table.
- Entity integrity prevents duplicate rows or records from being inserted into a table, and ensures that every row can be uniquely identified and referenced by other tables.
- Entity integrity also ensures that no part of a primary key can be null, because null values are unknown and cannot be compared or matched.
- Entity integrity is enforced by the database system by creating a unique index on the primary key column(s) and checking for null values before inserting or updating data.