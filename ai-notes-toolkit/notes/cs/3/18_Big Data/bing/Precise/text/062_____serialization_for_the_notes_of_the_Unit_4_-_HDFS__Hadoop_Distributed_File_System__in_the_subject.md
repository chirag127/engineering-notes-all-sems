### Serialization for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

1. Serialization is the process of converting an object into a stream of bytes to store the object or transmit it to memory, a database, or a file.
2. Its main purpose is to save the state of an object in order to be able to recreate it when needed.
3. The reverse process is called deserialization.
4. HDFS uses serialization to store data in a distributed manner.
5. Serialization is important in HDFS because it allows data to be stored in a format that can be easily accessed and processed by the system.
6. HDFS uses a specific serialization framework called Writable to serialize and deserialize data.
7. Writable provides a set of classes for common data types and allows developers to create custom Writable classes for more complex data structures.
8. Serialization in HDFS is optimized for performance and is designed to minimize the amount of data that needs to be transmitted over the network.
9. This is important in a distributed system like HDFS where data is stored on multiple nodes and needs to be accessed and processed quickly.
