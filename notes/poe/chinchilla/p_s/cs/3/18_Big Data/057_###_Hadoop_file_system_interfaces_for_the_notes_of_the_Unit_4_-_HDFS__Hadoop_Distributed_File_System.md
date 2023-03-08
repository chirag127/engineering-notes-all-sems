### Hadoop File System Interfaces

Hadoop Distributed File System (HDFS) is a distributed file system that is designed to store large data sets across multiple commodity hardware machines. HDFS is a key component of the Hadoop ecosystem and provides a reliable, scalable, and fault-tolerant storage system for big data applications. HDFS provides several interfaces for accessing the file system, including:

1. Command Line Interface (CLI): HDFS provides a command-line interface (CLI) for interacting with the file system. The CLI provides a set of commands that can be used to perform various operations on files and directories in the file system. Some of the common CLI commands are `ls`, `mkdir`, `rm`, `cp`, `mv`, etc.

2. Java API: HDFS provides a Java API for developers to interact with the file system. The Java API provides a set of classes and methods that can be used to perform various file system operations. The Java API can be used to write Hadoop MapReduce jobs and other Hadoop applications.

3. WebHDFS REST API: HDFS provides a REST API called WebHDFS that can be used to interact with the file system over HTTP. The WebHDFS API provides a set of REST endpoints that can be used to perform various file system operations.

4. NFS Gateway: HDFS also provides an NFS gateway that allows users to access the file system using the NFS protocol. The NFS gateway provides a standard file system interface that can be used by applications that are not Hadoop-aware.

Advantages of Hadoop File System Interfaces:
- CLI provides a simple and easy-to-use interface for interacting with the file system.
- Java API provides a powerful and flexible interface for developers to interact with the file system.
- WebHDFS API provides a RESTful interface that can be used by applications that are not written in Java.
- NFS gateway provides a standard file system interface that can be used by applications that are not Hadoop-aware.

Disadvantages of Hadoop File System Interfaces:
- CLI can be difficult to use for complex operations.
- Java API can be complex and requires knowledge of the Hadoop framework.
- WebHDFS API can be slow for large data transfers.
- NFS gateway can have performance issues and may not be suitable for high-performance applications.

Examples of Hadoop File System Interfaces:
- Using the CLI to create a new directory in HDFS: `hdfs dfs -mkdir /user/hadoop/data`
- Using the Java API to read a file from HDFS: `FileSystem fs = FileSystem.get(new Configuration()); InputStream in = fs.open(new Path("/user/hadoop/data/file.txt"));`
- Using the WebHDFS API to upload a file to HDFS: `curl -i -X PUT -T localfile.txt "http://<HOST>:<PORT>/webhdfs/v1/user/hadoop/data/file.txt?op=CREATE"`
- Using the NFS gateway to mount HDFS as a file system: `mount -t nfs -o vers=3,proto=tcp,nfsvers=3,rsize=1048576,wsize=1048576,hard,intr <HOST>:/ /mnt/hdfs`

Applications of Hadoop File System Interfaces:
- Storing and accessing large data sets in HDFS.
- Developing Hadoop MapReduce jobs and other Hadoop applications using the Java API.
- Integrating non-Hadoop applications with HDFS using the WebHDFS API and NFS gateway.