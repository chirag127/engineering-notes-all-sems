#### How ZooKeeper helps in monitoring a cluster

- ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.
- ZooKeeper hosts are deployed in a cluster and, as long as a majority of hosts are up, the service will be available.
- ZooKeeper helps in monitoring a cluster by providing the following features:

  - **Status**: ZooKeeper exposes the status of each node in the cluster, such as the mode (leader or follower), the state (serving or not), the session count, the latency, and the outstanding requests.
  - **Metrics**: ZooKeeper collects and exposes various metrics related to the performance and health of the cluster, such as the number of connections, the number of requests, the number of watches, the number of ephemeral nodes, the data size, the JVM usage, and the thread usage .
  - **Coordination**: ZooKeeper provides a distributed coordination mechanism for the cluster, such as leader election, group membership, locks, barriers, and queues.
  - **Synchronization**: ZooKeeper ensures that the data in the cluster is consistent and up-to-date, by using a consensus protocol called Zab. Zab guarantees that any change to the data is replicated to a majority of nodes before being committed.
  - **Configuration**: ZooKeeper allows the cluster to store and manage configuration information, such as the cluster size, the node roles, the node properties, and the application settings. ZooKeeper also supports dynamic configuration changes, which can be applied without restarting the nodes.