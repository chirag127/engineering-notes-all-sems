Hadoop file system interfaces are the Java abstract classes and interfaces that represent the client interface to a file system in Hadoop. There are several concrete implementations of these interfaces, such as HDFS, S3, FTP, etc. Hadoop uses the URI scheme to select the appropriate file system instance to communicate with.

#### Hadoop file system interfaces

The following is a simplified ASCII diagram of the Hadoop file system interfaces and some of their implementations:

```
+---------------------+    +---------------------+
| org.apache.hadoop.fs|    | org.apache.hadoop.fs|
|       .FileSystem   |    |    .FSDataInputStream|
+---------------------+    +---------------------+
| +get(URI,Config)    |    | +read()             |
| +create(Path)       |    | +seek()             |
| +open(Path)         |    | +skip()             |
| +delete(Path)       |    | +close()            |
| +rename(Path,Path)  |    +---------------------+
| +listStatus(Path)   |    |                     |
| +setReplication()   |    |                     |
| +mkdirs(Path)       |    |                     |
| +getFileStatus(Path)|    |                     |
+---------------------+    |                     |
       ^                   |                     |
       |                   |                     |
       |                   |                     |
+---------------------+    |                     |
| org.apache.hadoop.fs|    |                     |
|  .FilterFileSystem  |    |                     |
+---------------------+    |                     |
| +create(Path)       |    |                     |
| +open(Path)         |    |                     |
| +delete(Path)       |    |                     |
| +rename(Path,Path)  |    |                     |
| +listStatus(Path)   |    |                     |
| +setReplication()   |    |                     |
| +mkdirs(Path)       |    |                     |
| +getFileStatus(Path)|    |                     |
+---------------------+    |                     |
       ^                   |                     |
       |                   |                     |
       |                   |                     |
+---------------------+    |                     |
| org.apache.hadoop.fs|    |                     |
|    .LocalFileSystem |    |                     |
+---------------------+    |                     |
| +create(Path)       |    |                     |
| +open(Path)         |    |                     |
| +delete(Path)       |    |                     |
| +rename(Path,Path)  |    |                     |
| +listStatus(Path)   |    |                     |
| +setReplication()   |    |                     |
| +mkdirs(Path)       |    |                     |
| +getFileStatus(Path)|    |                     |
+---------------------+    |                     |
       ^                   |                     |
       |                   |                     |
       |                   |                     |
+---------------------+    |                     |
| org.apache.hadoop.fs|    |                     |
|    .RawLocalFileSystem|  |                     |
+---------------------+    |                     |
| +create(Path)       |    |                     |
| +open(Path)         |    |                     |
| +delete(Path)       |    |                     |
| +rename(Path,Path)  |    |                     |
| +listStatus(Path)   |    |                     |
| +setReplication()   |    |                     |
| +mkdirs(Path)       |    |                     |
| +getFileStatus(Path)|    |                     |
+---------------------+    |                     |
       ^                   |                     |
       |                   |                     |
       |                   |                     |
+---------------------+    |                     |
| org.apache.hadoop.fs|    |                     |
|    .Hdfs            |    |                     |
+---------------------+    |                     |
| +create(Path)       |    |                     |
| +open(Path)         |    |                     |
| +delete(Path)       |    |                     |
| +rename(Path,Path)  |    |                     |
| +listStatus(Path)   |    |                     |
| +setReplication()   |    |                     |
| +mkdirs(Path)       |    |                     |
| +getFileStatus(Path)|    |                     |
+---------------------+    |                     |
       ^                   |                     |
       |                   |                     |
       |                   |                     |
+---------------------+    |                     |
| org.apache.hadoop.fs|    |                     |
|    .S3FileSystem    |    |                     |
+---------------------+    |                     |
| +create(Path)       |