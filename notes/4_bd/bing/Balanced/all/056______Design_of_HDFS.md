#### Design of HDFS

HDFS stands for Hadoop Distributed File System. It is a file system that is designed to store very large files across multiple machines in a cluster. HDFS is part of the Hadoop ecosystem, which is a framework for processing and analyzing big data.

Some of the key features and design principles of HDFS are:

- **Fault tolerance**: HDFS can handle failures of machines, disks, or network by replicating data blocks across multiple nodes. The default replication factor is 3, which means each block is stored on 3 different nodes. If a node fails, the data can be accessed from another replica. HDFS also performs checksums to detect and correct corrupted data blocks.
- **Scalability**: HDFS can scale to thousands of nodes and petabytes of data by adding more machines to the cluster. HDFS does not impose any limit on the size or number of files that can be stored. HDFS also supports horizontal scaling, which means adding more machines without changing the existing ones.
- **Streaming data access**: HDFS is optimized for sequential read and write operations, rather than random access. HDFS supports high throughput of data by using large data blocks (typically 128 MB or 256 MB) and transferring data in parallel across the cluster. HDFS also supports compression and decompression of data blocks to reduce the network bandwidth and disk space usage.
- **Simple and robust coherency model**: HDFS follows a write-once-read-many model, which means a file can be written only once and then read multiple times. This simplifies the consistency and concurrency issues that arise in distributed systems. HDFS also provides atomic and visible file renames and appends, which means the changes are either applied completely or not at all, and are visible to all readers immediately.
- **Rack awareness**: HDFS is aware of the physical location of the nodes in the cluster, such as which rack they belong to. This helps HDFS to optimize the data placement and replication strategy based on the network topology and bandwidth. For example, HDFS tries to place replicas of a block on different racks to improve the availability and reliability of the data.

A mnemonic to remember the key features and design principles of HDFS is:

**F**ault tolerance
**S**calability
**S**treaming data access
**S**imple and robust coherency model
**R**ack awareness

FSSSR or **F**ive **S**tar **R**ating.