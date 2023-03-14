#### I/O in Core Java

- I/O stands for input/output, which refers to the process of reading and writing data from and to different sources and destinations, such as files, network, console, etc.
- Java provides a rich set of classes and interfaces in the `java.io` package to handle various types of I/O operations.
- The main concepts and components of I/O in Core Java are:

  - **Streams**: A stream is an abstraction that represents a sequence of bytes that can be read from or written to a source or destination. Streams can be categorized into two types: input streams and output streams. Input streams are used to read data from a source, while output streams are used to write data to a destination. Streams can also be classified based on the type of data they handle: byte streams and character streams. Byte streams deal with raw bytes, while character streams deal with Unicode characters.
  - **Readers and Writers**: Readers and writers are subclasses of character streams that provide convenient methods for reading and writing text data. Readers and writers can be further divided into two types: buffered and unbuffered. Buffered readers and writers use an internal buffer to store data temporarily, which improves the performance and efficiency of I/O operations. Unbuffered readers and writers directly access the underlying stream, which may be slower and less reliable.
  - **File I/O**: File I/O refers to the process of reading and writing data from and to files on the disk. Java provides several classes and methods to perform file I/O, such as `File`, `FileInputStream`, `FileOutputStream`, `FileReader`, `FileWriter`, `RandomAccessFile`, etc. File I/O can be done using either byte streams or character streams, depending on the type and format of the file. File I/O can also be done using the newer `java.nio.file` package, which offers more features and flexibility than the `java.io` package.
  - **Console I/O**: Console I/O refers to the process of reading and writing data from and to the standard input and output devices, such as the keyboard and the screen. Java provides a class called `Console` to perform console I/O, which can be obtained using the `System.console()` method. The `Console` class provides methods such as `readLine()`, `readPassword()`, `format()`, etc. to read and write text data from and to the console. Console I/O can also be done using the `System.in`, `System.out`, and `System.err` streams, which are byte streams that can be wrapped with readers and writers for convenience.
  - **Network I/O**: Network I/O refers to the process of reading and writing data from and to remote hosts over the network. Java provides a class called `Socket` to perform network I/O, which represents a connection between two endpoints. A socket can be created using the `Socket` constructor, which takes the host name and the port number as parameters. The socket can then be used to obtain input and output streams, which can be used to read and write data from and to the network. Network I/O can also be done using the `ServerSocket` class, which represents a server that can accept connections from clients. A server socket can be created using the `ServerSocket` constructor, which takes the port number as a parameter. The server socket can then be used to obtain a socket for each client using the `accept()` method.

- Some of the advantages of using I/O in Core Java are:

  - It provides a consistent and uniform way of handling different types of I/O operations, regardless of the source or destination.
  - It supports various features and functionalities, such as buffering, encoding, serialization, compression, encryption, etc. to enhance the performance and security of I/O operations.
  - It follows the principle of composition, which allows creating complex and customized streams by combining and wrapping existing streams.

- Some of the disadvantages of using I/O in Core Java are:

  - It may be complex and verbose to use, especially for beginners and simple tasks.
  - It may be inefficient and slow for some scenarios, such as concurrent and asynchronous I/O, which require more advanced techniques and frameworks.
  - It may be outdated and deprecated for some features, such as file I/O, which have been replaced by newer and better alternatives in the `java.nio` package.

- Some of the examples of using I/O in Core Java are:

  - Copying a file using byte streams:

    ```java
    import java.io.*;

    public class CopyFile {
      public static void main(String[] args) {
        // Declare input and output streams
        FileInputStream in = null;
        FileOutputStream out = null;

        try {
          // Create input and output streams for the