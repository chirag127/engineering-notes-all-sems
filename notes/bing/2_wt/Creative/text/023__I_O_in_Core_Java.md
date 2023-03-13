#### I/O in Core Java

- I/O stands for Input and Output, which are the basic operations of any program that interacts with external sources, such as files, networks, databases, etc.
- Core Java provides a rich set of classes and interfaces in the `java.io` and `java.nio` packages to support various I/O operations.
- The main concept behind I/O in Core Java is the **stream**, which is an abstract representation of a sequence of bytes that can be read from or written to a source or a destination.
- There are two types of streams in Core Java: **byte streams** and **character streams**. Byte streams deal with raw binary data, while character streams deal with text data encoded in a specific charset.
- Byte streams are subclasses of `InputStream` and `OutputStream`, while character streams are subclasses of `Reader` and `Writer`.
- Some of the common byte stream classes are `FileInputStream`, `FileOutputStream`, `BufferedInputStream`, `BufferedOutputStream`, `DataInputStream`, `DataOutputStream`, etc.
- Some of the common character stream classes are `FileReader`, `FileWriter`, `BufferedReader`, `BufferedWriter`, `InputStreamReader`, `OutputStreamWriter`, etc.
- Core Java also supports **serialization**, which is the process of converting an object into a stream of bytes that can be stored or transmitted, and **deserialization**, which is the reverse process of reconstructing an object from a stream of bytes.
- Serialization and deserialization are implemented by the `ObjectInputStream` and `ObjectOutputStream` classes, which extend `InputStream` and `OutputStream`, respectively.
- To make an object serializable, it must implement the `Serializable` interface, which is a marker interface with no methods.
- Core Java also provides the `java.nio` package, which stands for New I/O or Non-blocking I/O, which is an alternative way of performing I/O operations using **channels** and **buffers**.
- A channel is a connection to a source or a destination of data, such as a file, a socket, a pipe, etc. A buffer is a container for a fixed amount of data of a specific type, such as a byte, a char, an int, etc.
- Channels and buffers support both blocking and non-blocking modes of operation, which means that they can either wait for the data to be available or return immediately with whatever data is available.
- Some of the common channel classes are `FileChannel`, `SocketChannel`, `ServerSocketChannel`, `DatagramChannel`, etc.
- Some of the common buffer classes are `ByteBuffer`, `CharBuffer`, `IntBuffer`, etc.