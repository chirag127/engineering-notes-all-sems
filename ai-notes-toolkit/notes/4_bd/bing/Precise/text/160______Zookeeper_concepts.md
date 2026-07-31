#### Zookeeper concepts

Apache ZooKeeper is a distributed coordination service that enables synchronization across a cluster. It is used to maintain configuration information, naming, and provide distributed synchronization and group services. Some of the key concepts of ZooKeeper are:

1. **Znodes**: ZooKeeper stores data in a hierarchical namespace, much like a file system. The data is stored in znodes, which are similar to files and directories. Each znode can store up to 1 MB of data and can have children.

2. **Watches**: Clients can set watches on znodes. When a znode changes, the client is notified of the change. This allows clients to be notified of changes in the data they are interested in.

3. **Ephemeral nodes**: Ephemeral nodes are znodes that are automatically deleted when the session that created them ends. This is useful for implementing locks and leader election.

4. **Sequential nodes**: Sequential nodes are znodes that are automatically assigned a unique monotonically increasing number by the ZooKeeper cluster. This is useful for implementing queues and other data structures that require unique identifiers.

5. **Consistency**: ZooKeeper guarantees that all clients will see the same view of the data at any given time. This is achieved through the use of a consensus protocol.

6. **Atomicity**: All updates to the ZooKeeper data are atomic. This means that either all the changes are applied, or none of them are.

7. **Reliability**: ZooKeeper is designed to be highly reliable. It can survive the failure of any single node in the cluster. If a majority of the nodes are available, the service will continue to operate.
