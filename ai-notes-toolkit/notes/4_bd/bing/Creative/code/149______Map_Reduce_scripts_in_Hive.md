#### Map Reduce scripts in Hive

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Hive is a data warehousing platform that provides SQL-like language for querying and analyzing data stored in Hadoop.
- Hive can translate SQL queries into Map Reduce jobs and execute them on Hadoop cluster.
- Users can also plug in their own custom mappers and reducers in the data stream by using features natively supported in the Hive language .
- The TRANSFORM clause can be used to embed the mapper and reducer scripts in the Hive query.
- The mapper and reducer scripts can be written in any language that can read from standard input and write to standard output, such as Python, Ruby, Perl, etc.
- The mapper script takes one row of input and produces zero or more rows of output.
- The reducer script takes zero or more rows of input and produces one or more rows of output.
- The input and output format of the mapper and reducer scripts can be specified by using ROW FORMAT and DELIMITED clauses.
- The input and output columns of the mapper and reducer scripts can be specified by using AS clause.
- The mapper and reducer scripts can be stored in local file system or HDFS and can be referenced by using absolute or relative paths.
- The mapper and reducer scripts can also be passed as inline commands by using single quotes.
- The mapper and reducer scripts can access external resources such as files, databases, web services, etc. by using ADD FILE, ADD JAR, or ADD ARCHIVE commands.
- The mapper and reducer scripts can also use Hive built-in functions or user-defined functions by using USING clause.
- The mapper and reducer scripts can be combined with other Hive clauses such as WHERE, GROUP BY, ORDER BY, etc. to perform complex data transformations and aggregations.