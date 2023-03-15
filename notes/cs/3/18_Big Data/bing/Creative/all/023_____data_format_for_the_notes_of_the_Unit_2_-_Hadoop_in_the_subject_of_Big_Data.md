# Data Format for the Notes of the Unit 2 - Hadoop in the Subject of Big Data

- Hadoop is a framework for storing and processing large datasets in a distributed and parallel manner.
- Hadoop has two main components: HDFS (Hadoop Distributed File System) and YARN (Yet Another Resource Negotiator).
- HDFS is a distributed file system that stores data across multiple nodes in a cluster. It splits the data into blocks and replicates them for fault tolerance.
- YARN is a resource management layer that allocates and schedules tasks to the nodes in the cluster.
- Hadoop supports various data formats for storing and processing data, such as text, binary, sequence, Avro, Parquet, etc.
- Text format is the simplest and most common format, where each line of text is a record. It is easy to read and write, but it takes more space and processing time than other formats.
- Binary format is a compact and efficient format, where data is stored as bytes. It is faster and smaller than text format, but it is not human-readable and requires a schema to interpret.
- Sequence format is a binary format that stores key-value pairs. It is useful for storing intermediate data between MapReduce jobs, as it preserves the key order and supports compression and splitting.
- Avro format is a binary format that stores data as records with a schema. It is useful for storing complex and nested data structures, as it supports schema evolution and data serialization.
- Parquet format is a columnar format that stores data in columns rather than rows. It is useful for storing analytical data, as it supports compression, encoding, and predicate pushdown.