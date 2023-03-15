Hello, I am Sydney, your AI assistant. I can help you with writing basic SQL SELECT statements for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab. Here is some content that you can use for your notes:

### Writing basic SQL SELECT statements

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- A SQL SELECT statement is used to retrieve data from one or more tables or views in a database.
- The basic syntax of a SQL SELECT statement is:

```sql
SELECT column1, column2, ...
FROM table1, table2, ...
WHERE condition1, condition2, ...
ORDER BY column1, column2, ...
GROUP BY column1, column2, ...
HAVING condition1, condition2, ...
```

- The SELECT clause specifies which columns or expressions to return in the result set. You can use * to select all columns from a table or view.
- The FROM clause specifies which tables or views to query data from. You can use joins to combine data from multiple tables or views based on a common column or condition.
- The WHERE clause specifies which rows to filter based on one or more conditions. You can use logical operators such as AND, OR, and NOT to combine multiple conditions.
- The ORDER BY clause specifies how to sort the result set based on one or more columns or expressions. You can use ASC or DESC to specify ascending or descending order.
- The GROUP BY clause specifies how to group the result set based on one or more columns or expressions. You can use aggregate functions such as SUM, AVG, COUNT, MIN, or MAX to calculate summary values for each group.
- The HAVING clause specifies which groups to filter based on one or more conditions. You can use logical operators such as AND, OR, and NOT to combine multiple conditions.

- Here are some examples of SQL SELECT statements using ORACLE /MYSQL:

```sql
-- Select all columns from the EMPLOYEES table
SELECT *
FROM EMPLOYEES;

-- Select the first name, last name, and salary of employees who work in department 10
SELECT FIRST_NAME, LAST_NAME, SALARY
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 10;

-- Select the first name, last name, and job title of employees who earn more than 10000 or less than 3000
SELECT FIRST_NAME, LAST_NAME, JOB_TITLE
FROM EMPLOYEES
WHERE SALARY > 10000 OR SALARY < 3000;

-- Select the first name, last name, and department name of employees who work in IT or Sales
SELECT E.FIRST_NAME, E.LAST_NAME, D.DEPARTMENT_NAME
FROM EMPLOYEES E
JOIN DEPARTMENTS D
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
WHERE D.DEPARTMENT_NAME IN ('IT', 'Sales');

-- Select the average salary of employees by department
SELECT D.DEPARTMENT_NAME, AVG(E.SALARY) AS AVG_SALARY
FROM EMPLOYEES E
JOIN DEPARTMENTS D
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
GROUP BY D.DEPARTMENT_NAME;

-- Select the department name and the number of employees in each department who earn more than 5000
SELECT D.DEPARTMENT_NAME, COUNT(E.EMPLOYEE_ID) AS EMP_COUNT
FROM EMPLOYEES E
JOIN DEPARTMENTS D
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
WHERE E.SALARY > 5000
GROUP BY D.DEPARTMENT_NAME
HAVING COUNT(E.EMPLOYEE_ID) > 1;

-- Select the first name, last name, and salary of employees who earn the highest salary in their department
SELECT E.FIRST_NAME, E.LAST_NAME, E.SALARY
FROM EMPLOYEES E
JOIN (
  SELECT DEPARTMENT_ID, MAX(SALARY) AS MAX_SALARY
  FROM EMPLOYEES
  GROUP BY DEPARTMENT_ID
) M
ON E.DEPARTMENT_ID = M.DEPARTMENT_ID AND E.SALARY = M.MAX_SALARY;
```