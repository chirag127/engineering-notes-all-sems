##### Compression in Hadoop IO

- Compression is a technique to reduce the size of data by encoding it in a different format that uses fewer bits.
- Compression can improve the performance of Hadoop applications by reducing the disk space, network bandwidth, and CPU usage required to store and process data.
- Hadoop supports various compression codecs, such as Gzip, Bzip2, Snappy, LZO, LZ4, and Zstandard, that have different trade-offs between compression ratio, speed, and splittability.
- Splittability refers to the ability to split a compressed file into smaller chunks that can be processed independently by different mappers.
- Some compression codecs, such as Gzip and Bzip2, are splittable only at file boundaries, while others, such as Snappy and LZO, are splittable within files using an index file or a container format.
- Hadoop allows users to configure compression at different levels, such as input, output, intermediate, and shuffle, by setting the appropriate properties in the configuration files or the code.
- Hadoop also provides a compression API that allows users to create and use custom compression codecs.