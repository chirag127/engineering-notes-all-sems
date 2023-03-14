#### File sizes in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed and scalable file system that stores large amounts of data across multiple nodes in a cluster.
- Files in HDFS are broken into block-sized chunks called data blocks. These blocks are stored as independent units. The size of these HDFS data blocks is 128 MB by default.
- The size of a file in HDFS is the base size of the file before replication. This shows the amount of space in bytes that have been used by the file that matches the specified file pattern.
- A typical file in HDFS is gigabytes to terabytes in size. Thus, HDFS is tuned to support large files. It should provide high aggregate data bandwidth and scale to hundreds of nodes in a single cluster .
- To find the size of a file or a directory in HDFS, one can use the following commands:

  - `hadoop fs -ls <path>`: This command lists the files and directories in the given path along with their details. The fifth column in the command output contains the file size in bytes.
  - `hadoop fs -du <path>`: This command displays the sizes of files and directories contained in the given path or the length of a file in case it is just a file.
  - `hadoop fs -du -s <path>`: This command displays an aggregate summary of file lengths being displayed, rather than the individual files.
  - `hadoop fs -du -h <path>`: This command displays the file sizes in a human-readable format, such as KB, MB, GB, etc.
  - `hadoop fs -du -s -h <path>`: This command displays the aggregate summary of file lengths in a human-readable format.

- Here is an example of using these commands to find the size of a file named `sample.txt` in HDFS:

  ```
  $ hadoop fs -ls sample.txt
  -rw-r--r--   3 user group    1024000 2023-03-14 18:25 sample.txt
  $ hadoop fs -du sample.txt
  1024000  sample.txt
  $ hadoop fs -du -s sample.txt
  1024000
  $ hadoop fs -du -h sample.txt
  1000.0 K  sample.txt
  $ hadoop fs -du -s -h sample.txt
  1000.0 K
  ```

- A possible mnemonic to remember the file sizes in HDFS is:

  - **L**arge files are stored in **L**arge blocks of 128 MB by default.
  - **D**U command is used to find the **D**isk **U**sage of files and directories in HDFS.
  - **S** option displays the **S**ummary of file lengths, rather than individual files.
  - **H** option displays the file sizes in **H**uman-readable format, such as KB, MB, GB, etc.