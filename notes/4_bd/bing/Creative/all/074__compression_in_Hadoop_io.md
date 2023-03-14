##### Compression in Hadoop IO

- Compression is a technique to reduce the size of data by encoding it in a different format that uses fewer bits.
- Compression can improve the performance of Hadoop applications by reducing the disk space, network bandwidth, and CPU usage required to store and process data.
- Compression can also improve the reliability of Hadoop applications by reducing the chance of data corruption and disk failures.
- Hadoop supports two types of compression: file-based compression and record-based compression.
- File-based compression applies to the entire file and requires the file to be decompressed before processing. Examples of file-based compression formats are gzip, bzip2, and LZO.
- Record-based compression applies to individual records within a file and allows the file to be processed without decompression. Examples of record-based compression formats are Snappy, Zstandard, and LZ4.
- Hadoop provides various classes and interfaces to work with compressed data, such as CompressionCodec, CompressionInputStream, CompressionOutputStream, Compressor, and Decompressor.
- Hadoop also provides various utilities and tools to compress and decompress data, such as the hadoop fs -text command, the CompressionTest tool, and the CodecPool class.
- Hadoop allows compression to be configured at different levels, such as the input format, the output format, the map output, and the shuffle output.
- Hadoop also allows compression to be enabled or disabled for specific files, directories, or file extensions using the io.compression.codecs and io.compression.codec.extensions properties.
- A mnemonic to remember the benefits of compression in Hadoop is **RIP DISC**: Reliability, Input, Performance, Disk space, Intermediary data, Shuffle data, and CPU usage.