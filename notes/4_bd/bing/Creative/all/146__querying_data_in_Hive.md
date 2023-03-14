#### Querying data in Hive

- Hive is a data warehouse system built on top of Hadoop that allows users to query and analyze large datasets using a SQL-like language called HiveQL or HQL .
- HiveQL is a declarative language that converts queries into MapReduce, Tez, or Spark jobs under the hood .
- Hive can handle structured, semi-structured, and unstructured data and supports various file formats, compression methods, and storage formats.
- Hive supports two types of tables: managed tables and external tables. Managed tables are owned by Hive and their data and schema are stored in the Hive metastore. External tables are used to access data that is managed by an external source, such as HDFS or another system. The schema of external tables is stored in the Hive metastore, but the data is not.
- Hive also supports partitioning and bucketing of tables to improve query performance and scalability. Partitioning divides a table into multiple directories based on the values of a partition column. Bucketing splits the data within a partition into multiple files based on the hash value of a bucketing column.
- To query data in Hive, users can use the Hive command line interface (CLI), the Hive web interface (HWI), or connect to the Hive server using JDBC or ODBC drivers.
- The basic syntax of a HiveQL query is similar to SQL. For example, to select all the columns from a table called who, we can write:

```sql
SELECT * FROM who;
```

- To filter the rows based on a condition, we can use the WHERE clause. For example, to select only the rows where the country column is 'India', we can write:

```sql
SELECT * FROM who WHERE country = 'India';
```

- To sort the rows based on one or more columns, we can use the ORDER BY or SORT BY clause. The difference is that ORDER BY sorts the entire result set globally, while SORT BY sorts the data within each reducer partition. For example, to sort the rows by the year column in descending order, we can write:

```sql
SELECT * FROM who ORDER BY year DESC;
```

- To group the rows based on one or more columns and apply aggregate functions, we can use the GROUP BY clause. For example, to calculate the average life expectancy by country, we can write:

```sql
SELECT country, AVG(life_expectancy) FROM who GROUP BY country;
```

- To join two or more tables based on a common column, we can use the JOIN clause. Hive supports different types of joins, such as inner join, left outer join, right outer join, full outer join, and cross join. For example, to join the who table with another table called country_info on the country column, we can write:

```sql
SELECT who.*, country_info.population, country_info.gdp
FROM who JOIN country_info ON who.country = country_info.country;
```

- Hive supports various built-in functions to perform operations on the data. These functions can be categorized into different types, such as string functions, mathematical functions, date functions, conditional functions, collection functions, etc. For example, to get the current date, we can use the current_date() function:

```sql
SELECT current_date();
```

- Hive also allows users to define their own functions using Java or Python and use them in their queries. These functions are called user-defined functions (UDFs) and can be either scalar functions or table functions. Scalar functions take one or more input values and return a single output value. Table functions take one or more input values and return a table of output values. For example, to create a UDF that returns the length of a string, we can write:

```java
// Java code to define the UDF
import org.apache.hadoop.hive.ql.exec.UDF;
import org.apache.hadoop.io.Text;

public class StringLength extends UDF {
  public int evaluate(Text input) {
    if (input == null) {
      return 0;
    }
    return input.toString().length();
  }
}
```

```sql
-- HiveQL code to register and use the UDF
ADD JAR /path/to/jar/file;
CREATE TEMPORARY FUNCTION str_len AS 'StringLength';
SELECT str_len(country) FROM who;
```

- To improve the readability and maintainability of the queries, Hive supports the use of variables, comments, and subqueries. Variables are placeholders for values that can be set and used in