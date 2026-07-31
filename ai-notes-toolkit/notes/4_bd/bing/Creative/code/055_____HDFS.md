### HDFS
HDFS stands for Hadoop Distributed File System. It is a file system that stores large amounts of data across multiple nodes in a cluster. HDFS provides high availability, fault tolerance, scalability, and parallel processing of data.

To write code for HDFS, you need to use the Hadoop command-line interface (CLI) or the Hadoop API in Java, Python, or other languages. Here are some examples of HDFS commands and code snippets:

- To list the files and directories in HDFS, you can use the `hdfs dfs -ls` command. For example, to list the files in the `/user` directory, you can run:

```bash
hdfs dfs -ls /user
```

- To create a directory in HDFS, you can use the `hdfs dfs -mkdir` command. For example, to create a directory named `/user/data`, you can run:

```bash
hdfs dfs -mkdir /user/data
```

- To copy a file from the local file system to HDFS, you can use the `hdfs dfs -put` command. For example, to copy a file named `sample.txt` from the local file system to the `/user/data` directory in HDFS, you can run:

```bash
hdfs dfs -put sample.txt /user/data
```

- To read a file from HDFS, you can use the `hdfs dfs -cat` command. For example, to read the file named `sample.txt` from the `/user/data` directory in HDFS, you can run:

```bash
hdfs dfs -cat /user/data/sample.txt
```

- To write code for HDFS using the Java API, you need to import the `org.apache.hadoop.fs` package and create a `FileSystem` object. For example, to create a directory named `/user/data` in HDFS using the Java API, you can write:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class HDFSExample {

  public static void main(String[] args) throws Exception {
    // Create a configuration object
    Configuration conf = new Configuration();
    // Set the HDFS URI
    conf.set("fs.defaultFS", "hdfs://localhost:9000");
    // Create a file system object
    FileSystem fs = FileSystem.get(conf);
    // Create a path object
    Path path = new Path("/user/data");
    // Create a directory in HDFS
    fs.mkdirs(path);
    // Close the file system
    fs.close();
  }
}
```

- To write code for HDFS using the Python API, you need to install the `hdfs` module and create a `Client` object. For example, to list the files and directories in the `/user` directory in HDFS using the Python API, you can write:

```python
from hdfs import InsecureClient

# Create a client object
client = InsecureClient('http://localhost:50070')
# List the files and directories in HDFS
client.list('/user')
```