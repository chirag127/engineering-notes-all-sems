# Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- Functional dependency is a constraint between two sets of attributes in a relation from a database.
- Functional dependency mathematically expresses the relation between different values in a database management system (DBMS).
- Functional dependency is denoted by an arrow, such as X → Y, which means that the value of Y is determined by the value of X.
- Functional dependency is an essential factor in designing database parameters and functions to help store and manage data.
- Functional dependency is used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity.
- There are four primary types of functional dependency :
  - Trivial functional dependency: A dependent is always a subset of the determinant, such as X → X or X → XY.
  - Non-trivial functional dependency: A dependent is strictly not a subset of the determinant, such as X → Y, where Y is not a part of X.
  - Multivalued functional dependency: A determinant can have more than one dependent, such as X → YZ, where Y and Z are independent of each other.
  - Transitive functional dependency: A dependent is indirectly determined by the determinant through another attribute, such as X → Y and Y → Z, which implies X → Z.
- Functional dependency can be used to check the normal forms of a relation, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF).
- Functional dependency can be used to decompose a relation into smaller relations that preserve the original information and satisfy the desired normal form.
- Functional dependency can be used to find the candidate keys, superkeys, and primary keys of a relation, which are the minimal sets of attributes that can uniquely identify a tuple.