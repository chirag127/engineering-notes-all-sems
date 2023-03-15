
#### Read Operations in HDFS

- **HDFS Read Operation** is the process of retrieving data from the Hadoop Distributed File System.
- Read operations are performed by the **NameNode** and **DataNode** daemons.
- The NameNode is responsible for keeping track of the files stored in the HDFS. It stores the metadata about the files, such as their location, size, and permissions.
- The DataNode is responsible for storing the actual data blocks.
- When a client requests a read operation, the NameNode will return the list of DataNodes that have the requested data blocks.
- The client will then contact each DataNode to retrieve the data blocks.
- **Mnemonics and Learning Tricks**: 
  - HDFS: Hadoop Distributed File System.
  - NameNode: Keeps track of the files stored in HDFS.
  - DataNode: Stores the actual data blocks.
  - Read Operation: Retrieve data from HDFS.