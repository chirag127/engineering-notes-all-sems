### Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A super key is a set of one or more attributes that can uniquely identify a tuple (or row) in a relation (or table) of a database.
- A super key may contain extra attributes that are not necessary for unique identification.
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify a tuple.
- A candidate key can be derived from a super key by removing the redundant attributes.
- A primary key is a special candidate key that is chosen by the database designer to identify the tuples in a relation.
- A primary key should be non-null and unique for each tuple in a relation.
- A relation can have more than one super key, but only one primary key.
- A super key can be used to enforce referential integrity constraints, which ensure that the values of a foreign key in one relation match the values of a primary key in another relation.
- A super key can also be used to define functional dependencies, which specify the attributes that are determined by another attribute or a set of attributes in a relation.
- A super key can help to reduce data redundancy and inconsistency by eliminating partial and transitive dependencies in a relation.