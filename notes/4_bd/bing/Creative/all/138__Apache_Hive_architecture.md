#### Apache Hive architecture

Apache Hive is a distributed, fault-tolerant data warehouse system that enables analytics at a massive scale and facilitates reading, writing, and managing petabytes of data residing in distributed storage using SQL. It is built on top of Apache Hadoop and supports storage on various file systems such as HDFS, S3, ADLS, GS, etc. 

The main components of Apache Hive architecture are:

- **Hive Clients**: These are the user interfaces for users to submit queries and other operations to the system. Hive supports a command line interface (CLI), a web-based graphical user interface (GUI), and a JDBC/ODBC driver for connecting to external applications.
- **Hive Driver**: This is the component that receives the queries from the clients and creates a session handle for the query. It also provides execute and fetch APIs modeled on JDBC/ODBC interfaces.
- **Hive Compiler**: This is the component that parses the query, does semantic analysis on the different query blocks and query expressions, and eventually generates an execution plan with the help of the table and partition metadata looked up from the metastore.
- **Hive Metastore**: This is the component that stores all the structure information of the various tables and partitions in the warehouse, including column and column type information, the serializers and deserializers necessary to read and write data, and the corresponding HDFS files where the data is stored. The metastore can be configured to use different relational databases such as MySQL, PostgreSQL, Oracle, etc.
- **Hive Execution Engine**: This is the component that executes the execution plan created by the compiler. The plan is a directed acyclic graph (DAG) of stages, with each stage being either a map/reduce job, a metadata operation, or an operation on HDFS. The execution engine manages the dependencies between these different stages of the plan and executes them on the appropriate system components.
- **Hive Query Language (HQL)**: This is the SQL-like language that Hive uses to express queries and other operations on the data. HQL supports most of the standard SQL features such as joins, subqueries, aggregations, window functions, etc. It also supports some Hive-specific extensions such as partitioning, bucketing, user-defined functions, etc.
- **Hive Beeline Shell**: This is the command line tool that allows users to interact with Hive using HQL. It is based on the Apache JDBC driver and supports multiple concurrent sessions and queries.
- **Hive Server 2**: This is the service that provides a thrift interface for clients to connect to Hive and submit queries. It supports multi-client concurrency and authentication and is designed to provide better support for open API clients like JDBC and ODBC.
- **Hive LLAP**: This is the component that enables interactive and subsecond SQL queries through low latency analytical processing (LLAP). It is introduced in Hive 2.0 and makes Hive faster by using persistent query infrastructure and optimized data caching.

A typical query flow through the Hive architecture is as follows:

- The user submits a query to the Hive client, which sends it to the Hive driver (step 1).
- The Hive driver creates a session handle for the query and sends it to the Hive compiler to generate an execution plan (step 2).
- The Hive compiler gets the necessary metadata from the Hive metastore (steps 3 and 4). This metadata is used to typecheck the expressions in the query tree as well as to prune partitions based on query predicates.
- The Hive compiler generates a DAG of stages with each stage being either a map/reduce job, a metadata operation, or an operation on HDFS (step 5). For map/reduce stages, the plan contains map operator trees (operator trees that are executed on the mappers) and a reduce operator tree (for operations that need reducers).
- The Hive execution engine submits these stages to the appropriate components (steps 6, 6.1, 6.2, and 6.3). In each task (mapper/reducer) the deserializer associated with the table or intermediate outputs is used to read the rows from HDFS files and these are passed through the associated operator tree. Once the output is generated, it is written to a temporary HDFS file through the serializer (this happens in the mapper in case the operation does not need a reduce). The temporary files are used to provide data to subsequent map/reduce stages of the plan.
- The final output of the query is stored in a specified location on HDFS or returned to the Hive client (step 7).

The following diagram illustrates the Hive architecture and the query flow