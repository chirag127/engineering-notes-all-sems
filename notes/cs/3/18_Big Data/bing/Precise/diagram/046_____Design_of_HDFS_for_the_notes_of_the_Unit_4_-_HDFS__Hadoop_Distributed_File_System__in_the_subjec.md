### Design of HDFS

HDFS (Hadoop Distributed File System) is a distributed file system designed for storing very large files with streaming data access patterns, running on clusters of commodity hardware. Here are some key points about the design of HDFS:

- The design of HDFS was based on the Google File System.
- It was originally built as infrastructure for the Apache Nutch web search engine project but has since become a member of the Hadoop Ecosystem.
- HDFS is designed to reliably store very large files across machines in a large cluster.
- The emphasis is on high throughput of data access rather than low latency of data access.
- HDFS is designed more for batch processing rather than interactive use by users.
- POSIX imposes many hard requirements that are not needed for applications that are targeted for HDFS.