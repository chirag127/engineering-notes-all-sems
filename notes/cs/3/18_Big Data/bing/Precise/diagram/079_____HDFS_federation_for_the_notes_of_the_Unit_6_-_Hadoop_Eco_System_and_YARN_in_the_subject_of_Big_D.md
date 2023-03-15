### HDFS Federation

HDFS Federation is a feature added to Hadoop 2.x that provides support for multiple NameNodes/namespaces. This overcomes the isolation, scalability, and performance limitations of the prior HDFS architecture. HDFS Federation architecture also opens up the architecture for future innovations.

HDFS Federation improves the existing HDFS architecture through a clear separation of namespace and storage, enabling generic block storage layer. It enables support for multiple namespaces in the cluster to improve scalability and isolation.

HDFS has two main layers: Namespace and Block Storage Service. Namespace consists of directories, files, and blocks. It supports all the namespace-related file system operations such as create, delete, modify, and list files and directories. Block Storage Service has two parts: Block Management (which is done in Namenode) .

HDFS Federation gives a way of separating the existing architecture having two layers called name layer and block storage layer. By doing this it enables to expand the architecture and enables the block storage layer.