### Referential Integrity

- Referential integrity is a property of data stating that all its references are valid .
- In the context of relational databases, it requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist .
- For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can only contain either null values or values from a parent table's primary key or a candidate key.
- In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table.
- Referential integrity ensures that relationships between tables remain consistent .
- Referential integrity prevents the insertion, update, or deletion of data that would violate the consistency of the relationships.
- Referential integrity can be enforced by using constraints, triggers, or application logic.
- Referential integrity is a type of data integrity, which is a broader concept that encompasses the accuracy, consistency, and validity of data.