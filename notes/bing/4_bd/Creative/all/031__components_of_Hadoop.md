#### Components of Hadoop

Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers. It consists of the following core components:

- **Hadoop Distributed File System (HDFS)**: This is the storage layer of Hadoop that provides a reliable and scalable file system for storing and accessing data. HDFS splits the data into blocks and distributes them across multiple nodes in the cluster, ensuring fault tolerance and high availability. HDFS also maintains metadata about the data blocks, such as their location, size, and replication factor. HDFS has two main components: NameNode and DataNode. NameNode is the master node that manages the namespace and the metadata of the file system. DataNode is the worker node that stores and serves the data blocks. A mnemonic to remember the components of HDFS is **H**ave **D**ata **F**or **S**ure.

- **MapReduce**: This is the processing layer of Hadoop that provides a parallel programming model for writing applications that can process large amounts of data. MapReduce consists of two phases: Map and Reduce. Map phase takes the input data and transforms it into key-value pairs. Reduce phase takes the output of the Map phase and aggregates the values based on the keys. MapReduce also handles the partitioning, shuffling, and sorting of the data between the phases. MapReduce has two main components: JobTracker and TaskTracker. JobTracker is the master node that coordinates the execution of the MapReduce jobs and assigns tasks to the TaskTrackers. TaskTracker is the worker node that runs the tasks and reports the progress to the JobTracker. A mnemonic to remember the components of MapReduce is **M**ake **A** **P**lan, **R**eview and **E**xecute.

- **Yet Another Resource Negotiator (YARN)**: This is the resource management layer of Hadoop that allocates and manages the resources (such as CPU, memory, disk, and network) for the applications running on the cluster. YARN also provides a platform for running various types of applications on Hadoop, such as batch, interactive, streaming, and machine learning. YARN has two main components: ResourceManager and NodeManager. ResourceManager is the master node that oversees the resource allocation and scheduling of the applications. NodeManager is the worker node that monitors and reports the resource utilization and status of the containers running on the node. A container is a unit of execution that encapsulates the resources and the application logic. A mnemonic to remember the components of YARN is **Y**ou **A**re **R**esourceful, **N**o doubt.

Besides these core components, Hadoop also has a rich ecosystem of tools and applications that help with data ingestion, transformation, analysis, and visualization. Some of these are:

- **Apache Pig**: A scripting language for writing data pipelines on Hadoop.
- **Apache Hive**: A query language for performing SQL-like operations on Hadoop.
- **Apache HBase**: A NoSQL database for storing and accessing sparse and structured data on Hadoop.
- **Apache Spark**: A fast and general-purpose engine for large-scale data processing on Hadoop.
- **Presto**: A distributed query engine for interactive analytics on Hadoop.
- **Apache Zeppelin**: A web-based notebook for data exploration and visualization on Hadoop.