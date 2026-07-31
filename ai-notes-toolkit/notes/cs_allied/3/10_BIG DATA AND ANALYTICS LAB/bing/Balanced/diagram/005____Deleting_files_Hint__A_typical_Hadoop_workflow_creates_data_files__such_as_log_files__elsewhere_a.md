## Deleting files

- A typical Hadoop workflow creates data files (such as log files) elsewhere and copies them into HDFS using one of the above command line utilities.
- To delete a file or a directory from HDFS, the `-rm` or `-rmr` argument can be used with the `hadoop fs` command .
- The syntax for deleting a file is: `hadoop fs -rm <path to file>`.
- The syntax for deleting a directory is: `hadoop fs -rmr <path to directory>`.
- The `-r` option is used to delete recursively, meaning that all the subdirectories and files inside the directory will be deleted as well .
- The `-skipTrash` option is used to bypass the trash and delete the file or directory permanently. This can be useful when it is necessary to delete files from an over-quota directory.
- To delete all the files inside a specific directory, the asterisk (*) can be used as a wildcard. For example, `hadoop fs -rm -r '/user/your_user_name/*'` will delete all the files inside the `/user/your_user_name/` directory.