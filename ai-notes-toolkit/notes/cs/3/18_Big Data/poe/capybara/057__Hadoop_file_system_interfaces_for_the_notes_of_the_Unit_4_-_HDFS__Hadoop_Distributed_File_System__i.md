

### Hadoop File System Interfaces

Hadoop Distributed File System (HDFS) provides several interfaces for interacting with the file system. These interfaces make it easy for users to manage and manipulate files and directories stored in HDFS. Here are some of the important Hadoop file system interfaces:

1. **Command-Line Interface (CLI):** The CLI is the most basic interface for interacting with HDFS. It provides a set of shell commands that can be used to manage files and directories stored in HDFS. Some of the commonly used CLI commands include `ls`, `mkdir`, `put`, `get`, `rm`, `mv`, and `cp`.

2. **Java API:** Hadoop provides a set of Java classes that can be used to interact with HDFS. These classes are part of the `org.apache.hadoop.fs` package and can be used to create, read, and write files stored in HDFS. Some of the commonly used classes include `FileSystem`, `Path`, `FSDataInputStream`, and `FSDataOutputStream`.

3. **Hadoop Streaming API:** The Hadoop Streaming API allows users to write MapReduce jobs in languages other than Java (such as Python, Perl, or Ruby). This API uses a standard input/output format that can be used to read and write data to HDFS.

4. **WebHDFS:** WebHDFS is a RESTful API that provides a HTTP-based interface for interacting with HDFS. It allows users to create, read, and write files and directories stored in HDFS. WebHDFS can be used with any programming language that supports HTTP requests.

5. **HDFS NFS Gateway:** The HDFS NFS Gateway provides a standard Network File System (NFS) interface for accessing files and directories stored in HDFS. This allows users to mount HDFS as a local file system on their machines and access files using standard NFS commands.

In conclusion, Hadoop provides several interfaces for interacting with HDFS. These interfaces make it easy for users to manage and manipulate files and directories stored in HDFS using a variety of programming languages and tools. Understanding these interfaces is essential for working with HDFS and building applications that use Hadoop.