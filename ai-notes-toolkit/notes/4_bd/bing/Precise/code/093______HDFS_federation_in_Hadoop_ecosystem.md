#### HDFS Federation in Hadoop Ecosystem

- HDFS Federation is a feature introduced in Hadoop 2 that enhances the existing HDFS architecture.
- It overcomes HDFS architecture limitations by adding support for multiple NameNodes/namespaces to HDFS. This allows the use of more than one NameNode/namespace.
- HDFS Federation overcomes the isolation, scalability, and performance limitations of the prior HDFS architecture.
- The HDFS Federation architecture has a collection of Namespace volumes, which are self-contained management units. On deleting a NameNode or namespace, the corresponding block pool present in the DataNodes also gets deleted. On upgrading the cluster, each namespace volume gets upgraded as a unit.
- HDFS has two main layers: Namespace and Block Storage Service. Namespace consists of directories, files, and blocks and supports all namespace-related file system operations such as creating, deleting, modifying, and listing files and directories. Block Storage Service has two parts: Block Management (performed in the NameNode) and Block Storage (performed in the DataNodes).