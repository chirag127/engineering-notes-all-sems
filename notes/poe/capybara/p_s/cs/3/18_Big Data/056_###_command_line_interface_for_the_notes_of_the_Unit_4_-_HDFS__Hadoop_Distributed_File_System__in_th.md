### Command Line Interface for HDFS

Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications. It provides a distributed file system that can handle large amounts of data and is fault-tolerant. HDFS can be accessed through a command-line interface (CLI) that provides a range of commands to interact with the file system.

Here are some important commands for HDFS CLI:

#### 1. Creating a directory

To create a new directory in HDFS, use the following command:

```
hdfs dfs -mkdir /path/to/directory
```

#### 2. Uploading files

To upload a file from the local file system to HDFS, use the following command:

```
hdfs dfs -put /path/to/local/file /path/to/hdfs/location
```

#### 3. Downloading files

To download a file from HDFS to the local file system, use the following command:

```
hdfs dfs -get /path/to/hdfs/file /path/to/local/location
```

#### 4. Listing directories and files

To list the contents of a directory in HDFS, use the following command:

```
hdfs dfs -ls /path/to/directory
```

#### 5. Removing files and directories

To remove a file or directory from HDFS, use the following command:

```
hdfs dfs -rm /path/to/file/or/directory
```

#### 6. Checking the status of a file

To check the status of a file in HDFS, use the following command:

```
hdfs dfs -stat /path/to/file
```

#### 7. Setting and checking permissions

To set permissions for a file or directory in HDFS, use the following command:

```
hdfs dfs -chmod <permissions> /path/to/file/or/directory
```

To check the permissions for a file or directory in HDFS, use the following command:

```
hdfs dfs -ls /path/to/file/or/directory
```

#### Advantages of HDFS CLI

- Provides a simple and efficient way to interact with HDFS.
- Allows for automation of file operations through scripts.
- Supports a wide range of file operations.

#### Disadvantages of HDFS CLI

- Requires knowledge of command-line interfaces and Hadoop file systems.
- Commands can be complex and difficult to remember.

#### Example Usage

Here is an example usage of the HDFS CLI to upload a file to HDFS:

```
hdfs dfs -put /home/user/data.txt /user/hadoop/data/
```

#### Applications

The HDFS CLI is primarily used for managing files and directories in HDFS. It can be used for a wide range of applications, including:

- Uploading and downloading data to and from HDFS.
- Managing files and directories in HDFS.
- Automating file operations through scripts.