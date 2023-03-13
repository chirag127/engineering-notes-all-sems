I/O in Core Java refers to the input and output operations performed by Java programs using the classes and interfaces in the java.io package. Java uses the concept of a stream to make I/O operations fast and efficient. A stream is a sequence of data that can be read from a source or written to a destination. Streams can be byte-oriented or character-oriented, depending on the type of data they handle. Byte-oriented streams are used for binary data, such as images, audio, or video. Character-oriented streams are used for text data, such as documents, web pages, or source code.

The following diagram illustrates the basic architecture of I/O in Core Java using ASCII characters:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Byte Streams   |    |  Character      |    |  Buffered       |
|                 |    |  Streams        |    |  Streams        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  InputStream    |    |  Reader         |    |  BufferedReader |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  OutputStream   |    |  Writer         |    |  BufferedWriter |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  FileInputStream|    |  FileReader     |    |  PrintWriter    |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  FileOutputStream|    |  FileWriter     |    |  PrintStream    |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  DataInputStream|    |  InputStreamReader|  |  LineNumberReader|
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  DataOutputStream|   |  OutputStreamWriter| |  PushbackReader  |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram shows the hierarchy of the classes and interfaces in the java.io package. The byte streams are the base classes for all the other streams. The character streams are wrappers around the byte streams that provide methods for reading and writing text data. The buffered streams are subclasses of the character streams that improve the performance by using internal buffers. The file streams are subclasses of the byte streams that provide methods for reading and writing files. The data streams are subclasses of the byte streams that provide methods for reading and writing primitive data types and strings. The print streams are subclasses of the character streams that provide methods for printing formatted output. The input stream reader and output stream writer are bridges between the byte streams and the character streams that allow the conversion of bytes to characters and vice versa. The line number reader and pushback reader are subclasses of the buffered reader that provide additional functionality, such as counting the lines and pushing back characters to the stream.