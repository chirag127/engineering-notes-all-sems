### Avro and file-based data structures

- Avro is a data serialization system that can store data in a compact, fast, binary format .
- Avro can also store the schema of the data in JSON format, which makes it easy to read and interpret by any program.
- Avro supports rich data structures, such as arrays, maps, records, enums, unions, and fixed types .
- Avro can be used as a container file format, to store persistent data in HDFS or other file systems .
- Avro can also be used for remote procedure call (RPC), to exchange data and messages between different applications or services .
- Avro does not require code generation to read or write data files nor to use or implement RPC protocols, which simplifies the integration with dynamic languages .
- Avro file format is a row-based format, which means that each record is stored as a whole and can be processed independently.
- Avro file format is suitable for cases where the data is accessed or processed in a sequential manner, such as streaming or batch processing.
- Avro file format is compatible with many connectors, such as Amazon S3, Azure Blob, Azure Data Lake Storage, Google Cloud Storage, HDFS, HTTP, and more.