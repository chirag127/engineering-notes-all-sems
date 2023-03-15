### Design of HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system designed for storing very large files with streaming data access patterns, running on clusters of commodity hardware .
- HDFS is based on the Google File System, which was originally built for the Apache Nutch web search engine project.
- HDFS has the following key design features   :
  - Fault tolerance: HDFS can handle failures of nodes, disks, or network by replicating data blocks across multiple machines and providing mechanisms for detecting and recovering from faults.
  - High throughput: HDFS can support high bandwidth data transfers by dividing files into fixed-size blocks and distributing them across the cluster. HDFS also uses a pipelined data transfer protocol to minimize network overhead and disk seek time.
  - Scalability: HDFS can scale to thousands of nodes and petabytes of data by using a master-slave architecture, where a single NameNode manages the namespace and metadata of the file system, and multiple DataNodes store and serve the data blocks.
  - Simplicity: HDFS does not impose any specific data structure or schema on the files, and does not support random writes or updates. HDFS is designed for batch processing rather than interactive use, and assumes that the applications have a streaming access pattern to the data.
  - Portability: HDFS can run on various platforms and operating systems, and can interoperate with other file systems and data sources. HDFS also provides a Java API and a command-line interface for accessing and manipulating the file system.