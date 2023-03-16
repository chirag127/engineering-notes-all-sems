## Deleting files

In the context of Hadoop, deleting files is an important operation that is used to manage data stored in the Hadoop Distributed File System (HDFS). Here are some key points to consider when deleting files in HDFS:

1. **Command Line Utilities**: Hadoop provides several command line utilities for managing files in HDFS, including the `hadoop fs -rm` command, which can be used to delete files.

2. **Recursively Deleting Files**: The `hadoop fs -rm` command can be used with the `-r` option to recursively delete files and directories. This is useful when you need to delete a directory and all of its contents.

3. **Skipping Trash**: By default, when you delete a file in HDFS, it is moved to the trash directory. This allows you to recover the file if you accidentally delete it. However, if you are sure that you want to permanently delete a file, you can use the `-skipTrash` option with the `hadoop fs -rm` command to bypass the trash and permanently delete the file.

4. **Deleting Large Directories**: When deleting large directories with many files, it is recommended to use the `hadoop fs -rm -r -skipTrash` command to bypass the trash and delete the files more quickly.

5. **A Typical Hadoop Workflow**: A typical Hadoop workflow creates data files (such as log files) elsewhere and copies them into HDFS using one of the above command line utilities. Once the data is no longer needed, it can be deleted using the `hadoop fs -rm` command.
