# Components of Hadoop

Hadoop is a framework for distributed storage and processing of large-scale data. It consists of the following components:

- **Hadoop Distributed File System (HDFS)**: This is the storage layer of Hadoop that stores data in a distributed manner across multiple nodes in a cluster. HDFS provides high availability, fault tolerance, scalability, and data locality. HDFS splits the data into blocks and replicates them across different nodes for redundancy and faster access. HDFS also supports various file formats and compression techniques.   

- **Hadoop MapReduce**: This is the processing layer of Hadoop that implements a programming model for parallel processing of data. MapReduce consists of two phases: map and reduce. The map phase takes the input data and transforms it into key-value pairs. The reduce phase aggregates the values associated with the same key and produces the output. MapReduce can handle structured, semi-structured, and unstructured data. MapReduce also supports various programming languages and frameworks such as Java, Python, Pig, Hive, etc.   

- **Hadoop YARN**: This is the resource management layer of Hadoop that allocates and manages the resources (CPU, memory, disk, network, etc.) for the applications running on the cluster. YARN consists of two components: a resource manager and a node manager. The resource manager is the master node that oversees the cluster resources and schedules the applications. The node manager is the slave node that monitors and reports the resource usage and status of the node. YARN also supports various types of applications such as batch, interactive, streaming, etc.   

- **Hadoop Common**: This is the set of shared libraries and utilities that are used by the other components of Hadoop. Hadoop Common provides the basic functionality such as configuration, logging, security, serialization, etc. Hadoop Common also includes the Hadoop command-line interface and the Hadoop web interface.  

- **Hadoop Ecosystem**: This is the collection of tools and frameworks that extend the functionality of Hadoop and provide additional features such as data ingestion, data integration, data analysis, data visualization, etc. Some of the popular tools and frameworks in the Hadoop ecosystem are:

  - **Apache Sqoop**: This is a tool for transferring data between Hadoop and relational databases.
  - **Apache Flume**: This is a tool for collecting and streaming data from various sources to Hadoop.
  - **Apache Kafka**: This is a distributed messaging system that can handle high-throughput and low-latency data streams.
  - **Apache Pig**: This is a scripting language for data analysis and manipulation on Hadoop.
  - **Apache Hive**: This is a data warehouse system that provides a SQL-like interface for querying and analyzing data on Hadoop.
  - **Apache Spark**: This is a fast and general-purpose engine for large-scale data processing on Hadoop. Spark supports batch, streaming, interactive, and machine learning applications.
  - **Apache HBase**: This is a distributed and scalable NoSQL database that provides random access and real-time updates for large-scale data on Hadoop.
  - **Apache Oozie**: This is a workflow scheduler that coordinates and executes the tasks and dependencies of Hadoop applications.
  - **Apache Mahout**: This is a library of scalable machine learning algorithms that can run on Hadoop.
  - **Apache Zeppelin**: This is a web-based notebook that allows interactive data exploration and visualization on Hadoop. 

: https://www.datavail.com/blog/3-core-components-of-the-hadoop-framework/
: https://www.digitalvidya.com/blog/what-is-hadoop/
: https://www.simplilearn.com/tutorials/hadoop-tutorial/what-is-hadoop
: https://www.educba.com/hadoop-components/
: https://phoenixnap.com/kb/apache-hadoop-architecture-explained