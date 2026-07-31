

### Data Format for the Notes of the Unit 2 - Hadoop in the Subject of Big Data

In this unit, we will dive deeper into Hadoop, a popular open-source software framework used for storing and processing large datasets. To effectively take notes and understand the concepts discussed, it is important to understand the data format used in Hadoop. Here are some key points to keep in mind:

- Hadoop uses a distributed file system called Hadoop Distributed File System (HDFS) for storing large datasets across multiple nodes in a cluster.
- Data in HDFS is stored in blocks, typically 128MB or 256MB in size, and is replicated across multiple nodes for fault tolerance.
- Hadoop stores data in a key-value pair format, where each record is represented as a key-value pair.
- The key is used to identify the record and the value contains the actual data. 
- Hadoop supports various data formats for storing data, including Text, SequenceFile, Avro, Parquet, and ORC.
- Text format is a simple format that stores data as plain text, with each record separated by a newline character.
- SequenceFile format is a binary format that stores data as key-value pairs, with each key-value pair separated by a sync marker.
- Avro format is a compact binary format that allows for schema evolution and supports rich data structures.
- Parquet format is a columnar storage format that is optimized for querying large datasets.
- ORC format is another columnar storage format that is optimized for performance and supports compression and predicate pushdown.
- Hadoop also supports various serialization formats for converting data into a binary format, including Java Serialization, Thrift, and Protocol Buffers.

By understanding the data format used in Hadoop, we can effectively store and process large datasets in a distributed and fault-tolerant manner.