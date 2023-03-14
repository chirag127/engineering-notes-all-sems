Serialization in Hadoop io is a mechanism for using different serialization frameworks in Hadoop. The property "io.serializations" defines a list of Serialization s that know how to create Serializer s and Deserializer s. Serialization refers to the conversion of structured objects into byte streams for transmission over the network or permanent storage on disk; deserialization refers to the conversion of byte streams back to the original structured objects.

The following diagram illustrates the basic architecture of serialization in Hadoop io using ASCII characters:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Structured     |     |  Byte Stream    |     |  Structured     |
|  Object         |     |                 |     |  Object         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Serialization  |     |  Network or     |     |  Deserialization|
|  Framework      |     |  Disk Storage   |     |  Framework      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Serializer     |---->|                 |<----|  Deserializer   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```