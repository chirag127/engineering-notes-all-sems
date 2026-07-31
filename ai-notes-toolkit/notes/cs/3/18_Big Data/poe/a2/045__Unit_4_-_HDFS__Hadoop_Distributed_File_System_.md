 Here is the content in Markdown format without any emojis or external links as per your instructions:

## Unit 4 - HDFS (Hadoop Distributed File System)

1. HDFS is the primary storage system used by Hadoop applications. It is designed to store very large data sets reliably, and to stream those data sets at high bandwidth to user applications.

2. HDFS has a master/slave architecture. An HDFS cluster consists of a single NameNode, a master server that manages the file system namespace and regulates access to files by clients. In addition, there are a number of DataNodes, usually one per node in the cluster, which manages storage attached to the nodes that they run on.

3. HDFS provides high throughput access to application data and is suitable for applications that have large data sets. HDFS is designed to be very fault-tolerant, with data redundancy so that in the event of data loss, the data can be easily recovered without loss of accessibility.

4. The main benefits of HDFS are:

- Scalability - HDFS can scale to store and process very large data sets on commodity hardware.
- Fault Tolerance - HDFS is designed to be reliable and fault-tolerant, with high data redundancy and no single point of failure.
- Streaming Access - HDFS supports streaming access of files at high throughput.
- Simplicity - HDFS has a simple design that facilitates easy understanding, deployment and maintenance.

5. The key components of HDFS are:

- NameNode - The master node that manages the file system namespace and regulates access to files by clients.
- DataNode - Each node in the cluster that stores data and serves read/write requests from clients.
- Client - The application that interacts with the NameNode and accesses data from DataNodes.

The content is written in a formal tone with points in Markdown format as per your instructions. Please let me know if you would like me to modify or expand the content in any way.