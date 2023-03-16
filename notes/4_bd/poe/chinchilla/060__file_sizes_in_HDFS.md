#### File Sizes in HDFS

When working with Hadoop Distributed File System (HDFS), it is important to understand file sizes and how they are handled. Here are some key points to keep in mind:

- HDFS is designed to handle large files, typically in the range of gigabytes to terabytes. It is not optimized for small files.
- In HDFS, files are split into blocks, which are typically 128 MB in size. The actual block size can be configured, but it is generally recommended to use the default size.
- When a file is uploaded to HDFS, it is split into blocks and each block is stored on a different node in the cluster. This allows for parallel processing of the file.
- The last block of a file may be smaller than the block size. This is known as the "under-replicated block" and it is replicated to ensure data redundancy.
- When a file is deleted from HDFS, the blocks are not immediately deleted. Instead, they are marked as "trash" and are only deleted after a configurable amount of time.
- HDFS provides a command-line tool called `hadoop fs -du` to display the size of files and directories in HDFS. The output shows the size in bytes, as well as the size in human-readable format (e.g. KB, MB, GB, etc.).
- HDFS also provides a web-based user interface called the Hadoop NameNode UI, which displays information about the files and blocks stored in HDFS.

In summary, understanding file sizes and how they are handled in HDFS is important for efficient and effective use of the system. HDFS is optimized for handling large files and uses block-based storage for parallel processing. The `hadoop fs -du` command and the Hadoop NameNode UI are useful tools for monitoring file sizes in HDFS.