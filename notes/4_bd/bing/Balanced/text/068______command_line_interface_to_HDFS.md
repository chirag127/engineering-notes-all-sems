#### Command Line Interface to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for big data processing.
- Command Line Interface (CLI) is one of the simplest ways to interact with HDFS. CLI has support for filesystem operations like reading the file, creating directories, moving files, deleting data, and listing directories .
- To use CLI, we need to run the `hdfs` command with the appropriate subcommand and options. For example, `hdfs dfs -ls /` will list the contents of the root directory in HDFS.
- The `hdfs` command has several subcommands, such as `dfs`, `dfsadmin`, `fsck`, `balancer`, etc. Each subcommand has its own syntax and options. We can run `hdfs <subcommand> -help` to get detailed help on every subcommand.
- Some of the common subcommands and their usage are:

  - `dfs` : Performs basic file system operations on HDFS, such as copy, move, delete, etc. For example, `hdfs dfs -put localfile.txt /user/hadoop/hdfsfile.txt` will copy a local file to HDFS.
  - `dfsadmin` : Performs administrative operations on HDFS, such as report, safemode, refresh, etc. For example, `hdfs dfsadmin -report` will display the summary of the cluster status, such as the number of live and dead nodes, the total and used capacity, etc.
  - `fsck` : Checks the health of the HDFS file system, such as the number of missing or corrupted blocks, the replication factor, etc. For example, `hdfs fsck /user/hadoop` will check the integrity of the files and directories under the given path.
  - `balancer` : Balances the disk space usage across the data nodes in the cluster, by moving blocks from over-utilized nodes to under-utilized nodes. For example, `hdfs balancer -threshold 10` will start the balancer process with a threshold of 10%, which means the balancer will try to make the disk space usage of each node within 10% of the cluster average.

- To use CLI with Data Lake Storage Gen2, which is a cloud-based storage service that supports HDFS, we need to establish remote access to an HDInsight Hadoop cluster on Linux, and then execute the basic HDFS commands as usual. For example, `ssh sshuser@clustername-ssh.azurehdinsight.net` will connect to the cluster via SSH, and then `hdfs dfs -ls /` will list the contents of the root directory in Data Lake Storage Gen2.