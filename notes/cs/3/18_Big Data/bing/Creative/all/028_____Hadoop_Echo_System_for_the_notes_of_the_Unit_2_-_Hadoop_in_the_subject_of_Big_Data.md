# Hadoop Ecosystem

- The Hadoop Ecosystem is a collection of tools, libraries, and frameworks that help you build applications on top of Apache Hadoop.
- Hadoop is an open-source software framework for storing data and running applications on clusters of commodity hardware .
- Hadoop provides massive storage for any kind of data, enormous processing power and the ability to handle virtually limitless concurrent tasks or jobs.
- Hadoop is designed to scale up from a single computer to thousands of clustered computers, with each machine offering local computation and storage.
- Hadoop enables multiple types of analytic workloads to run on the same data, at the same time, at massive scale on industry-standard hardware.

## Components of Hadoop Ecosystem

- Following are some of the major components that collectively form a Hadoop ecosystem:

  - **HDFS**: Hadoop Distributed File System. It is the storage layer of Hadoop that splits large files into blocks and distributes them across the cluster nodes.
  - **YARN**: Yet Another Resource Negotiator. It is the resource management layer of Hadoop that allocates and schedules resources (CPU, memory, disk, network) for different applications running on the cluster.
  - **MapReduce**: Programming based Data Processing. It is the processing layer of Hadoop that allows users to write parallel programs using a map and reduce function. It handles the data movement, fault tolerance, and load balancing of the tasks.
  - **Spark**: In-Memory data processing. It is an alternative to MapReduce that offers faster and more flexible data processing using in-memory caching and DAG (Directed Acyclic Graph) execution engine. It supports various languages (Scala, Python, Java, R) and libraries (MLlib, GraphX, Spark SQL, Spark Streaming) for different use cases.
  - **PIG, HIVE**: Query based processing of data services. They are high-level languages that allow users to query and analyze data stored in HDFS using a SQL-like syntax. PIG is a procedural language that converts queries into MapReduce jobs, while HIVE is a declarative language that uses a metastore to store the schema and metadata of the tables.
  - **HBase**: NoSQL Database. It is a distributed and scalable column-oriented database that provides random access and strong consistency for large amounts of structured and semi-structured data. It is built on top of HDFS and supports CRUD (Create, Read, Update, Delete) operations and MapReduce integration.
  - **Sqoop, Flume, Kafka**: Data Ingestion. They are tools that help users to import and export data from and to various sources and destinations. Sqoop is used to transfer data between HDFS and relational databases, Flume is used to collect and stream log data from various sources to HDFS, and Kafka is used to publish and subscribe to streams of data in real-time.
  - **Oozie, Zookeeper**: Coordination and Workflow. They are services that help users to manage and orchestrate the execution of multiple applications and tasks on the cluster. Oozie is a workflow scheduler that allows users to define a sequence of actions and dependencies using XML, while Zookeeper is a distributed coordination service that maintains configuration information, naming, synchronization, and group services.