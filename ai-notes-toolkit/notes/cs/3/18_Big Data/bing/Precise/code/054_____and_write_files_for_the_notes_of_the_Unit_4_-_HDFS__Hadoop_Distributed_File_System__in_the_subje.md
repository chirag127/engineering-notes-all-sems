### Unit 4 - HDFS (Hadoop Distributed File System)

Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It is a part of the Apache Hadoop project and is used to store and process large datasets.

1. **Architecture:** HDFS has a master/slave architecture. The master node, called the NameNode, manages the file system namespace and regulates access to files by clients. The slave nodes, called DataNodes, store the data blocks of the files and serve read and write requests from the clients.

2. **Data Replication:** HDFS replicates data blocks across multiple DataNodes to ensure data availability and fault tolerance. The default replication factor is 3, meaning that each data block is stored on 3 different DataNodes.

3. **Data Blocks:** HDFS stores files as a sequence of blocks. The default block size is 128 MB, but it can be configured by the user.

4. **Data Locality:** HDFS tries to place data blocks on the same node or rack as the client accessing the data to reduce network traffic and improve performance.

5. **Scalability:** HDFS can scale to store and process petabytes of data by adding more DataNodes to the cluster.

6. **High Availability:** HDFS supports high availability through the use of multiple NameNodes. In the event of a failure of the primary NameNode, a secondary NameNode can take over its responsibilities.

7. **Accessing Data:** Data in HDFS can be accessed through the Hadoop command line, the Hadoop API, or through other tools such as Apache Hive and Apache Pig.

8. **Security:** HDFS supports Kerberos authentication and authorization through Access Control Lists (ACLs).
