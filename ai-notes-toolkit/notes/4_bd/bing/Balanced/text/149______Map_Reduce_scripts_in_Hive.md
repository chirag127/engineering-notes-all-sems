#### Map Reduce Scripts in Hive

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Hive is a data warehousing platform that supports SQL-like queries and analysis of large volumes of data stored in Hadoop.
- Hive can translate SQL queries into Map Reduce jobs and execute them on Hadoop cluster.
- Users can also plug in their own custom mappers and reducers in the data stream by using features natively supported in the Hive language.
- The TRANSFORM clause can be used to embed the custom mapper and reducer scripts in the Hive query.
- The syntax of the TRANSFORM clause is as follows:

```sql
SELECT TRANSFORM (input_columns) 
USING 'mapper_script' [AS output_columns] 
FROM input_table 
[WHERE conditions] 
[CLUSTER BY columns] 
[MAPREDUCE 'reducer_script' [AS output_columns]];
```

- The input_columns are the columns from the input_table that are passed to the mapper_script as standard input (stdin).
- The mapper_script is any executable file that can read from stdin and write to standard output (stdout).
- The output_columns are the columns that are produced by the mapper_script as stdout and returned by the TRANSFORM clause.
- The input_table is the source table that contains the data to be processed by the mapper_script.
- The WHERE clause can be used to filter the input data based on some conditions.
- The CLUSTER BY clause can be used to partition the output data based on some columns and send them to the reducer_script as input.
- The reducer_script is any executable file that can read from stdin and write to stdout.
- The output_columns are the columns that are produced by the reducer_script as stdout and returned by the MAPREDUCE clause.

- The mapper_script and the reducer_script can be written in any programming language, such as Python, Perl, Ruby, etc.
- The mapper_script and the reducer_script should follow the following rules:

  - They should read one line from stdin at a time and write one line to stdout at a time.
  - They should use the tab character (\t) as the delimiter for both input and output columns.
  - They should not write anything to standard error (stderr) unless there is an error.
  - They should handle any exceptions or errors gracefully and exit with a non-zero status code if there is a failure.

- The TRANSFORM and MAPREDUCE clauses can be used to perform complex data transformations and aggregations that are not supported by the built-in Hive functions or operators.
- They can also be used to leverage existing scripts or libraries that are written in other languages or frameworks.