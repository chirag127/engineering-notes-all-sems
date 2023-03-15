# Referential Integrity

- Referential integrity is a database concept that ensures that relationships between tables remain consistent .
- Referential integrity requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist.
- Referential integrity is enforced by using primary keys and foreign keys .
- A primary key is a column or a set of columns that uniquely identifies each row in a table .
- A foreign key is a column or a set of columns that references a primary key in another table .
- Referential integrity constraints prevent the following actions :
  - Inserting a record in a table that contains a foreign key without a corresponding record in the referenced table.
  - Updating a primary key value in a table that is referenced by a foreign key in another table without updating the foreign key value accordingly.
  - Deleting a record in a table that is referenced by a foreign key in another table without deleting the referencing record or setting the foreign key value to null.
- Referential integrity ensures data integrity, consistency, and accuracy in a relational database .