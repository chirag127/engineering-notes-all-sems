 Here is the content in markdown format for the topic #### introduction to Big SQL:

#### Introduction to Big SQL

Big SQL is a SQL-on-Hadoop engine that extends the familiar SQL language to work on data stored in Hadoop clusters. It allows you to query data without the complexity of learning MapReduce.

**Key points:**

1. Big SQL provides a standard SQL interface to query data in Hadoop (HDFS). This makes it easy for SQL users and developers to leverage the scalability and cost effectiveness of Hadoop for big data analytics.

2. Big SQL compiles SQL queries into MapReduce jobs which are executed on Hadoop clusters. This enables scalability, distributed processing of large data sets and fault tolerance.

3. Big SQL supports standard SQL concepts like tables, schemas, columns, rows, indexes, partitions, etc. This makes the transition from traditional RDBMS to Big SQL simple for SQL users.

4. Big SQL provides high performance for interactive and batch SQL queries through various optimizations. This makes it suitable for both data exploration and production workloads.

**Advantages:**

- Standard SQL interface makes it easy to learn and use for SQL users.
- Scalability and distributed processing of Hadoop clusters.
- Fault tolerance through replication of data.
- High performance for both interactive and batch queries.

**Disadvantages:**

- Limited to basic SQL concepts. Complex queries and advanced SQL features are not supported.
- Single node scalability is limited. It requires a Hadoop cluster to scale.
- Administrative complexity of managing a Hadoop cluster.

**Applications:** Data warehousing, analytics, data mining, ETL, reporting on large data sets stored in Hadoop.

**Mnemonics:**

- Big SQL = SQL on Hadoop
- Standard SQL interface
- Hadoop scalability and fault tolerance
- High performance for interactive and batch queries