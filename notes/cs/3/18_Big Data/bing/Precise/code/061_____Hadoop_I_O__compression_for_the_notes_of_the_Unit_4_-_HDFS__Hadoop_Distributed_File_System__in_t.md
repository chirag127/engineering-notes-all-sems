### Hadoop I/O: Compression

- Compression is a technique used to reduce the size of data being stored or transmitted.
- Hadoop supports several compression codecs, including Gzip, Bzip2, Snappy, and LZO.
- Compression can be applied at different stages of data processing in Hadoop, including during input, output, and intermediate stages.
- Using compression can reduce the amount of disk space required to store data and can also reduce the amount of data that needs to be transferred between nodes, potentially improving performance.
- However, compression also adds some overhead, as data needs to be compressed and decompressed, which can increase CPU usage.
- The choice of compression codec and the level of compression used can affect the trade-off between storage space, data transfer, and CPU usage.
- Hadoop provides configuration options to enable or disable compression for different stages of data processing and to specify the compression codec to use.
- It is important to carefully consider the use of compression in a Hadoop cluster, taking into account the characteristics of the data being processed and the resources available in the cluster.