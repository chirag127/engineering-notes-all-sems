##### Avro and file based data structures in Hadoop io

- Avro is a data serialization system that allows data to be stored and exchanged in a compact and efficient binary format.
- Avro supports schema evolution, which means that the schema of the data can change over time without breaking compatibility with existing data or applications.
- Avro also provides a rich set of data types, such as records, enums, arrays, maps, unions, and logical types, that can represent complex and nested data structures.
- Avro data can be stored in files or transmitted over the network using Avro's RPC (remote procedure call) framework.
- Avro files have a self-describing format that includes the schema of the data and a sync marker that allows random access and splitting of the file.
- Avro files can be compressed using various codecs, such as Snappy, Deflate, or Bzip2, to reduce the size of the data and improve the performance of reading and writing.
- Avro files can be processed by Hadoop MapReduce, Spark, Hive, Pig, and other frameworks that support the Hadoop io API.
- Avro files can also be integrated with other data formats, such as Parquet, ORC, JSON, and CSV, using tools like Avro Tools, Sqoop, Flume, and Kafka Connect.