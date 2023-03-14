Compression in Hadoop io is the process of reducing the size of data files or streams to save disk space, network bandwidth, and processing time. Hadoop supports various compression codecs, such as DEFLATE, gzip, bzip2, LZO, LZ4, and Snappy, which can be applied to different types of files or streams. Compression can be performed at different stages of the Hadoop pipeline, such as input, output, intermediate, or shuffle and sort.

The following diagram illustrates the basic architecture of a Hadoop mapreduce job with compression enabled at different stages:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Input File    |      |  Output File   |      |  Output File   |
|  (compressed)  |      |  (compressed)  |      |  (uncompressed)|
|                |      |                |      |                |
+-------+--------+      +--------+-------+      +--------+-------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
+-------v--------+      +-------v--------+      +--------v-------+
|                |      |                |      |                |
|  Input Split   |      |  Output Split  |      |  Output Split  |
|  (compressed)  |      |  (compressed)  |      |  (uncompressed)|
|                |      |                |      |                |
+-------+--------+      +--------+-------+      +--------+-------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
+-------v--------+      +-------v--------+      +--------v-------+
|                |      |                |      |                |
|  Map Task      |      |  Reduce Task   |      |  Reduce Task   |
|  (uncompressed)|      |  (uncompressed)|      |  (uncompressed)|
|                |      |                |      |                |
+-------+--------+      +--------+-------+      +--------+-------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
+-------v--------+      +-------v--------+      +--------v-------+
|                |      |                |      |                |
|  Map Output    |      |  Reduce Input  |      |  Reduce Output |
|  (compressed)  |      |  (compressed)  |      |  (uncompressed)|
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```