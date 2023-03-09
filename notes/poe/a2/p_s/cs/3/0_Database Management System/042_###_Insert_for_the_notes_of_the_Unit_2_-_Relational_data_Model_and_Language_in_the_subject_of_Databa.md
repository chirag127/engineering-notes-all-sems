 Here are the notes for Unit 2 - Relational data Model and Language in the subject of Database Management System:

### Relational Model

- The relational model is a graphical representation of data using relations/tables.
- A relation is made up of attributes (columns) and tuples (rows).
- Attributes have domains which specify the values that are allowed.
- Relations have a schema which specifies name of relation, attributes and their domains.
- Relations are two-dimensional tables with rows and columns.
- Real-world entities and relationships can be represented using relations.

### Relational Algebra

- Relational algebra is a procedural query language consisting of a set of operations that take one or two relations as input and produce a new relation as output.
- Operations are performed recursively on relations.
- Main operations are:

1. Select - Retrieves tuples that satisfy a given predicate.

2. Project - Deletes unwanted attributes.

3. Union - Merges two relations (duplicates are eliminated).

4. Difference - Tuples in one relation but not in another.

5. Cartesian Product (Cross Product) - Combines every tuple of one relation with every tuple of another.

6. Join - Combines two relations based on common attribute values.

- Relational algebra is a theoretical model and forms the basis for relational database languages like SQL.

### Relational Calculus

- Relational calculus is a non-procedural query language that specifies what to retrieve without specifying how to obtain it.
- Two forms: tuple relational calculus and domain relational calculus.
- In tuple relational calculus, queries are expressed in terms of tuples/rows to be retrieved. Uses conditional logic.
- In domain relational calculus, queries are expressed in terms of domain constraints. Uses logical connectives on predicates.
- Relational calculus is used as a query language for theoretical purposes but SQL is mainly used in practice.