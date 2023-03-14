##### Avro and file based data structures in Hadoop io

- Avro is a language-independent, schema-based data serialization framework that is widely used in Hadoop and its ecosystem .
- Avro uses JSON format to specify the data structure and schema of the data, which makes it more expressive and powerful .
- Avro creates a data file where it stores the data along with the schema in its metadata section, which allows schema evolution and backward compatibility .
- Avro supports two types of data: primitive types and complex types. Primitive types include boolean, int, long, float, double, string, bytes, and null. Complex types include record, enum, array, map, union, and fixed .
- Avro provides a Java API for performing serialization and deserialization of data. To use Avro, we need to follow these steps:
  - Define a schema for the data using JSON format and save it as a .avsc file.
  - Use the Avro tools to generate a Java class for the schema using the avro-tools-1.10.2.jar file.
  - Create an instance of the generated class and populate it with data.
  - Use a DatumWriter and a DataFileWriter to write the data to an Avro file.
  - Use a DatumReader and a DataFileReader to read the data from an Avro file.
- Avro is similar to a sequential file in Hadoop, which is a binary file format that stores records in a serialized form. However, Avro has some advantages over sequential files, such as :
  - Avro files are compact and splittable, which makes them suitable for large-scale data processing.
  - Avro files can be processed by various tools and frameworks, such as MapReduce, Spark, Hive, Pig, and Sqoop.
  - Avro files can handle schema evolution and schema projection, which means they can handle changes in the schema without breaking the compatibility or losing the data.
- Avro also has some disadvantages, such as:
  - Avro files are not human-readable, which makes them difficult to debug or inspect.
  - Avro files require a schema to read and write the data, which adds some complexity and overhead to the data processing.
  - Avro files do not support random access or indexing, which means they cannot be queried efficiently.