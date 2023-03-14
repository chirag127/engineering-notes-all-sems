#### Apache Hive architecture

Apache Hive is a distributed, fault-tolerant data warehouse system that enables analytics at a massive scale and facilitates reading, writing, and managing petabytes of data residing in distributed storage using SQL. The main components of Apache Hive architecture are :

- **UI**: The user interface for users to submit queries and other operations to the system. It can be a command line interface or a web based GUI.
- **Driver**: The component which receives the queries from the UI and creates a session handle for the query. It provides execute and fetch APIs modeled on JDBC/ODBC interfaces.
- **Compiler**: The component that parses the query, does semantic analysis on the different query blocks and query expressions and eventually generates an execution plan with the help of the table and partition metadata looked up from the metastore.
- **Metastore**: The component that stores all the structure information of the various tables and partitions in the warehouse including column and column type information, the serializers and deserializers necessary to read and write data and the corresponding HDFS files where the data is stored. It can be an external relational database or an embedded one.
- **Execution Engine**: The component which executes the execution plan created by the compiler. The plan is a DAG of stages with each stage being either a map/reduce job, a metadata operation or an operation on HDFS. The execution engine manages the dependencies between these different stages of the plan and executes these stages on the appropriate system components.
- **Hive Server 2**: The component that accepts incoming requests from users and applications and creates an execution plan and auto generates a YARN job to process SQL queries. It supports multi-client concurrency and authentication and provides a JDBC/ODBC interface.
- **Hive Query Language (HQL)**: The SQL-like language that is used to write queries and commands for Hive. It supports a subset of ANSI SQL and some Hive-specific extensions.
- **Hive Beeline Shell**: The command line interface that connects to Hive Server 2 and allows users to interact with Hive using HQL.

The following figure shows how a typical query flows through the Hive architecture:

![Hive architecture diagram](https://cwiki.apache.org/confluence/download/attachments/27362075/HiveArch.png?version=1&modificationDate=1218588265000&api=v2)

: https://hive.apache.org/
: https://cwiki.apache.org/confluence/display/Hive/Design
: https://data-flair.training/blogs/apache-hive-architecture/
: https://www.databricks.com/glossary/apache-hive