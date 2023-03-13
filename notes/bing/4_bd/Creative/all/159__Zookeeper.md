### Zookeeper

- Zookeeper is a distributed coordination service that provides a consistent, reliable and scalable way to manage configuration, synchronization, naming, leader election and group membership of a cluster of nodes.
- Zookeeper is based on the concept of a **znode**, which is a data structure that represents a file or a directory in a hierarchical namespace. A znode can store data, have children znodes, and have a version number that changes whenever the znode is modified.
- Zookeeper maintains a **quorum** of servers that replicate the znode data and handle client requests. A quorum is a majority of servers that agree on the state of the system. A quorum ensures that Zookeeper can tolerate failures and network partitions without losing data consistency.
- Zookeeper provides four types of guarantees to its clients: **sequential consistency**, **atomicity**, **single system image**, and **reliability**. These guarantees mean that Zookeeper will execute client operations in the order they are received, apply them atomically, present the same view of the system to all clients, and recover from failures without losing data.
- Zookeeper exposes a simple API to its clients, consisting of four basic operations: **create**, **delete**, **read**, and **write**. Clients can also use **watchers** to get notified of changes to znodes, and **ephemeral nodes** to create znodes that are automatically deleted when the client session ends.
- Zookeeper can be used for various distributed system scenarios, such as:
  - **Configuration management**: Zookeeper can store and update configuration parameters for a cluster of nodes, and notify the nodes of any changes.
  - **Synchronization**: Zookeeper can provide barriers, locks, and queues to coordinate the actions of multiple nodes.
  - **Naming**: Zookeeper can assign unique names or identifiers to nodes or resources in a cluster, and resolve them to their locations or addresses.
  - **Leader election**: Zookeeper can elect a leader among a group of nodes, and handle leader changes in case of failures or network partitions.
  - **Group membership**: Zookeeper can keep track of the nodes that belong to a group, and their status and availability.