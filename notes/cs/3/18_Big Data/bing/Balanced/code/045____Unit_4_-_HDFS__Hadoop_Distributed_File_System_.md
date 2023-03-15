## Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that handles large data sets running on commodity hardware. It is one of the major components of Apache Hadoop, the others being MapReduce and YARN.

Some of the key features and characteristics of HDFS are:

- HDFS is designed to store very large files across multiple machines. It can scale up to thousands of nodes and petabytes of data.
- HDFS is highly fault-tolerant and resilient to hardware failures. It replicates each block of data to multiple nodes to ensure availability and durability.
- HDFS follows a master/slave architecture, where a single NameNode manages the file system namespace and metadata, and multiple DataNodes store and serve the actual data blocks .
- HDFS supports a write-once-read-many model, where files are written in large sequential blocks by a single writer, and then read by multiple readers. HDFS does not support random writes or modifications to existing files.
- HDFS provides a simple and consistent interface to access data, using the standard Java API, the Hadoop shell commands, or the Hadoop web UI.
- HDFS is optimized for batch processing and high-throughput access, rather than low-latency access. It is suitable for applications that need to scan large amounts of data, such as MapReduce jobs .