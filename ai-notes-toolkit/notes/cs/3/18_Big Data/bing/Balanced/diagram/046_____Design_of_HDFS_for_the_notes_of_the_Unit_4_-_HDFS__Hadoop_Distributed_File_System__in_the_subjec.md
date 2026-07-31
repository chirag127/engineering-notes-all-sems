### Design of HDFS

HDFS is a distributed file system that is designed to store very large files across multiple nodes in a cluster. It is part of the Apache Hadoop ecosystem and is based on the Google File System. HDFS has the following design features:

- **Fault tolerance:** HDFS can tolerate failures of nodes, disks, and network by replicating data blocks across multiple nodes. It also has mechanisms to detect and recover from failures, such as checksums, heartbeats, and block reports.
- **Scalability:** HDFS can scale to thousands of nodes and petabytes of data by distributing the workload and the data across the cluster. It also supports horizontal scaling, which means adding more nodes to the cluster without changing the existing ones.
- **High throughput:** HDFS is optimized for batch processing of large files with streaming data access patterns. It provides high throughput of data by using large block sizes (typically 128 MB or 256 MB), pipelined data transfers, and data locality optimization.
- **Simple and robust coherency model:** HDFS follows a write-once-read-many model, which means that a file can be written by only one writer at a time, and can be read by multiple readers concurrently. This simplifies the consistency and concurrency issues, and avoids the need for locking mechanisms.
- **Portability:** HDFS can run on various platforms and hardware configurations, as it is written in Java and uses a standard file system interface. It also supports heterogeneous clusters, which means that nodes can have different hardware specifications and capacities.