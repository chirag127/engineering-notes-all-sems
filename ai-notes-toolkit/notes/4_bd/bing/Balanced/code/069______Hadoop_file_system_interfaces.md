Hello, I am Sydney, your AI assistant. I can write code for you in markdown format. Here is the code for Hadoop file system interfaces:

#### Hadoop file system interfaces

```java
// Import the required packages
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

// Create a configuration object
Configuration conf = new Configuration();

// Set the Hadoop file system URI
conf.set("fs.defaultFS", "hdfs://localhost:9000");

// Get a file system object
FileSystem fs = FileSystem.get(conf);

// Create a new file
Path file = new Path("/user/sydney/test.txt");
fs.create(file);

// Write some data to the file
fs.append(file).write("Hello, this is a test file.\n".getBytes());

// Close the file system
fs.close();
```