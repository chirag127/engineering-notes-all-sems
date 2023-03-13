### I/O in Core Java

Input/Output (I/O) operations are a crucial part of any programming language. In Core Java, input/output is performed using streams. A stream is a sequence of data that flows from a source to a destination. The source and destination can be a file, a network connection, or any other input/output device.

Core Java provides several classes for performing input/output operations. These classes are organized into two categories: byte streams and character streams.

#### Byte Streams

Byte streams are used for reading and writing binary data. In Core Java, the `InputStream` and `OutputStream` classes are used for performing byte-oriented I/O operations.

##### Mnemonics and Learning Tricks

One useful mnemonic for remembering the difference between `InputStream` and `OutputStream` is to think of the "I" in `InputStream` as standing for "incoming" data, while the "O" in `OutputStream` stands for "outgoing" data.

#### Character Streams

Character streams are used for reading and writing text data. In Core Java, the `Reader` and `Writer` classes are used for performing character-oriented I/O operations.

##### Mnemonics and Learning Tricks

One useful mnemonic for remembering the difference between `Reader` and `Writer` is to think of the "R" in `Reader` as standing for "reading" data, while the "W" in `Writer` stands for "writing" data.

#### Advantages of I/O in Core Java

- Core Java's I/O classes provide a consistent and easy-to-use interface for performing input/output operations.
- The byte and character streams allow for flexible handling of different data types.
- Core Java's I/O classes support a wide range of input/output devices, including files, network connections, and other devices.

#### Disadvantages of I/O in Core Java

- The I/O classes in Core Java can be complex to learn and use effectively.
- Some I/O operations can be slow, particularly when dealing with large files or network connections.

#### Example Usage

Here is an example of reading text input from the console using a `BufferedReader`:

```java
import java.io.*;

public class Example {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter your name: ");
        String name = reader.readLine();
        System.out.println("Hello, " + name + "!");
    }
}
```

#### Applications of I/O in Core Java

- Reading and writing data to and from files
- Communicating with network sockets
- Parsing and generating data in various formats, such as CSV or JSON