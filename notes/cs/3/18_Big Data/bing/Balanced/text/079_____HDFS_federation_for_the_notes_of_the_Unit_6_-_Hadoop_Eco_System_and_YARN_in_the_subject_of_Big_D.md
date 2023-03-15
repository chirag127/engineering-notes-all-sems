### HDFS Federation

- HDFS Federation is a feature of Hadoop 2.x that allows the cluster to have multiple NameNodes or namespaces, each managing a subset of the file system.
- HDFS Federation improves the scalability, performance, and isolation of the HDFS architecture by separating the namespace and the block storage layers.
- In HDFS Federation, each NameNode has its own block pool, which is a set of blocks that the NameNode is responsible for. The block pools are independent of each other and do not share any information.
- The DataNodes in the cluster store the blocks from multiple block pools and report them to the respective NameNodes. The DataNodes act as a common storage layer for all the NameNodes.
- The clients can access any namespace by specifying the NameNode address in the URI. The clients cache the location of the NameNodes and the block locations to reduce the lookup overhead.
- HDFS Federation provides the following benefits: 
  - It increases the aggregate capacity and throughput of the cluster by allowing more files, blocks, and transactions.
  - It isolates the namespaces from each other and reduces the impact of failures.
  - It allows different namespaces to have different replication and storage policies.
  - It enables the cluster to scale horizontally by adding more NameNodes as needed.
- HDFS Federation requires the following components to work:
  - A State Store that tracks the active and standby states of the NameNodes and the block pool mappings. ZooKeeper can be used as a State Store.
  - A Router that acts as a proxy between the clients and the NameNodes and routes the requests to the appropriate namespace. The Router also caches the namespace information and the block locations to improve performance.
  - A NameNode Federation Wizard that helps to configure and manage the federated cluster. The wizard can add, remove, or migrate namespaces and block pools.