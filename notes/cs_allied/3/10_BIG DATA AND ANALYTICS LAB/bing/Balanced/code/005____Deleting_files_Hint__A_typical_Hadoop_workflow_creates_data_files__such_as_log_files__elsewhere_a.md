## Deleting files

- To delete files from HDFS, we can use the `hadoop fs -rm` command, which takes one or more paths as arguments and removes them from the file system.
- The `hadoop fs -rm` command supports the following options:
  - `-f`: Force the deletion of files or directories without prompting for confirmation.
  - `-r`: Recursively delete all files and directories under the specified path.
  - `-skipTrash`: Skip moving the files to the trash directory before deleting them. By default, files are moved to the trash directory configured by `fs.trash.interval` property in `core-site.xml`.
- For example, to delete a file named `log.txt` from the `/user/hadoop` directory, we can use the command:

  ```
  hadoop fs -rm /user/hadoop/log.txt
  ```

- To delete a directory named `logs` and all its contents from the `/user/hadoop` directory, we can use the command:

  ```
  hadoop fs -rm -r /user/hadoop/logs
  ```

- To delete a file named `log.txt` from the `/user/hadoop` directory without moving it to the trash, we can use the command:

  ```
  hadoop fs -rm -skipTrash /user/hadoop/log.txt
  ```

- To delete multiple files or directories from HDFS, we can specify them as separate arguments to the `hadoop fs -rm` command. For example, to delete `log.txt`, `logs` and `data` from the `/user/hadoop` directory, we can use the command:

  ```
  hadoop fs -rm -r /user/hadoop/log.txt /user/hadoop/logs /user/hadoop/data
  ```

- To delete files or directories that match a certain pattern, we can use the `hadoop fs -rm` command with a wildcard character (`*`). For example, to delete all files that start with `log` from the `/user/hadoop` directory, we can use the command:

  ```
  hadoop fs -rm /user/hadoop/log*
  ```