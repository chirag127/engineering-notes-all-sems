### Avro and file-based data structures for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

- Avro is an efficient data serialization framework and is widely supported throughout Hadoop and its ecosystem.
- Data serialization is a way of representing data in memory as a series of bytes.
- Avro uses a schema to define the structure and types of the data.
- The schema is stored in a JSON format and can be extracted from an Avro file using avro-tools.jar .
- Avro files can be imported to and exported from HDFS using Sqoop, a tool designed to transfer data between Hadoop and relational database management systems (RDBMS).
- To import data to HDFS in Avro format, add the parameter --as-avrodatafile in the Sqoop command.
- To export data from HDFS in Avro format to RDBMS, add the parameter --as-avrodatafile in the Sqoop command.
- Avro files can also be used to create Hive and Impala tables in HDFS.
- Avro files have some advantages over other file formats, such as:
  - They support schema evolution, which means the schema can be changed without breaking the compatibility with existing data.
  - They support complex data types, such as arrays, maps, records, unions, etc.
  - They compress the data efficiently and reduce the storage space.
  - They enable fast data processing and querying by various Hadoop tools.