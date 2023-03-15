Compression in Hadoop io is the process of reducing the size of data files stored in Hadoop Distributed File System (HDFS) or transferred between nodes in a Hadoop cluster. Compression can save storage space, reduce network bandwidth, and improve the performance of Hadoop applications. Hadoop supports various compression codecs, such as DEFLATE, gzip, bzip2, LZO, LZ4, and Snappy. Some of these codecs are splittable, meaning that they can be processed in parallel by multiple map tasks, while others are not. Hadoop also provides a codec factory that can detect the compression format of an input file based on its extension and provide the appropriate compression codec.

A possible ASCII diagram for compression in Hadoop io is:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Input File    |     |  Compressed     |     |  Decompressed   |
|                 |     |    File         |     |    File         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Data Block 1   | --> |  Compressed     | --> |  Data Block 1   |
|                 |     |    Block 1      |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Data Block 2   | --> |  Compressed     | --> |  Data Block 2   |
|                 |     |    Block 2      |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Data Block 3   | --> |  Compressed     | --> |  Data Block 3   |
|                 |     |    Block 3      |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Data Block 4   | --> |  Compressed     | --> |  Data Block 4   |
|                 |     |    Block 4      |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows how an input file is divided into data blocks, which are then compressed and stored or transmitted as compressed blocks. The compressed blocks can be decompressed to recover the original data blocks. The compression and decompression can be done by different compression codecs, depending on the file format and the splittability.