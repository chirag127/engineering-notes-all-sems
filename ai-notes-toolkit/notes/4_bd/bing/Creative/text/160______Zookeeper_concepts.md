#### Zookeeper concepts

- Zookeeper is a distributed application that provides coordination services for other distributed systems.
- Zookeeper has a simple client-server model, where clients are nodes (machines) that use the services, and servers are nodes that provide the services.
- Zookeeper services include naming, configuration management, synchronization, and group services.
- Zookeeper can be thought of as a distributed file system, where each node can store data in a hierarchical namespace of znodes.
- Zookeeper ensures that the data stored in the znodes is consistent, ordered, and durable across the cluster.
- Zookeeper uses a leader-follower architecture, where one server acts as the leader and the rest are followers.
- Zookeeper uses a consensus protocol called Zab to elect the leader and replicate the data.
- Zookeeper clients can connect to any server in the cluster, and the server will forward the requests to the leader if necessary.
- Zookeeper clients can also watch the znodes for changes and receive notifications from the server.
- Zookeeper is designed to be fast, reliable, scalable, and simple to use.