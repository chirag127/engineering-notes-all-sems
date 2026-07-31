## Deleting files

- A file or a directory can be removed from HDFS by using the `hadoop fs -rm` or `hadoop fs -rmr` command .
- The `-rm` option deletes a single file, while the `-rmr` option deletes a directory and all its contents recursively .
- The syntax for deleting files or directories is: `hadoop fs -rmr <path to file or directory>` .
- To delete all files inside a specific directory, use the asterisk (*) wildcard character. For example, `hadoop fs -rmr /user/your_user_name/*`.
- To delete a file or a directory without moving it to the trash, use the `-skipTrash` option. For example, `hadoop fs -rm -r -skipTrash /folder_name`.
- To delete a file or a directory from the trash, use the `hadoop fs -expunge` command.
- To delete a file or a directory from the local file system, use the `hadoop fs -rm -f` command.