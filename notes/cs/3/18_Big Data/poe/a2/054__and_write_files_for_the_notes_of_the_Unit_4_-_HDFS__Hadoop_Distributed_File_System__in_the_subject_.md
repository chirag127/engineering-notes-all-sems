 Here are the notes for Unit 4 - HDFS (Hadoop Distributed File System) in markdown format:

### HDFS (Hadoop Distributed File System)

- HDFS is the primary storage system used by Hadoop applications. It is designed to store very large data sets reliably, and to stream those data sets at high bandwidth to user applications.
- HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware.
- HDFS provides high throughput access to application data and is suitable for applications that have large data sets.
- HDFS is designed to run on commodity hardware. It has many redundant data and system elements and can continue operation in spite of failures and it prioritizes high throughput over low latency.
- The HDFS architecture consists of a master/slave topology. The HDFS architecture consists of a single NameNode and a cluster of DataNodes.

The NameNode is responsible for managing the file system namespace and regulating access to files by clients. The DataNodes are responsible for serving read/write requests from the file system's clients. The NameNode and DataNodes are pieces of software designed to run on commodity machines.

The files in HDFS are broken into large blocks (typically 128 megabytes) and designed for streaming access of large files. The blocks are replicated for fault tolerance. The replication factor can be configured based on the durability requirements.

The advantages of HDFS are:

- Fault Tolerance - HDFS is designed to be highly fault-tolerant and designed to reliably store very large files across machines in a large cluster.
- Scalability - HDFS is scalable and designed to store very large data sets reliably and designed to scale to tens of petabytes.
- Simple Coherency Model - The HDFS has a simple coherency model for file consistency.
- Streaming Data Access - The HDFS supports streaming access of files.
- Low Cost - HDFS runs on clusters of commodity machines which makes it low cost.

The limitations of HDFS are:

- Not suitable for low latency data access. HDFS is designed and optimized for throughput rather than latency.
- Limited Number of Files - HDFS is optimized for handling files that are hundreds of megabytes or gigabytes in size as it has a limit on the number of files in a single HDFS cluster.
- Not suited for Random Writes - HDFS is optimized for streaming reads and writes of large files and is not suitable for random writes.