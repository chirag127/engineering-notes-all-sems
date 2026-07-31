### Command Line Interface for HDFS

- The command line interface (CLI) is one of the simplest ways to interact with HDFS.
- The CLI has support for filesystem operations like reading, writing, creating, moving, deleting, and listing files and directories in HDFS.
- The CLI can be accessed by running `$HADOOP_HOME/bin/hdfs dfs` followed by a subcommand and its arguments.
- The CLI can also be used to perform administrative tasks such as checking the status, health, and configuration of HDFS.
- Some of the common subcommands and their usage are:

  - `-help`: Displays the help message for a given subcommand or all subcommands if none is specified.
  - `-ls`: Lists the contents of a directory or file in HDFS.
  - `-cat`: Displays the contents of a file in HDFS to standard output.
  - `-get`: Copies one or more files from HDFS to the local file system.
  - `-put`: Copies one or more files from the local file system to HDFS.
  - `-cp`: Copies one or more files from one location to another within HDFS.
  - `-mv`: Moves one or more files from one location to another within HDFS.
  - `-rm`: Deletes one or more files or directories from HDFS.
  - `-mkdir`: Creates one or more directories in HDFS.
  - `-chmod`: Changes the permissions of files or directories in HDFS.
  - `-chown`: Changes the owner and group of files or directories in HDFS.
  - `-du`: Displays the disk usage of files or directories in HDFS.
  - `-df`: Displays the available and used space in HDFS.
  - `-count`: Counts the number of files, directories, and bytes in HDFS.
  - `-tail`: Displays the last kilobyte of a file in HDFS to standard output.
  - `-test`: Tests if a file or directory exists in HDFS.
  - `-stat`: Displays the statistics of a file or directory in HDFS.
  - `-setrep`: Changes the replication factor of a file or directory in HDFS.
  - `-checksum`: Displays the checksum of a file in HDFS.
  - `-touchz`: Creates a zero-length file in HDFS.
  - `-expunge`: Empties the trash directory in HDFS.
  - `-text`: Converts a binary file in HDFS to text and displays it to standard output.
  - `-appendToFile`: Appends the contents of one or more local files to a file in HDFS.
  - `-getmerge`: Concatenates the contents of one or more files in HDFS and copies it to the local file system.
  - `-setfacl`: Sets the access control list (ACL) of files or directories in HDFS.
  - `-getfacl`: Displays the access control list (ACL) of files or directories in HDFS.
  - `-snapshot`: Manages the snapshots of directories in HDFS.
  - `-storagepolicies`: Manages the storage policies of files or directories in HDFS.
  - `-trash`: Moves files or directories to the trash directory in HDFS.
  - `-find`: Finds files or directories in HDFS that match a given expression.

- For more details and examples of each subcommand, run `$HADOOP_HOME/bin/hdfs dfs -help <subcommand>` or refer to the official documentation.