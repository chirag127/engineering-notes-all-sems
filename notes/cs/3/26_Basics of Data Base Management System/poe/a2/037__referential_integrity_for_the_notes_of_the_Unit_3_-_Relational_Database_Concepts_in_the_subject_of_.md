 Here are the notes on Referential Integrity for Unit 3 - Relational Database Concepts:

### Referential Integrity

- Referential integrity is a relational database concept that ensures that relationships between data in tables remain consistent.
- It means that foreign key values must match primary key values of the rows they reference.
- For example, if a table `Orders` has a `CustomerID` column that references the `ID` column of the `Customers` table, then we must ensure that the `CustomerID` value for each order exists in the `Customers` table.
- Otherwise, the relationship is broken and referential integrity is violated.
- This can be ensured through constraints, like foreign key constraints. The database enforces referential integrity and prevents invalid data from being entered.
- Benefits:
    - Data consistency and accuracy is maintained.
    - Unrelated data is not connected.
    - Database optimization is possible.
- Challenges:
    - Deletion of referenced data must handle the foreign keys that point to it. Either the reference must be removed (cascading deletion) or disallowed (restriction).
    - Insertion/update of referenced data must not break existing references.

[No external links or emojis included as per the guidelines.]