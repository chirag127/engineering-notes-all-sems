### Hadoop I/O: Compression

- Compression is a technique used to reduce the size of data being stored or transmitted.
- In the context of Hadoop, compression is used to reduce the amount of data that needs to be stored on HDFS (Hadoop Distributed File System).
- Compression can also improve the performance of data processing by reducing the amount of data that needs to be read from or written to disk.
- Hadoop supports several compression codecs, including Gzip, Bzip2, Snappy, and LZO.
- The choice of compression codec depends on the specific requirements of the application, such as the desired compression ratio and the speed of compression and decompression.
- Compression can be applied at different stages of data processing, such as when data is written to HDFS, when data is read from HDFS, or when data is processed by MapReduce or other data processing frameworks.
- Hadoop provides APIs for developers to integrate compression into their applications.
- It is important to note that compression can increase the CPU usage of data processing, so it is important to balance the benefits of compression with the additional CPU overhead.