#### I/O in Core Java

- I/O in Core Java stands for Input/Output in Core Java. It is used to process the input and produce the output in a Java program.   
- I/O in Core Java uses the concept of a **stream** to make I/O operations fast. A stream is a sequence of data that can be read from or written to a source or a destination.    
- The `java.io` package contains all the classes and interfaces required for input and output operations. Some of the important classes and interfaces in this package are:    

  - `InputStream` and `OutputStream`: These are abstract classes that represent byte streams. They are the base classes for all other byte stream classes.    
  - `Reader` and `Writer`: These are abstract classes that represent character streams. They are the base classes for all other character stream classes.    
  - `FileInputStream` and `FileOutputStream`: These are subclasses of `InputStream` and `OutputStream` that read from and write to files.    
  - `FileReader` and `FileWriter`: These are subclasses of `Reader` and `Writer` that read from and write to files.    
  - `BufferedInputStream` and `BufferedOutputStream`: These are subclasses of `InputStream` and `OutputStream` that provide buffering for byte streams. Buffering improves the performance of I/O operations by reducing the number of system calls.    
  - `BufferedReader` and `BufferedWriter`: These are subclasses of `Reader` and `Writer` that provide buffering for character streams. Buffering improves the performance of I/O operations by reducing the number of system calls.    
  - `DataInputStream` and `DataOutputStream`: These are subclasses of `InputStream` and `OutputStream` that provide methods for reading and writing primitive data types and strings.    
  - `ObjectInputStream` and `ObjectOutputStream`: These are subclasses of `InputStream` and `OutputStream` that provide methods for reading and writing objects. They use a mechanism called **serialization** to convert objects into bytes and vice versa. Serialization allows a program to write whole objects out to streams and read them back again.    
  - `PrintStream` and `PrintWriter`: These are subclasses of `OutputStream` and `Writer` that provide methods for printing various data types and strings. They are commonly used to write to the standard output and error streams.    
  - `Scanner`: This is a class that provides methods for parsing various data types and strings from a source. It can read from any object that implements the `Readable` interface, such as `InputStream`, `Reader`, or `String`.    
  - `File`: This is a class that represents a file or a directory in the file system. It provides methods for creating, deleting, renaming, and checking the properties of files and directories.    

- I/O in Core Java can be classified into two types: **byte-oriented I/O** and **character-oriented I/O**. Byte-oriented I/O deals with bytes, while character-oriented I/O deals with characters. Characters are encoded into bytes using a **charset**, which is a mapping between characters and bytes. The default charset in Java is **UTF-8**, which can encode all Unicode characters.     
- Byte-oriented