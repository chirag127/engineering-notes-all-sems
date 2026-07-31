#### I/O in Core Java
- I/O stands for Input/Output and is used to read and write data.
- In Core Java, I/O is handled by the java.io package.
- The java.io package contains classes for system input and output through data streams, serialization and the file system.
- The two main classes for handling I/O operations are `InputStream` and `OutputStream`.
- `InputStream` is an abstract class that represents an input stream of bytes.
- `OutputStream` is an abstract class that represents an output stream of bytes.
- There are several subclasses of `InputStream` and `OutputStream` that provide functionality for reading and writing different types of data, such as `FileInputStream` and `FileOutputStream` for reading and writing data to and from files.
- One of the advantages of using the I/O classes in Core Java is that they provide a consistent interface for reading and writing data, regardless of the data source or destination.
- One of the disadvantages of using the I/O classes in Core Java is that they can be somewhat complex to use, especially for beginners.
- A common use case for I/O in Core Java is reading data from a file, processing it, and then writing the results to another file.
- Here is an example of using `FileInputStream` and `FileOutputStream` to copy the contents of one file to another:

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class CopyFile {
    public static void main(String[] args) {
        try (FileInputStream in = new FileInputStream("input.txt");
             FileOutputStream out = new FileOutputStream("output.txt")) {
            int c;
            while ((c = in.read()) != -1) {
                out.write(c);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
- This code reads the contents of the file `input.txt` one byte at a time using the `read()` method of `FileInputStream`, and writes the data to the file `output.txt` using the `write()` method of `FileOutputStream`.
- The `try-with-resources` statement is used to automatically close the input and output streams when the try block is exited.
- This is just one example of how I/O can be used in Core Java. There are many other classes and methods available in the java.io package for handling different types of data and I/O operations.