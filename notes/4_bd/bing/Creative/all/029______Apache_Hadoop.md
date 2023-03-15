#### Apache Hadoop

- Apache Hadoop is a collection of open-source software utilities that facilitates using a network of many computers to solve problems involving massive amounts of data and computation .
- Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models .
- Apache Hadoop is designed to scale up from single servers to thousands of machines, each offering local computation and storage.
- Apache Hadoop consists of four main modules: Hadoop Common, Hadoop Distributed File System (HDFS), Hadoop MapReduce, and Hadoop YARN .
  - Hadoop Common: The common utilities that support the other Hadoop modules.
  - Hadoop Distributed File System (HDFS): A distributed file system that provides high-throughput access to application data.
  - Hadoop MapReduce: A programming model for large-scale data processing.
  - Hadoop YARN: A framework for job scheduling and cluster resource management.
- Apache Hadoop also has several subprojects that provide additional features and functionalities, such as Hadoop ZooKeeper, Hadoop HBase, Hadoop Hive, Hadoop Pig, Hadoop Spark, etc .
- Apache Hadoop is widely used for big data analytics, data warehousing, machine learning, natural language processing, image processing, etc .
- Apache Hadoop has several advantages, such as:
  - Scalability: Hadoop can handle petabytes of data by adding more nodes to the cluster.
  - Fault-tolerance: Hadoop replicates data across multiple nodes and can recover from node failures.
  - Cost-effectiveness: Hadoop runs on commodity hardware and uses open-source software, reducing the cost of data storage and processing.
  - Flexibility: Hadoop can process structured, semi-structured, and unstructured data from various sources and formats.
  - Parallelism: Hadoop can perform parallel processing of data using the MapReduce model, which divides the data into smaller chunks and assigns them to different nodes for processing.
- Apache Hadoop also has some disadvantages, such as:
  - Complexity: Hadoop requires a lot of configuration and tuning to optimize its performance and security.
  - Latency: Hadoop is not suitable for real-time or interactive applications, as it has high latency due to the batch processing nature of MapReduce.
  - Skill gap: Hadoop requires skilled programmers and administrators who can understand and use the Hadoop ecosystem.
  - Security: Hadoop has limited security features and relies on external tools and frameworks for authentication, authorization, encryption, etc.

- A possible mnemonic to remember the four main modules of Hadoop is: **H**ave **C**ommon **F**iles **M**apped **Y**early.
  - H: Hadoop Common
  - C: Hadoop Distributed File System (HDFS)
  - F: Hadoop MapReduce
  - M: Hadoop YARN
  - Y: Yearly (to indicate the frequency of data processing)