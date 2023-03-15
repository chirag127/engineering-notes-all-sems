Compression in Hadoop io is the process of reducing the size of data files stored in Hadoop Distributed File System (HDFS) or transferred across the network or to or from disk. Compression can save space and speed up data transfer, which are important benefits when dealing with large volumes of data.

Hadoop supports various compression codecs, such as DEFLATE, gzip, bzip2, LZO, LZ4, and Snappy. Each codec has different characteristics, such as compression ratio, speed, and splittability. Splittability means that a compressed file can be split into smaller chunks and processed by multiple map tasks in parallel. Only bzip2 is splittable among the standard codecs, but some custom codecs, such as LZO with an index file, can also be splittable.

Hadoop provides a CodecFactory class that can detect the compression format of an input file based on the file extension and provide the appropriate CompressionCodec object. A CompressionCodec can create a CompressionInputStream or a CompressionOutputStream to read or write compressed data.

Here is a simplified ASCII diagram of compression in Hadoop io:

##### Compression in Hadoop io

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Input File   |       |  Compressed    |       |  Output File   |
|                |       |    File        |       |                |
+----------------+       +----------------+       +----------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       V                        V                        V
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
| Compression    |       |  CodecFactory  |       | Decompression  |
|   Output       |       |                |       |   Input        |
|   Stream       |       |                |       |   Stream       |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       V                        V                        V
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
| Compression    |       |  Compression   |       | Decompression  |
|   Codec        |       |    Codec       |       |   Codec        |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```