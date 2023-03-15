## Unit 4 - Normalization

Normalization is a process used in database design to minimize data redundancy and dependency. It involves organizing data into tables in such a way that the results of using the database are always unambiguous and as intended. Normalization is achieved by dividing larger tables into smaller, more manageable tables and establishing relationships between them.

The main objectives of normalization are:
- To eliminate redundant data, which reduces the chances of data inconsistency.
- To minimize the need for restructuring the database when new types of data are introduced.
- To make the database more flexible by reducing the number of interrelationships between tables.

There are several levels of normalization, each with its own set of rules and guidelines. These levels are referred to as normal forms and include First Normal Form (1NF), Second Normal Form (2NF), Third Normal Form (3NF), Boyce-Codd Normal Form (BCNF), Fourth Normal Form (4NF), and Fifth Normal Form (5NF).

Each normal form has a set of rules that must be followed in order to achieve that level of normalization. For example, to achieve 1NF, each table must have a primary key and each column must contain only atomic values. To achieve 2NF, all non-key attributes must be dependent on the entire primary key.

Normalization is an important part of database design and can greatly improve the efficiency and effectiveness of a database. However, it is not always necessary to fully normalize a database, and in some cases, it may be more practical to denormalize certain tables for performance reasons.