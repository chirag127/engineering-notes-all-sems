##### Avro and file based data structures in Hadoop io

- Avro is a language-neutral data serialization system that can be used for Hadoop and other big data processing frameworks.
- Avro creates binary structured files that are both compressible and splittable, which makes them efficient for Hadoop MapReduce jobs .
- Avro files store data along with the schema in JSON format in the metadata section, which makes them self-describing and easy to read and interpret by any program  .
- Avro files support schema evolution, which means that the schema can be changed without breaking the compatibility with older data.
- Avro files can be imported and exported to and from HDFS using Sqoop, a tool for transferring data between relational databases and Hadoop.
- Avro files are similar to sequential files, which are one of the oldest binary file formats in Hadoop. Sequential files store key-value pairs in a compressed and serialized format .
- Avro files are different from map files, which are another binary file format in Hadoop. Map files store key-value pairs in a sorted order, which allows for faster lookup by key .
- Avro files are also different from parquet files, which are a column-based file format in Hadoop. Parquet files store data in columns rather than rows, which allows for better compression and performance for analytical queries.

A possible mnemonic to remember the features of Avro files is:

**A**vro: **A**pplicable for many languages, **A**ble to compress and split, **A**ttached with schema, **A**daptable to schema changes, **A**ccessible by Sqoop.