#### Hadoop archives in HDFS

- Hadoop archives (HAR) are a file archiving facility provided by Hadoop Distributed File System (HDFS).
- HAR files are used to compact small files in HDFS into larger files to reduce the load on the NameNode.
- HAR files are created using the `hadoop archive` command.
- The `hadoop archive` command takes a list of files and directories as input and creates a single HAR file as output.
- The HAR file is stored in HDFS and can be accessed using the `har://` URI scheme.
- HAR files can be used to improve the performance of MapReduce jobs by reducing the number of small files that need to be processed.
- HAR files can be unpacked using the `hadoop fs -cp` command.
- HAR files are read-only and cannot be modified once created.
- HAR files can be deleted using the `hadoop fs -rm` command.