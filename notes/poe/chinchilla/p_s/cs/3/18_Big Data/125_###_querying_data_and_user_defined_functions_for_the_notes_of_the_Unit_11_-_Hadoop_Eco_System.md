### Querying Data and User Defined Functions

When working with Hadoop, querying data and user defined functions (UDFs) can greatly enhance the functionality and analysis capabilities of the system. In this section, we will explore the basics of querying data and creating UDFs within the Hadoop ecosystem.

#### Querying Data

One of the most common ways to query data in Hadoop is through Apache Hive. Hive is a data warehouse infrastructure that provides data summarization, query, and analysis capabilities. Some key features of Hive include:

- SQL-like syntax: HiveQL is a SQL-like language that enables users to query and analyze data stored in Hadoop.
- Data summarization: Hive provides the ability to summarize data using common aggregation functions such as COUNT, SUM, AVG, and more.
- Data integration: Hive can integrate data from various sources, including HDFS, HBase, and other databases.

To use Hive, a user must create a table that maps to the data stored in Hadoop. Once the table is created, the user can run queries on the data using HiveQL. Here is an example of how to create a table in Hive:

```
CREATE TABLE users (
    id INT,
    name STRING,
    age INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
```

Once the table is created, the user can run queries on the data. For example, to select all users over the age of 30:

```
SELECT * FROM users WHERE age > 30;
```

#### User Defined Functions

User defined functions (UDFs) can be created to extend the functionality of HiveQL. UDFs allow users to define custom functions that can be used in queries just like built-in functions. Some common types of UDFs include:

- Scalar functions: These take a single input and return a single output, such as a mathematical operation.
- Aggregate functions: These take multiple inputs and return a single output, such as an average or sum.
- Table generating functions: These generate a table as output, such as a list of dates.

To create a UDF in Hive, a user must first write the UDF code in their preferred language (such as Java or Python). Once the UDF code is written, it can be compiled and registered with Hive. Here is an example of how to create a UDF in Java:

```
public class MyUDF extends UDF {
  public String evaluate(String input) {
    return input.toUpperCase();
  }
}
```

Once the UDF is registered with Hive, it can be used in queries. For example, to use the MyUDF function to convert all names in the users table to uppercase:

```
SELECT id, MyUDF(name), age FROM users;
```

In conclusion, querying data and creating UDFs are powerful tools in the Hadoop ecosystem that can greatly enhance the functionality and analysis capabilities of the system. By using Apache Hive and creating custom functions, users can gain valuable insights from the data stored in Hadoop.