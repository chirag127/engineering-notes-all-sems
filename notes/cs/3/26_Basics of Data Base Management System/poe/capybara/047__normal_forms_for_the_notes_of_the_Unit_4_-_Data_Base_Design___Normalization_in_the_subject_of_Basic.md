### Normal Forms for the Notes of Unit 4 - Database Design & Normalization

Database normalization is the process of organizing data in a database in a way that reduces redundancy and dependency. Normalization involves applying a set of formal rules to a database design to ensure that it is organized in a way that is efficient, scalable, and maintainable. In this unit, we will cover the different normal forms that are used in database design and normalization.

Here are the different normal forms that we will cover:

#### First Normal Form (1NF)

- A table is in first normal form (1NF) if it does not contain any repeating groups or arrays.
- Each column in a 1NF table contains atomic values, which means that it cannot be further divided into smaller values.
- 1NF tables are easy to maintain and update, but they can still contain redundancy.

#### Second Normal Form (2NF)

- A table is in second normal form (2NF) if it is in 1NF and every non-key column is functionally dependent on the entire primary key.
- In other words, a 2NF table does not contain any partial dependencies, where a non-key column is dependent on only a part of the primary key.
- 2NF tables are more normalized than 1NF tables, but they can still contain redundancy.

#### Third Normal Form (3NF)

- A table is in third normal form (3NF) if it is in 2NF and every non-key column is functionally dependent on the primary key, and not on any other non-key column.
- In other words, a 3NF table does not contain any transitive dependencies, where a non-key column is dependent on another non-key column.
- 3NF tables are even more normalized than 2NF tables, and they contain minimal redundancy.

#### Boyce-Codd Normal Form (BCNF)

- Boyce-Codd normal form (BCNF) is a stricter form of 3NF, where every determinant is a candidate key.
- In other words, a BCNF table does not contain any non-trivial dependencies, where a non-key column is dependent on another non-key column that is not a subset of any candidate key.
- BCNF tables are the most normalized tables, and they contain no redundancy.

These are the different normal forms that are used in database design and normalization. By applying these normal forms to a database design, we can ensure that the database is efficient, scalable, and maintainable.