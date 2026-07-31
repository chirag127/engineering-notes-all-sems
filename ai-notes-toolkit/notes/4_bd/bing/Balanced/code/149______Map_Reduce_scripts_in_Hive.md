#### Map Reduce scripts in Hive

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Hive is a data warehousing platform that supports SQL-like queries and Map Reduce operations on structured and semi-structured data stored in Hadoop.
- Users can plug in their own custom mappers and reducers in the data stream by using the TRANSFORM clause in the Hive language .
- The TRANSFORM clause allows the user to specify an executable script or program that can read the input data from the standard input and write the output data to the standard output.
- The syntax of the TRANSFORM clause is as follows:

```sql
SELECT TRANSFORM (input_columns)
USING 'script' [AS output_columns]
FROM table
```

- The input_columns are the columns from the table that are passed to the script as tab-separated values.
- The script is the path or name of the executable script or program that can process the input data and produce the output data.
- The output_columns are the optional aliases for the output data columns. If not specified, the output data columns are named as _c0, _c1, etc.
- The TRANSFORM clause can be used in the SELECT, GROUP BY, or CLUSTER BY clauses of a Hive query.
- The script can be written in any language that can read from the standard input and write to the standard output, such as Python, Ruby, Perl, etc.
- The script can also access the environment variables and configuration properties set by Hive, such as HADOOP_USER_NAME, mapred.job.name, etc.
- The script can also use the Distributed Cache feature of Hadoop to access external files or libraries that are needed for the processing.
- The script can also use the counters feature of Hadoop to report the progress and statistics of the processing.
- The script can also use the logging feature of Hadoop to write the messages to the standard error stream, which can be viewed in the job logs.
- The script can also use the exit status feature of Hadoop to indicate the success or failure of the processing. A non-zero exit status will cause the job to fail.
- The script can also use the partitioning and bucketing features of Hive to optimize the data distribution and processing.
- The script can also use the compression and serialization features of Hive to reduce the data size and improve the performance.