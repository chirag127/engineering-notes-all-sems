 Here is the content in markdown format on the topic ##### Avro and file based data structures in Hadoop io:

##### Avro and file based data structures in Hadoop io

Avro is a data serialization system used in Hadoop ecosystem. It provides:-

1. A schema language to define data structures
2. A binary data encoding format
3. APIs in multiple languages to read/write data

Advantages of Avro:-

- Schema evolution: Avro can handle schema changes gracefully. Older schema can read data written in a newer schema.
- Dynamic typing: Avro supports dynamic typing and late binding.
- Efficient serialization: Avro conversion to and from JSON and binary data is fast and size efficient.
- Language independence: Avro provides API in multiple languages like Java, C, C++, C#, Python, etc. so data can be shared across languages.

File based data structures in Hadoop io include:-

1. SequenceFile: File with serialized key-value pairs. Supports APIs in multiple languages.
2. MapFile: Sorted key-value map implementations. Supports range queries and block compression.
3. RCFile: Record Columnar File. Stores table in columnar format for efficient queries on columns.

Advantages of file based data structures:-

- Efficient storage: Supports compression and efficiency as data is stored in blocks.
- Language independence: Supports multiple language APIs.
- Query support: Some structures like MapFile and RCFile support range queries and queries on columns respectively.

Disadvantages:-

- Complexity: The file formats can be complex to understand and implement.
- Overhead: There is some overhead in serialization and deserialization of data.

Applications:-

- Storing and processing large datasets in Hadoop ecosystem.
- Sharing data across multiple languages in Hadoop jobs.

Mnemonics/Learning tricks:-

- Remember Avro provides schema and serialization.
- Think of sequence file as key-value pairs, MapFile as sorted map and RCFile as columnar format.
- Understand advantages and applications to learn usefulness of these formats.

[Detailed diagrams and examples can be added if required]