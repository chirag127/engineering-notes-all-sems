Compression in Hadoop io is the process of reducing the size of data files stored in Hadoop Distributed File System (HDFS) or transferred between nodes in a MapReduce job. Compression can save storage space, network bandwidth, and disk I/O, and improve the performance of Hadoop applications.

Hadoop supports various compression codecs, such as DEFLATE, gzip, bzip2, LZO, LZ4, and Snappy. Each codec has different characteristics in terms of compression ratio, speed, and splittability. Splittability means that a compressed file can be split into smaller chunks and processed by multiple map tasks in parallel. Only bzip2 is splittable among the standard codecs, but some third-party codecs like LZO can also be made splittable with the help of index files.

Hadoop provides a CodecFactory class that can detect the compression format of an input file based on its extension and return the appropriate CompressionCodec object. A CompressionCodec can be used to create an InputStream or an OutputStream that can read or write compressed data. Hadoop also provides a CompressionInputStream and a CompressionOutputStream class that can handle direct byte buffers for faster compression and decompression.

The following diagram illustrates the basic architecture of compression in Hadoop io using ASCII characters:

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Input File      |     |  Compressed File |     |  Output File     |
|  (e.g. text.txt) |     |  (e.g. text.gz)  |     |  (e.g. text.out) |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
       |                       |                       ^
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
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       v                       |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  InputStream     |     |  CompressionCodec|     |  OutputStream    |
|  (e.g. FSDataInputStream) |  (e.g. GzipCodec)  |  (e.g. FSDataOutputStream) |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
       |                       |                       ^
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
       |                       v                       |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  CompressionInputStream |  CompressionOutputStream|  CompressionInputStream |
|  (e.g. GzipInputStream) |  (e.g. GzipOutputStream) |  (e.g. GzipInputStream) |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
       |                       |                       ^
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       v                       |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  MapReduce Job   |     |  HDFS            |     |  MapReduce Job   |
|  (e.g. WordCount) |     |  (e.g. /user/hadoop) |     |  (e.g. WordCount) |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
```