#### Design of HDFS

Hadoop Distributed File System (HDFS) is a distributed file system that provides scalable and reliable storage for large-scale data processing applications. The design of HDFS is based on the following principles:

- **Large Data Sets:** HDFS is designed to store and manage large data sets. The default block size in HDFS is 128MB, which can be configured based on the requirements of the application.

- **Streaming Data Access:** HDFS is optimized for streaming data access, where data is written once and read many times. This makes it suitable for applications that require high throughput, such as batch processing and data warehousing.

- **Fault Tolerance:** HDFS is designed to be fault-tolerant. Data is replicated across multiple nodes in the cluster to ensure reliability and availability. If a node fails, the data can be retrieved from another node.

- **Data Locality:** HDFS is designed to optimize data locality. This means that data is stored on nodes where it is processed, which reduces network traffic and improves performance.

- **Simple Coherency Model:** HDFS has a simple coherency model. When a file is written to HDFS, it is visible to all readers immediately. There is no need for locking or other complex synchronization mechanisms.

- **Metadata Operations:** HDFS separates metadata operations from data operations. This allows for efficient processing of large data sets, as metadata operations are not a bottleneck.

- **Scalability:** HDFS is designed to be scalable. It can support clusters with thousands of nodes and petabytes of data.

Overall, the design of HDFS is focused on providing reliable, scalable, and high-performance storage for large data sets. It is optimized for batch processing and data warehousing applications, and provides fault tolerance, data locality, and a simple coherency model.