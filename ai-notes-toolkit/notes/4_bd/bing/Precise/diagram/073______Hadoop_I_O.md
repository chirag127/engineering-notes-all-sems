#### Hadoop I/O
Here is an ASCII diagram for Hadoop I/O:

```
+----------------+      +----------------+
|   Input File   |      |   Output File  |
|   (HDFS)       |      |   (HDFS)       |
+-------+--------+      +--------+-------+
        |                       ^
        |                       |
        v                       |
+-------+--------+      +--------+-------+
|   InputFormat  |      |   OutputFormat |
|   (MapReduce)  |      |   (MapReduce)  |
+-------+--------+      +--------+-------+
        |                       ^
        |                       |
        v                       |
+-------+--------+      +--------+-------+
|   RecordReader |      |   RecordWriter |
|   (MapReduce)  |      |   (MapReduce)  |
+-------+--------+      +--------+-------+
        |                       ^
        |                       |
        v                       |
+-------+--------+      +--------+-------+
|     Mapper     |----->|    Reducer     |
|   (MapReduce)  |      |   (MapReduce)  |
+----------------+      +----------------+
```
