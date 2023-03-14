#### File sizes in HDFS

HDFS is a distributed file system that stores large files across multiple nodes in a cluster. HDFS breaks down files into fixed-size blocks, called data blocks, and distributes them across the cluster. Each data block is replicated on multiple nodes for fault tolerance. The default size of a data block is 128 MB, but it can be configured by the user .

The following diagram illustrates the basic architecture of a HDFS cluster with three data blocks of a file:

```
+-----------------+    +-----------------+    +-----------------+
| NameNode        |    | DataNode 1      |    | DataNode 2      |
| (Master)        |    | (Slave)         |    | (Slave)         |
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | File System | |    | | Data Block  | |    | | Data Block  | |
| | Metadata    | |    | | A           | |    | | A           | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|                 |    | +-------------+ |    | +-------------+ |
|                 |    | | Data Block  | |    | | Data Block  | |
|                 |    | | B           | |    | | B           | |
|                 |    | +-------------+ |    | +-------------+ |
+-----------------+    +-----------------+    +-----------------+
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             |                         |
                             +-----------------+    +-----------------+
                             | DataNode 3      |    | DataNode 4      |
                             | (Slave)         |    | (Slave)         |
                             |                 |    |                 |
                             | +-------------+ |    | +-------------+ |
                             | | Data Block  | |    | | Data Block  | |
                             | | A           | |    | | A           | |
                             | +-------------+ |    | +-------------+ |
                             | +-------------+ |    | +-------------+ |
                             | | Data Block  | |    | | Data Block  | |
                             | | C           | |    | | C           | |
                             | +-------------+ |    | +-------------+ |
                             +-----------------+    +-----------------+
```

In this diagram, the NameNode is the master node that manages the file system metadata, such as the file names, locations, permissions, etc. The DataNodes are the slave nodes that store the actual data blocks. The file in this example has three data blocks: A, B, and C. Each data block is replicated three times on different DataNodes, as specified by the replication factor. The NameNode keeps track of which DataNodes have which data blocks, and coordinates the read and write operations from the clients.

To find the size of a file or a directory in HDFS, one can use the command `hdfs dfs -du [-s] [-h] URI [URI ...]` . This command displays the size of the file or the directory in bytes, or in a human-readable format if the `-h` option is specified. The `-s` option will display the aggregate summary of the file lengths, rather than the individual files. For example, to find the size of a file named `input.txt` in HDFS, one can run:

```
hdfs dfs -du -h /user/hadoop/input.txt
```

This will display the size of the file in a human-readable format, such as 64.0 MB. Note that this is the base size of the file before replication. The actual disk space consumed by the file will depend on the replication factor. For example, if the replication factor is 3, the file will consume 192.0 MB of disk space. To find the disk space consumed by the file, one can use the command `hdfs dfs -dus -h /user/hadoop/input.txt`. This will display the size of the file and the disk space consumed by the file with all replicas, such as:

```
64.0 MB  192.