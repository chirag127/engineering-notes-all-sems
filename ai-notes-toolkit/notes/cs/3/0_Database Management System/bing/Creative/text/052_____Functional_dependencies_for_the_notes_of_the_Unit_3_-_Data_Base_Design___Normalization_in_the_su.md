### Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database  .
- A functional dependency is denoted by X -> Y, where X and Y are sets of attributes and X is called the determinant and Y is called the dependent  .
- A functional dependency X -> Y means that for every valid instance of X, that value of X uniquely determines the value of Y .
- Functional dependencies are used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization, which helps to minimize data redundancy and improve data integrity .
- There are four primary types of functional dependencies in DBMS :
  - Trivial functional dependency: A trivial functional dependency is one where the dependent is always a subset of the determinant. For example, A -> A or A -> AB are trivial functional dependencies .
  - Non-trivial functional dependency: A non-trivial functional dependency is one where the dependent is strictly not a subset of the determinant. For example, A -> B or AB -> C are non-trivial functional dependencies .
  - Multivalued functional dependency: A multivalued functional dependency is one where the determinant determines more than one attribute that are independent of each other. For example, A ->> B and A ->> C are multivalued functional dependencies, where B and C are independent of each other .
  - Transitive functional dependency: A transitive functional dependency is one where the determinant determines another attribute that in turn determines the dependent. For example, A -> B and B -> C are transitive functional dependencies, where A determines B and B determines C .
- Functional dependencies are used to define various normal forms of a relation, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF) .
- Normalization is the process of decomposing a relation into smaller relations that satisfy certain properties, such as eliminating partial dependencies, transitive dependencies, multivalued dependencies, and join dependencies .
- Normalization helps to achieve the following objectives :
  - Reduce data redundancy and duplication
  - Avoid data anomalies, such as insertion, deletion, and update anomalies
  - Preserve data integrity and consistency
  - Enhance data security and performance
  - Simplify data manipulation and querying