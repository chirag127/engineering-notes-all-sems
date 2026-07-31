##### Avro and file based data structures in Hadoop io

- Avro is a language-neutral data serialization system that can be used for Hadoop and other big data processing frameworks.
- Avro creates binary structured files that are both compressible and splittable, which makes them efficient for Hadoop MapReduce jobs .
- Avro files store data along with schema in JSON format in their metadata section, which makes them self-describing and easy to read and interpret by any program  .
- Avro files can be imported to and exported from HDFS using Sqoop, a tool for transferring data between Hadoop and relational databases.
- Avro files are similar to sequential files, which are the oldest binary file format in Hadoop, but have some advantages over them, such as:
  - Avro files support schema evolution, which means that the schema can be changed without breaking the compatibility with older data .
  - Avro files can use different compression codecs, such as Snappy, Deflate, or Bzip2, to reduce the file size and improve the performance .
  - Avro files can use a rich data structure that supports complex types, such as arrays, maps, records, enums, and unions .
- A possible mnemonic to remember the features of Avro files is: **A**vro is **V**ersatile, **R**ich, and **O**ptimized.