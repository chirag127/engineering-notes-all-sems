# Hadoop I/O: compression

- Data compression is a technique to reduce the size of data files by using algorithms that encode the data more efficiently.
- Data compression can improve the performance of Hadoop applications by reducing the amount of I/O and network bandwidth required to store and process large data sets.
- Data compression can also save disk space and reduce the cost of storage.
- However, data compression also has some drawbacks, such as increased CPU usage, reduced random access, and compatibility issues with some tools and formats.
- Hadoop supports various compression codecs, such as Gzip, Bzip2, Snappy, LZO, LZ4, and Zstandard, that can be applied at different stages of the data processing pipeline, such as input, output, intermediate, and shuffle.
- Hadoop also provides a common interface for compression and decompression, called the CompressionCodec, that allows users to plug in different compression algorithms and use them with Hadoop I/O classes, such as SequenceFile, MapFile, and RecordIO.
- Hadoop also supports splitting compressed files, which enables parallel processing of compressed data, by using splittable compression formats, such as Bzip2 and Zstandard, or by using container formats, such as SequenceFile and Avro, that store compressed records.