## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

Data management issues in mobile computing include data availability, consistency, security, and scalability. Data replication is a technique to improve data availability and performance by creating and maintaining multiple copies of data on different devices or servers. Adaptive clustering is a technique to organize mobile devices into groups based on their location, connectivity, and data access patterns, to facilitate data replication and synchronization.

The following diagram illustrates the basic architecture of a data replication system for mobile computers using adaptive clustering:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Mobile Host 1 |      |  Mobile Host 2 |      |  Mobile Host 3 |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Cluster Head  |      |  Cluster Head  |      |  Cluster Head  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Data Server 1 |      |  Data Server 2 |      |  Data Server 3 |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

Each mobile host belongs to a cluster, which is managed by a cluster head. The cluster head is responsible for replicating data from the data servers to the mobile hosts, and synchronizing any updates made by the mobile hosts to the data servers. The cluster head also communicates with other cluster heads to exchange information about the data availability and the mobility of the mobile hosts. The data servers store the original data and handle the requests from the cluster heads. The data servers may also replicate data among themselves to improve fault tolerance and load balancing. The adaptive clustering algorithm dynamically adjusts the cluster formation and the data replication strategy based on the changing network conditions and the data access patterns of the mobile hosts.