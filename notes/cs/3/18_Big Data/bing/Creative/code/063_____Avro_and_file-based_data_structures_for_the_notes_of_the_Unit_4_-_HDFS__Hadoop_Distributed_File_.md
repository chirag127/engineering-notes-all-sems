### Avro and file-based data structures for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

- Avro is an efficient data serialization framework and is widely supported throughout Hadoop and its ecosystem.
- Data serialization is a way of representing data in memory as a series of bytes.
- Avro files have a self-describing schema that can be extracted using avro-tools.jar .
- Avro files can be imported to and exported from HDFS using Sqoop, a tool designed to transfer data between Hadoop and relational database management systems (RDBMS).
- To import data to HDFS in Avro format, add the parameter `--as-avrodatafile` in the Sqoop command.
- To export data from HDFS in Avro format to RDBMS, add the parameter `--as-avrodatafile` in the Sqoop command.
- Avro files can be used to create Hive and Impala tables in HDFS.
- Avro files have some advantages over other file formats, such as:
  - They support schema evolution, which means that the schema can be changed without breaking the compatibility with existing data.
  - They support complex data types, such as arrays, maps, records, and unions.
  - They have a compact binary format that reduces the storage space and network bandwidth.
  - They have a built-in compression mechanism that can be configured with different codecs, such as snappy, deflate, or bzip2.
  - They have a rich set of APIs for various languages, such as Java, Python, C#, Ruby, and PHP.