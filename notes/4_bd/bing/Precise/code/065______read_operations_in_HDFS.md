#### Read operations in HDFS

Here is an example of how to perform read operations in HDFS using the Hadoop FileSystem API:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import java.io.InputStream;
import java.net.URI;

public class HDFSRead {
    public static void main(String[] args) throws Exception {
        String uri = args[0];
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(URI.create(uri), conf);
        InputStream in = null;
        try {
            in = fs.open(new Path(uri));
            // Read data from the input stream
        } finally {
            in.close();
        }
    }
}
```

This code reads data from a file in HDFS by opening an input stream to the file and reading data from the stream. The input stream is closed in the `finally` block to ensure that resources are released properly.