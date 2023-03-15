### Normal Forms for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

- Normal forms are used to eliminate or reduce redundancy in database tables.
- Normal forms are based on the concept of functional dependency, which is a relationship between two sets of attributes in a relation.
- Normal forms are of four major forms: 1NF, 2NF, 3NF, and BCNF. A majority of the database systems have their databases normalized up to the 3NF in DBMS.
- 1NF: A relation is in first normal form if it does not contain any composite or multi-valued attribute. This means that each attribute should have a single atomic value and no repeating groups of attributes.
- 2NF: A relation is in second normal form if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. This means that there should be no partial dependency of any attribute on the primary key.
- 3NF: A relation is in third normal form if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. This means that there should be no transitive dependency of any attribute on the primary key.
- BCNF: A relation is in Boyce-Codd normal form if it is in 3NF and every determinant is a candidate key. This means that there should be no non-trivial functional dependency where the left-hand side is not a superkey.
- Normalization helps to avoid redundancy and maintain the integrity of the database. It also helps to eliminate undesirable characteristics associated with insertion, deletion, and updating.