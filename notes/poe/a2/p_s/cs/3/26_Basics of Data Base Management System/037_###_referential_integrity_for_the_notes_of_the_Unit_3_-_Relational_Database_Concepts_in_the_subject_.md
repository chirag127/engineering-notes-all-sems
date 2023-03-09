 Here is the content in markdown format for the topic ### Referential Integrity for the notes of Unit 3 - Relational Database Concepts:

### Referential Integrity

- Referential integrity is a type of constraint that ensures that the relationship between two data tables remains consistent.
- It means that if a table has a foreign key that references a primary key of another table, then the foreign key value must either match an existing primary key value, or be null.
- In other words, the foreign key column of one table must contain only values that exist in the primary key of the other table, or contain null values.
- This enforces a link between the data in two tables, and ensures that the connection makes logical sense.
- For example, if table "Orders" has a foreign key that references the "Customers" table, then we cannot add an order for a customer that does not exist in the Customers table. That would break the referential integrity.
- Advantages:
    - Prevents invalid data and inconsistent connections between tables.
    - Ensures data integrity and accuracy.
- Disadvantages:
    - Additional overhead to maintain relationships.
    - Deletion/updation of data may get complicated due to dependence on other tables.
- Examples:
    - Orders table with foreign key CustomerID referencing primary key of Customers table. Only existing customer IDs can be added to Orders table.
    - Employees table with foreign key DepartmentID referencing primary key of Departments table. Employees must belong to an existing department.
- Applications: Widely used in relational databases to establish and maintain relationships between data tables and ensure accuracy.

[Diagrams and code snippets can be added here to aid learning]