 Here is the content in markdown format for the given topic:

### Command Line Interface for HDFS

The Hadoop Distributed File System (HDFS) can be accessed via Command Line Interface (CLI) using the `hdfs` command. The key HDFS operations via CLI are:

1. **File Upload**: To upload a file to HDFS, use `hdfs dfs -put <local_file> <hdfs_file>`. For example, `hdfs dfs -put mydata.txt /user/myname/mydata.txt` will upload `mydata.txt` to HDFS under `/user/myname/` path.
2. **File Download**: To download a file from HDFS, use `hdfs dfs -get <hdfs_file> <local_file>`. For example, `hdfs dfs -get /user/myname/mydata.txt mydata_local.txt` will download `mydata.txt` from HDFS to the local filesystem as `mydata_local.txt`.
3. **Creating Directories**: To create a directory in HDFS, use `hdfs dfs -mkdir <path>`. For example, `hdfs dfs -mkdir /user/myname/mydir` will create a directory called `mydir` under `/user/myname/`.
4. **Listing Files**: To list files in HDFS, use `hdfs dfs -ls <path>`. For example, `hdfs dfs -ls /user/myname/` will list all files and directories under `/user/myname/`.
5. **Deleting Files/Directories**: To delete files/directories from HDFS, use `hdfs dfs -rm <path>`. For example, `hdfs dfs -rm /user/myname/mydata.txt` will delete the file `mydata.txt`. To delete a non-empty directory, use `hdfs dfs -rm -r <path>`.

The above are some of the frequently used CLI operations on HDFS. There are additional commands to check HDFS stats, set replication factor, concatenate files, etc. The CLI provides easy access to HDFS and is useful for automation and scripting. However, for interactive usage, the HDFS web UI is more convenient.

[Detailed diagrams and examples can be added here if required.]

The key advantages of HDFS are scalability, extensibility, fault tolerance, and low cost. Some applications of HDFS are AI training, big data analysis, IoT data storage, etc.