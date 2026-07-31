# Hadoop I/O: compression

- Data compression is a technique to reduce the size of data files by using algorithms that encode the data more efficiently.
- Data compression can improve the performance of Hadoop applications by reducing the amount of I/O and network transfer required for processing large data sets.
- Data compression can also save disk space and reduce the cost of storage in Hadoop clusters.
- However, data compression also has some drawbacks, such as increased CPU usage and reduced random access capability.
- Therefore, data compression in Hadoop is usually a trade-off between I/O and speed of computation, and it depends on the characteristics of the data and the application.

## Types of compression

- There are two types of compression: lossless and lossy.
- Lossless compression preserves the exact information of the original data, and it can be decompressed to recover the original data without any loss.
- Lossy compression discards some information of the original data, and it cannot be decompressed to recover the original data exactly. However, lossy compression can achieve higher compression ratios than lossless compression, and it is suitable for data that can tolerate some loss of quality, such as images, audio, and video.
- Hadoop supports both lossless and lossy compression, and it provides a set of interfaces and classes for data compression and decompression in the org.apache.hadoop.io.compress package.

## Compression codecs

- A compression codec is a software component that implements a specific compression algorithm and provides methods for compressing and decompressing data streams.
- Hadoop supports several compression codecs, such as Gzip, Bzip2, Snappy, LZO, LZ4, and Zstandard. Each codec has different characteristics in terms of compression ratio, speed, and CPU usage.
- Hadoop also allows users to plug in their own custom compression codecs by implementing the CompressionCodec interface and registering them in the configuration file.
- Hadoop uses the CompressionCodecFactory class to create instances of compression codecs based on the file extensions or the configuration properties.

## Compression modes

- Hadoop supports three modes of compression: record-level, block-level, and file-level.
- Record-level compression compresses each record (such as a key-value pair) individually, and it preserves the ability to split the input files for parallel processing. However, record-level compression has lower compression ratios and higher CPU overhead than block-level or file-level compression.
- Block-level compression compresses a block of records together, and it achieves higher compression ratios and lower CPU overhead than record-level compression. However, block-level compression requires the input files to have a special format that supports block boundaries, such as SequenceFile or Avro.
- File-level compression compresses the entire file as a single unit, and it achieves the highest compression ratios and the lowest CPU overhead among the three modes. However, file-level compression does not allow the input files to be split for parallel processing, and it reduces the scalability and fault tolerance of Hadoop applications.

## Compression in Hadoop components

- Data compression can be applied to different components of Hadoop, such as HDFS, MapReduce, and YARN.
- HDFS supports file-level compression, and it can store compressed files as regular files without any special treatment. However, HDFS does not support splitting compressed files for parallel processing, unless the compression codec supports splittable compression, such as Bzip2.
- MapReduce supports record-level and block-level compression, and it can compress the input, output, and intermediate data of the map and reduce tasks. MapReduce can also split compressed input files for parallel processing, if the compression codec and the input format support splittable compression, such as Bzip2 and SequenceFileInputFormat.
- YARN supports compressing the logs of the application containers, and it can reduce the disk space and network bandwidth required for storing and transferring the logs. YARN can also decompress the logs on demand for viewing or analysis.