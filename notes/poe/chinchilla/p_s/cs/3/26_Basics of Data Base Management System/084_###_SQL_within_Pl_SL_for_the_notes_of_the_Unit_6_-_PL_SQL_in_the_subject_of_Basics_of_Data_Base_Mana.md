### SQL within PL/SQL

Structured Query Language (SQL) is a powerful language used to manage and manipulate data in a relational database. In PL/SQL, SQL statements can be embedded within procedural code, allowing for more complex and powerful database operations.

#### Syntax

To embed SQL within PL/SQL, the SQL statement must be enclosed in quotes and preceded by the keyword `EXECUTE IMMEDIATE`. For example:

```
EXECUTE IMMEDIATE 'SELECT * FROM employees WHERE department_id = :dept_id'
   INTO emp_rec
   USING dept_id;
```

The `INTO` clause is used to retrieve the results of the query and store them in a variable, while the `USING` clause is used to pass in any parameters to the query.

#### Advantages

- SQL within PL/SQL allows for more complex and powerful database operations than can be achieved with SQL alone.
- It allows for better integration of database operations with procedural code.
- It can improve performance by reducing the number of round-trips between the database and application.

#### Disadvantages

- SQL within PL/SQL can be more difficult to debug than SQL alone.
- It can make code more complex and difficult to read.
- It may not be necessary for simpler database operations.

#### Example

Here is an example of using SQL within PL/SQL to update a table based on a query:

```
DECLARE
   v_dept_id NUMBER := 10;
   v_salary NUMBER;
BEGIN
   EXECUTE IMMEDIATE 'SELECT AVG(salary) FROM employees WHERE department_id = :dept_id'
      INTO v_salary
      USING v_dept_id;
   EXECUTE IMMEDIATE 'UPDATE departments SET avg_salary = :salary WHERE department_id = :dept_id'
      USING v_salary, v_dept_id;
END;
```

This code calculates the average salary for employees in department 10, and then updates the `avg_salary` column in the `departments` table with that value.

#### Applications

SQL within PL/SQL can be used in a variety of applications, including:

- Data analysis and reporting
- Data migration and integration
- ETL (Extract, Transform, Load) processes
- Complex data manipulation and calculations.