#### Command Line Interface to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for big data processing.
- Command Line Interface (CLI) is one of the simplest ways to interact with HDFS. CLI has support for filesystem operations like reading, writing, creating, moving, deleting, and listing files and directories.
- To use CLI, we need to have a Hadoop cluster running and access it through SSH or a terminal.
- The basic syntax of CLI commands is `hdfs dfs -command [options] [arguments]`, where `hdfs` is the command name, `dfs` is the subcommand name, `-command` is the specific operation, `[options]` are the optional parameters, and `[arguments]` are the required arguments.
- Some of the common CLI commands are:

  - `hdfs dfs -ls [path]`: List the contents of a directory or file.
  - `hdfs dfs -mkdir [path]`: Create a directory or directories.
  - `hdfs dfs -put [local_path] [hdfs_path]`: Copy a file or directory from the local filesystem to HDFS.
  - `hdfs dfs -get [hdfs_path] [local_path]`: Copy a file or directory from HDFS to the local filesystem.
  - `hdfs dfs -cat [path]`: Display the contents of a file or files.
  - `hdfs dfs -rm [path]`: Delete a file or directory.
  - `hdfs dfs -mv [source_path] [destination_path]`: Move or rename a file or directory.
  - `hdfs dfs -cp [source_path] [destination_path]`: Copy a file or directory within HDFS.
  - `hdfs dfs -du [path]`: Display the disk usage of a file or directory.
  - `hdfs dfs -help [command]`: Display the help information for a specific command or all commands.

- To get more details and examples of CLI commands, we can refer to the official documentation or run `hdfs dfs -help` in the terminal.