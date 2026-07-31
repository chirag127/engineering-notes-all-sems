### Functional dependencies for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database.
- A functional dependency mathematically expresses the relation between different values in a database management system (DBMS).
- A functional dependency is denoted by an arrow, such as X -> Y, which means that the value of Y is determined by the value of X.
- Functional dependencies are used to establish relationships between attributes in a database, and to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity.
- There are four primary types of functional dependencies in DBMS :
  - Trivial functional dependency: A dependent is always a subset of the determinant, such as X -> X or X -> XY.
  - Non-trivial functional dependency: A dependent is strictly not a subset of the determinant, such as X -> Y, where Y is not a part of X.
  - Multivalued functional dependency: A determinant can have more than one dependent, such as X -> YZ, where Y and Z are independent of each other.
  - Transitive functional dependency: A dependent is determined by another dependent, such as X -> Y and Y -> Z, which implies X -> Z.
- Functional dependencies are used to identify the candidate keys, primary keys, and foreign keys of a relation, and to check the normal forms of a relation.
- Normal forms are the rules or standards that a relation must follow to be well-structured and free of anomalies.
- There are several normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF).
- Each normal form has a set of conditions that a relation must satisfy to be in that normal form.
- The higher the normal form, the more normalized the relation is, and the less redundancy and inconsistency it has.
- Normalization is the process of decomposing a relation into smaller relations that satisfy higher normal forms.
- Normalization helps to improve the performance, security, and maintainability of the database.