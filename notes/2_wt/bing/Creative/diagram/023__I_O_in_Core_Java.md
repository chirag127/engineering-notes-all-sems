I/O in Core Java refers to the input and output operations performed by Java programs using the classes and interfaces in the java.io and java.nio packages. These packages provide various streams, buffers, channels, selectors, charsets, encoders, decoders, files, file systems and other components to support I/O operations.

The following diagram illustrates the basic architecture of I/O in Core Java using ASCII characters:

```
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    java.io      |  |    java.nio     |  |  java.nio.file  |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Input Streams  |  |    Buffers      |  |      Paths      |
|                 |  |                 |  |                 |
| Output Streams  |  |    Channels     |  |      Files      |
|                 |  |                 |  |                 |
| Object Streams  |  |    Selectors    |  |  File Systems   |
|                 |  |                 |  |                 |
|  Data Streams   |  |    Charsets     |  | File Attributes |
|                 |  |                 |  |                 |
|  Console I/O    |  |  Encoders/      |  |  File Tree      |
|                 |  |  Decoders       |  |  Operations     |
|  Scanning and   |  |                 |  |                 |
|  Formatting     |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    System       |  |    Memory       |  |    File         |
|    Devices      |  |    Devices      |  |    Devices      |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
```