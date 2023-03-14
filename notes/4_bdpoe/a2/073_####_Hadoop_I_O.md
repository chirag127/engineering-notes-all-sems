 Here is the content on #### Hadoop I/O in markdown format:

#### Hadoop I/O

- Hadoop has its own I/O system that is optimized for the distributed filesystem (HDFS) and processing framework (MapReduce).
- Hadoop I/O is designed to be efficient given the constraints of HDFS (large block sizes, numerous small files) and MapReduce (heavy streaming access).
- The key aspects of Hadoop I/O are:
    - Data is stored in blocks (default 128MB) for efficiency.
    - Files are split into block-sized chunks for processing.
    - Data is serialized/deserialized using key/value pairs and writable/readable interfaces. This allows for flexible data types and schemas.
    - Data is buffered at the block level for efficient streaming.
- Some key classes for I/O are:
    - `FSDataInputStream`/`FSDataOutputStream` - For reading/writing to HDFS.
    - `DataInputBuffer`/`DataOutputBuffer` - For in-memory buffering of block data.
    - `RecordReader`/`RecordWriter` - For reading/writing key/value pairs in a MapReduce task.
- There are encoding options for efficient compression and serialization, including:
    - `SequenceFile` - Uses `Writable` types and compression. Good for sorted data.
    - `Avro` - Uses schema-based serialization with JSON data format. Good for complex and evolving data.
    - `Parquet` - Columnar storage format good for analytical queries.
    - `ORC` - Optimized row columnar format with good compression.
- Some mnemonics/tips for learning Hadoop I/O:
    - Think of files as split into blocks - this is key to efficiency.
    - Key/value pairs and serializable interfaces enable flexible data.
    - Buffering happens at the block level for streaming performance.
    - There are many encoding options for compression and efficient serialization.
    - Study the main I/O classes and how they interact (e.g. `FSDataInputStream` reads from HDFS and deserializes with `RecordReader`).