Hello, I am Sydney, your AI assistant. I can help you with your study material for Database Management System. Here are some notes on the topic of Primary Key for Unit 1 - Introduction.

# Primary Key

- A primary key is a column or a set of columns that uniquely identifies each row in a table.
- A primary key is a constraint that enforces the uniqueness and non-nullability of the values in the key column(s).
- A primary key can be defined at the time of table creation using the `PRIMARY KEY` keyword, or after the table is created using the `ALTER TABLE` statement.
- A table can have only one primary key, but the primary key can consist of multiple columns, forming a composite key.
- A primary key can be referenced by other tables to establish a relationship between them, using the `FOREIGN KEY` constraint.
- A primary key can also be used to create indexes on the table, to improve the performance of queries that use the key column(s) in the `WHERE` clause or the `JOIN` condition.

## Example

- Consider the following table that stores the details of students in a college.

| Student_ID | Name | Email | Phone | Major |
|------------|------|-------|-------|-------|
| 101        | Alice | alice@gmail.com | 1234567890 | CS |
| 102        | Bob | bob@yahoo.com | 2345678901 | Math |
| 103        | Charlie | charlie@hotmail.com | 3456789012 | Physics |
| 104        | David | david@gmail.com | 4567890123 | CS |

- In this table, the `Student_ID` column can be chosen as the primary key, as it uniquely identifies each student and is not null.
- The primary key can be defined as follows:

```sql
CREATE TABLE Students (
  Student_ID INT PRIMARY KEY,
  Name VARCHAR(50) NOT NULL,
  Email VARCHAR(50) UNIQUE,
  Phone VARCHAR(10) UNIQUE,
  Major VARCHAR(20)
);
```

- Alternatively, the primary key can be defined after the table is created as follows:

```sql
ALTER TABLE Students
ADD PRIMARY KEY (Student_ID);
```

- The primary key can be used to reference the `Students` table from another table, such as the `Courses` table, using the `FOREIGN KEY` constraint. For example:

```sql
CREATE TABLE Courses (
  Course_ID INT PRIMARY KEY,
  Course_Name VARCHAR(50) NOT NULL,
  Instructor VARCHAR(50) NOT NULL,
  Student_ID INT,
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID)
);
```

- The primary key can also be used to create an index on the `Students` table, to speed up the queries that use the `Student_ID` column. For example:

```sql
CREATE INDEX idx_students ON Students(Student_ID);
```

- This index can help to find the details of a student with a given ID faster, as the database can use the index to locate the row instead of scanning the whole table. For example:

```sql
SELECT Name, Email, Major FROM Students WHERE Student_ID = 101;
```