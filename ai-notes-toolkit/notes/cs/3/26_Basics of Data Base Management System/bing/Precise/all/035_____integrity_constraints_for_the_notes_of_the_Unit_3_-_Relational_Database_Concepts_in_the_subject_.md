# Integrity Constraints

Integrity constraints are rules that help ensure the accuracy and consistency of data in a relational database. These constraints are used to enforce the database's schema, which is the logical design of the database. Here are some common types of integrity constraints in a relational database:

1. **Domain constraints**: These constraints define the valid values for an attribute. For example, a domain constraint on an attribute representing age might specify that the value must be a non-negative integer.

2. **Key constraints**: These constraints ensure that the data in a table is unique. A primary key constraint, for example, specifies that the values of the primary key attribute(s) must be unique for each row in the table.

3. **Referential integrity constraints**: These constraints ensure that relationships between tables are maintained. A foreign key constraint, for example, specifies that the values of the foreign key attribute(s) in one table must match the values of the primary key attribute(s) in another table.

4. **Entity integrity constraints**: These constraints ensure that each row in a table represents a unique entity. An entity integrity constraint, for example, specifies that the primary key attribute(s) of a table cannot contain null values.

These are some of the common integrity constraints used in relational databases to ensure the accuracy and consistency of data. It is important to carefully design and implement these constraints to maintain the integrity of the database.