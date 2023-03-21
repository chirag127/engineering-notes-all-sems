### Java Interfaces to HDFS

Java interfaces to HDFS are the application programming interfaces (APIs) that allow Java applications to interact with the Hadoop Distributed File System (HDFS). In this unit, we will cover the following Java interfaces to HDFS:

1. `org.apache.hadoop.fs.FileSystem`: This interface is used to represent a file system object in Hadoop. It provides methods to perform various operations on the file system, such as creating, deleting, and opening files, as well as listing directories.

2. `org.apache.hadoop.fs.Path`: This interface represents a path in Hadoop. It provides methods to manipulate paths, such as joining them together, checking if they are absolute or relative, and resolving one path against another.

3. `org.apache.hadoop.fs.FSDataInputStream` and `org.apache.hadoop.fs.FSDataOutputStream`: These interfaces are used to read from and write to files in Hadoop. They provide methods to read and write bytes, seek to a particular position in a file, and close the file.

4. `org.apache.hadoop.fs.FileStatus`: This interface represents the status of a file or directory in Hadoop. It provides methods to get information about the file or directory, such as its length, modification time, owner, and permissions.

5. `org.apache.hadoop.fs.FileSystem.Statistics`: This interface provides statistics about the file system, such as the number of bytes read and written, the number of files created and deleted, and the number of operations performed.

Using these Java interfaces, Java applications can easily interact with HDFS and perform various operations on files and directories. In addition, Hadoop provides a number of utility classes that make it easy to work with these interfaces, such as `org.apache.hadoop.fs.FileSystem#get` and `org.apache.hadoop.fs.FileSystem#newInstance`, which can be used to obtain instances of the `FileSystem` interface.