#### Zookeeper concepts

- Zookeeper is a distributed application that provides coordination services for distributed systems, such as naming, configuration management, synchronization, and group services  .
- Zookeeper has a simple client-server model, where clients are nodes (machines) that use the services, and servers are nodes that provide the services.
- Zookeeper uses a hierarchical namespace, similar to a file system, to store data and metadata in znodes (zookeeper nodes) . Znodes can be persistent, ephemeral, or sequential.
- Zookeeper guarantees that the data and operations are consistent, ordered, and atomic across the cluster  . Zookeeper also ensures that the clients always see the most recent data.
- Zookeeper can operate in standalone mode, with a single server, or in replicated mode, with a quorum of servers  . In replicated mode, one server acts as the leader and the others as followers .
- Zookeeper uses a consensus protocol, such as Zab or Raft, to elect a leader and synchronize the state of the servers  . The leader is responsible for coordinating the requests from the clients and broadcasting the updates to the followers .
- Zookeeper is designed to be reliable, scalable, and fast  . Zookeeper can handle thousands of concurrent clients and millions of znodes. Zookeeper can also tolerate failures and recover from them  .