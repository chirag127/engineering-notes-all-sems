### Primary Key

- A primary key is a column or a set of columns that uniquely identifies each row in a table.
- A primary key must satisfy the following properties:
  - It must not contain null values. This is also known as the entity integrity constraint.
  - It must have a unique value for each row. This is also known as the key uniqueness constraint.
  - It must be minimal, meaning that no subset of the columns can satisfy the above properties.
- A primary key can be either simple or composite. A simple primary key consists of a single column, while a composite primary key consists of two or more columns.
- A primary key can be either natural or surrogate. A natural primary key is based on a meaningful attribute of the entity, such as a student ID or a social security number. A surrogate primary key is an artificial attribute that is assigned by the system, such as a sequential number or a UUID.
- A primary key can be either declared or inferred. A declared primary key is explicitly specified by the database designer or the user, using a constraint or a keyword. An inferred primary key is implicitly derived from the data or the business rules, without being explicitly specified.
- A primary key serves as a reference for other tables that want to establish a relationship with the table. A foreign key is a column or a set of columns in another table that refers to the primary key of the table. A foreign key must match the values and the data type of the primary key it references. A foreign key can also have null values, unless it is part of a primary key of its own table.