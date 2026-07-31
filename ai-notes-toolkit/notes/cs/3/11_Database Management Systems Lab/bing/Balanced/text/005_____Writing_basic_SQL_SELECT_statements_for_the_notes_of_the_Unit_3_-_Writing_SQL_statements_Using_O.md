### Writing basic SQL SELECT statements for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- A SQL SELECT statement is used to retrieve data from one or more tables or views in a database.
- The basic syntax of a SQL SELECT statement is:

```sql
SELECT column_list
FROM table_list
WHERE condition;
```

- The column_list specifies the columns or expressions to be displayed in the result set. It can be a single column, multiple columns separated by commas, or a wildcard character (*) to select all columns.
- The table_list specifies the tables or views to be queried. It can be a single table or view, or multiple tables or views joined by join operators.
- The condition specifies the criteria for filtering the rows in the result set. It can be a single condition or a combination of conditions using logical operators such as AND, OR, and NOT.
- Some examples of SQL SELECT statements are:

```sql
-- Select all columns and rows from the EMPLOYEES table
SELECT *
FROM EMPLOYEES;

-- Select the first name, last name, and salary of employees who work in department 10
SELECT FIRST_NAME, LAST_NAME, SALARY
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 10;

-- Select the name and phone number of customers who live in New York or California
SELECT NAME, PHONE
FROM CUSTOMERS
WHERE STATE = 'NY' OR STATE = 'CA';
```