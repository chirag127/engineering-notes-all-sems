InputFormat is the first step in MapReduce job execution. It describes how to split and read input files. Input files store the data for MapReduce job and reside in HDFS. InputFormat is also responsible for creating the input splits and dividing them into records. Input splits are logical chunks of data that are assigned to different mappers for parallel processing. Records are key-value pairs that represent the input data for the mapper function.

There are different types of InputFormat in MapReduce, such as FileInputFormat, TextInputFormat, KeyValueTextInputFormat, SequenceFileInputFormat, SequenceFileAsTextInputFormat, SequenceFileAsBinaryInputFormat, NLineInputFormat, and DBInputFormat. Each type of InputFormat has its own way of splitting and reading the input files.

The following diagram illustrates the basic architecture of a MapReduce job with different types of InputFormat:

```
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|  Input File 1  |    |  Input File 2  |    |  Input File 3  |    |  Input File 4  |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       v                     v                     v                     v
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|  InputFormat   |    |  InputFormat   |    |  InputFormat   |    |  InputFormat   |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       v                     v                     v                     v
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|  Input Split 1 |    |  Input Split 2 |    |  Input Split 3 |    |  Input Split 4 |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       |                     |                     |                     |
       v                     v                     v                     v
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|    Mapper 1    |    |    Mapper 2    |    |    Mapper 3    |    |    Mapper 4    |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+
```