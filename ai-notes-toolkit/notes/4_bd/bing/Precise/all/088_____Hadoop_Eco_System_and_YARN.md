### Hadoop Eco System and YARN

Hadoop is an open-source software framework for storing and processing large datasets. It is designed to scale up from a single server to thousands of machines, each offering local computation and storage. The Hadoop ecosystem consists of several components, including:

1. **Hadoop Distributed File System (HDFS)**: A distributed file system that provides high-throughput access to application data.

2. **MapReduce**: A programming model for processing large datasets in parallel.

3. **YARN (Yet Another Resource Negotiator)**: A resource management platform responsible for managing compute resources in clusters and using them for scheduling of users' applications.

4. **HBase**: A non-relational distributed database that runs on top of HDFS.

5. **Hive**: A data warehousing and SQL-like query language for Hadoop.

6. **Pig**: A high-level platform for creating MapReduce programs used with Hadoop.

7. **ZooKeeper**: A centralized service for maintaining configuration information, naming, and providing distributed synchronization.

YARN is the architectural center of Hadoop that allows multiple data processing engines such as interactive SQL, real-time streaming, data science, and batch processing to handle data stored in a single platform, unlocking an entirely new approach to analytics. YARN provides a central resource management and a common platform to deliver consistent operations, security, and data governance tools across Hadoop clusters.

YARN is responsible for allocating system resources to the various applications running in a Hadoop cluster and scheduling tasks to be run on different cluster nodes. It is designed to be scalable, efficient, and flexible, allowing for dynamic allocation of cluster resources as needed by applications. YARN also provides a central platform for delivering common services such as security, governance, and operations for all Hadoop components.