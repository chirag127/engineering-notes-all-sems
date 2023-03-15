### HDFS

Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It is highly fault-tolerant and is designed to be deployed on low-cost hardware. Here is an example of how to write data to HDFS using the Hadoop API in Java:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class HdfsWrite {
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        conf.set("fs.defaultFS", "hdfs://localhost:9000");
        FileSystem fs = FileSystem.get(conf);
        Path path = new Path("/user/hadoop/test.txt");
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(fs.create(path)));
        writer.write("Hello, HDFS!");
        writer.close();
        fs.close();
    }
}
```
This code creates a new file in HDFS at the specified path and writes the string "Hello, HDFS!" to it. The `fs.defaultFS` property specifies the HDFS URI, and the `FileSystem` object is used to interact with the file system. The `BufferedWriter` is used to write data to the file.