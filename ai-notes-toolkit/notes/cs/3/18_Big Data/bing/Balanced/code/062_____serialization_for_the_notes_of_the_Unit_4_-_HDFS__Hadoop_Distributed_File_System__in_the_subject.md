### Serialization

- Serialization is the process of converting object data into byte stream data for transmission over a network across different nodes in a cluster or for persistent data storage.
- Deserialization is the reverse process of serialization and converts byte stream data into object data for reading data from HDFS.
- Hadoop provides Writables for serialization and deserialization purpose. Writable and WritableComparable Interfaces are the two interfaces that are used to implement serialization in Hadoop.
- Data serialization is a way of representing data in memory as a series of bytes. It helps in reducing the size of data and improving the performance of data processing.
- Hadoop supports various data serialization frameworks, such as Avro, Thrift, Protocol Buffers, etc. These frameworks provide schema evolution, compression, and cross-language support .
- HDFS can store data in different file formats, such as text files, sequence files, Avro data files, and Parquet file formats. These file formats have different advantages and disadvantages in terms of storage efficiency, data access, and compatibility.