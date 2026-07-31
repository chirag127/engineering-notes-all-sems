##### Avro and file based data structures in Hadoop io

- Avro is a language-neutral data serialization system that can be used for Hadoop and other big data processing frameworks.
- Avro creates binary structured files that are both compressible and splittable, which makes them efficient for Hadoop MapReduce jobs .
- Avro files store data along with the schema in JSON format in the metadata section, which makes them self-describing and easy to read and interpret by any program  .
- Avro supports a rich data structure that includes primitive types, complex types, and logical types.
- Avro files can be imported and exported to and from HDFS using Sqoop, a tool for transferring data between relational databases and Hadoop.
- Avro files are similar to sequential files, which are the oldest binary file format in Hadoop, but offer better performance and features.
- Avro files can be used with Kafka, a distributed streaming platform, for faster data processing.