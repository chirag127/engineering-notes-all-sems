### Serialization in HDFS (Unit 4 - Hadoop Distributed File System)

1. Serialization is the process of converting data structures or objects into a format that can be stored or transmitted and reconstructed later.
2. In the context of HDFS, serialization is used to store data in a format that can be efficiently read and written by the distributed file system.
3. HDFS uses a specific serialization framework called Writable to serialize data.
4. Writable provides a set of classes for common data types, such as IntWritable for integers and Text for strings.
5. To use Writable, data must be converted into Writable objects before being written to HDFS and converted back after being read from HDFS.
6. Custom data types can also be serialized by implementing the Writable interface and providing methods for reading and writing data.
7. Serialization is important in HDFS because it allows data to be efficiently stored and transmitted between nodes in the distributed file system.
8. It also enables data to be processed in parallel by multiple nodes, as each node can read and write data in a standardized format.
