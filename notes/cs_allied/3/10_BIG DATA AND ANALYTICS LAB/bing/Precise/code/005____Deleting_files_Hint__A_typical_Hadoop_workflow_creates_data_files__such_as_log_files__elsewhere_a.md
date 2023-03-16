## Deleting files

In Hadoop, data files can be deleted from the Hadoop Distributed File System (HDFS) using command line utilities. Here are some points to consider when deleting files in Hadoop:

1. Files can be deleted using the `hadoop fs -rm` command. This command takes the path of the file to be deleted as an argument. For example, to delete a file named `example.txt` in the `/user/hadoop` directory, the command would be `hadoop fs -rm /user/hadoop/example.txt`.
2. The `-skipTrash` option can be used with the `hadoop fs -rm` command to delete a file permanently, bypassing the trash. For example, to delete the `example.txt` file permanently, the command would be `hadoop fs -rm -skipTrash /user/hadoop/example.txt`.
3. The `hadoop fs -rmr` command can be used to delete a directory and all its contents recursively. For example, to delete the `/user/hadoop/data` directory and all its contents, the command would be `hadoop fs -rmr /user/hadoop/data`.
4. The `-r` option can be used with the `hadoop fs -rm` command to delete a directory and all its contents recursively. This is equivalent to using the `hadoop fs -rmr` command. For example, to delete the `/user/hadoop/data` directory and all its contents, the command would be `hadoop fs -rm -r /user/hadoop/data`.
5. A typical Hadoop workflow creates data files (such as log files) elsewhere and copies them into HDFS using one of the above command line utilities. Once the data is no longer needed, it can be deleted using the `hadoop fs -rm` or `hadoop fs -rmr` command.
