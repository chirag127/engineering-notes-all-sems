# Hadoop I/O: compression

- Data compression is a technique to reduce the size of data files by using algorithms that encode the data more efficiently.
- Data compression can improve the performance of Hadoop applications by reducing the amount of I/O and network traffic, which are often the bottlenecks in large-scale data processing.
- Data compression can also save disk space and reduce the cost of storage.
- However, data compression also has some drawbacks, such as the CPU overhead of compression and decompression, and the loss of data locality and random access.
- Therefore, data compression in Hadoop is usually a trade-off between I/O and speed of computation, and should be used carefully depending on the data characteristics and the application requirements.
- Hadoop supports various compression codecs, such as Gzip, Bzip2, LZO, Snappy, and Zstandard, which have different compression ratios, speeds, and splittability.
- Splittability refers to the ability to split a compressed file into smaller chunks that can be processed independently by different mappers, without decompressing the whole file.
- Splittable codecs, such as Bzip2 and Zstandard, can preserve the data locality and parallelism of MapReduce, but they usually have lower compression ratios and speeds than non-splittable codecs, such as Gzip and Snappy.
- Hadoop allows users to configure the compression codec, the compression level, and the compression type for different stages of data processing, such as input, intermediate, and output.
- Hadoop also provides a set of APIs and classes for data I/O, such as Writable, SequenceFile, and Avro, which can support data compression and serialization. Serialization is the process of converting data structures into byte streams that can be stored or transmitted.
- Writable is the interface that Hadoop uses for serializing data types, such as IntWritable, Text, and ArrayWritable. Writable objects can be compressed by using CompressionOutputStream and CompressionInputStream classes.
- SequenceFile is a binary file format that stores key-value pairs in a sequence. SequenceFile can compress the keys, the values, or both, by using different compression types, such as NONE, RECORD, and BLOCK.
- Avro is a data serialization system that supports schema evolution, meaning that the data schema can change over time without breaking the compatibility. Avro can compress the data by using any compression codec supported by Hadoop.