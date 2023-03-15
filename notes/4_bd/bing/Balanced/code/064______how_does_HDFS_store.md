#### How does HDFS store

HDFS is a distributed file system that stores large files across multiple nodes in a cluster. HDFS follows a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes are DataNodes (slaves).

The NameNode is responsible for managing the namespace, metadata, and access control of the file system. It also coordinates the placement and replication of data blocks on the DataNodes.

The DataNodes are responsible for storing the actual data blocks of the files. Each file is split into fixed-size blocks (typically 64 MB or 128 MB) and distributed across the DataNodes. Each block is replicated on a configurable number of DataNodes (typically 3) for fault tolerance and availability.

HDFS provides a client API and a command-line interface for users to interact with the file system. Users can create, read, write, delete, and append files, as well as perform other operations such as listing directories, copying files, changing permissions, etc.

HDFS also provides a web interface for users to monitor the status and performance of the cluster, as well as to browse the file system. Users can access the web interface by visiting the NameNode's URL on port 9870 (for Hadoop 3.x) or 50070 (for Hadoop 2.x).