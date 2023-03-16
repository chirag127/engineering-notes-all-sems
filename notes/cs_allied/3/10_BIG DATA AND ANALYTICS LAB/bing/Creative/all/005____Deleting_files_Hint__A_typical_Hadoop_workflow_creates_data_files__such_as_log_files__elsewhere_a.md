## Deleting files

- To delete files from HDFS, we can use the `hadoop fs -rm` command, which takes one or more paths as arguments and removes them from the file system.
- The `hadoop fs -rm` command supports the following options:
  - `-f`: Force the deletion of files or directories without asking for confirmation, even if they are non-empty.
  - `-r`: Recursively delete files and directories, including all their contents and subdirectories.
  - `-skipTrash`: Skip moving the files to the trash directory before deleting them. This option can be useful to save space and time when deleting large or temporary files.
- For example, to delete a file named `log.txt` from the current working directory in HDFS, we can use the command:

  ```
  hadoop fs -rm log.txt
  ```

- To delete a directory named `logs` and all its contents from the current working directory in HDFS, we can use the command:

  ```
  hadoop fs -rm -r logs
  ```

- To delete a file named `temp.txt` from the current working directory in HDFS without moving it to the trash, we can use the command:

  ```
  hadoop fs -rm -skipTrash temp.txt
  ```

- A typical Hadoop workflow creates data files (such as log files) elsewhere and copies them into HDFS using one of the above command line utilities. This is because HDFS is designed for storing large and immutable files that are written once and read many times, rather than small and frequently updated files. Therefore, it is advisable to delete the files from HDFS once they are no longer needed, to free up space and reduce the overhead of managing them.