### Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database  .
- A functional dependency is denoted by X -> Y, where X and Y are sets of attributes and X determines the value of Y  .
- A functional dependency is used to establish relationships between attributes and to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity .
- There are four primary types of functional dependencies in DBMS :
  - Trivial functional dependency: A FD is trivial if Y is a subset of X, i.e., X -> Y is trivial if Y ⊆ X. For example, A -> A or AB -> A are trivial FDs .
  - Non-trivial functional dependency: A FD is non-trivial if Y is not a subset of X, i.e., X -> Y is non-trivial if Y ⊄ X. For example, A -> B or AB -> C are non-trivial FDs .
  - Multivalued dependency: A FD is multivalued if for a given value of X, there are multiple values of Y that are independent of each other, i.e., X ->> Y. For example, if a student can have multiple hobbies and multiple phone numbers, then student_id ->> hobby and student_id ->> phone_number are multivalued FDs .
  - Transitive dependency: A FD is transitive if X -> Y and Y -> Z, then X -> Z. For example, if employee_id -> department_id and department_id -> location, then employee_id -> location is a transitive FD .
- A relation is said to be in a certain normal form if it satisfies certain functional dependencies and other constraints. The most common normal forms are:
  - First normal form (1NF): A relation is in 1NF if it contains only atomic values and no repeating groups .
  - Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key .
  - Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key .
  - Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key .
  - Fourth normal form (4NF): A relation is in 4NF if it is in BCNF and has no multivalued dependencies .
  - Fifth normal form (5NF): A relation is in 5NF if it is in 4NF and cannot be further decomposed without losing information .