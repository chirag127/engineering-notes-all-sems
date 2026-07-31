### Design of HDFS

HDFS is a distributed file system that is designed to store very large files across multiple nodes in a cluster. It is part of the Apache Hadoop ecosystem and is based on the Google File System. HDFS has the following design features:

- **Fault tolerance:** HDFS can handle node failures and data corruption by replicating data blocks across multiple nodes. It also has mechanisms to detect and recover from failures, such as checksums, heartbeats, and block reports.
- **Scalability:** HDFS can scale to thousands of nodes and petabytes of data by distributing the workload and the metadata across the cluster. It also supports horizontal scaling by adding or removing nodes without disrupting the system.
- **High throughput:** HDFS is optimized for batch processing of large files with streaming data access patterns. It achieves high throughput by using large block sizes (typically 128 MB), pipelined data transfers, and data locality optimization.
- **Simple and robust coherency model:** HDFS follows a write-once-read-many model, where files are appended to but not modified after creation. This simplifies the consistency and concurrency issues and improves the performance and reliability of the system.
- **Portability:** HDFS is written in Java and can run on various platforms and hardware configurations. It also supports different file formats and compression codecs.