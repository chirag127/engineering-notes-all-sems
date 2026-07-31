### File sizes for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

- HDFS is a distributed file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS is designed to handle very large files, typically in the range of gigabytes to terabytes.
- HDFS splits large files into fixed-size blocks, usually 128 MB or 256 MB, and distributes them across the cluster nodes.
- HDFS provides fault tolerance by replicating each block on multiple nodes, usually three by default.
- HDFS allows users to access the files as a single logical unit, regardless of how they are physically stored or replicated.
- HDFS supports high throughput by providing parallel access to the blocks from multiple nodes.
- HDFS is optimized for batch processing rather than interactive or random access.
- HDFS follows a master-slave architecture, where a single NameNode manages the metadata of the file system, and multiple DataNodes store and serve the blocks.
- HDFS provides a command-line interface and a Java API for users to interact with the file system.