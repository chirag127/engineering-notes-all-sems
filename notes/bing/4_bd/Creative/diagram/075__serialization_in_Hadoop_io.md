Serialization in Hadoop IO is the process of converting structured data objects into byte streams for transmission over the network or permanent storage on disk. Deserialization is the reverse process of converting byte streams back to structured data objects. Hadoop supports different serialization frameworks, such as Writable, Avro, Thrift, and Protocol Buffers, that can be configured using the "io.serializations" property. Each serialization framework has its own advantages and disadvantages in terms of performance, compatibility, and ease of use.

The following ASCII diagram illustrates the basic architecture of a serialization framework in Hadoop:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Data Object    |      |  Serializer     |      |  Byte Stream    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Structured     |----->|  Converts data  |----->|  Binary format  |
|  data, such as  |      |  object to byte |      |  for network or |
|  Java objects,  |      |  stream         |      |  disk           |
|  Writables, etc.|      |                 |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+

+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Byte Stream    |      |  Deserializer   |      |  Data Object    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Binary format  |----->|  Converts byte  |----->|  Structured     |
|  for network or |      |  stream to data |      |  data, such as  |
|  disk           |      |  object         |      |  Java objects,  |
|                 |      |                 |      |  Writables, etc.|
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```