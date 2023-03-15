##### Avro and file based data structures in Hadoop io

- Avro is a language-neutral data serialization system that can be used for Hadoop and other big data processing.
- Avro creates binary structured files that are both compressible and splittable, which makes them efficient for Hadoop MapReduce jobs .
- Avro files store data along with schema in JSON format in their metadata section, which makes them self-describing and easy to read and interpret by any program  .
- Avro supports a rich data structure that includes primitive types, complex types, and logical types.
- Avro files can be imported and exported to HDFS using Sqoop, a tool for transferring data between relational databases and Hadoop.
- Avro files are similar to sequential files, which are one of the oldest binary file formats in Hadoop.
- Sequential files store key-value pairs in a binary format and can be compressed and split.
- Map files are another binary file format in Hadoop that are based on sequential files, but with an index to allow random access to the records.