#### HDFS Federation in Hadoop Ecosystem

HDFS Federation is a feature introduced in Hadoop 2 that enhances the existing HDFS architecture. It overcomes the limitations of the previous HDFS architecture by adding support for multiple NameNodes/namespaces to HDFS. This allows the use of more than one NameNode/namespace .

The HDFS Federation architecture has a collection of Namespace volumes, which are self-contained management units. When a NameNode or namespace is deleted, the corresponding block pool present in the DataNodes also gets deleted. When upgrading the cluster, each namespace volume is upgraded as a unit .

HDFS has two main layers: Namespace and Block Storage Service. The Namespace layer consists of directories, files, and blocks and supports all namespace-related file system operations such as creating, deleting, modifying, and listing files and directories. The Block Storage Service has two parts: Block Management (performed in the NameNode) and Block Storage (performed in the DataNodes) .

Overall, the HDFS Federation feature added to Hadoop 2.x provides support for multiple NameNodes/namespaces, overcoming the isolation, scalability, and performance limitations of the prior HDFS architecture. It also opens up the architecture for future innovations .