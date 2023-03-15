### Normalization using FD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

Normalization is the process of organizing data in a database. This includes creating tables and establishing relationships between those tables according to rules designed both to protect the data and to make the database more flexible by eliminating redundancy and inconsistent dependency.

Functional dependencies (FDs) are used to specify formal measures of the "goodness" of relational designs. FDs are constraints that describe the relationship between attributes in a relation. They are used to establish relationships between tables and to identify the attributes that should be used as keys.

Normalization using FD involves the following steps:

1. Identify all the functional dependencies in the relation.
2. Use the identified functional dependencies to decompose the relation into smaller relations that are in a higher normal form.
3. Repeat the process until all the relations are in the desired normal form.

The normal forms commonly used in normalization using FD are:

1. First Normal Form (1NF): A relation is in 1NF if and only if the domain of each attribute contains only atomic values, and the value of each attribute contains only a single value from that domain.
2. Second Normal Form (2NF): A relation is in 2NF if it is in 1NF and every non-prime attribute is fully functionally dependent on the primary key.
3. Third Normal Form (3NF): A relation is in 3NF if it is in 2NF and there is no transitive dependency between non-prime attributes.
4. Boyce-Codd Normal Form (BCNF): A relation is in BCNF if it is in 3NF and for every non-trivial functional dependency X -> Y, X is a superkey.

Normalization using FD is an important process in database design that helps to minimize data redundancy and improve data integrity. It is a crucial step in creating an efficient and flexible database.