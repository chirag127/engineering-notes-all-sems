## Deleting files

- To delete files from HDFS, we can use the `hadoop fs -rm` command with the path of the file or directory to be deleted.
- For example, `hadoop fs -rm /user/hadoop/file.txt` will delete the file `file.txt` from the `/user/hadoop` directory in HDFS.
- To delete a directory and all its contents recursively, we can use the `-r` option with the `hadoop fs -rm` command.
- For example, `hadoop fs -rm -r /user/hadoop/dir` will delete the directory `dir` and all its subdirectories and files from the `/user/hadoop` directory in HDFS.
- To delete files or directories without moving them to the trash, we can use the `-skipTrash` option with the `hadoop fs -rm` command.
- For example, `hadoop fs -rm -skipTrash /user/hadoop/file.txt` will delete the file `file.txt` from the `/user/hadoop` directory in HDFS without moving it to the trash.
- To delete files or directories from the trash, we can use the `hadoop fs -expunge` command, which will permanently delete all the files and directories in the trash that have exceeded the retention period.
- For example, `hadoop fs -expunge` will delete all the files and directories in the trash that have been there for more than the configured retention period (default is 30 days).
- To view the contents of the trash, we can use the `hadoop fs -ls` command with the `.Trash` directory in the user's home directory in HDFS.
- For example, `hadoop fs -ls /user/hadoop/.Trash` will list all the files and directories in the trash for the user `hadoop`.