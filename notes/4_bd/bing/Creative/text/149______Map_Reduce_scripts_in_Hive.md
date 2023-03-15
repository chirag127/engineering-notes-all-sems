#### Map Reduce scripts in Hive

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Hive is a data warehousing platform that provides SQL-like language for querying and analyzing data stored in Hadoop.
- Hive can translate SQL queries into Map Reduce jobs and execute them on Hadoop cluster.
- Users can also plug in their own custom mappers and reducers in the data stream by using features natively supported in the Hive language .
- The TRANSFORM clause can be used to embed the mapper and reducer scripts in the Hive query.
- The mapper and reducer scripts can be written in any language that can read from standard input and write to standard output, such as Python, Ruby, Perl, etc.
- The mapper script takes one row of input and produces zero or more rows of output, separated by tabs.
- The reducer script takes zero or more rows of input (grouped by key) and produces zero or more rows of output, separated by tabs.
- The input and output schema of the mapper and reducer scripts must be specified in the Hive query using AS clause.
- The input and output format of the mapper and reducer scripts can be customized by using ROW FORMAT and SERDE clauses.
- The mapper and reducer scripts can access external resources such as files, databases, web services, etc. by using DISTRIBUTE and RESOURCE clauses.
- The mapper and reducer scripts can also use Hive built-in functions and UDFs by using USING clause.
- The mapper and reducer scripts can be tested locally by using LOCAL clause.
- The mapper and reducer scripts can be debugged by using EXPLAIN and LOG clauses.
- The performance of the mapper and reducer scripts can be improved by using CLUSTER BY, SORT BY, and DISTRIBUTE BY clauses.