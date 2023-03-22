 Here are the notes on Avro and file-based data structures for the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data:

### Avro

- Avro is a row-oriented remote procedure call and data serialization framework developed within Apache's Hadoop project.
- Avro provides a compact binary data serialization format with JSON-like schemas.
- Avro schema is used to define the data types of fields in a record and the records within a file. The schema is stored with the data, so that files may be processed later without requiring the schema.
- Avro data is described using a schema, and that schema is used to validate and serialize the data. This makes it suitable for remote procedure calls, persistent data storage, data synchronization, and other uses where binary data is read and processed by systems written in multiple programming languages.
- Key benefits of Avro:

- Serialization - Converting objects into bytes and vice versa.
- Cross-language compatibility - Code generators are available in many languages to enable consistent encoding.
- Dynamic typing - Schema can evolve over time.
- Efficiency - Binary encoded data is compact and fast to encode/decode.

### File-based data structures

- Apache Hadoop uses file-based data structures like SequenceFile and MapFile.
- SequenceFile: It stores key/value pairs in a flat binary file. It uses various record compressors to improve space and I/O efficiency. SequenceFiles are splittable, so they can be used as input to a MapReduce job.
- MapFile: It is an extension of SequenceFile that indexes keys in the file to enable fast lookups by key. Using MapFiles, we can perform point lookups and range scans efficiently without reading the entire file.
- Key benefits of file-based data structures:

- Space efficiency due to compression.
- Splittability enables parallel processing via MapReduce.
- Sorting and indexing enable efficient lookups/scans.
- Language independence since data is stored in a binary format.