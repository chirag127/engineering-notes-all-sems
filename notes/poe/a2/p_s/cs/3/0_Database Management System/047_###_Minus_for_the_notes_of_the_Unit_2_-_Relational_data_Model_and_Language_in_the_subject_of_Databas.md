 Here are the notes for Unit 2 - Relational data Model and Language in the subject of Database Management System:

### Relational Model

- The relational model is based on first-order predicate logic and defines a table as an n-ary relation.
- A relational database consists of a collection of tables (relations).
- Each table has a fixed set of attributes/columns and a variable number of tuples/rows.
- Tables are related to each other through common attributes which are known as foreign keys.
- The relational model ensures data independence, manages structural complexity through normalization, and supports non-procedural access to data through declarative queries.

### Relational Algebra

- Relational algebra is a procedural query language consisting of a set of operations that take one or two relations as input and produce a new relation as output.
- The basic operators in relational algebra are:

1. Select (σ) - selects tuples that satisfy a given predicate/condition.
2. Project (π) - selects a subset of the attributes/columns.
3. Union (∪) - retrieves tuples that are in either of two relations.
4. Difference (-) - retrieves tuples that are in the first relation but not in the second.
5. Cartesian Product (x) - joins two relations and produces a relation with a tuple for every possible combination of tuples from both relations.
6. Rename (ρ) - renames the output relation and attributes.

- Additional operators can be defined in terms of these basic operators.
- Relational algebra can be used to express queries in a declarative manner without prescribing the steps to evaluate them.

[Detailed diagrams and examples can be added here for better understanding]

Advantages:
- Declarative approach
- Facilitates optimization
- Basis for relational query languages like SQL

Disadvantages:
- Does not directly support aggregation and grouping
- Not a complete data definition language

Applications:
- Query formulation and optimization
- Providing theoretical foundation for relational database systems and SQL