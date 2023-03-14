 Here is the content in markdown format for the topic #### Hadoop 2.0 New Features - NameNode high availability:

#### Hadoop 2.0 New Features - NameNode high availability

- In Hadoop 1.x, the NameNode is a single point of failure (SPOF) in the Hadoop cluster. If the NameNode goes down, the entire cluster becomes inoperable.
- To overcome this limitation and achieve high availability for the NameNode, Hadoop 2.0 introduced the concept of an Active/Standby NameNode.
- In this configuration, there are two NameNodes in the cluster - an active NameNode that serves all the read/write requests, and a standby NameNode that remains synchronized with the active NameNode and takes over as the active NameNode when required (e.g. if the active NameNode fails).
- The metadata modifications from the active NameNode are replicated to the standby NameNode to keep it in sync. This is achieved using a new feature called Namespace Federation (implemented using ZooKeeper coordination).
- The clients are aware of both the NameNodes, and send all the requests to the active NameNode. In case of a failover, the clients detect the change and start sending requests to the new active NameNode.
- The key benefits of this model are high availability and automatic failover of the NameNode. There is negligible disruption to the service during the failover process.
- However, the additional (standby) NameNode adds to the cluster cost. There is also additional overhead to replicate the namespace updates to the standby NameNode, though this overhead is typically minimal.

The key points to remember are:

- Hadoop 2.0 provides high availability for the NameNode using an Active/Standby architecture with two NameNodes.
- The standby NameNode remains synchronized with the active NameNode and takes over on failure.
- Namespace updates are replicated from the active NameNode to the standby NameNode.
- Clients are aware of both NameNodes and send requests to the active one. They detect and handle failovers automatically.
- Additional hardware cost and minimal replication overhead are the main downsides.

Hope this helps! Let me know if you would like me to clarify or expand on any of the points.