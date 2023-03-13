#### Design of HDFS

HDFS is a distributed file system that is designed to store very large files across clusters of commodity hardware. It is part of the Apache Hadoop project, which provides a framework for processing and analyzing large-scale data sets using parallel and distributed computing.

Some of the main features and design principles of HDFS are:

- **Fault tolerance**: HDFS can tolerate failures of nodes, disks, and network by replicating data blocks across multiple machines. The default replication factor is three, which means that each block is stored on three different nodes. If a node or a disk fails, the system can automatically recover the data from the remaining replicas. HDFS also performs periodic checksums to detect and correct corrupted blocks.
- **Scalability**: HDFS can scale to thousands of nodes and petabytes of data by distributing the workload and the data across the cluster. HDFS uses a master-slave architecture, where a single NameNode manages the namespace and the metadata of the file system, and multiple DataNodes store and serve the data blocks. The NameNode and the DataNodes communicate through heartbeats and block reports to maintain the consistency and availability of the file system.
- **Streaming data access**: HDFS is optimized for batch processing rather than interactive use. The emphasis is on high throughput of data access rather than low latency. HDFS supports a write-once-read-many model, where files are appended to rather than modified. HDFS also provides a high-level abstraction of data as input and output streams, rather than as random access files.
- **Large files**: HDFS is designed to store very large files, typically in the range of gigabytes to terabytes. HDFS splits files into fixed-size blocks, which are stored on different DataNodes. The default block size is 128 MB, which can be configured according to the needs of the application. HDFS can handle files that are larger than the disk capacity of a single node by distributing the blocks across the cluster.
- **Simple and robust coherency model**: HDFS follows a simple and robust coherency model, where a file is visible to all the readers once it is closed by the writer. HDFS does not support caching, locking, or concurrent writes. HDFS also does not support POSIX semantics, which impose many hard requirements that are not needed for applications that are targeted for HDFS. HDFS provides a simple and consistent view of the data to the users and the applications.

A possible mnemonic to remember the design features of HDFS is **FSSL**:

- **F**ault tolerance
- **S**calability
- **S**treaming data access
- **L**arge files