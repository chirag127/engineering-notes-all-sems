# Unit 4 - Normalization in Database Management Systems Lab

## Normalization

- Normalization is a technique to reduce data redundancy and remove anomalies related to insertion, deletion and updation from the database .
- Normalization of the database is a process of arranging the data in the database.
- The core idea of database normalization is to divide the tables into smaller subtables and store pointers to data rather than replicating it.
- Normalization is a process used for data modelling or database creation, where you organise your data and tables so it can be added and updated efficiently.
- Normalization is something a person does manually, as opposed to a system or a tool doing it.

## Keys

- Keys are column attributes that identify a database record uniquely.
- Keys are used to establish and identify relationships between tables and also to uniquely identify any record or row of data inside a table.
- There are different types of keys, such as primary key, foreign key, candidate key, alternate key, composite key, super key, etc.

## Functional Dependencies

- Functional dependencies are constraints between two attributes in a relation.
- A functional dependency is a relationship that exists when one attribute uniquely determines another attribute.
- For example, if A and B are attributes of a relation R, and every value of A is associated with exactly one value of B, then we say that B is functionally dependent on A, or A determines B, denoted by A -> B.

## Normal Forms

- Normal forms are steps to accomplish a certain quality of a database.
- Normal forms are based on the concept of functional dependencies and keys.
- There are different levels of normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), etc.
- Each normal form has a set of rules or criteria that a relation must satisfy to be in that normal form.
- The higher the normal form, the less redundancy and anomalies in the database.

## References

: https://medium.com/geekculture/normalization-in-database-management-system-82a5f14e117
: https://www.includehelp.com/dbms/normalization-in-database-management-system.aspx
: https://hackr.io/blog/dbms-normalization
: https://www.databasestar.com/database-normalization/
: https://phoenixnap.com/kb/database-normalization