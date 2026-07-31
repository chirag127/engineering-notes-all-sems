#### Command line interface to HDFS

- The command line interface (CLI) is one of the simplest ways to interact with HDFS. It allows users to perform various filesystem operations such as reading, writing, moving, deleting, and listing files and directories in HDFS.
- The CLI is based on the Java API of HDFS and can be accessed by running the `hdfs` command from the `$HADOOP_HOME/bin` directory. The `hdfs` command has several subcommands, such as `dfs`, `dfsadmin`, `fsck`, `balancer`, etc. Each subcommand has its own syntax and options, which can be displayed by using the `-help` option.
- The most commonly used subcommand is `dfs`, which provides shell-like commands for interacting with HDFS. For example, to list the files and directories in the root directory of HDFS, one can run:

```
hdfs dfs -ls /
```

- To copy a local file to HDFS, one can run:

```
hdfs dfs -put localfile.txt /hdfsdir
```

- To display the contents of a file in HDFS, one can run:

```
hdfs dfs -cat /hdfsdir/localfile.txt
```

- To delete a file or directory in HDFS, one can run:

```
hdfs dfs -rm /hdfsdir/localfile.txt
hdfs dfs -rmdir /hdfsdir
```

- To create a directory in HDFS, one can run:

```
hdfs dfs -mkdir /newdir
```

- To move or rename a file or directory in HDFS, one can run:

```
hdfs dfs -mv /hdfsdir/localfile.txt /newdir/newfile.txt
hdfs dfs -mv /hdfsdir /newdir
```

- To get the summary of the disk usage of a file or directory in HDFS, one can run:

```
hdfs dfs -du /hdfsdir
```

- To get the detailed information of a file or directory in HDFS, one can run:

```
hdfs dfs -stat /hdfsdir
hdfs dfs -stat %r /hdfsdir # to get the replication factor
hdfs dfs -stat %b /hdfsdir # to get the block size
hdfs dfs -stat %o /hdfsdir # to get the owner
hdfs dfs -stat %g /hdfsdir # to get the group
hdfs dfs -stat %y /hdfsdir # to get the modification time
hdfs dfs -stat %n /hdfsdir # to get the name
```

- To get the help on any `dfs` command, one can run:

```
hdfs dfs -help ls # to get the help on ls command
hdfs dfs -help put # to get the help on put command
hdfs dfs -help cat # to get the help on cat command
hdfs dfs -help rm # to get the help on rm command
hdfs dfs -help rmdir # to get the help on rmdir command
hdfs dfs -help mkdir # to get the help on mkdir command
hdfs dfs -help mv # to get the help on mv command
hdfs dfs -help du # to get the help on du command
hdfs dfs -help stat # to get the help on stat command
```

- Some mnemonics and learning tricks for the command line interface to HDFS are:

  - The `dfs` subcommand stands for distributed file system, which is the main component of HDFS.
  - The `put` command is similar to the `cp` command in Linux, which copies a file from one location to another. The `put` command copies a file from the local file system to HDFS.
  - The `cat` command is similar to the `cat` command in Linux, which concatenates and displays the contents of a file. The `cat` command displays the contents of a file in HDFS.
  - The `rm` command is similar to the `rm` command in Linux, which removes a file. The `rm` command removes a file in HDFS.
  - The `rmdir` command is similar to the `rmdir` command in Linux, which removes an empty directory. The `rmdir` command removes an empty directory in HDFS.
  - The `mkdir` command is similar to the `mkdir` command in Linux, which creates a directory. The `mkdir` command creates a