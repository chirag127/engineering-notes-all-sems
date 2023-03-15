#### Hadoop file system interfaces

```
+---------------------+
|   User Application  |
+---------------------+
          |
          |
          V
+---------------------+
|  Hadoop Filesystem  |
|       Interface     |
+---------------------+
          |
          |
          V
+---------------------+
|  Local Filesystem   |
|   HDFS, S3, etc.    |
+---------------------+
```

The Hadoop filesystem interface provides a common abstraction for different filesystem implementations, such as local filesystem, HDFS, S3, etc. This allows user applications to interact with different filesystems using the same interface. The diagram above illustrates the relationship between the user application, the Hadoop filesystem interface, and the underlying filesystem implementation.