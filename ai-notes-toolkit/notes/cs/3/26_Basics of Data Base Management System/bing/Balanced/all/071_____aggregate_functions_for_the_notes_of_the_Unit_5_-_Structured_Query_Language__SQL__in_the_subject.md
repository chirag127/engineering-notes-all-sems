# Aggregate Functions

- Aggregate functions are SQL functions that perform calculations on a set of values and return a single value.
- Aggregate functions can be used in the select list or the having clause of a select statement.
- Aggregate functions ignore null values in the input set, except for the count function, which counts all rows.
- Aggregate functions can be used with the group by clause to group the input set by one or more columns and apply the function to each group.
- Some common aggregate functions are:

  - **avg**: returns the average of the numeric values in the input set.
  - **count**: returns the number of rows in the input set, or the number of rows with non-null values in a specific column.
  - **max**: returns the maximum value in the input set, or the maximum value of a specific column.
  - **min**: returns the minimum value in the input set, or the minimum value of a specific column.
  - **sum**: returns the sum of the numeric values in the input set, or the sum of the numeric values of a specific column.
  - **string_agg**: returns a string that concatenates the values of a string column in the input set, separated by a specified delimiter.

- Example of using aggregate functions:

  - To find the average, minimum, and maximum salary of all employees in the employees table, use the following query:

    ```sql
    select avg(salary) as average_salary, min(salary) as minimum_salary, max(salary) as maximum_salary
    from employees;
    ```

  - To find the number of employees in each department, use the following query:

    ```sql
    select department_id, count(*) as employee_count
    from employees
    group by department_id;
    ```

  - To find the total salary of each department, use the following query:

    ```sql
    select department_id, sum(salary) as total_salary
    from employees
    group by department_id;
    ```

  - To find the names of the employees who have the highest salary in each department, use the following query:

    ```sql
    select e.name, e.department_id, e.salary
    from employees e
    join (
      select department_id, max(salary) as max_salary
      from employees
      group by department_id
    ) m
    on e.department_id = m.department_id and e.salary = m.max_salary;
    ```