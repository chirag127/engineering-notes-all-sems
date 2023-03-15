Hello, I am Sydney, your AI assistant. I can help you with writing basic SQL SELECT statements for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab. Here is some content that you can use for your notes:

### Writing basic SQL SELECT statements

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- A SQL SELECT statement is used to retrieve data from one or more tables or views in a database.
- The basic syntax of a SQL SELECT statement is:

```sql
SELECT column1, column2, ..., columnN
FROM table1, table2, ..., tableN
WHERE condition;
```

- The SELECT clause specifies the columns or expressions that you want to display in the result set. You can use * to select all columns from the tables.
- The FROM clause specifies the tables or views that you want to query data from. You can use aliases to give them short names or to join them with other tables or views.
- The WHERE clause specifies the conditions that filter the rows in the result set. You can use logical operators such as AND, OR, and NOT to combine multiple conditions. You can also use comparison operators such as =, <, >, <=, >=, <>, and LIKE to compare values.

- Here are some examples of basic SQL SELECT statements:

```sql
-- Select all columns and rows from the EMP table
SELECT *
FROM EMP;

-- Select the employee name and salary from the EMP table
SELECT ENAME, SAL
FROM EMP;

-- Select the employee name and salary from the EMP table where the salary is greater than 3000
SELECT ENAME, SAL
FROM EMP
WHERE SAL > 3000;

-- Select the employee name and department number from the EMP table where the department number is either 10 or 20
SELECT ENAME, DEPTNO
FROM EMP
WHERE DEPTNO = 10 OR DEPTNO = 20;

-- Select the employee name and job from the EMP table where the job is not 'MANAGER'
SELECT ENAME, JOB
FROM EMP
WHERE JOB <> 'MANAGER';
```