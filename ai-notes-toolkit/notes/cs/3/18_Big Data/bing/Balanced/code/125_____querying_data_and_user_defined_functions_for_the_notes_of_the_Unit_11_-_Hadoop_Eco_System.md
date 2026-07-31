### Querying Data and User Defined Functions for the Notes of the Unit 11 - Hadoop Eco System

- Querying data in Hadoop is the process of retrieving and analyzing data stored in HDFS using various tools and frameworks.
- One of the most popular tools for querying data in Hadoop is Apache Hive, which is a data warehouse system that provides a SQL-like language called HiveQL for querying and summarizing large data sets.
- HiveQL supports many standard SQL features, such as joins, group by, order by, subqueries, and aggregate functions, as well as some extensions, such as partitioning, bucketing, windowing, and sampling.
- HiveQL also allows users to define their own functions (UDFs) in Java or other languages, and use them in queries to perform custom logic or transformations on column values.
- UDFs can be classified into four types based on their input and output:
  - Scalar UDFs: These take one or more input values and return a single output value. For example, a UDF that converts temperature from Celsius to Fahrenheit.
  - Aggregate UDFs: These take a set of input values and return a single output value. For example, a UDF that calculates the median of a column.
  - Table UDFs: These take one or more input values and return a table of output values. For example, a UDF that splits a string into words and returns a table of words.
  - Window UDFs: These take a set of input values and return a set of output values based on a window specification. For example, a UDF that calculates the moving average of a column over a specified window.
- To create and use a UDF in Hive, the following steps are required:
  - Write the UDF code in Java or another language, and compile it into a JAR file.
  - Copy the JAR file to a location accessible by Hive, such as HDFS or a local directory.
  - Register the JAR file with Hive using the `ADD JAR` command.
  - Create a function in Hive using the `CREATE FUNCTION` command, and specify the class name and the JAR file of the UDF.
  - Use the function in Hive queries as if it were a built-in function.
- Some examples of UDFs in Hive are:
  - A UDF that converts a string to uppercase:

```java
// UDF code in Java
import org.apache.hadoop.hive.ql.exec.UDF;
import org.apache.hadoop.io.Text;

public class UpperCaseUDF extends UDF {
  public Text evaluate(Text input) {
    if (input == null) return null;
    return new Text(input.toString().toUpperCase());
  }
}

// Hive commands
ADD JAR /path/to/UpperCaseUDF.jar;
CREATE FUNCTION upper AS 'UpperCaseUDF';
SELECT upper(name) FROM employees;
```

  - A UDF that calculates the factorial of a number:

```java
// UDF code in Java
import org.apache.hadoop.hive.ql.exec.UDF;
import org.apache.hadoop.io.LongWritable;

public class FactorialUDF extends UDF {
  public LongWritable evaluate(LongWritable input) {
    if (input == null) return null;
    long n = input.get();
    long result = 1;
    for (long i = 1; i <= n; i++) {
      result *= i;
    }
    return new LongWritable(result);
  }
}

// Hive commands
ADD JAR /path/to/FactorialUDF.jar;
CREATE FUNCTION factorial AS 'FactorialUDF';
SELECT factorial(5) FROM dummy;
```

  - A UDF that returns the current date and time:

```java
// UDF code in Java
import org.apache.hadoop.hive.ql.exec.UDF;
import org.apache.hadoop.io.Text;
import java.text.SimpleDateFormat;
import java.util.Date;

public class CurrentDateTimeUDF extends UDF {
  public Text evaluate() {
    SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    Date date = new Date();
    return new Text(sdf.format(date));
  }
}

// Hive commands
ADD JAR /path/to/CurrentDateTimeUDF.jar;
CREATE FUNCTION current_datetime AS 'CurrentDateTimeUDF';
SELECT current_datetime() FROM dummy;
```