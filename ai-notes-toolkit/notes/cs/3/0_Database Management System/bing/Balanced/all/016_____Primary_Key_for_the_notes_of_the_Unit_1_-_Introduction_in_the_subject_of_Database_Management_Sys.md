# Primary Key

- A primary key is a column or a set of columns that uniquely identifies each row in a table.
- A primary key must satisfy the following properties:
  - It must not contain null values. This is called the **not null** constraint.
  - It must have a unique value for each row. This is called the **unique** constraint.
  - It must be minimal, meaning that no subset of the columns can satisfy the uniqueness property. This is called the **irreducibility** property.
- A primary key can be either **simple** or **composite**. A simple primary key consists of a single column, while a composite primary key consists of two or more columns.
- A primary key can be either **natural** or **surrogate**. A natural primary key is based on a column or a set of columns that have a logical meaning in the domain of the table, such as a student ID or a product code. A surrogate primary key is based on a column or a set of columns that have no logical meaning in the domain of the table, such as a sequential number or a random string.
- A primary key serves two main purposes in a database:
  - It ensures the **integrity** of the data, by preventing duplicate rows and null values.
  - It enables the **referential** integrity of the data, by allowing other tables to reference the rows in the table using foreign keys.