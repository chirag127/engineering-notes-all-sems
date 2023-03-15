#### Data flow in HDFS

HDFS (Hadoop Distributed File System) is a distributed file system that handles large data sets running on commodity hardware. It is used to scale a single Apache Hadoop cluster to hundreds (and even thousands) of nodes.

- **Reading data**: As data is stored in a distributed manner, reading operations will run in parallel. The client interacts directly with the slaves and reads data blocks from there. The client opens the file it wishes to read by calling `open()` on the File System Object (which for HDFS is an instance of Distributed File System).

- **Writing data**: The client creates the file by calling `create()` on DistributedFileSystem (DFS). DFS makes an RPC call to the name node to create a new file in the file system’s namespace, with no blocks associated with it. As the client writes data, the DFSOutputStream splits it into packets, which it writes to an internal queue called the data queue.

- **Integration with other systems**: HDFS can be integrated with other systems, such as SQL Server Integration Services (SSIS), to write data to an HDFS file. The supported file formats are Text, Avro, and ORC.