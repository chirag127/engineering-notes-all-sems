 Here is the formal content on file sizes in HDFS in Markdown format:

#### File Sizes in HDFS

1. HDFS is designed to store very large files with streaming access patterns, running on clusters of commodity hardware.
2. The default block size in HDFS is 128MB. This means that any file size in HDFS is always a multiple of 128MB. For example, a file of size 256MB will be stored as 2 blocks of size 128MB each.
3. The default replication factor in HDFS is 3. This means that for every block of data, there will be 3 replicas stored on different DataNodes for fault tolerance.
4. Hence, for a file of size 256MB with default settings, there will be:
- 2 blocks of 128MB each
- 2 x 3 = 6 replicas of each 128MB block
- Total 6 blocks stored = 6 x 128MB = 768MB storage space

The large block size and replication factor in HDFS allows for streaming access of large files, and also provides fault tolerance for the data. The trade-off is that HDFS is not suitable for small file storage or frequent random access of files. HDFS is optimized for throughput of large files instead of latency.

How's that? I have written the content in points in a formal tone without any emojis or external links as instructed. Let me know if you would like me to modify or expand the content in any way.