### Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- A functional dependency (FD) is a constraint between two sets of attributes in a relation from a database.
- A functional dependency mathematically expresses the relation between different values in a database management system (DBMS).
- A functional dependency is denoted by an arrow, such as X → Y, which means that the value of Y is determined by the value of X.
- There are four primary types of functional dependencies in DBMS: trivial, non-trivial, multivalued, and transitive .
- A trivial functional dependency is when the dependent attribute is a subset of the determinant attribute, such as X → X or X → XY.
- A non-trivial functional dependency is when the dependent attribute is not a subset of the determinant attribute, such as X → Y, where Y is not a part of X.
- A multivalued functional dependency is when the value of an attribute depends on the value of another attribute, and both attributes are independent of each other, such as X → YZ, where Y and Z are not functionally dependent on each other.
- A transitive functional dependency is when the value of an attribute depends on the value of another attribute, which in turn depends on the value of a third attribute, such as X → Y and Y → Z, which implies X → Z.
- Functional dependencies are used to establish relationships between attributes in a database and to ensure that the database is in a state of normalization .
- Normalization is the process of organizing the data in a database to minimize data redundancy and improve data integrity .
- Normalization involves applying a series of normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), and so on, to the relations in a database .
- Each normal form has a set of criteria that the relations must satisfy to be in that normal form .
- For example, to be in 1NF, a relation must have no repeating groups, no multivalued attributes, and no composite attributes.
- To be in 2NF, a relation must be in 1NF and have no partial dependencies, which means that every non-key attribute must depend on the whole primary key.
- To be in 3NF, a relation must be in 2NF and have no transitive dependencies, which means that every non-key attribute must depend only on the primary key and not on any other non-key attribute.
- Functional dependencies are used to identify the primary key and the non-key attributes of a relation, and to check if the relation satisfies the criteria of each normal form .
- Functional dependencies are also used to decompose a relation into smaller relations that are in a higher normal form, which reduces data anomalies and improves data consistency .