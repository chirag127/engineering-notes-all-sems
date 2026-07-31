# Referential Integrity

- Referential integrity is a property of data stating that all its references are valid .
- In the context of relational databases, it requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist .
- For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can only contain either null values or values from a parent table's primary key or a candidate key.
- In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table.
- Referential integrity ensures that relationships between tables remain consistent .
- Referential integrity prevents the following problems:
  - Orphan records: records that have a foreign key value that does not match any primary key value in the parent table.
  - Inconsistent data: records that have different values for the same attribute in different tables.
  - Invalid operations: operations that violate the rules of referential integrity, such as deleting a parent record without deleting the related child records, or inserting a child record without a corresponding parent record.
- Referential integrity can be enforced by the following methods:
  - Database constraints: rules that are defined at the table level to specify the conditions for referential integrity, such as primary key, foreign key, unique, not null, and check constraints.
  - Database triggers: procedures that are executed automatically when a certain event occurs, such as insert, update, or delete, to perform actions that maintain referential integrity, such as cascading delete or update.
  - Application logic: code that is written in the application layer to validate the data before sending it to the database, or to handle the errors that occur when referential integrity is violated.