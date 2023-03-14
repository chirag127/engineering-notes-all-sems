#### Sorting and aggregating in Hive

- Sorting and aggregating are common operations in data analysis that involve rearranging and summarizing data based on certain criteria.
- Hive supports two types of sorting: **order by** and **sort by**.
  - **Order by** sorts the entire data set globally and returns the top N rows based on the limit clause. It uses only one reducer, which can be slow and memory-intensive for large data sets.
  - **Sort by** sorts the data locally within each reducer partition and returns all the rows. It can use multiple reducers, which can improve performance and scalability for large data sets. However, the global order of the data is not guaranteed.
- Hive also supports two types of aggregating: **group by** and **distinct**.
  - **Group by** groups the data by one or more columns and applies an aggregate function (such as sum, count, avg, min, max, etc.) to each group. It can use multiple reducers, which can improve performance and scalability for large data sets. However, the order of the groups is not guaranteed.
  - **Distinct** eliminates duplicate values from one or more columns and returns the unique values. It can use multiple reducers, which can improve performance and scalability for large data sets. However, the order of the values is not guaranteed.
- Here are some examples of sorting and aggregating in Hive:

  - To sort the data by salary in descending order and return the top 10 rows, use order by with limit:

  ```sql
  select * from employee order by salary desc limit 10;
  ```

  - To sort the data by department and salary in ascending order and return all the rows, use sort by:

  ```sql
  select * from employee sort by department, salary;
  ```

  - To group the data by department and calculate the average salary for each department, use group by with avg:

  ```sql
  select department, avg(salary) as avg_salary from employee group by department;
  ```

  - To find the distinct values of department and gender from the employee table, use distinct:

  ```sql
  select distinct department, gender from employee;
  ```

- Some mnemonics and learning tricks for sorting and aggregating in Hive are:

  - Order by orders the data globally and returns the top rows. Think of ordering a pizza and getting the first slice.
  - Sort by sorts the data locally and returns all the rows. Think of sorting your clothes by color and putting them in different drawers.
  - Group by groups the data by columns and applies an aggregate function. Think of grouping your friends by hobbies and finding the average age of each group.
  - Distinct eliminates duplicate values and returns the unique values. Think of finding the distinct flavors of ice cream in your freezer.