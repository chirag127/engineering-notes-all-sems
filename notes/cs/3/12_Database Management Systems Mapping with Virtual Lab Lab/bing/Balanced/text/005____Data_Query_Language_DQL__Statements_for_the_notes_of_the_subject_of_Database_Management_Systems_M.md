## Data Query Language(DQL) Statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Data Query Language (DQL) is a component of SQL (Structured Query Language) that is used to retrieve and manipulate data in a relational database management system  .
- DQL statements are used to perform queries on the data within schema objects, such as tables, views, or indexes .
- The purpose of DQL is to get some schema relation based on the query passed to it, and to impose order upon it.
- The most common DQL statement is the SELECT statement, which allows you to select data from one or more tables or views, and apply filters, joins, aggregations, or sorting to the result set  .
- Some examples of DQL statements are:

  - SELECT * FROM employees; -- This statement selects all the data from the employees table.
  - SELECT name, salary FROM employees WHERE department = 'Sales'; -- This statement selects the name and salary columns from the employees table, where the department is 'Sales'.
  - SELECT e.name, e.salary, d.name AS department FROM employees e JOIN departments d ON e.department_id = d.id ORDER BY e.salary DESC; -- This statement selects the name and salary of the employees, and the name of their department, from the employees and departments tables, using a join condition on the department_id column, and sorts the result by salary in descending order.
  - SELECT AVG(salary) AS average_salary FROM employees; -- This statement calculates the average salary of the employees, and assigns it an alias of average_salary.

- DQL statements can be executed using various tools, such as command-line interfaces, graphical user interfaces, or web applications, depending on the database system and the user preference .
- DQL statements can also be embedded in other programming languages, such as Java, Python, or PHP, to interact with the database from the application code .