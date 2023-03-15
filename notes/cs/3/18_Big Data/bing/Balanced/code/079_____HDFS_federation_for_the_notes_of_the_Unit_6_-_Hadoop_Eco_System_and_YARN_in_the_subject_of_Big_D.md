### HDFS Federation

HDFS Federation is a feature of Hadoop 2.x that allows the HDFS architecture to support multiple NameNodes or namespaces in a cluster. This improves the scalability, performance, and isolation of the HDFS system. 

#### Architecture of HDFS Federation

HDFS Federation separates the two main layers of HDFS: the namespace layer and the block storage layer. The namespace layer consists of directories, files, and blocks, and supports file system operations such as create, delete, modify, and list. The block storage layer consists of DataNodes that store and manage the blocks of data. 

In HDFS Federation, each namespace is managed by a separate NameNode, which is independent of other NameNodes. Each NameNode has its own metadata, such as the file system tree, the file-to-block mapping, the block locations, etc. The DataNodes are shared by all the NameNodes and can store blocks from multiple namespaces. Each DataNode registers with and sends periodic heartbeats and block reports to all the NameNodes in the cluster. 

To access a file in HDFS Federation, a client needs to know the NameNode that manages the namespace of the file. This can be achieved by using a logical URI that contains the scheme, the authority, and the path of the file. For example, `hdfs://nn1/user/foo/bar.txt` refers to a file in the namespace managed by the NameNode nn1. The authority part of the URI can also be a logical name that maps to a set of NameNodes for high availability. 

#### Benefits of HDFS Federation

HDFS Federation provides the following benefits:

- It increases the aggregate capacity and throughput of the cluster by allowing more files, blocks, and file system operations.
- It improves the availability and reliability of the cluster by isolating the impact of failures to a single namespace.
- It allows for more flexible and fine-grained administration and quota management of different namespaces by different users or groups.
- It enables future innovations and extensions of the HDFS architecture, such as supporting different types of storage media, block placement policies, erasure coding, etc.