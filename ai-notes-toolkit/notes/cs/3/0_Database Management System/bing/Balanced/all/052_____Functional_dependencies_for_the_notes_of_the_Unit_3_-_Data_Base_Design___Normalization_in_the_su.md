# Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database.
- A functional dependency mathematically expresses the relation between different values in a database management system (DBMS).
- A functional dependency is denoted by an arrow, such as X → Y, which means that the value of Y is determined by the value of X.
- A functional dependency is an essential factor in designing database parameters and functions to help store and manage data.
- A functional dependency is used to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity.
- There are four primary types of functional dependencies in DBMS: trivial, non-trivial, multivalued, and transitive .
  - A trivial functional dependency is a functional dependency where the dependent is always a subset of the determinant, such as X → X or X → XY.
  - A non-trivial functional dependency is a functional dependency where the dependent is strictly not a subset of the determinant, such as X → Y, where Y is not a part of X.
  - A multivalued functional dependency is a functional dependency where the determinant can have multiple values for the dependent, such as X → YZ, where Y and Z are independent of each other.
  - A transitive functional dependency is a functional dependency where the determinant depends on another attribute, which in turn depends on another attribute, such as X → Y and Y → Z, which implies X → Z.
- A functional dependency can be used to identify the primary key (PK) and other non-key attributes within a table.
- A functional dependency can be used to decompose a relation into smaller relations that are in higher normal forms.
- A functional dependency can be used to check the consistency and validity of the data in a relation.