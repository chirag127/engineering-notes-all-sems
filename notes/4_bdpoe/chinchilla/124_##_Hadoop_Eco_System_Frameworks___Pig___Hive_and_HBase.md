## Hadoop Eco System Frameworks, Pig, Hive, and HBase

Hadoop is an open-source framework that is widely used for distributed storage and processing of large datasets. It consists of various components that together form the Hadoop ecosystem. Among these, Pig, Hive, and HBase are widely used frameworks that offer different functionalities when working with Hadoop.

### Hadoop Eco System Frameworks

The Hadoop ecosystem includes various frameworks that are used for different purposes, including:

1. HDFS (Hadoop Distributed File System): A distributed file system designed to store large files across multiple nodes in a Hadoop cluster.
2. YARN (Yet Another Resource Negotiator): A resource manager that schedules tasks and allocates resources in a Hadoop cluster.
3. MapReduce: A programming model used for processing large datasets in parallel across a cluster of computers.
4. Spark: A fast and general-purpose cluster computing system that can process data in-memory.
5. Kafka: A distributed streaming platform used for building real-time data pipelines and streaming applications.
6. Flume: A distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data.
7. Sqoop: A tool used to transfer data between Hadoop and relational databases.
8. Oozie: A workflow scheduler system used to manage Hadoop jobs.

### Pig

Pig is a high-level scripting language used for analyzing large datasets in Hadoop. It provides a simple and flexible way to write MapReduce jobs without needing to write complex Java code. Some of the features of Pig include:

1. Pig Latin: A high-level scripting language used to write Pig scripts.
2. Simple syntax: Pig's syntax is easy to learn and write.
3. Rich set of operators: Pig provides a rich set of operators for performing various data transformations.
4. Extensibility: Pig can be extended by writing user-defined functions (UDFs) in Java or Python.

Mnemonic trick: Pigs love to play with data.

### Hive

Hive is a data warehousing framework used for querying and analyzing large datasets stored in Hadoop. It provides a SQL-like interface for querying data and can be used by users who are familiar with SQL. Some of the features of Hive include:

1. HiveQL: A SQL-like query language used to write Hive queries.
2. Schema on read: Hive allows users to define a schema for their data when it is queried, rather than when it is stored.
3. Support for complex data types: Hive supports complex data types such as arrays, maps, and structs.
4. Extensibility: Hive can be extended by writing UDFs in Java or Python.

Mnemonic trick: Bees love to store and analyze data in their hives.

### HBase

HBase is a column-oriented NoSQL database that runs on top of Hadoop. It is designed to handle large datasets with high write and read throughput. Some of the features of HBase include:

1. Column-oriented: Data is stored in columns, rather than rows.
2. Scalability: HBase can scale to handle large datasets across multiple nodes in a Hadoop cluster.
3. High write and read throughput: HBase is designed to handle high write and read throughput.
4. Consistency: HBase provides strong consistency guarantees.

Mnemonic trick: HBase is like a big book with columns instead of rows, where you can quickly write and read information.

Overall, these frameworks provide a wide range of functionalities and are essential for working with large datasets in Hadoop. Understanding their features and use cases is important for developers and data analysts working with Hadoop.