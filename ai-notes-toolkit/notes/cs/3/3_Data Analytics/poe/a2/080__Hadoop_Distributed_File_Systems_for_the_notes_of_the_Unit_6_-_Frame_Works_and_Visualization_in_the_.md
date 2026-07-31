 Here is the content in markdown format without any emojis or external links for the topic "Hadoop Distributed File Systems" for Unit 6 notes on Frameworks and Visualization in Data Analytics:

### Hadoop Distributed File Systems

- Hadoop Distributed File System (HDFS) is a distributed file system that handles large data sets running on commodity hardware.
- It is highly fault-tolerant and is designed to be deployed on low-cost hardware.
- HDFS provides high throughput access to application data and is suitable for applications that have large data sets.
- HDFS is designed to hold very large data sets (typically in terabytes or petabytes).
- The HDFS architecture is based on the master/slave model. The Namenode is the master server that manages the file system namespace and regulates access to files by clients. The Datanodes are slave nodes that store data and serve read/write requests from clients.
- Data gets broken into large blocks that get distributed across multiple servers for redundancy and fault tolerance.
- The data blocks are replicated on multiple DataNodes based on a replication factor. This provides fault tolerance and ensures data is not lost in case of DataNode failure.
- HDFS offers a Write Once Read Many access model. It is optimized for batch processing of large data sets. Random writes are not efficient as the blocks are immutable.
- HDFS provides interfaces for Java programs and comes with additional features like snapshots, datanode enter/exit safe mode, balancer etc.

[No emojis or external links have been included as per the given instructions]