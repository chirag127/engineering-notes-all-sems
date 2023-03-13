#### Command line interface to HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed and scalable file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS provides a command line interface (CLI) that allows users to interact with the file system using commands similar to Unix/Linux shell commands.
- The CLI can be accessed by typing `hdfs dfs` followed by the command name and its arguments. For example, `hdfs dfs -ls /` will list the files and directories in the root directory of HDFS.
- Some of the common commands and their functions are:

| Command | Function |
|---------|----------|
| -cat | Concatenate files and print on the standard output |
| -chgrp | Change group association of files |
| -chmod | Change permissions of files |
| -chown | Change owner of files |
| -copyFromLocal | Copy files from the local file system to HDFS |
| -copyToLocal | Copy files from HDFS to the local file system |
| -cp | Copy files from source to destination within HDFS |
| -du | Display disk usage of files and directories |
| -get | Copy files from HDFS to the local file system |
| -getmerge | Get all the files in the directories that match the source file pattern and merge and sort them to only one file on the local file system |
| -ls | List the contents of a directory |
| -mkdir | Create a directory in HDFS |
| -moveFromLocal | Move files from the local file system to HDFS |
| -moveToLocal | Move files from HDFS to the local file system |
| -mv | Move files from source to destination within HDFS |
| -put | Copy files from the local file system to HDFS |
| -rm | Delete files from HDFS |
| -rmdir | Remove a directory from HDFS |
| -tail | Display the last kilobyte of a file |
| -test | Test a file for existence, accessibility, zero length, etc. |

- To get more information about a command, use the `-help` option. For example, `hdfs dfs -help ls` will display the usage and options of the `ls` command.
- To get a list of all the commands, use the `-help` option without any arguments. For example, `hdfs dfs -help` will display the usage and options of all the commands.
- A mnemonic to remember some of the common commands is: **C**ats **C**hange **C**hange **C**hange **C**opy **C**opy **C**opy **D**isk **G**et **G**et **L**ist **M**ake **M**ove **M**ove **M**ove **P**ut **R**emove **R**emove **T**ail **T**est. The first letter of each word corresponds to the first letter of the command. For example, **C**ats corresponds to `-cat`, **C**hange corresponds to `-chgrp`, `-chmod`, and `-chown`, etc.