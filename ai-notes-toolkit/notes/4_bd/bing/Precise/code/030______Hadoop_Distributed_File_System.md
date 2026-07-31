#### Hadoop Distributed File System

Here is an example of code for Hadoop Distributed File System (HDFS) written in Java:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.IOException;

public class HDFSExample {
    public static void main(String[] args) throws IOException {
        Configuration conf = new Configuration();
        conf.set("fs.defaultFS", "hdfs://localhost:9000");
        FileSystem fs = FileSystem.get(conf);
        Path path = new Path("/user/hadoop/file.txt");
        if (fs.exists(path)) {
            System.out.println("File exists");
        } else {
            System.out.println("File does not exist");
        }
        fs.close();
    }
}
```
This code creates a `Configuration` object and sets the Hadoop file system to be HDFS with the `fs.defaultFS` property. It then creates a `FileSystem` object using the configuration and checks if a file exists at the specified path on the HDFS. If the file exists, it prints "File exists" to the console, otherwise it prints "File does not exist". Finally, it closes the `FileSystem` object.
