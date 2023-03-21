### Hadoop Archives

Hadoop Archives (HAR) is a file format that helps in storing large amounts of small files in Hadoop Distributed File System (HDFS). HAR is used to archive small files into a single file, which reduces the NameNode memory usage and improves the overall performance of the Hadoop cluster.

Here are some important points about Hadoop Archives:

- Hadoop Archives are created using the Hadoop archive tool (`hadoop archive`), which is a command-line tool used to create and manipulate HAR files.
- HAR files are immutable, which means that once a HAR file is created, it cannot be modified.
- HAR files can be used just like any other Hadoop file. They can be read, written, and moved between different HDFS directories.
- The `hadoop archive` tool provides various options to create and manipulate HAR files. For example, you can specify the number of files to be included in each HAR file, the compression codec to be used, and the HDFS path where the HAR file should be created.
- HAR files are particularly useful for storing log files, small images, and other small files that are generated frequently by applications.
- HAR files are stored in a compressed format, which reduces the storage requirements and improves the overall performance of the Hadoop cluster.
- HAR files are transparent to the applications that use them. That is, applications do not need to know whether the data is stored in a HAR file or not. They can simply access the data as if it were stored in a regular Hadoop file.

In conclusion, Hadoop Archives are a useful feature of Hadoop that helps in storing large amounts of small files in a more efficient manner. They provide a simple and transparent way of archiving data in HDFS, which reduces the NameNode memory usage and improves the performance of the Hadoop cluster.