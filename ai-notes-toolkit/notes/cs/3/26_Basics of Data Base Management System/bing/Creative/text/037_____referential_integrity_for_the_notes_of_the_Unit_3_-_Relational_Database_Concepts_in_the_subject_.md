### Referential integrity

- Referential integrity is a database concept that ensures that relationships between tables remain consistent .
- It requires that if a value of one attribute (column) of a table references a value of another attribute (either in the same or a different table), then the referenced value must exist.
- It prevents the insertion, update, or deletion of data that would violate the consistency of the relationships .
- It is enforced by using primary keys and foreign keys.
- A primary key is a column or a set of columns that uniquely identifies a row in a table.
- A foreign key is a column or a set of columns that references a primary key in another table.
- For example, consider the following two tables:

| StudentID | Name | Major |
|-----------|------|-------|
| 1001      | Alice| CS    |
| 1002      | Bob  | Math  |
| 1003      | Carol| CS    |

| CourseID | CourseName | Instructor | StudentID |
|----------|------------|------------|-----------|
| CS101    | Programming| Smith      | 1001      |
| CS102    | Data Struct| Jones      | 1001      |
| CS102    | Data Struct| Jones      | 1003      |
| Math101  | Calculus   | Lee        | 1002      |

- In this example, StudentID is the primary key of the first table and a foreign key of the second table.
- Referential integrity ensures that every value of StudentID in the second table matches a value of StudentID in the first table.
- This means that we cannot insert a row in the second table with a StudentID that does not exist in the first table.
- Similarly, we cannot update or delete a row in the first table if it is referenced by a row in the second table.
- Referential integrity helps to maintain the accuracy and consistency of data in a relational database.