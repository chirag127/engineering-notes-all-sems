### Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Aggregate functions are functions that operate on a set of rows and return a single value for each group of rows. They are commonly used to perform calculations, such as sum, count, average, minimum, and maximum, on numeric or date values. 
- Aggregate functions can be used in the select list and in the order by and having clauses of a select statement. They can also be used as window functions, which apply to each row of a partition or result set.
- Group functions are a type of aggregate functions that divide the rows of a table or view into groups and return a single value for each group. Group functions are often used with the group by clause, which specifies the columns or expressions to group by. The group by clause also allows the use of grouping sets, rollup, and cube operators, which provide different levels of aggregation. 
- Oracle and MySQL support many common aggregate and group functions, such as sum, count, avg, min, max, stddev, variance, etc. However, there are some differences and limitations in their syntax and behavior. For example, Oracle supports the listagg function, which concatenates the values of a column for each group, while MySQL does not have a direct equivalent, but can use json functions or group_concat function with some limitations.  
- Some examples of using aggregate and group functions in Oracle and MySQL are:

  - To calculate the total salary of all employees in each department:

    ```sql
    -- Oracle and MySQL
    select deptno, sum(sal) as total_salary
    from emp
    group by deptno;
    ```

  - To count the number of employees in each job category and sort them by descending order:

    ```sql
    -- Oracle and MySQL
    select job, count(*) as emp_count
    from emp
    group by job
    order by emp_count desc;
    ```

  - To find the average salary and the highest salary of each department, and also the grand total and maximum of all salaries:

    ```sql
    -- Oracle
    select deptno, avg(sal) as avg_salary, max(sal) as max_salary
    from emp
    group by rollup(deptno);

    -- MySQL
    select deptno, avg(sal) as avg_salary, max(sal) as max_salary
    from emp
    group by deptno with rollup;
    ```

  - To list the names of all employees in each department, separated by commas:

    ```sql
    -- Oracle
    select deptno, listagg(ename, ',') within group (order by ename) as emp_names
    from emp
    group by deptno;

    -- MySQL
    select deptno, group_concat(ename order by ename separator ',') as emp_names
    from emp
    group by deptno;
    ```