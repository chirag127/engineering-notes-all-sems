#### Zookeeper concepts

- Zookeeper is a distributed application that provides coordination services for distributed systems.
- Zookeeper has a simple client-server model, where clients are nodes (machines) that use the services, and servers are nodes that provide the services.
- Zookeeper exposes common services such as naming, configuration management, synchronization, and group services in a simple interface.
- Zookeeper can be thought of as a distributed file system, where each node in the system has a path name and can store some data.
- Zookeeper maintains a hierarchical namespace of znodes, which are data nodes that can have children and data associated with them.
- Zookeeper guarantees that the data in the znodes is consistent, ordered, and atomic across the cluster.
- Zookeeper uses a leader-follower model, where one server acts as the leader and coordinates the updates from the followers.
- Zookeeper uses a quorum-based protocol, where a majority of servers must agree on a change before it is committed.
- Zookeeper supports ephemeral znodes, which are znodes that are automatically deleted when the client session that created them ends.
- Zookeeper supports watches, which are notifications that a client can set on a znode to be alerted when the znode changes.