# Functional dependencies for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database .
- A functional dependency mathematically expresses the relation between different values in a database management system (DBMS).
- A functional dependency acts as a constraint between the two sets of attributes and is an essential factor in designing database parameters and functions.
- A functional dependency is denoted by an arrow, such as X -> Y, which means that the value of Y is determined by the value of X  .
- There are four primary types of functional dependencies in DBMS :
  - Trivial functional dependency: A dependent is always a subset of the determinant, such as X -> X or X -> XY.
  - Non-trivial functional dependency: A dependent is strictly not a subset of the determinant, such as X -> Y, where Y is not a part of X.
  - Multivalued functional dependency: A determinant can have more than one dependent, such as X -> YZ, where Y and Z are independent of each other.
  - Transitive functional dependency: A dependent is determined by another dependent, such as X -> Y and Y -> Z, which implies X -> Z.
- Functional dependencies are used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization .
- Normalization is the process of organizing the data in a database to minimize data redundancy and improve data integrity .
- Normalization involves applying a series of normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), and so on, to the relations in a database .
- Each normal form has a set of criteria that the relations must satisfy to be in that normal form .
- Functional dependencies are used to check whether a relation satisfies the criteria of a normal form or not .
- For example, to be in 2NF, a relation must be in 1NF and have no partial dependencies, which means that no non-key attribute is dependent on a part of the primary key .
- Functional dependencies help to identify the primary key and the non-key attributes of a relation, and to determine whether there are any partial dependencies or not .