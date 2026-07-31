#### Hadoop I/O

- Hadoop I/O is the set of data types and I/O classes that are common to Hadoop MapReduce and HDFS.
- Hadoop I/O supports serialization and compression of data, as well as file-based and network-based data access.
- Serialization is the process of converting an object into a sequence of bytes that can be stored or transmitted. Hadoop I/O provides several serialization frameworks, such as Writable, Avro, and Protocol Buffers, that are optimized for performance and interoperability.
- Compression is the process of reducing the size of data by applying a compression algorithm. Hadoop I/O supports various compression codecs, such as Gzip, Snappy, and Bzip2, that can be applied to different types of data, such as text, binary, or splittable.
- File-based data access refers to reading and writing data from files stored on HDFS or other file systems. Hadoop I/O provides several file formats, such as SequenceFile, MapFile, and Parquet, that are suitable for different use cases, such as storing key-value pairs, sorted data, or columnar data.
- Network-based data access refers to reading and writing data from sockets or RPC services. Hadoop I/O provides several network protocols, such as Hadoop RPC, HTTP, and Thrift, that are used for communication between Hadoop components, such as NameNode, DataNode, JobTracker, and TaskTracker.