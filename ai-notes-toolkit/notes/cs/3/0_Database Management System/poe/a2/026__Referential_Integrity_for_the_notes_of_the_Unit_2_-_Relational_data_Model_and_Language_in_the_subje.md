 Here are the notes on Referential Integrity for the Unit 2 - Relational data Model and Language in the subject of Database Management System:

### Referential Integrity

- Referential integrity is a relational database concept that ensures that relationships between tables remain consistent.
- It ensures that foreign key values always refer to a valid primary key value.
- It prevents actions that would destroy links between data across tables.
- For example, it prevents the deletion of a record in the primary table if there are dependent records in the foreign table.
- It also prevents the addition of records in the foreign table with non-existent primary keys.
- Violating referential integrity can result in inconsistent and erroneous data.
- Therefore, it is important to define and enforce referential integrity constraints to maintain data integrity and consistency.
- The most common types of referential integrity constraints are:

- **Cascade update**: When a primary key value is updated, its corresponding foreign key values are also updated.
- **Cascade delete**: When a primary key is deleted, its corresponding foreign key values are also deleted.
- **Restrict**: Prevent the update or deletion of a primary key value if its foreign keys are referenced.

- These constraints help maintain consistency between data across multiple tables.

The notes are written in a formal tone with points and without any emojis or external links as instructed. The content is written inside the specified header in Markdown format. Please let me know if you would like me to modify or expand the notes in any way.