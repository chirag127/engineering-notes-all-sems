### Functional dependencies for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database  .
- A functional dependency is denoted by X -> Y, where X and Y are sets of attributes and X is called the determinant and Y is called the dependent .
- A functional dependency X -> Y means that for every valid instance of X, that value of X uniquely determines the value of Y .
- For example, in a relation R(A, B, C), if A -> B, then for every value of A, there is only one value of B associated with it.
- Functional dependencies are used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity .
- There are four primary types of functional dependencies in DBMS :
  - Trivial functional dependency: A trivial functional dependency is one where the dependent is always a subset of the determinant. For example, A -> A or A, B -> A are trivial functional dependencies.
  - Non-trivial functional dependency: A non-trivial functional dependency is one where the dependent is strictly not a subset of the determinant. For example, A -> B or A, B -> C are non-trivial functional dependencies.
  - Multivalued functional dependency: A multivalued functional dependency is one where the determinant determines a set of values for the dependent, and the dependent can have multiple values for each value of the determinant. For example, A ->> B means that for each value of A, there can be multiple values of B associated with it.
  - Transitive functional dependency: A transitive functional dependency is one where the determinant determines another attribute, which in turn determines the dependent. For example, A -> B and B -> C imply A -> C, which is a transitive functional dependency.