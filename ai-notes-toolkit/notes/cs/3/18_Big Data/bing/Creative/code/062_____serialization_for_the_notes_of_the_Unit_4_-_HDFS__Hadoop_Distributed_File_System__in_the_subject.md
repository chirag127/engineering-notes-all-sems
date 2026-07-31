### Serialization

- Serialization is the process of converting object data into byte stream data for transmission over a network across different nodes in a cluster or for persistent data storage.
- Deserialization is the reverse process of serialization and converts byte stream data into object data for reading data from HDFS.
- Hadoop provides Writables for serialization and deserialization purpose. Writable and WritableComparable Interfaces are the two interfaces that are used to implement serialization in Hadoop.
- Data serialization is a way of representing data in memory as a series of bytes. It helps in reducing the size of data and improving the performance of data processing.
- Hadoop supports various file formats for serialization, such as text files, sequence files, Avro data files, and Parquet file formats.
- Avro is an efficient data serialization framework and is widely supported throughout Hadoop and its ecosystem. It uses JSON for defining data types and protocols, and serializes data in a compact binary format.
- Parquet is a columnar storage format that provides high compression and encoding schemes. It is compatible with most of the data processing frameworks in the Hadoop environment.