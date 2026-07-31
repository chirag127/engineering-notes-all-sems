### Data Processing Operators for the Notes of the Unit 11 - Hadoop Eco System Frameworks in the Subject of Big Data

- Data processing operators are the commands or functions that are used to manipulate, transform, or analyze data in Hadoop.
- Hadoop is a framework that uses distributed storage and parallel processing to store and manage big data.
- Hadoop has three main components: Hadoop Distributed File System (HDFS), MapReduce, and YARN.
- HDFS is the storage layer that splits and distributes large data sets across multiple nodes in a cluster.
- MapReduce is the processing layer that applies a user-defined function (map) to each data block and then aggregates the results (reduce) across the cluster.
- YARN is the resource management layer that allocates and schedules the tasks on the nodes.
- Hadoop can handle any type of data: structured, semi-structured, and unstructured.
- Hadoop supports various data processing operators that can be used to perform different operations on the data, such as filtering, grouping, joining, sorting, aggregating, etc.
- Some of the common data processing operators in Hadoop are:
  - Pig operators: Pig is a high-level procedural language for querying large data sets using Hadoop and MapReduce. Pig operators are the commands or functions that take a relation as input and produce another relation as output. Some examples of Pig operators are: LOAD, STORE, FILTER, FOREACH, GROUP, JOIN, ORDER, LIMIT, etc.
  - Hive operators: Hive is a data warehouse system that provides a SQL-like interface for querying and analyzing data stored in HDFS. Hive operators are the commands or functions that are used to manipulate or query data in Hive tables or views. Some examples of Hive operators are: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, SORT BY, DISTRIBUTE BY, CLUSTER BY, JOIN, UNION, etc.
  - STREAM operator: The STREAM operator allows you to transform data in a relation using an external program or script. It is named by analogy with Hadoop Streaming, which provides a similar capability for MapReduce. STREAM can use built-in commands with arguments, such as awk, sed, grep, etc., or user-defined scripts written in any language, such as Python, Ruby, Perl, etc. The syntax of the STREAM operator is:

    ```
    relation2 = STREAM relation1 THROUGH command [AS schema];
    ```

    where relation1 is the input relation, command is the external program or script, and relation2 is the output relation with an optional schema.