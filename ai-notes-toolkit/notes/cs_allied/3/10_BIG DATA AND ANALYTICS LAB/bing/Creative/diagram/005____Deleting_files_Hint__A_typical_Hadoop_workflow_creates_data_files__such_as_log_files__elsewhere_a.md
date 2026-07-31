## Deleting files

- To delete files from HDFS, we can use the `hadoop fs -rm` command, which takes one or more paths as arguments and removes them from the file system.
- The `hadoop fs -rm` command supports the following options:
  - `-f`: Force the deletion of files or directories without asking for confirmation.
  - `-r`: Recursively delete all files and directories under the specified path.
  - `-skipTrash`: Skip moving the files to the trash directory before deleting them. This option is useful when we want to delete large files or directories that would otherwise fill up the trash space.
- For example, to delete a file named `log.txt` from the HDFS directory `/user/hadoop`, we can use the command:

  ```
  hadoop fs -rm /user/hadoop/log.txt
  ```

- To delete a directory named `logs` and all its contents from the HDFS directory `/user/hadoop`, we can use the command:

  ```
  hadoop fs -rm -r /user/hadoop/logs
  ```

- To delete a file named `bigdata.txt` from the HDFS directory `/user/hadoop` without moving it to the trash, we can use the command:

  ```
  hadoop fs -rm -skipTrash /user/hadoop/bigdata.txt
  ```

- Note: The `hadoop fs -rm` command does not delete the files permanently from the HDFS. The files are moved to a trash directory under the user's home directory, which is `/user/<username>/.Trash` by default. The trash directory has a retention period, which is 6 hours by default, after which the files are deleted permanently. The trash directory can be configured or disabled by setting the `fs.trash.interval` property in the `core-site.xml` file. To restore a file from the trash, we can use the `hadoop fs -mv` command to move it back to the original location. For example, to restore the file `log.txt` that was deleted from the HDFS directory `/user/hadoop`, we can use the command:

  ```
  hadoop fs -mv /user/hadoop/.Trash/Current/user/hadoop/log.txt /user/hadoop/log.txt
  ```