#### Components of Hadoop

Hadoop is a framework for distributed storage and processing of large-scale data sets. It consists of the following core components:

- **Hadoop Distributed File System (HDFS)**: This is the storage layer of Hadoop that stores data in a distributed manner across multiple nodes in a cluster. HDFS provides high availability, fault tolerance, scalability, and data locality. HDFS can store any kind of data without prior organization .
- **Hadoop MapReduce**: This is the processing layer of Hadoop that allows parallel execution of user-defined functions on the data stored in HDFS. MapReduce consists of two phases: map and reduce. The map phase applies a function to each input key-value pair and produces intermediate key-value pairs. The reduce phase aggregates the intermediate values associated with the same key and produces the final output .
- **Hadoop YARN**: This is the resource management layer of Hadoop that allocates and schedules resources (such as CPU, memory, disk, and network) for the applications running on the cluster. YARN also monitors the health and performance of the nodes and the applications. YARN enables multiple processing frameworks (such as Spark, Hive, Pig, etc.) to run on the same cluster and share resources .

Hadoop also has some other components that provide additional functionality, such as:

- **Hadoop Common**: This is a set of shared libraries and utilities that support the other Hadoop components. It includes configuration, logging, security, serialization, and networking modules.
- **Hadoop ZooKeeper**: This is a service that provides coordination and synchronization for distributed applications. It maintains configuration information, naming, group membership, and leader election for the applications.
- **Hadoop Oozie**: This is a workflow scheduler that manages and executes Hadoop jobs. It supports dependency management, concurrency control, retry policies, and notifications for the jobs.
- **Hadoop HBase**: This is a column-oriented database that provides random access and real-time updates for large-scale data. It is built on top of HDFS and supports MapReduce operations.
- **Hadoop Hive**: This is a data warehouse that provides a SQL-like interface for querying and analyzing data stored in HDFS. It supports various data formats, such as text, JSON, ORC, Parquet, etc. It also supports user-defined functions and custom data types.
- **Hadoop Pig**: This is a scripting language that allows users to write complex data transformations and analysis using a high-level syntax. It compiles the scripts into MapReduce jobs and executes them on the cluster.
- **Hadoop Spark**: This is a fast and general-purpose processing framework that supports batch, streaming, interactive, and machine learning applications. It uses in-memory caching and lazy evaluation to optimize performance. It also provides various libraries, such as Spark SQL, Spark Streaming, MLlib, and GraphX.