#### HiveQL

HiveQL is a query language for Apache Hive, a data warehouse software project built on top of Apache Hadoop for providing data query and analysis. HiveQL allows users to read, write, and manage petabytes of data using SQL-like syntax. HiveQL supports various data types, operators, functions, and clauses for manipulating and processing structured and semi-structured data in a distributed environment. Some of the features and benefits of HiveQL are:

- HiveQL provides a schema on read approach, which means that the data schema is inferred at the time of query execution, rather than at the time of data loading. This allows users to work with different data formats and schemas without modifying the data.
- HiveQL transparently converts queries to MapReduce, Apache Tez, or Spark jobs, which run on the Hadoop cluster and leverage its scalability and fault-tolerance. Users do not need to write low-level Java code or understand the details of the underlying execution framework.
- HiveQL supports a variety of built-in operators and functions for common data analysis tasks, such as filtering, grouping, aggregating, joining, sorting, and ranking. Users can also define their own user-defined functions (UDFs), user-defined aggregate functions (UDAFs), and user-defined table functions (UDTFs) using Java, Python, or other languages.
- HiveQL supports a subset of the standard SQL syntax, as well as some extensions and variations. For example, HiveQL supports the use of backticks (`) to escape reserved keywords, the use of explain to show the query execution plan, and the use of show to display the metadata of tables, partitions, columns, etc. HiveQL also supports some Hive-specific clauses, such as partition by, cluster by, distribute by, and sort by, which control the data distribution and ordering in the output.
- HiveQL supports the creation and management of tables, databases, views, and indexes using the create, alter, drop, and describe commands. Users can also use the load, insert, update, and delete commands to load and modify data in Hive tables. HiveQL supports both managed tables, which are stored and managed by Hive, and external tables, which are stored and managed by external sources, such as HDFS, S3, or Alluxio.

Here is an example of a HiveQL query that selects the average salary and the number of employees for each department from a table called emp:

```sql
select dept, avg(salary) as avg_salary, count(*) as num_emp
from emp
group by dept
order by avg_salary desc;
```

The output of this query might look like this:

| dept | avg_salary | num_emp |
|------|------------|---------|
| IT   | 80000      | 10      |
| HR   | 60000      | 5       |
| Sales| 50000      | 15      |
| Ops  | 40000      | 20      |

Some of the mnemonics and learning tricks for HiveQL are:

- Remember that HiveQL is case-insensitive, except for string literals and column aliases. For example, select * from emp is equivalent to SELECT * FROM emp, but select name as 'Name' from emp is not the same as select name as 'name' from emp.
- Remember that HiveQL supports both single-line comments (--) and multi-line comments (/* ... */). For example, -- this is a comment and /* this is also a comment */ are both valid comments in HiveQL.
- Remember that HiveQL supports the use of variables and parameters, which can be set and referenced using the set and ${} syntax. For example, set hive.exec.mode.local.auto=true; and select * from ${hiveconf:table_name}; are both valid statements in HiveQL.
- Remember that HiveQL supports the use of subqueries, which can be nested inside the from, where, and having clauses. For example, select name, salary from emp where salary > (select avg(salary) from emp); is a valid query in HiveQL.