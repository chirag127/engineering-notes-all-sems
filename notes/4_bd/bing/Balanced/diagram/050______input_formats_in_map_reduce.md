InputFormat is the first step in MapReduce job execution. It describes how to split and read input files from HDFS. InputFormat also creates input splits and divides them into records, which are then assigned to individual mappers. There are different types of InputFormat, such as FileInputFormat, TextInputFormat, KeyValueTextInputFormat, SequenceFileInputFormat, etc. Each type has its own way of reading and processing the input data.

A possible ASCII diagram for input formats in MapReduce is:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Input File 1  |      |  Input File 2  |      |  Input File 3  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  InputFormat   |      |  InputFormat   |      |  InputFormat   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  InputSplit 1  |      |  InputSplit 2  |      |  InputSplit 3  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Mapper 1    |      |    Mapper 2    |      |    Mapper 3    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```