#### File sizes in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system designed to store large files across multiple machines in a cluster.
- Files in HDFS are broken into block-sized chunks called data blocks. These blocks are stored as independent units. The size of these HDFS data blocks is 128 MB by default.
- The size of a file in HDFS is the base size of the file before replication. Replication is the process of creating multiple copies of a data block and storing them on different nodes for fault tolerance. The replication factor is the number of copies of a data block that are created. The default replication factor is 3.
- To find the size of a file or a directory in HDFS, one can use the command `hdfs dfs -du [-s] [-h] URI [URI ...]` . This command displays the size of files and directories contained in the given URI or the length of a file in case it's just a file. The options are:
  - The `-s` option will result in an aggregate summary of file lengths being displayed, rather than the individual files. Without the `-s` option, the calculation is done by going 1-level deep from the given path.
  - The `-h` option will format file sizes in a human-readable fashion (e.g 64.0m instead of 67108864)
  - The `-v` option will display the names of columns as a header line.
  - The `-x` option will exclude snapshots from the result calculation. Without the `-x` option (default), the result is always calculated from all INodes, including all snapshots under the given path.
- The command `hdfs dfs -du` returns three columns with the following format:

| size | disk_space_consumed_with_all_replicas | full_path_name |
|------|---------------------------------------|----------------|
| The base size of the file or directory before replication | The actual space consumed by the file or directory on disk after replication | The full path of the file or directory |

- For example, the command `hdfs dfs -du -h /user/hadoop/dir1` might give the following output:

| size | disk_space_consumed_with_all_replicas | full_path_name |
|------|---------------------------------------|----------------|
| 64.0m | 192.0m | /user/hadoop/dir1/file1 |
| 128.0m | 384.0m | /user/hadoop/dir1/file2 |
| 256.0m | 768.0m | /user/hadoop/dir1/file3 |

- This means that the directory `/user/hadoop/dir1` contains three files, each with a different size and a replication factor of 3. The total size of the directory is 448.0m (64.0m + 128.0m + 256.0m) and the total disk space consumed by the directory is 1.3g (192.0m + 384.0m + 768.0m).