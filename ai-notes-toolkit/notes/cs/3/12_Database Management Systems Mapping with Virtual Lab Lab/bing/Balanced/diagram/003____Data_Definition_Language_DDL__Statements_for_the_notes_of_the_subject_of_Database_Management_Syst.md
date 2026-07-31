## Data Definition Language(DDL) Statements

- Data Definition Language (DDL) is a group of SQL statements that you can execute to manage database objects, such as tables, views, functions, and policies   .
- Using DDL statements, you can perform powerful commands in your database such as creating, modifying, and dropping objects   .
- DDL commands are usually executed in a SQL browser or stored procedure.
- Some common DDL commands are:
  - CREATE: to create a new database object   .
  - ALTER: to modify an existing database object   .
  - DROP: to delete a database object   .
  - RENAME: to change the name of a database object .
  - TRUNCATE: to remove all the data from a table .
- DDL statements are different from Data Manipulation Language (DML) statements, which are used to insert, update, and delete data from database objects .
- DDL statements are also different from Data Control Language (DCL) statements, which are used to grant and revoke permissions and roles to users and groups .
- Here is an example of a DDL statement that creates a table named `students` with four columns: `id`, `name`, `age`, and `grade` :

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT CHECK (age > 0),
  grade CHAR(1) CHECK (grade IN ('A', 'B', 'C', 'D', 'F'))
);
```