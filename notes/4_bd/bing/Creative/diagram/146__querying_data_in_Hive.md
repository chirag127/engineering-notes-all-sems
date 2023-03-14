Querying data in Hive is similar to querying data in SQL. Hive provides a query language called HiveQL, which is based on SQL syntax and supports many SQL features. HiveQL allows users to perform various operations on data stored in Hive tables, such as filtering, grouping, sorting, joining, aggregating, and transforming.

To query data in Hive, users need to connect to a Hive server and use a Hive client, such as Hive shell, Beeline, or Hue. Users can also use JDBC or ODBC drivers to connect to Hive from other applications. Users can write HiveQL statements in the Hive client and execute them on the Hive server. The Hive server will then compile the HiveQL statements into MapReduce, Tez, or Spark jobs and run them on the Hadoop cluster. The results of the query will be returned to the Hive client and displayed to the user.

The following diagram illustrates the basic architecture of querying data in Hive:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|   Hive Client   | <----> |   Hive Server   | <----> |   Hadoop Cluster|
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  - Hive Shell   |        |  - Hive Driver  |        |  - HDFS         |
|  - Beeline      |        |  - Hive Compiler|        |  - MapReduce    |
|  - Hue          |        |  - Hive Executor|        |  - Tez          |
|  - JDBC/ODBC    |        |  - Hive Metastore|       |  - Spark        |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```

Some examples of HiveQL statements are:

- To create a table called employees with four columns: id, name, salary, and dept:

```sql
CREATE TABLE employees (id INT, name STRING, salary FLOAT, dept STRING);
```

- To load data from a file into the employees table:

```sql
LOAD DATA LOCAL INPATH '/path/to/file' INTO TABLE employees;
```

- To select all the records from the employees table:

```sql
SELECT * FROM employees;
```

- To select the name and salary of the employees who work in the IT department:

```sql
SELECT name, salary FROM employees WHERE dept = 'IT';
```

- To select the average salary of each department:

```sql
SELECT dept, AVG(salary) FROM employees GROUP BY dept;
```

- To join the employees table with another table called managers on the dept column:

```sql
SELECT e.name, e.salary, m.name AS manager FROM employees e JOIN managers m ON e.dept = m.dept;
```

- To create a view called high_paid_employees that contains the name and salary of the employees who earn more than 10000:

```sql
CREATE VIEW high_paid_employees AS SELECT name, salary FROM employees WHERE salary > 10000;
```

- To drop the employees table:

```sql
DROP TABLE employees;
```