Serialization in Hadoop io is the process of converting structured objects into byte streams for transmission over the network or permanent storage on disk  . Hadoop provides a mechanism for using different serialization frameworks in Hadoop , such as Writable, Avro, Thrift, and Protobuf. Serialization in Hadoop io can be illustrated by the following diagram:

##### Serialization in Hadoop io

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Structured    |      |  Serialized    |      |  Structured    |
|    Object      |      |    Byte        |      |    Object      |
|                |      |    Stream      |      |                |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
+-----v-----------------+      |      +-----------------v-----+
|                         |     |     |                         |
|  Serialization          |     |     |  Deserialization       |
|  Framework              |     |     |  Framework              |
|                         |     |     |                         |
+-------------------------+     |     +-------------------------+
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
+-----v-----------------+      |      +-----------------v-----+
|                         |     |     |                         |
|  RPC Protocol           |     |     |  RPC Protocol           |
|                         |     |     |                         |
+-------------------------+     |     +-------------------------+
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
+-----v-----------------+      |      +-----------------v-----+
|                         |     |     |                         |
|  Network                |<----+---->|  Network                |
|                         |     |     |                         |
+-------------------------+     |     +-------------------------+
```