# Referential Integrity

- Referential integrity is a property of data stating that all its references are valid.
- In the context of relational databases, it requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist.
- For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can only contain either null values or values from a parent table's primary key or a candidate key.
- In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table.
- Referential integrity ensures the accuracy and consistency of data within a relationship.
- Referential integrity also prevents the deletion or modification of data that is referenced by other data.
- To enforce referential integrity, relational database systems use constraints, triggers, or cascading actions .
- Constraints are rules that restrict the values that can be inserted, updated, or deleted in a table.
- Triggers are procedures that are executed automatically when a specified event occurs, such as inserting, updating, or deleting data.
- Cascading actions are actions that are performed automatically on the related data when a primary key value is modified or deleted .
- For example, if a primary key value is deleted, the cascading action can be to delete all the related records in the associated table (cascade delete), or to set their foreign key values to null (set null) .
- Similarly, if a primary key value is updated, the cascading action can be to update all the related records in the associated table with the new value (cascade update), or to set their foreign key values to null (set null) .
- Referential integrity is an important aspect of relational data modeling, as it ensures the validity and consistency of the data and the relationships between tables .