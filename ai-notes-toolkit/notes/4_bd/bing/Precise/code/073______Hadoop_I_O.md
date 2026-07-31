#### Hadoop I/O
Hadoop provides its own implementations of several standard Java I/O classes, which are optimized for use within the Hadoop environment. Here is an example of how to use Hadoop's `SequenceFile` class to write key-value pairs to a file:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.SequenceFile;
import org.apache.hadoop.io.Text;

Configuration conf = new Configuration();
FileSystem fs = FileSystem.get(conf);
Path path = new Path("/tmp/sequencefile");

IntWritable key = new IntWritable();
Text value = new Text();
SequenceFile.Writer writer = SequenceFile.createWriter(fs, conf, path, key.getClass(), value.getClass());

for (int i = 0; i < 100; i++) {
    key.set(i);
    value.set("Value" + i);
    writer.append(key, value);
}

writer.close();
```

This code creates a new `SequenceFile.Writer` object, which is used to write key-value pairs to a file located at `/tmp/sequencefile`. The key and value classes are specified as `IntWritable` and `Text`, respectively. The `for` loop writes 100 key-value pairs to the file, where the key is an integer and the value is a string. Finally, the `writer` is closed to flush all data to the file.
