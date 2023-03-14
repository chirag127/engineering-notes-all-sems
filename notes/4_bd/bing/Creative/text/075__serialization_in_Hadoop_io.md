##### Serialization in Hadoop io

- Serialization is the process of converting structured data into a byte stream for transmission over the network or storage on disk.
- Deserialization is the process of converting the byte stream back into the original structured data.
- Hadoop uses serialization for interprocess communication between nodes in the system using remote procedure calls (RPCs).
- Hadoop also uses serialization for storing data in different file formats, such as plain text, sequence files, RC files, Avro, and Parquet.
- Hadoop provides a mechanism for using different serialization frameworks by defining a list of Serialization classes in the property "io.serializations".
- A Serialization class knows how to create Serializer and Deserializer objects for a given type of data.
- A Serializer object can write an instance of a data type to an output stream, and a Deserializer object can read an instance of a data type from an input stream.
- Hadoop comes with two built-in Serialization classes: WritableSerialization and JavaSerialization.
- WritableSerialization is the default serialization framework for Hadoop. It uses the Writable interface to define how data types can be serialized and deserialized.
- JavaSerialization is an experimental serialization framework that uses the Java Serializable interface to serialize and deserialize data types.
- Other serialization frameworks, such as Avro and Parquet, can be added to Hadoop by implementing the Serialization interface and adding their names to the "io.serializations" property.