# Unit 2 - Relational Data Model and Language

## Relational Data Model
- A relational data model is a way of representing data in a database using tables, columns, rows, and keys.
- A table is a collection of related data, where each column represents an attribute and each row represents a record or a tuple.
- A key is a column or a combination of columns that uniquely identifies a row in a table.
- A primary key is a key that is chosen to be the main identifier of a row in a table. A table can have only one primary key.
- A foreign key is a key that references a primary key of another table. A table can have multiple foreign keys.
- A relational schema is a set of table definitions, along with their keys and constraints.
- A constraint is a rule that restricts the values that can be stored in a table or a column. Some common types of constraints are:
  - Not null: a column cannot have null values.
  - Unique: a column or a combination of columns cannot have duplicate values.
  - Check: a column or a row must satisfy a specified condition.
  - Default: a column has a default value if no value is specified.
  - Referential integrity: a foreign key must match an existing value of a primary key in the referenced table.

## Relational Algebra
- Relational algebra is a set of operations that can be applied to one or more tables to manipulate and query data.
- Relational algebra operations can be classified into two categories: unary and binary.
- Unary operations take one table as input and produce one table as output. Some common unary operations are:
  - Select: selects a subset of rows from a table that satisfy a given condition.
  - Project: selects a subset of columns from a table.
  - Rename: changes the name of a table or a column.
- Binary operations take two tables as input and produce one table as output. Some common binary operations are:
  - Union: combines the rows of two tables that have the same schema (same number and names of columns).
  - Intersection: selects the rows that are common to both tables that have the same schema.
  - Difference: selects the rows that are in the first table but not in the second table that have the same schema.
  - Cartesian product: combines every row of the first table with every row of the second table, regardless of the schema.
  - Join: combines the rows of two tables that have a common attribute or a matching condition. There are different types of joins, such as:
    - Natural join: joins two tables on all the common attributes.
    - Equi-join: joins two tables on a specified condition that involves equality.
    - Theta-join: joins two tables on a specified condition that involves any comparison operator.
    - Inner join: selects only the matching rows from both tables.
    - Outer join: selects all the rows from one or both tables, and fills the missing values with nulls. There are three types of outer joins: left, right, and full.
    - Semi-join: selects the rows from the first table that have a matching row in the second table, but does not include the columns from the second table.
    - Anti-join: selects the rows from the first table that do not have a matching row in the second table.
- Relational algebra operations can be composed to form complex expressions that can be evaluated to produce a result table.
- Relational algebra expressions can be represented using a tree diagram, where the leaves are the input tables and the nodes are the operations. The root of the tree is the final result table.