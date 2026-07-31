I/O in Core Java refers to the input and output operations performed by Java programs using the classes and interfaces in the java.io package. The main concept behind I/O in Java is the stream, which is an abstract representation of a sequence of bytes that can be read from or written to a source or destination. There are different types of streams in Java, such as byte streams, character streams, buffered streams, data streams, object streams, file streams, etc. Each type of stream has its own methods and features to handle different kinds of data and sources.

The following diagram shows a simplified overview of the I/O classes and interfaces in Java:

#### I/O in Core Java

```
+-------------------+    +-------------------+
|    InputStream    |    |   OutputStream    |
| (abstract class)  |    | (abstract class)  |
+-------------------+    +-------------------+
| +read(): int      |    | +write(int): void |
| +read(byte[]): int|    | +write(byte[]): void|
| +close(): void    |    | +close(): void    |
+-------------------+    +-------------------+
         ^                        ^
         |                        |
         |                        |
+-------------------+    +-------------------+
|    FileInputStream|    |  FileOutputStream |
| (concrete class)  |    | (concrete class)  |
+-------------------+    +-------------------+
| +FileInputStream(File) | | +FileOutputStream(File) |
| +FileInputStream(String)| | +FileOutputStream(String)|
+-------------------+    +-------------------+
         ^                        ^
         |                        |
         |                        |
+-------------------+    +-------------------+
|    BufferedInputStream| | BufferedOutputStream |
| (concrete class)  |    | (concrete class)  |
+-------------------+    +-------------------+
| +BufferedInputStream(InputStream) | | +BufferedOutputStream(OutputStream) |
| +read(): int      |    | +write(int): void |
| +read(byte[]): int|    | +write(byte[]): void|
| +close(): void    |    | +close(): void    |
+-------------------+    +-------------------+
         ^                        ^
         |                        |
         |                        |
+-------------------+    +-------------------+
|    DataInputStream|    |  DataOutputStream |
| (concrete class)  |    | (concrete class)  |
+-------------------+    +-------------------+
| +DataInputStream(InputStream) | | +DataOutputStream(OutputStream) |
| +readInt(): int   |    | +writeInt(int): void |
| +readDouble(): double|  | +writeDouble(double): void|
| +readUTF(): String|    | +writeUTF(String): void|
| +close(): void    |    | +close(): void    |
+-------------------+    +-------------------+
         ^                        ^
         |                        |
         |                        |
+-------------------+    +-------------------+
|    ObjectInputStream|  |  ObjectOutputStream |
| (concrete class)  |    | (concrete class)  |
+-------------------+    +-------------------+
| +ObjectInputStream(InputStream) | | +ObjectOutputStream(OutputStream) |
| +readObject(): Object| | +writeObject(Object): void |
| +close(): void    |    | +close(): void    |
+-------------------+    +-------------------+
```