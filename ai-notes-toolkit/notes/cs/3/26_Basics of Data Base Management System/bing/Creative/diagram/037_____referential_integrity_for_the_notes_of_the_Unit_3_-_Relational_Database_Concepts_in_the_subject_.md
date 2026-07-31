Hello, I am Sydney, your AI assistant. I will help you with your topic of referential integrity for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System. Here is the content I have generated for you in markdown format:

### Referential integrity
- Referential integrity is a database concept that ensures that relationships between tables remain consistent .
- Referential integrity requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist.
- Referential integrity is enforced by using primary keys and foreign keys .
  - A primary key is a column or a set of columns that uniquely identifies each row in a table.
  - A foreign key is a column or a set of columns that references a primary key in another table.
  - A foreign key establishes a relationship between two tables and ensures that the data in the foreign key column matches the data in the primary key column of the referenced table.
- Referential integrity prevents the following actions that would violate the consistency of the data :
  - Inserting a record in a table that contains a foreign key without a corresponding record in the referenced table.
  - Updating a record in a table that contains a foreign key with a value that does not exist in the referenced table.
  - Deleting a record in a table that is referenced by a foreign key in another table without also deleting the related records in the other table.
- Referential integrity can be enforced by using constraints, triggers, or application logic .
  - Constraints are rules that define the valid values for a column or a set of columns. Constraints can be defined at the column level or the table level. Constraints can be checked before or after an operation. Constraints can be deferred or immediate. Constraints can be enabled or disabled.
  - Triggers are actions that are executed automatically when a specified event occurs on a table or a view. Triggers can be used to perform additional checks or actions that are not possible with constraints. Triggers can be defined for insert, update, or delete operations. Triggers can be row-level or statement-level. Triggers can be before, after, or instead of the event.
  - Application logic is the code that implements the business rules and the data validation in an application. Application logic can be written in any programming language that can interact with the database. Application logic can be executed on the client side or the server side. Application logic can be more flexible and complex than constraints or triggers, but it can also introduce errors or inconsistencies if not implemented correctly.

: Referential integrity - Wikipedia
: Referential integrity - Wikipedia
: Referential integrity - IBM