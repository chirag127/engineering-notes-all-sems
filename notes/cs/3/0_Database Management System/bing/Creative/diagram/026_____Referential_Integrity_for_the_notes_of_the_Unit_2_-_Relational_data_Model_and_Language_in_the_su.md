### Referential Integrity

- Referential integrity is a property of data stating that all its references are valid .
- In the context of relational databases, it requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist .
- For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can only contain either null values or values from a parent table's primary key or a candidate key .
- In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table .
- Referential integrity ensures that relationships between tables remain consistent and that data is not corrupted or orphaned .
- Referential integrity can be enforced by using constraints, triggers, or application logic .
- Referential integrity can also be implemented by using cascading actions, such as cascade restrict, cascade delete, or cascade update.
- Cascade restrict prevents any operation that would violate referential integrity, such as deleting or updating a parent record that has dependent child records.
- Cascade delete automatically deletes all the child records that reference a parent record when the parent record is deleted.
- Cascade update automatically updates all the child records that reference a parent record when the parent record is updated.
- Referential integrity is an important aspect of relational data modeling and design, as it ensures data integrity, consistency, and quality  .