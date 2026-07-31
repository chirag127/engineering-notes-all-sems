#### Java interfaces to HDFS

Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It is a part of the Apache Hadoop project and provides scalable and reliable data storage for Hadoop applications.

Java interfaces to HDFS allow developers to interact with the file system using the Java programming language. Some of the key Java interfaces to HDFS include:

1. **FileSystem**: This is the primary interface for accessing HDFS. It provides methods for creating, deleting, and renaming files and directories, as well as for reading and writing data.

2. **FileContext**: This interface provides a more advanced API for interacting with HDFS. It includes methods for setting permissions, creating symbolic links, and working with file attributes.

3. **FSDataInputStream**: This interface extends the standard Java `InputStream` and provides methods for reading data from HDFS.

4. **FSDataOutputStream**: This interface extends the standard Java `OutputStream` and provides methods for writing data to HDFS.

5. **Path**: This class represents a file or directory in HDFS. It is used to specify the location of files and directories when interacting with the file system.

Here is an example of how to use the `FileSystem` interface to create a new file in HDFS:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.IOException;

public class HdfsExample {
    public static void main(String[] args) throws IOException {
        Configuration conf = new Configuration();
        conf.set("fs.defaultFS", "hdfs://localhost:9000");
        FileSystem fs = FileSystem.get(conf);
        Path path = new Path("/user/example/file.txt");
        if (!fs.exists(path)) {
            fs.create(path);
            System.out.println("File created");
        } else {
            System.out.println("File already exists");
        }
        fs.close();
    }
}
```

In this example, we create a new `Configuration` object and set the `fs.defaultFS` property to the URI of our HDFS instance. We then use the `FileSystem.get` method to obtain an instance of the `FileSystem` interface. We create a new `Path` object to represent the file we want to create and use the `exists` method to check if the file already exists. If it does not, we use the `create` method to create the file. Finally, we close the `FileSystem` instance to release any resources it is holding.

A mnemonic to remember the key Java interfaces to HDFS is **"F.F.F.P."** which stands for **FileSystem, FileContext, FSDataInputStream, FSDataOutputStream, and Path**. This can be helpful when trying to recall the different interfaces available for interacting with HDFS using Java.