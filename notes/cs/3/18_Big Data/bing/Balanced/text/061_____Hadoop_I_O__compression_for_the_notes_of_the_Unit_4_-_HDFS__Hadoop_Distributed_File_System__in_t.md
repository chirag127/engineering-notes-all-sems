### Hadoop I/O: compression

- Data compression is a technique to reduce the size of data files by using algorithms that encode the data more efficiently.
- Data compression can improve the performance of Hadoop applications by reducing the amount of I/O and network traffic, which are often the bottlenecks in large-scale data processing.
- Data compression can also save disk space and reduce the cost of storage.
- However, data compression also has some drawbacks, such as the CPU overhead of compression and decompression, and the loss of data locality and random access.
- Hadoop supports several compression codecs, such as Gzip, Bzip2, Snappy, LZO, and LZ4, which have different trade-offs between compression ratio, speed, and splittability.
- Splittability refers to the ability to split a compressed file into smaller chunks that can be processed independently by different mappers, without decompressing the whole file.
- Hadoop allows users to configure compression at different levels of the data processing pipeline, such as input, intermediate, and output.
- Hadoop also provides a set of classes and interfaces in the org.apache.hadoop.io.compress package to implement and use compression codecs.