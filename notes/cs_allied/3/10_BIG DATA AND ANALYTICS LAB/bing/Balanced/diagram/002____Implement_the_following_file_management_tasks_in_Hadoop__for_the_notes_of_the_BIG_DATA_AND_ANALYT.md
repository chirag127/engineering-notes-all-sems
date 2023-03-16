## Implement the following file management tasks in Hadoop:

- Hadoop is a framework that allows distributed processing of large data sets across clusters of computers using simple programming models.
- Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications. It provides high-performance access to data across scalable Hadoop clusters.
- HDFS operations and commands are used to perform various file management tasks on HDFS, such as creating directories, copying files, deleting files, changing permissions, etc.
- Some of the common HDFS commands are:

  - `hadoop fs -ls`: List the contents of a directory.
  - `hadoop fs -mkdir`: Create a directory.
  - `hadoop fs -put`: Copy a file from local file system to HDFS.
  - `hadoop fs -get`: Copy a file from HDFS to local file system.
  - `hadoop fs -cat`: Display the contents of a file.
  - `hadoop fs -rm`: Delete a file.
  - `hadoop fs -rmdir`: Delete a directory.
  - `hadoop fs -chmod`: Change the permissions of a file or directory.
  - `hadoop fs -chown`: Change the owner and group of a file or directory.
  - `hadoop fs -du`: Display the disk usage of a file or directory.
  - `hadoop fs -df`: Display the available space on the file system.
  - `hadoop fs -help`: Display the help for a command.

- To execute HDFS commands, you need to prefix them with `hadoop fs` or `hdfs dfs`.
- For example, to create a directory named `test` in HDFS, you can use the command:

  ```
  hadoop fs -mkdir /test
  ```

- To copy a file named `data.txt` from local file system to HDFS, you can use the command:

  ```
  hadoop fs -put data.txt /test
  ```

- To display the contents of the file `data.txt` in HDFS, you can use the command:

  ```
  hadoop fs -cat /test/data.txt
  ```

- To delete the file `data.txt` from HDFS, you can use the command:

  ```
  hadoop fs -rm /test/data.txt
  ```

- To delete the directory `test` from HDFS, you can use the command:

  ```
  hadoop fs -rmdir /test
  ```

- To change the permissions of the file `data.txt` in HDFS to read-only for everyone, you can use the command:

  ```
  hadoop fs -chmod 444 /test/data.txt
  ```

- To change the owner and group of the file `data.txt` in HDFS to `user1` and `group1`, you can use the command:

  ```
  hadoop fs -chown user1:group1 /test/data.txt
  ```

- To display the disk usage of the file `data.txt` in HDFS, you can use the command:

  ```
  hadoop fs -du /test/data.txt
  ```

- To display the available space on the HDFS file system, you can use the command:

  ```
  hadoop fs -df /
  ```

- To display the help for the command `hadoop fs -put`, you can use the command:

  ```
  hadoop fs -help put
  ```

- These are some of the basic file management tasks that can be performed on HDFS using Hadoop commands. For more information, you can refer to the official documentation of Hadoop    .