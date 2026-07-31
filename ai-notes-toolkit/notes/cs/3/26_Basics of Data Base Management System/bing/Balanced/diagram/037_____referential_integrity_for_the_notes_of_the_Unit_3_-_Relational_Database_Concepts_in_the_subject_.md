### Referential integrity

- Referential integrity is a database concept that ensures that relationships between tables remain consistent .
- It requires that if a value of one attribute (column) of a table references a value of another attribute (either in the same or a different table), then the referenced value must exist.
- It is achieved by having the foreign key (in the associated table) reference a primary key value (in the primary or parent table).
- It prevents the insertion, update, or deletion of data that would violate the consistency of the relationships.
- It can be enforced by using constraints, triggers, or application logic.
- It ensures data integrity, avoids data anomalies, and preserves the logical meaning of the data .