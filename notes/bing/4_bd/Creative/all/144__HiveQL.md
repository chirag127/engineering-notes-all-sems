#### HiveQL

- HiveQL is a query language for Apache Hive, a data warehouse system for Apache Hadoop  .
- HiveQL allows users to process and analyze structured data in a Metastore, which is a central repository of metadata that can easily be analyzed to make informed, data driven decisions.
- HiveQL provides the basic SQL-like operations, such as SELECT, INSERT, UPDATE, DELETE, JOIN, GROUP BY, HAVING, ORDER BY, etc .
- HiveQL also supports some advanced features, such as partitioning, bucketing, windowing, user-defined functions, and user-defined aggregate functions .
- HiveQL separates users from the complexity of Map Reduce programming, which is a low-level Java API for processing large-scale data in parallel .
- HiveQL reuses common concepts from relational databases, such as tables, rows, columns, and schema, to ease learning .
- HiveQL supports storage on various file systems, such as HDFS, S3, ADLS, GS, etc.
- HiveQL can be executed using various interfaces, such as Hive CLI, Hive Web UI, Hive JDBC, Hive ODBC, etc .

Some examples of HiveQL queries are:

- To create a table named employee with four columns:

```sql
CREATE TABLE employee (
  emp_id INT,
  name STRING,
  dept STRING,
  salary FLOAT
);
```

- To load data from a file into the employee table:

```sql
LOAD DATA LOCAL INPATH '/path/to/file' INTO TABLE employee;
```

- To select all the records from the employee table:

```sql
SELECT * FROM employee;
```

- To select the name and salary of the employees who work in the sales department:

```sql
SELECT name, salary FROM employee WHERE dept = 'sales';
```

- To join the employee table with another table named bonus based on the emp_id column:

```sql
SELECT e.name, e.salary, b.amount FROM employee e JOIN bonus b ON e.emp_id = b.emp_id;
```

- To calculate the average salary of each department and sort them in descending order:

```sql
SELECT dept, AVG(salary) AS avg_salary FROM employee GROUP BY dept ORDER BY avg_salary DESC;
```

Some mnemonics and learning tricks for HiveQL are:

- Remember that HiveQL is similar to SQL, so you can use your existing knowledge of SQL to learn HiveQL.
- Remember that HiveQL is case-insensitive, so you don't have to worry about the capitalization of keywords, table names, column names, etc.
- Remember that HiveQL supports comments, which are lines that start with -- or /* and end with */. You can use comments to explain your queries or to temporarily disable some parts of your queries.
- Remember that HiveQL supports various data types, such as INT, STRING, FLOAT, BOOLEAN, ARRAY, MAP, STRUCT, etc. You can use these data types to define the schema of your tables and to manipulate the data in your queries.
- Remember that HiveQL supports various operators, such as arithmetic operators (+, -, *, /, %), comparison operators (=, <, >, <=, >=, !=, <>, <=>), logical operators (AND, OR, NOT), etc. You can use these operators to perform calculations, comparisons, and conditions in your queries.