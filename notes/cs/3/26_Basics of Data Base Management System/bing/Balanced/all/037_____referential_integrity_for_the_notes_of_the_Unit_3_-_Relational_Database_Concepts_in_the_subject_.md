# Referential Integrity

- Referential integrity is a property of relational database that ensures the consistency and validity of the data across different tables.
- Referential integrity is enforced by using foreign keys, which are columns in one table that reference the primary key of another table.
- A foreign key can either have a matching value in the referenced table, or be null (meaning no value).
- Referential integrity rules prevent the following actions that would violate the consistency of the data:
  - Inserting a record in a table with a foreign key that does not exist in the referenced table.
  - Updating a record in a table with a foreign key that would make it not match any value in the referenced table.
  - Deleting a record in a table that is referenced by a foreign key in another table, unless the foreign key is set to null or cascaded.
- Referential integrity can be enforced by the database system using constraints, triggers, or stored procedures.
- Referential integrity can also be implemented by the application logic using transactions, validations, or error handling.