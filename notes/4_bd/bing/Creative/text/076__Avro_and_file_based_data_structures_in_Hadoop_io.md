##### Avro and file based data structures in Hadoop io

- Avro is a language-independent, schema-based data serialization framework that is widely used in Hadoop and its ecosystem  .
- Avro uses a JSON format to specify the data structure and schema of the data, which makes it more powerful and expressive .
- Avro supports two types of data: primitive types and complex types. Primitive types include boolean, int, long, float, double, string, bytes, and null. Complex types include record, enum, array, map, union, and fixed .
- Avro creates a data file where it keeps data along with schema in its metadata section. This makes the data self-describing and portable across different platforms and languages  .
- Avro is a good fit for big data processing because it is compact, fast, and splittable. It also supports schema evolution, which means the data can be read with different schemas than the one it was written with  .
- Avro provides a Java API for performing serialization and deserialization of data. The API can be used in two ways: using specific or generic records. Specific records are Java classes that are generated from the schema using a tool called Avro Compiler. Generic records are dynamic data structures that do not require code generation.
- Avro also provides a tool called Avro Data File Tools that can be used to manipulate Avro data files from the command line. The tool can perform operations such as getting schema, extracting data, concatenating files, and converting between Avro and JSON formats.
- Avro is similar to some other file-based data structures in Hadoop, such as SequenceFile and MapFile. SequenceFile is a simple binary file format that stores key-value pairs in a sequential order. MapFile is an extension of SequenceFile that adds an index file for faster lookup of keys. However, Avro has some advantages over these formats, such as:
  - Avro supports a richer set of data types and schemas than SequenceFile and MapFile, which only support Writable types .
  - Avro supports schema evolution, which means the data can be read with different schemas than the one it was written with. SequenceFile and MapFile require the same schema for reading and writing data .
  - Avro supports compression and encryption at the block level, which can improve performance and security. SequenceFile and MapFile only support compression at the file level .
  - Avro is more portable and interoperable than SequenceFile and MapFile, as it can be used with different languages and platforms. SequenceFile and MapFile are specific to Java and Hadoop .