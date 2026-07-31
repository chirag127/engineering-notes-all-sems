### File Sizes - Unit 4: HDFS (Hadoop Distributed File System)

1. HDFS is designed to handle very large files, with the default block size being 128 MB.
2. Files in HDFS are broken down into blocks, and each block is stored on multiple DataNodes for redundancy.
3. The NameNode keeps track of the location of each block and coordinates access to the file data.
4. HDFS can handle files that are much larger than the available physical memory on the cluster.
5. The maximum file size that HDFS can handle is determined by the available storage capacity of the cluster and the configured block size.
6. Larger block sizes can improve performance for large files, but may result in inefficient use of storage for small files.
7. HDFS supports appending to files, but does not support random writes.
8. Files in HDFS are write-once and have strictly one writer at any time.
