##### Avro and file based data structures in Hadoop io

- Avro is a data serialization system that is used to encode data structures into a compact binary format.
- It is commonly used in Hadoop for storing and processing large data sets.
- Avro uses a schema to define the structure of the data, which allows for efficient encoding and decoding of the data.
- The schema is stored with the data, which allows for schema evolution over time.
- Avro supports a wide range of data types, including complex data structures such as arrays, maps, and records.
- File-based data structures in Hadoop are used to store and organize data on disk.
- These data structures include SequenceFiles, MapFiles, and SetFiles.
- SequenceFiles store key-value pairs in a binary format, with the keys sorted in ascending order.
- MapFiles are similar to SequenceFiles, but they also include an index to allow for faster lookups of specific keys.
- SetFiles store a set of keys, with no associated values.
- These file-based data structures are commonly used in Hadoop for storing intermediate data during processing, as well as for storing the final output of a job.
- Avro and file-based data structures in Hadoop provide efficient and flexible ways to store and process large data sets.