### Aggregate Functions for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Aggregate functions are functions that take a collection of values as input and return a single value as output.
- Aggregate functions are used to perform calculations or selections on groups of values, such as finding the average, sum, minimum, maximum, or count of values in a set.
- Aggregate functions can be applied to any relation or expression that produces a relation in the relational data model.
- Aggregate functions can be combined with grouping and sorting operations to generate summaries or statistics on the data.
- Some examples of aggregate functions are:

  - `avg`: returns the average value of a numeric column or expression.
  - `min`: returns the minimum value of a column or expression.
  - `max`: returns the maximum value of a column or expression.
  - `sum`: returns the sum of values of a numeric column or expression.
  - `count`: returns the number of values or rows in a column or relation.

- Some examples of queries using aggregate functions in relational algebra are:

  - Find the average salary of employees: `avg(πsalary(Employees))`
  - Find the number of employees in each department: `γdepartment,count(*)→num_emp(πdepartment,employee_id(Employees))`
  - Find the total sales amount of each product: `γproduct_id,sum(amount)→total_sales(σstatus='sold'(Orders))`