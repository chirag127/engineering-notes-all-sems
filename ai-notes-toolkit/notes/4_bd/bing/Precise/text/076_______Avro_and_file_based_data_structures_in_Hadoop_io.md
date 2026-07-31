##### Avro and file based data structures in Hadoop io

- Avro is a data serialization system that is used to encode data structures into a compact binary format.
- Avro is used in Hadoop to store and process large amounts of data in a distributed computing environment.
- Avro provides a way to define data structures using a schema, which can be used to validate and encode data.
- Avro schemas are defined using JSON, which makes them easy to read and write.
- Avro supports schema evolution, which means that data can be read even if the schema has changed.
- File-based data structures in Hadoop are used to store and organize data on disk.
- Hadoop provides several file-based data structures, including SequenceFile, MapFile, and SetFile.
- SequenceFile is a flat file that stores key-value pairs in a binary format.
- MapFile is an indexed file that provides fast lookup of key-value pairs.
- SetFile is a file that stores a set of keys, with no associated values.
- These file-based data structures are used to store intermediate data during MapReduce processing, as well as to store the final output of a MapReduce job.
- Hadoop provides APIs for reading and writing these file-based data structures, making it easy to work with data stored in Hadoop.