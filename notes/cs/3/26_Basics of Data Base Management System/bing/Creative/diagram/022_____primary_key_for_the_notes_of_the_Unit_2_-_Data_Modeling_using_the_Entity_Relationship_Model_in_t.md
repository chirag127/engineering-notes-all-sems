Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of primary key for the unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System.

### Primary Key
- A primary key is a column or a set of columns that uniquely identifies each row in a table.
- A primary key must satisfy the following properties:
  - It must not contain null values. This is called the entity integrity constraint.
  - It must have a unique value for each row. This is called the key uniqueness constraint.
  - It must be minimal, meaning that no subset of the columns can satisfy the uniqueness constraint. This is called the key irreducibility constraint.
- A primary key can be either simple or composite. A simple primary key consists of a single column, while a composite primary key consists of two or more columns.
- A primary key can be either natural or surrogate. A natural primary key is based on some attribute or combination of attributes that are inherent to the entity, such as a student ID or a passport number. A surrogate primary key is an artificial attribute that is assigned by the system, such as a sequential number or a UUID.
- A primary key can be either explicit or implicit. An explicit primary key is declared by the user or the database designer, while an implicit primary key is inferred by the system based on some rules or conventions, such as the first column or the column with the smallest data type.
- A primary key can be either single or alternate. A single primary key is the only primary key for a table, while an alternate primary key is one of the possible primary keys for a table. An alternate primary key can be used as a foreign key in another table to establish a relationship.
- A primary key can be either candidate or non-candidate. A candidate primary key is a column or a set of columns that satisfies the properties of a primary key, but is not chosen as the primary key. A non-candidate primary key is a column or a set of columns that does not satisfy the properties of a primary key.
- A primary key can be either primary or foreign. A primary key is a primary key in its own table, while a foreign key is a primary key in another table that is used to reference the related rows. A foreign key must match the primary key of the referenced table in terms of number, type, and order of columns. A foreign key can also have a referential integrity constraint, which specifies the actions to be taken when the referenced rows are updated or deleted.