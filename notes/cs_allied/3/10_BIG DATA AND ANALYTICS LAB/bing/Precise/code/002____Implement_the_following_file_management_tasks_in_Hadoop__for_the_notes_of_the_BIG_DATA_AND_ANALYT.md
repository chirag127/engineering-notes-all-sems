## Implement the following file management tasks in Hadoop:

1. **Creating a directory in HDFS:** To create a directory in HDFS, use the `hadoop fs -mkdir` command. For example, to create a directory named `mydir`, use the command `hadoop fs -mkdir /mydir`.

2. **Listing the contents of a directory in HDFS:** To list the contents of a directory in HDFS, use the `hadoop fs -ls` command. For example, to list the contents of the `mydir` directory, use the command `hadoop fs -ls /mydir`.

3. **Copying a file from the local file system to HDFS:** To copy a file from the local file system to HDFS, use the `hadoop fs -put` command. For example, to copy a file named `myfile.txt` from the local file system to the `mydir` directory in HDFS, use the command `hadoop fs -put myfile.txt /mydir`.

4. **Copying a file from HDFS to the local file system:** To copy a file from HDFS to the local file system, use the `hadoop fs -get` command. For example, to copy a file named `myfile.txt` from the `mydir` directory in HDFS to the local file system, use the command `hadoop fs -get /mydir/myfile.txt`.

5. **Deleting a file or directory in HDFS:** To delete a file or directory in HDFS, use the `hadoop fs -rm` command. For example, to delete a file named `myfile.txt` in the `mydir` directory in HDFS, use the command `hadoop fs -rm /mydir/myfile.txt`. To delete a directory, use the `hadoop fs -rm -r` command. For example, to delete the `mydir` directory, use the command `hadoop fs -rm -r /mydir`.
