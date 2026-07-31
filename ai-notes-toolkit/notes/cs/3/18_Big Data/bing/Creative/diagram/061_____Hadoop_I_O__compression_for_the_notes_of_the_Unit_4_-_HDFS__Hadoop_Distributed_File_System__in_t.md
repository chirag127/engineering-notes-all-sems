### Hadoop I/O: compression

- Data compression is a technique to reduce the size of data files by applying some algorithms that encode the data more efficiently.
- Data compression can improve the performance of Hadoop applications by reducing the amount of I/O and network traffic, which are often the bottlenecks in large-scale data processing.
- Data compression can also save disk space and reduce the cost of storage.
- However, data compression also has some drawbacks, such as the CPU overhead of compressing and decompressing data, and the loss of data locality and random access for some compression formats.
- Therefore, using data compression in Hadoop is a trade-off between I/O and CPU, and it depends on the characteristics of the data and the application.
- Hadoop supports several compression codecs, such as Gzip, Bzip2, Snappy, LZO, LZ4, and ZStandard, which have different compression ratios, speeds, and splittability.
- Splittability means whether a compressed file can be split into smaller chunks and processed in parallel by different mappers. Gzip and Bzip2 are not splittable, while Snappy, LZO, LZ4, and ZStandard are splittable.
- Hadoop also provides a framework for plugging in custom compression codecs, which can be implemented by extending the CompressionCodec interface and registering them in the core-site.xml file.
- Hadoop allows compression to be applied at different stages of the data processing pipeline, such as the input, the intermediate output, and the final output of MapReduce jobs, or the input and output of HDFS files.
- Hadoop also supports different compression formats, such as SequenceFile, Avro, Parquet, and ORC, which are designed to store structured or semi-structured data in a compact and efficient way.
- These formats combine compression with serialization, which is the process of converting data objects into byte streams that can be stored or transmitted. Hadoop provides several serialization frameworks, such as Writable, Record I/O, Avro, and Protocol Buffers, which have different advantages and disadvantages in terms of performance, compatibility, and ease of use.