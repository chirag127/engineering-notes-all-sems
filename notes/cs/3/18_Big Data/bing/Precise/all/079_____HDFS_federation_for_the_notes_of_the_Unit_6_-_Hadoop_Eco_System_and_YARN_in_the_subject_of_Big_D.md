# HDFS Federation

HDFS Federation is a feature added to Hadoop 2.x that provides support for multiple NameNodes/namespaces. This overcomes the isolation, scalability, and performance limitations of the prior HDFS architecture. HDFS Federation architecture also opens up the architecture for future innovations.

HDFS Federation improves the existing HDFS architecture through a clear separation of namespace and storage, enabling a generic block storage layer. It enables support for multiple namespaces in the cluster to improve scalability and isolation.

HDFS has two main layers: Namespace and Block Storage Service. The Namespace consists of directories, files, and blocks. It supports all the namespace-related file system operations such as create, delete, modify and list files and directories .

The Block Storage Service has two parts: Block Management (which is done in the NameNode) and the actual storage of blocks (which is done in the DataNodes).

HDFS Federation gives a way of separating the existing architecture having two layers called the name layer and block storage layer. By doing this it enables to expand the architecture and enables the block storage layer.