## Implement the following file management tasks in Hadoop:

1. **Creating a directory in HDFS:** To create a directory in HDFS, use the `hadoop fs -mkdir` command. For example, to create a directory named `mydir`, use the command `hadoop fs -mkdir /mydir`.

2. **Copying a file from local file system to HDFS:** To copy a file from the local file system to HDFS, use the `hadoop fs -put` command. For example, to copy a file named `myfile.txt` from the local file system to the HDFS directory `/mydir`, use the command `hadoop fs -put myfile.txt /mydir`.

3. **Copying a file from HDFS to local file system:** To copy a file from HDFS to the local file system, use the `hadoop fs -get` command. For example, to copy a file named `myfile.txt` from the HDFS directory `/mydir` to the local file system, use the command `hadoop fs -get /mydir/myfile.txt`.

4. **Deleting a file from HDFS:** To delete a file from HDFS, use the `hadoop fs -rm` command. For example, to delete a file named `myfile.txt` from the HDFS directory `/mydir`, use the command `hadoop fs -rm /mydir/myfile.txt`.

5. **Listing the contents of a directory in HDFS:** To list the contents of a directory in HDFS, use the `hadoop fs -ls` command. For example, to list the contents of the HDFS directory `/mydir`, use the command `hadoop fs -ls /mydir`.
