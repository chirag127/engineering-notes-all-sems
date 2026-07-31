### Hadoop I/O: Compression

Hadoop provides support for data compression to reduce the amount of data that needs to be stored and transferred between nodes in a Hadoop cluster. This can result in significant performance improvements and cost savings.

Here are some key points to note about Hadoop I/O compression:

1. Hadoop supports several compression codecs, including Gzip, Bzip2, Snappy, and LZO.
2. Compression can be applied at different stages of data processing, including when data is stored in HDFS, when data is transferred between nodes, and when data is processed by MapReduce jobs.
3. Compression can be configured at the cluster level or at the job level.
4. The choice of compression codec can have a significant impact on performance, as different codecs have different compression and decompression speeds.
5. Compression can also affect data locality, as compressed data blocks may be smaller and therefore more easily moved between nodes.
6. Hadoop provides a utility class, `CompressionCodecFactory`, for discovering and creating instances of compression codecs.

In summary, Hadoop I/O compression can provide significant performance and cost benefits, and should be carefully considered when designing and configuring Hadoop clusters and jobs. It is important to choose the appropriate compression codec and to apply compression at the appropriate stages of data processing to achieve the best results.