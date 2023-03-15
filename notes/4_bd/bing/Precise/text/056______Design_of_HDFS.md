#### Design of HDFS
- HDFS stands for Hadoop Distributed File System.
- The design of HDFS was based on the Google File System.
- It was originally built as infrastructure for the Apache Nutch web search engine project but has since become a member of the Hadoop Ecosystem.
- HDFS is a filesystem designed for storing very large files with streaming data access patterns, running on clusters of commodity hardware.
- HDFS is designed to reliably store very large files across machines in a large cluster.
- HDFS is designed more for batch processing rather than interactive use by users. The emphasis is on high throughput of data access rather than low latency of data access.
- POSIX imposes many hard requirements that are not needed for applications that are targeted for HDFS.