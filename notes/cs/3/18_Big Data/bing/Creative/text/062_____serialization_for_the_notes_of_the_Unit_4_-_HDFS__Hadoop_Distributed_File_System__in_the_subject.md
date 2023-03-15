### Serialization

- Serialization is the process of converting object data into byte stream data for transmission over a network across different nodes in a cluster or for persistent data storage .
- Deserialization is the reverse process of serialization and converts byte stream data into object data for reading data from HDFS.
- Hadoop provides Writables for serialization and deserialization purpose. Writable and WritableComparable Interfaces are the two interfaces that are used to implement serialization in Hadoop.
- Writable interface is used to serialize the data to be written to a file or to be transferred over the network. WritableComparable interface is used to compare the serialized data for sorting and grouping.
- Hadoop supports various file formats for serialization, such as text files, sequence files, Avro data files, and Parquet file formats.
- Text files are the simplest and most common file format in Hadoop. They store data as plain text, separated by a delimiter such as comma, tab, or newline. Text files are easy to read and write, but they are not efficient in terms of storage space and processing speed.
- Sequence files are binary files that store key-value pairs. They are suitable for storing large amounts of data in a compressed and splittable format. Sequence files can also store metadata and support different compression types.
- Avro data files are binary files that store data in a schema-based format. Avro is an efficient data serialization framework and is widely supported throughout Hadoop and its ecosystem. Avro data files can store complex data types, such as arrays, maps, and records, and can handle schema evolution .
- Parquet file format is a columnar storage format that stores data in a compressed and optimized way. Parquet file format is ideal for analytical queries that access only a subset of columns in a table. Parquet file format can also support nested data structures and schema evolution.