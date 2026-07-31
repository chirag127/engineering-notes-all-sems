### Java interfaces to HDFS

- Java interfaces to HDFS are the application programming interfaces (APIs) that allow Java applications to interact with the Hadoop Distributed File System (HDFS).
- HDFS is a distributed and scalable file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS provides high availability, fault tolerance, and data locality for big data processing.
- Java interfaces to HDFS include the following classes and methods:

  - `org.apache.hadoop.fs.FileSystem`: This is the abstract base class for all Hadoop file systems. It provides methods for creating, deleting, renaming, reading, writing, and querying files and directories in HDFS.
  - `org.apache.hadoop.fs.Path`: This is the class that represents a file or a directory in HDFS. It encapsulates the URI scheme, the authority, and the path of the file or directory.
  - `org.apache.hadoop.fs.FSDataInputStream`: This is the class that provides input streams for reading data from HDFS files. It supports random access and seek operations.
  - `org.apache.hadoop.fs.FSDataOutputStream`: This is the class that provides output streams for writing data to HDFS files. It supports flush and sync operations.
  - `org.apache.hadoop.conf.Configuration`: This is the class that holds the configuration settings for Hadoop and HDFS. It can load configuration files from the classpath or from the HDFS.
  - `org.apache.hadoop.io.IOUtils`: This is the utility class that provides methods for copying data between input and output streams, closing streams, and converting data types.

- Some examples of using the Java interfaces to HDFS are:

  - Creating a file system object:

    ```java
    Configuration conf = new Configuration();
    FileSystem fs = FileSystem.get(conf);
    ```

  - Writing data to a file:

    ```java
    Path path = new Path("/path/to/file.txt");
    FSDataOutputStream out = fs.create(path);
    out.writeUTF("Hello, HDFS!");
    out.close();
    ```

  - Reading data from a file:

    ```java
    Path path = new Path("/path/to/file.txt");
    FSDataInputStream in = fs.open(path);
    String data = in.readUTF();
    in.close();
    System.out.println(data);
    ```

  - Listing files and directories:

    ```java
    Path path = new Path("/path/to/directory");
    FileStatus[] status = fs.listStatus(path);
    for (FileStatus file : status) {
      System.out.println(file.getPath());
    }
    ```

  - Deleting a file or a directory:

    ```java
    Path path = new Path("/path/to/file_or_directory");
    boolean deleted = fs.delete(path, true); // true for recursive deletion
    System.out.println(deleted);
    ```

- References:

  - [CitizenChoice](https://citizenchoice.in/course/big-data/Chapter%203/8-java-interfaces-to-hdfs)
  - [HDFS Interfaces - Tutorial](https://www.vskills.in/certification/tutorial/hdfs-interfaces/)
  - [java interface for hadoop hdfs filesystems – examples and concept](https://timepasstechies.com/java-interface-hadoop-hdfs-filesystems-examples-concept/)
  - [hadoop - Upload data to HDFS with Java API - Stack Overflow](https://stackoverflow.com/questions/32399075/upload-data-to-hdfs-with-java-api)
  - [HDFS Tutorial: Architecture, Read & Write Operation using Java API - Guru99](https://www.guru99.com/learn-hdfs-a-beginners-guide.html)