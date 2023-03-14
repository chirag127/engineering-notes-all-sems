#### I/O in Core Java

- I/O stands for Input and Output, which is used to process the data from the source and send the data to the destination.
- Java uses the concept of a stream to make I/O operations fast and efficient. A stream is a sequence of data that can be read from or written to a source or a destination.
- The java.io package contains all the classes and interfaces required for input and output operations in Java. It supports various types of data, such as bytes, characters, objects, files, etc.
- The java.nio package contains classes and interfaces for non-blocking and asynchronous I/O operations. It also provides access to file systems and file attributes.
- The main types of streams in Java are:

  - Byte streams: These are low-level streams that handle I/O of raw binary data. They are abstracted by the InputStream and OutputStream classes and their subclasses.
  - Character streams: These are high-level streams that handle I/O of character data, automatically handling translation to and from the local character set. They are abstracted by the Reader and Writer classes and their subclasses.
  - Buffered streams: These are streams that optimize input and output by reducing the number of calls to the native API. They wrap around other streams and provide buffering and flushing mechanisms. They are implemented by the BufferedInputStream, BufferedOutputStream, BufferedReader and BufferedWriter classes.
  - Data streams: These are streams that handle binary I/O of primitive data types and String values. They are implemented by the DataInputStream and DataOutputStream classes.
  - Object streams: These are streams that handle binary I/O of objects. They use serialization and deserialization to convert objects to and from bytes. They are implemented by the ObjectInputStream and ObjectOutputStream classes.

- Some of the common classes and interfaces for file I/O and file system operations are:

  - File: This class represents a file or a directory in the file system. It provides methods to check, create, delete, rename, and list files and directories.
  - Path: This class represents a path in the file system. It provides methods to manipulate, normalize, resolve, and compare paths. It also supports symbolic and hard links.
  - Files: This class provides static methods to perform various file operations, such as copying, moving, reading, writing, and finding files. It also provides methods to access and modify file attributes.
  - FileSystem: This class represents a file system and provides methods to get information about the file system, such as the root directories, the separator characters, and the supported file attributes.
  - FileSystems: This class provides static methods to access and create file systems. It also supports creating custom file system providers and zip file system providers.
  - FileChannel: This class represents a channel for file I/O. It supports reading, writing, mapping, and locking files. It also supports transferring data between channels.