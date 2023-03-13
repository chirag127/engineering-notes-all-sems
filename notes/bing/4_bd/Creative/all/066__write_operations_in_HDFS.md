#### Write operations in HDFS

- HDFS is a distributed file system that stores large files across multiple nodes in a cluster.
- HDFS supports write-once-read-many model, which means a file can be written once and then read multiple times, but not modified or appended.
- HDFS write operations involve three main components: the client, the namenode, and the datanodes.
- The client is the application that initiates the write request to HDFS.
- The namenode is the master node that manages the metadata of the file system, such as the file name, size, location, replication factor, etc.
- The datanodes are the worker nodes that store the actual data blocks of the file.
- The following steps describe the write operations in HDFS:

  1. The client contacts the namenode and requests to create a new file with a given name, replication factor, and block size.
  2. The namenode checks if the file already exists or if the namespace quota is exceeded. If not, it grants the write permission to the client and returns a list of datanodes that can store the first block of the file.
  3. The client splits the file into fixed-size blocks (default 128 MB) and sends the first block to the first datanode in the list. The datanode stores the block locally and forwards it to the next datanode in the list. This process continues until the block is replicated to the desired number of datanodes (default 3).
  4. The client receives an acknowledgment from the last datanode in the pipeline and contacts the namenode again for the next block location. The namenode returns another list of datanodes for the second block.
  5. The client repeats steps 3 and 4 until all the blocks of the file are written and replicated.
  6. The client sends a close request to the namenode, indicating that the file write is complete. The namenode updates the metadata and commits the file creation.

- A possible mnemonic to remember the write operations in HDFS is: **C**reate, **S**plit, **S**end, **A**cknowledge, **C**lose. (CSSAC)
- A possible ascii diagram to illustrate the write operations in HDFS is:

```
  +--------+             +----------+             +----------+             +----------+
  | Client |             | Namenode |             | Datanode |             | Datanode |
  +--------+             +----------+             +----------+             +----------+
     |                       |                       |                       |
     | create(file)          |                       |                       |
     |---------------------> |                       |                       |
     |                       |                       |                       |
     |                       | datanode list         |                       |
     | <---------------------|                       |                       |
     |                       |                       |                       |
     | split(file)           |                       |                       |
     |                       |                       |                       |
     | send(block1)          |                       |                       |
     |---------------------> |                       |                       |
     |                       |                       |                       |
     |                       | send(block1)          |                       |
     |                       |---------------------> |                       |
     |                       |                       |                       |
     |                       |                       | send(block1)          |
     |                       |                       |---------------------> |
     |                       |                       |                       |
     |                       |                       |                       |
     |                       |                       | ack(block1)           |
     |                       |                       | <---------------------|
     |                       |                       |                       |
     |                       | ack(block1)           |                       |
     |                       | <---------------------|                       |
     |                       |                       |                       |
     | ack(block1)           |                       |                       |
     | <---------------------|                       |                       |
     |                       |                       |                       |
     | create(file)          |                       |                       |
     |---------------------> |                       |                       |
     |                       |                       |                       |
     |                       | datanode list         |                       |
     | <---------------------|                       |                       |
     |                       |                       |                       |
     | split(file)           |                       |                       |
     |                       |                       |                       |
     | send(block2)          |                       |                       |
     |---------------------> |                       |                       |
     |                       |                       |                       |
     |                       | send(block2)          |                       |
     |                       |---------------------> |                       |
     |                       |                       |                       |
     |                       |                       | send(block2)          |
     |                       |                       |---------------------> |
     |                       |                       |                       |
     |