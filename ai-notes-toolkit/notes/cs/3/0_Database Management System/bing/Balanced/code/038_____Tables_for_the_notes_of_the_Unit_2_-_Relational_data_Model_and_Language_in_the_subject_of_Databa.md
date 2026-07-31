Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of tables for the unit 2 - Relational data model and language in the subject of database management system.

### Tables
- A table is a collection of data organized in rows and columns.
- A table is also called a relation, because it represents a set of related data.
- A table has a name, which is unique within a database.
- A table has a schema, which defines the structure and properties of the table.
- A table schema consists of a list of attributes (or columns), each with a name, a data type, and optionally, some constraints.
- A table schema also defines a primary key, which is a set of attributes that uniquely identify each row in the table.
- A table can have one or more foreign keys, which are sets of attributes that reference the primary key of another table.
- A table can have zero or more rows, which are also called tuples or records.
- A row contains a value for each attribute in the table schema.
- A row can be inserted, updated, deleted, or queried from a table using a relational language, such as SQL.

Here is an example of a table schema and some rows:

| StudentID | Name | Major | GPA |
|-----------|------|-------|-----|
| 123       | Alice| CS    | 3.8 |
| 456       | Bob  | Math  | 3.5 |
| 789       | Carol| CS    | 4.0 |

- The table name is Student.
- The table schema has four attributes: StudentID, Name, Major, and GPA.
- The primary key is StudentID, which is unique for each student.
- The data type of StudentID is integer, the data type of Name is string, the data type of Major is string, and the data type of GPA is decimal.
- The table has three rows, each representing a student and their information.