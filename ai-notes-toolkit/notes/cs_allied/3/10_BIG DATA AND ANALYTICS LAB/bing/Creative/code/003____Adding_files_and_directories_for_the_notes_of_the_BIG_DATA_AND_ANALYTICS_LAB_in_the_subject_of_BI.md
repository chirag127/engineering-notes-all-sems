Hello, I am Sydney, your AI assistant. I can help you with your notes for the Big Data and Analytics Lab subject. Here is some content on the topic of adding files and directories:

## Adding files and directories

- To add files and directories to Hadoop Distributed File System (HDFS), you need to use the `hdfs dfs -put` command.
- The syntax of the command is `hdfs dfs -put <local_source> <hdfs_destination>`.
- The `<local_source>` can be a file or a directory on your local file system. The `<hdfs_destination>` can be a file or a directory on HDFS. If the destination does not exist, it will be created.
- You can also use the `-f` option to overwrite the existing destination file or directory.
- You can also use the `-p` option to preserve the permissions, ownership, and modification time of the source file or directory.
- You can also use the `-l` option to create a symbolic link to the source file or directory on HDFS.
- You can also use the `-r` option to recursively copy all the files and subdirectories from the source directory to the destination directory on HDFS.
- You can also use the `-v` option to display the verbose output of the command.
- For example, to copy a file named `data.txt` from your local file system to a directory named `/user/student` on HDFS, you can use the command `hdfs dfs -put data.txt /user/student`.
- To copy a directory named `input` from your local file system to a directory named `/user/student` on HDFS, you can use the command `hdfs dfs -put input /user/student`.
- To overwrite an existing file or directory named `output` on HDFS with a file or directory named `output` from your local file system, you can use the command `hdfs dfs -put -f output /user/student`.
- To create a symbolic link named `link` on HDFS that points to a file or directory named `source` on your local file system, you can use the command `hdfs dfs -put -l source /user/student/link`.
- To recursively copy all the files and subdirectories from a directory named `input` on your local file system to a directory named `/user/student` on HDFS, you can use the command `hdfs dfs -put -r input /user/student`.
- To display the verbose output of the command `hdfs dfs -put input /user/student`, you can use the command `hdfs dfs -put -v input /user/student`.