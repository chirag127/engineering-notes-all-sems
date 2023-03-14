#### Command line interface to HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed and scalable file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS provides a command line interface (CLI) that allows users to interact with the file system using commands similar to Unix/Linux shell commands.
- The CLI can be accessed by typing `hdfs dfs` followed by the command name and its arguments. For example, `hdfs dfs -ls /` will list the files and directories in the root directory of HDFS.
- Some of the common commands and their functions are:

  - `-mkdir`: creates a new directory in HDFS.
  - `-put`: copies a local file or directory to HDFS.
  - `-get`: copies a file or directory from HDFS to the local file system.
  - `-cat`: displays the contents of a file in HDFS.
  - `-rm`: deletes a file or directory from HDFS.
  - `-cp`: copies a file or directory within HDFS.
  - `-mv`: moves or renames a file or directory within HDFS.
  - `-du`: displays the disk usage of a file or directory in HDFS.
  - `-df`: displays the available and used space in HDFS.
  - `-chmod`: changes the permissions of a file or directory in HDFS.
  - `-chown`: changes the owner and group of a file or directory in HDFS.
  - `-help`: displays the usage information of a command.

- To get more information about a specific command, use `hdfs dfs -help <command>` or `hdfs dfs <command> -usage`.
- To get a list of all the commands, use `hdfs dfs -help`.
- Some of the advantages of using the CLI are:

  - It is easy to use and familiar to Unix/Linux users.
  - It allows users to perform basic file operations on HDFS without writing any code.
  - It can be used in scripts or automation tools to perform batch operations on HDFS.

- Some of the disadvantages of using the CLI are:

  - It does not provide advanced features or functionality that are available through the HDFS API or other tools.
  - It may not be compatible with some security or encryption mechanisms that are enabled on HDFS.
  - It may not be efficient or scalable for large or complex operations on HDFS.

- Some of the mnemonics and learning tricks for the CLI are:

  - The command names are mostly the same as the Unix/Linux shell commands, except they are prefixed with `hdfs dfs`.
  - The arguments and options of the commands are also similar to the Unix/Linux shell commands, except they use HDFS paths instead of local paths.
  - The HDFS paths start with a slash (/) and can be absolute or relative to the user's home directory in HDFS. For example, `/user/sydney` is an absolute path and `sydney` is a relative path.
  - The HDFS paths can also use wildcards (*) to match multiple files or directories. For example, `hdfs dfs -rm /user/sydney/*.txt` will delete all the text files in the user's home directory in HDFS.