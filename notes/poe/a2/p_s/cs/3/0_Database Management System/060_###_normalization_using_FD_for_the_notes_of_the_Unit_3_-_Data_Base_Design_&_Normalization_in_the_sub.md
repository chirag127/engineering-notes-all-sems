 Here is the content in markdown format for the topic ### normalization using FD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System:

## Functional Dependency (FD)
- A functional dependency is a constraint between two attributes (or columns) of a relation.
- It is denoted as X -> Y, where X is the determinant (LHS) and Y is the dependent (RHS).
- It means that the value of attribute Y is uniquely determined by the value of attribute X.
- Two types:
1. Trivial FD: X -> X (always holds)
2. Non-trivial FD: X -> Y (where X and Y are non-equal attributes)

## Normalization using FD
- The process of organizing data into a database structure with the goal of reducing redundancy and improving data integrity is called normalization.
- The most common forms of normalization applied using FD are:
1. 1NF: Remove duplicating groups of data, no multi-valued attributes
2. 2NF: Meet 1NF requirements, no partial dependency (X -> Y -> Z)
3. 3NF: Meet 2NF requirements, no transitive dependency (X -> Y -> Z -> W)
- Higher normal forms (BCNF, 4NF, 5NF, DKNF) also exist to handle more complex relationships.
- Advantages: Data consistency, avoid update anomalies, space efficiency
- Disadvantages: May result in additional tables and join operations

[Diagrams and examples can be added here to illustrate the concepts]

Applications: Basically used in the initial design of any database to ensure data quality.