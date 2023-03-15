### HDFS Federation

- HDFS Federation is a feature of Hadoop 2.x that allows multiple NameNodes to manage different namespaces in the same cluster .
- HDFS Federation improves the scalability, performance, and isolation of the HDFS architecture by separating the namespace and the block storage layers .
- HDFS Federation architecture consists of the following components :
  - NameNodes: Each NameNode manages a namespace and the metadata of the files and directories in that namespace. NameNodes do not communicate with each other and operate independently. Each NameNode has a unique identifier called Block Pool ID.
  - DataNodes: Each DataNode stores blocks from multiple namespaces and reports them to the respective NameNodes. DataNodes identify blocks by their Block Pool ID and Block ID. DataNodes can be dynamically added or removed from namespaces.
  - Clients: Each client contacts the NameNode of the namespace it wants to access and performs file system operations. Clients can access multiple namespaces by using different URIs or by using a mount table that maps paths to namespaces.
  - Routers: Each router is a proxy that routes requests from clients to the appropriate NameNode. Routers can also provide load balancing, caching, and federation monitoring functionalities.
- HDFS Federation has the following benefits :
  - It increases the overall throughput and availability of the cluster by distributing the load and the risk of failure among multiple NameNodes.
  - It allows for horizontal scaling of namespaces without affecting the block storage capacity or performance.
  - It enables finer-grained administration and isolation of namespaces by allowing different policies and permissions for different namespaces.
  - It facilitates the integration of existing HDFS clusters or other file systems into a federated cluster by using the mount table feature.