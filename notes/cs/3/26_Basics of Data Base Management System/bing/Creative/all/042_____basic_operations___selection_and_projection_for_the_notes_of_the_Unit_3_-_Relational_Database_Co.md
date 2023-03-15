# Basic Operations – Selection and Projection

- Selection and projection are two unary operations in relational algebra that are used to manipulate data in a relational database  .
- Selection operation targets records (rows) or specific entities in a relational database. It filters the rows that satisfy a given condition or predicate .
- Projection operation targets attributes (columns) or specific properties in a relational database. It selects the columns that are specified in the query  .
- In SQL, the SELECT statement combines both selection and projection operations in a single query.
- The syntax of the SELECT statement is as follows:

```sql
SELECT column_list
FROM table_name
WHERE condition;
```

- The column_list specifies the attributes or columns to be projected. The * symbol can be used to select all the columns.
- The table_name specifies the relation or table to be queried.
- The condition specifies the predicate or criteria to be applied for selection. The WHERE clause is optional and can be omitted if no condition is required.
- Some examples of the SELECT statement are:

```sql
-- Select all the columns and rows from the table student
SELECT * FROM student;

-- Select the name and age columns from the table student
SELECT name, age FROM student;

-- Select the name and age columns from the table student where age is greater than 18
SELECT name, age FROM student WHERE age > 18;
```