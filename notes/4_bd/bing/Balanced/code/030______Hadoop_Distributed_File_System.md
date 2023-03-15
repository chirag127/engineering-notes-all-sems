#### Hadoop Distributed File System

The Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It is fault-tolerant and provides high throughput access to the data stored. It consists of a master server called NameNode and multiple slave servers called DataNodes. The NameNode manages the file system namespace and the metadata of the files and directories. The DataNodes store the actual data blocks of the files and serve read and write requests from the clients. The NameNode and the DataNodes communicate with each other using heartbeats and block reports.

To write code for HDFS, you need to use the FileSystem class or its successor, FileContext class. These classes provide an abstract interface to access different types of file systems, such as local, HDFS, S3, etc. You can use the methods of these classes to create, delete, rename, copy, move, and list files and directories. You can also use the methods of these classes to read and write data from and to the files.

Here is an example of how to write code for HDFS using the FileSystem class in Java:

```java
// Import the required classes
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

// Create a configuration object and set the HDFS URI
Configuration conf = new Configuration();
conf.set("fs.defaultFS", "hdfs://namenode:9000");

// Create a FileSystem object using the configuration
FileSystem fs = FileSystem.get(conf);

// Create a Path object for the file to be created
Path file = new Path("/user/hadoop/test.txt");

// Check if the file already exists
if (fs.exists(file)) {
  // Delete the file if it exists
  fs.delete(file, true);
}

// Create an output stream to write data to the file
OutputStream out = fs.create(file);

// Write some data to the file
out.write("Hello, HDFS!".getBytes());

// Close the output stream
out.close();

// Create an input stream to read data from the file
InputStream in = fs.open(file);

// Read the data from the file and print it to the console
int b;
while ((b = in.read()) != -1) {
  System.out.print((char) b);
}

// Close the input stream
in.close();

// Close the FileSystem object
fs.close();
```

This code creates a file named test.txt in the /user/hadoop directory on HDFS, writes some data to it, reads the data from it, and prints it to the console. You can run this code using the hadoop command:

```bash
$ hadoop jar hdfs-example.jar
Hello, HDFS!
```

This is one way of writing code for HDFS. You can also use other languages, such as Python, Scala, or R, to interact with HDFS using various libraries and frameworks. For more details, you can refer to the official documentation of Hadoop and the FileSystem API.