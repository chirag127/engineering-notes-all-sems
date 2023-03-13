##### Serialization in Hadoop io

- Serialization is the process of converting structured data into a byte stream for transmission over the network or storage on disk.
- Deserialization is the reverse process of converting a byte stream back into structured data.
- Hadoop uses serialization for interprocess communication between nodes in the system using remote procedure calls (RPCs).
- Hadoop also uses serialization for storing data in HDFS and for passing data between map and reduce tasks.
- Hadoop provides a mechanism for using different serialization frameworks by defining a list of `Serialization` classes in the property `io.serializations`.
- A `Serialization` class knows how to create `Serializer` and `Deserializer` objects for a given type of data.
- A `Serializer` object can serialize an object of a given type into an `OutputStream`.
- A `Deserializer` object can deserialize an object of a given type from an `InputStream`.
- Hadoop provides a default `Serialization` class for `Writable` objects, which delegates to the `Writable.write(DataOutput)` and `Writable.readFields(DataInput)` methods.
- Hadoop also supports other serialization frameworks, such as Avro, Thrift, and Protocol Buffers, by providing corresponding `Serialization` classes.