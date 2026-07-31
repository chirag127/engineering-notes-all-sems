Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 2 - Relational data Model and Language in the subject of Database Management System. Here is some content in markdown format that you can use for your notes.

### Tables

- A table is a collection of data organized in rows and columns.
- A table is also called a relation, because it represents a set of related data.
- A table has a name, which is unique within a database.
- A table has a schema, which defines the structure and properties of the data in the table.
- A table schema consists of a list of attributes (or columns), each with a name, a data type, and optionally some constraints.
- A table can have a primary key, which is a set of one or more attributes that uniquely identify each row in the table.
- A table can have foreign keys, which are sets of attributes that reference the primary keys of other tables, to establish relationships between tables.
- A table can have indexes, which are data structures that improve the performance of queries on the table.
- A table can have triggers, which are actions that are executed automatically when certain events occur on the table.
- A table can have views, which are virtual tables that are derived from one or more base tables, and provide a different perspective of the data.

Some examples of tables are:

| StudentID | Name | Major | GPA |
|-----------|------|-------|-----|
| 1001      | Alice| CS    | 3.8 |
| 1002      | Bob  | Math  | 3.5 |
| 1003      | Carol| CS    | 3.9 |
| 1004      | David| Art   | 3.2 |

This table is called Student, and has four attributes: StudentID, Name, Major, and GPA. The primary key is StudentID, which uniquely identifies each student. The data type of StudentID is integer, the data type of Name is string, the data type of Major is string, and the data type of GPA is decimal.

| CourseID | Title | Instructor | Credits |
|----------|-------|------------|---------|
| CS101    | Intro to CS | Smith     | 3       |
| CS102    | Data Structures | Jones    | 4       |
| CS103    | Algorithms | Lee       | 4       |
| MATH101  | Calculus I | Chen      | 3       |

This table is called Course, and has four attributes: CourseID, Title, Instructor, and Credits. The primary key is CourseID, which uniquely identifies each course. The data type of CourseID is string, the data type of Title is string, the data type of Instructor is string, and the data type of Credits is integer.

| StudentID | CourseID | Grade |
|-----------|----------|-------|
| 1001      | CS101    | A     |
| 1001      | CS102    | B     |
| 1002      | CS101    | C     |
| 1002      | MATH101  | B     |
| 1003      | CS102    | A     |
| 1003      | CS103    | A     |
| 1004      | CS101    | D     |
| 1004      | MATH101  | C     |

This table is called Enrollment, and has three attributes: StudentID, CourseID, and Grade. The primary key is a combination of StudentID and CourseID, which uniquely identifies each enrollment. The data type of StudentID is integer, the data type of CourseID is string, and the data type of Grade is string. The StudentID attribute is a foreign key that references the StudentID attribute of the Student table, and the CourseID attribute is a foreign key that references the CourseID attribute of the Course table. These foreign keys establish the relationships between the tables.