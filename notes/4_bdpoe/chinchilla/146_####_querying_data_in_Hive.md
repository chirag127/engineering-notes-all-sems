#### Querying Data in Hive

Apache Hive is a data warehouse infrastructure that provides a SQL-like interface to query data stored in Hadoop Distributed File System (HDFS). It is built on top of Hadoop and allows users to perform data analysis and processing tasks using SQL-like queries. In this section, we will discuss how to query data in Hive.

##### Basic Query Syntax

The basic syntax for querying data in Hive is as follows:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition(s)
GROUP BY column1, column2, ...
HAVING condition(s)
ORDER BY column1, column2, ... [ASC|DESC];
```

Here, `SELECT` is used to select columns from a table, `FROM` is used to specify the table name, `WHERE` is used to filter the rows based on specific conditions, `GROUP BY` is used to group the rows based on one or more columns, `HAVING` is used to filter the groups based on specific conditions, and `ORDER BY` is used to sort the results based on one or more columns.

##### Examples

Let's consider some examples to understand how to query data in Hive:

###### Example 1: Selecting Columns

To select specific columns from a table, we can use the `SELECT` statement as follows:

```
SELECT name, age
FROM employees;
```

This will select the `name` and `age` columns from the `employees` table.

###### Example 2: Filtering Rows

To filter the rows based on specific conditions, we can use the `WHERE` clause as follows:

```
SELECT name, age
FROM employees
WHERE age > 30;
```

This will select the `name` and `age` columns from the `employees` table where the `age` is greater than 30.

###### Example 3: Grouping Rows

To group the rows based on one or more columns, we can use the `GROUP BY` clause as follows:

```
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

This will group the rows in the `employees` table by `department` and calculate the average salary for each department.

###### Example 4: Sorting Results

To sort the results based on one or more columns, we can use the `ORDER BY` clause as follows:

```
SELECT name, age
FROM employees
ORDER BY age DESC;
```

This will select the `name` and `age` columns from the `employees` table and sort the results in descending order based on the `age` column.

##### Mnemonic

A useful mnemonic to remember the basic query syntax in Hive is:

`SELECT` columns `FROM` table `WHERE` conditions `GROUP BY` columns `HAVING` conditions `ORDER BY` columns `ASC|DESC`.

##### Conclusion

In this section, we discussed how to query data in Hive using SQL-like syntax. We covered the basic query syntax and provided some examples to illustrate how to use it. We also provided a mnemonic to help remember the query syntax. With this knowledge, you should be able to perform basic data analysis and processing tasks using Hive.