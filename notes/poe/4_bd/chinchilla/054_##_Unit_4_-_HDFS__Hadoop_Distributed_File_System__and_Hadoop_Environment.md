## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

### Introduction

Hadoop is an open-source software framework used for distributed storage and processing of large datasets. Hadoop is based on the MapReduce programming model and the Hadoop Distributed File System (HDFS).

HDFS is a distributed file system designed to run on commodity hardware. It provides scalable and fault-tolerant storage for large datasets. Hadoop environment consists of multiple nodes, which are connected to each other to form a cluster. Each node in the cluster can be either a master node or a worker node.

### HDFS Architecture

HDFS is designed to store large files in a distributed environment. The architecture of HDFS consists of the following components:

1. NameNode: The NameNode is the master node in HDFS. It manages the file system namespace and regulates access to files by clients. It maintains information about the data blocks and their location in the cluster.

2. DataNode: The DataNode is the worker node in HDFS. It stores the actual data blocks of files. The DataNode communicates with the NameNode to report the status of the data blocks it stores and to receive instructions on where to store new data blocks.

3. Secondary NameNode: The Secondary NameNode is a helper node for the NameNode. It periodically merges the edits made to the file system namespace into a new checkpoint.

4. Client: The client is any application that needs to read or write data to HDFS. The client communicates with the NameNode to get the location of the data blocks and then communicates directly with the DataNodes to read or write the data.

### Hadoop Environment

Hadoop environment consists of a cluster of nodes, which are connected to each other to form a Hadoop cluster. Each node in the cluster can be either a master node or a worker node. The master node manages the cluster and coordinates the tasks that are executed on the worker nodes. The worker nodes perform the tasks assigned to them by the master node.

The Hadoop environment consists of the following components:

1. Hadoop Common: Hadoop Common contains the common utilities used by all the Hadoop modules.

2. Hadoop Distributed File System (HDFS): HDFS is used for storing large datasets in a distributed environment.

3. Hadoop MapReduce: Hadoop MapReduce is a programming model used for processing large datasets in a distributed environment.

4. YARN: YARN (Yet Another Resource Negotiator) is a resource management layer used to manage resources in a Hadoop cluster.

### Advantages of HDFS

1. Scalability: HDFS is designed to scale to petabytes of data. It can handle large files and large clusters of nodes.

2. Fault tolerance: HDFS is designed to be fault-tolerant. It can handle node failures and data corruption.

3. High throughput: HDFS is designed to provide high throughput for data-intensive applications.

### Learning Tricks

1. Remember that HDFS is designed to store and retrieve large files in a distributed environment.

2. Keep in mind that Hadoop environment consists of multiple nodes, which are connected to each other to form a cluster.

3. Remember that the NameNode is the master node in HDFS, and it manages the file system namespace and regulates access to files by clients.

4. Keep in mind that the DataNode is the worker node in HDFS, and it stores the actual data blocks of files.

5. Remember that HDFS is designed to be fault-tolerant and can handle node failures and data corruption.

6. Keep in mind that YARN is a resource management layer used to manage resources in a Hadoop cluster.

### Conclusion

HDFS is a distributed file system designed to store and retrieve large files in a distributed environment. Hadoop environment consists of multiple nodes, which are connected to each other to form a cluster. HDFS is designed to be fault-tolerant and can handle node failures and data corruption. YARN is a resource management layer used to manage resources in a Hadoop cluster. Understanding the architecture and components of HDFS and Hadoop environment is essential for working with big data and data-intensive applications.