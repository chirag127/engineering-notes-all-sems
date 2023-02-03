### relational model terminology – domains for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

In the relational model, a domain is a set of values that a particular attribute can take. The domain defines a constraint on the values that can be stored in a column of a table. 

1. Atomic Domain: An atomic domain is a domain that contains indivisible values. For example, an atomic domain for a column storing names might only allow for strings of text.

2. Null Values: In the relational model, a null value indicates that a particular attribute does not have a value. Null values are important for representing missing or unknown data in a database.

3. Key: A key is an attribute or set of attributes that uniquely identifies a tuple (row) in a relation (table). Keys are used to enforce integrity constraints and to ensure that each tuple has a unique identifier.

4. Foreign Key: A foreign key is an attribute or set of attributes in a relation (table) that refers to the primary key of another relation. Foreign keys are used to enforce referential integrity constraints and to create relationships between tables.

5. Normalization: Normalization is the process of organizing data in a relational database to minimize redundancy and improve data integrity. Normalization involves dividing a database into two or more tables and defining relationships between the tables.

6. Primary Key: A primary key is a key that is used to uniquely identify a tuple (row) in a relation (table). A relation can have only one primary key, and it must be unique for each tuple in the relation.

7. Super Key: A super key is a set of attributes that can be used to uniquely identify a tuple (row) in a relation (table). A super key can be a primary key or a combination of attributes that, together, form a unique identifier for each tuple.
