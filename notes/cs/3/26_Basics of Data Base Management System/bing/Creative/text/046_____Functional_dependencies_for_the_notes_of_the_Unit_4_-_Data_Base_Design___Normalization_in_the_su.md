### Functional dependencies for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database  .
- A functional dependency is denoted by X -> Y, where X and Y are sets of attributes and X determines the value of Y  .
- A functional dependency is used to establish relationships between attributes and to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity .
- There are four primary types of functional dependencies in DBMS :
  - Trivial functional dependency: A FD is trivial if Y is a subset of X, i.e., X -> Y is trivial if Y ⊆ X. For example, A -> A or A, B -> A are trivial FDs .
  - Non-trivial functional dependency: A FD is non-trivial if Y is not a subset of X, i.e., X -> Y is non-trivial if Y ⊄ X. For example, A -> B or A, B -> C are non-trivial FDs .
  - Multivalued functional dependency: A FD is multivalued if for a given value of X, there are multiple values of Y that are independent of each other, i.e., X ->> Y. For example, A ->> B, C means that for a given value of A, there are multiple values of B and C that are unrelated .
  - Transitive functional dependency: A FD is transitive if X -> Y and Y -> Z, then X -> Z. For example, A -> B and B -> C, then A -> C is a transitive FD .
- A relation is said to be in a certain normal form if it satisfies certain functional dependencies and other constraints. There are several normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF)  .
- The process of normalization is to decompose a relation into smaller relations that are in higher normal forms and that preserve the original information and functional dependencies  .