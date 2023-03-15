### Referential Integrity

- Referential integrity is a property of data stating that all its references are valid.
- In the context of relational databases, it requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist.
- Referential integrity ensures that the one-to-many relationship between tables remain consistent.
- When one table has a foreign key to another table, the concept of referential integrity states that you may not add a record to the table that contains the foreign key unless there is a corresponding record in the linked table.
- Referential integrity also prevents the deletion or modification of a record in the linked table if there are records in the foreign key table that refer to it.
- Referential integrity can be enforced by the database system using constraints, triggers, or cascading actions .
- Constraints are rules that define the valid values for an attribute or a combination of attributes.
- Triggers are procedures that are executed automatically when a specified event occurs, such as inserting, updating, or deleting a record.
- Cascading actions are actions that are performed automatically on the related records when a record in the primary table is modified or deleted.
- Some examples of cascading actions are:
  - Cascade restrict: prevents the modification or deletion of a record in the primary table if there are related records in the foreign key table.
  - Cascade delete: deletes the related records in the foreign key table when a record in the primary table is deleted.
  - Cascade update: updates the foreign key values in the related records when a primary key value in the primary table is modified.
- Referential integrity is important for maintaining the accuracy and consistency of data in a relational database.
- Referential integrity also helps to avoid data anomalies, such as insertion, deletion, or update anomalies, that can occur when data is duplicated or inconsistent across tables.
- Referential integrity also facilitates data integrity checks, data manipulation, and query optimization by the database system.