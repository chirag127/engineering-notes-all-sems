#### HDFS Federation in Hadoop Ecosystem

- HDFS Federation is a feature introduced in Hadoop 2 that enhances the existing HDFS architecture.
- It overcomes HDFS architecture limitations by adding multiple NameNode/namespaces support to HDFS, allowing the use of more than one NameNode/namespace .
- This overcomes the isolation, scalability, and performance limitations of the prior HDFS architecture and opens up the architecture for future innovations.
- The HDFS Federation architecture has a collection of Namespace volumes, which are self-contained management units. On deleting the NameNode or namespace, the corresponding block pool present in the DataNodes also gets deleted. On upgrading the cluster, each namespace volume gets upgraded as a unit.
- HDFS has two main layers: Namespace and Block Storage Service. Namespace consists of directories, files, and blocks and supports all the namespace-related file system operations such as create, delete, modify and list files and directories. Block Storage Service has two parts: Block Management (performed in the Namenode) and Block Storage (performed in the DataNodes).