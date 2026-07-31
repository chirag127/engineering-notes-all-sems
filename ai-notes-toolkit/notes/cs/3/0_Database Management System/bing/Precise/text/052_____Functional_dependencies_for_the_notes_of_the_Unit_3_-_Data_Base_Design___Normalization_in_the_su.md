### Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- A functional dependency is a constraint between two sets of attributes in a relation from a database.
- Given a relation R, a set of attributes X in R is said to functionally determine another set of attributes Y, also in R, (written X → Y) if, and only if, each X value is associated with precisely one Y value.
- In other words, the values of the Y attributes are determined by the values of the X attributes.
- The left-hand side of the functional dependency is called the determinant and the right-hand side is called the dependent.
- Functional dependencies are used to create a normalized design for a database, which reduces data redundancy and improves data integrity.
- Normalization is the process of organizing a database in a way that reduces redundancy and dependency.
- Normalization typically involves dividing a database into two or more tables and defining relationships between the tables.
- The objective is to isolate data so that additions, deletions, and modifications of a field can be made in just one table and then propagated through the rest of the database via the defined relationships.
- There are several normal forms, including first normal form (1NF), second normal form (2NF), third normal form (3NF), and so on.
- Each normal form has a set of rules that must be followed in order to achieve that normal form.
- The process of normalization typically involves breaking down a single table into two or more smaller, more focused tables and defining relationships between those tables.
- Normalization can help to reduce data redundancy, improve data integrity, and simplify the process of maintaining the database.
