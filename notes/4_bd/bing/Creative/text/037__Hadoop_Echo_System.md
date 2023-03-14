#### Hadoop Ecosystem

The Hadoop Ecosystem is a platform or a suite that provides various services to solve the big data problems. It includes Apache projects and various commercial tools and solutions. It is based on Apache Hadoop, an open source framework that allows for the distributed storage and processing of large datasets across clusters of computers using simple programming models. Hadoop is designed to scale up from a single computer to thousands of clustered computers, with each machine offering local computation and storage. In this way, Hadoop can efficiently store and process large datasets ranging in size from gigabytes to petabytes of data .

There are four major elements of Hadoop i.e. HDFS, MapReduce, YARN, and Hadoop Common. Most of the tools or solutions are used to supplement or support these major elements. All these tools work collectively to provide services such as absorption, analysis, storage and maintenance of data etc.

- **HDFS**: Hadoop Distributed File System. It is the primary component of the Hadoop ecosystem and is responsible for storing large data sets of structured or unstructured data across various nodes and thereby maintaining the metadata in the form of log files. HDFS consists of two core components i.e. Name node and Data Node. Name Node is the prime node which contains metadata (data about data) requiring comparatively fewer resources than the data nodes that store the actual data. These data nodes are commodity hardware in the distributed environment. HDFS provides high-throughput access to application data with no need for schemas to be defined up front .
- **YARN**: Yet Another Resource Negotiator. It is a resource-management platform responsible for managing compute resources in clusters and using them to schedule users’ applications. It performs scheduling and resource allocation across the Hadoop system. It consists of three major components i.e. Resource Manager, Nodes Manager and Application Manager .
- **MapReduce**: It is a programming model for large-scale data processing. Using distributed and parallel computation algorithms, MapReduce makes it possible to carry over processing logic and helps to write applications that transform big datasets into one manageable set.
- **Hadoop Common**: It includes the libraries and utilities used and shared by other Hadoop modules. It provides the common functionality and abstraction for the Hadoop framework.

Beyond HDFS, YARN, and MapReduce, the entire Hadoop open source ecosystem continues to grow and includes many tools and applications to help collect, store, process, analyze, and manage big data. These include Apache Pig, Apache Hive, Apache HBase, Apache Spark, Presto, and Apache Zeppelin .

Some of the benefits of Hadoop are:

- **Fault tolerance**: Hadoop can handle hardware failures of individual machines or racks of machines by replicating data across a cluster so that it can be recovered easily should disk, node, or rack failures occur.
- **Cost control**: Hadoop can store data more affordably per terabyte than other platforms by using affordable standard commodity hardware instead of expensive specialized hardware.
- **Open source framework innovation**: Hadoop is backed by global communities united around introducing new concepts and capabilities faster and more effectively than internal teams working on proprietary solutions.

Hadoop is one of the most critical developments in Big Data. It provides tools for storing and analyzing data and a framework for other companies to develop their applications.