### Referential Integrity

- Referential integrity is a property of a relational database that ensures that the data in the tables is consistent and valid.
- Referential integrity is based on the concept of foreign keys, which are columns in one table that reference the primary key of another table.
- Referential integrity rules prevent the following actions:
  - Inserting a record in a child table that does not have a corresponding record in the parent table.
  - Updating a record in the parent table that would make it incompatible with the records in the child table.
  - Deleting a record in the parent table that has related records in the child table.
- Referential integrity can be enforced by using constraints, triggers, or application logic.
- Referential integrity helps to maintain the accuracy, integrity, and quality of the data in the database.