#### Zookeeper concepts

Apache ZooKeeper is an open-source server that enables highly reliable distributed coordination. It is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. Here are some key concepts of ZooKeeper:

1. **Znodes**: ZooKeeper stores data in a hierarchical namespace, much like a file system. The nodes in this namespace are called znodes. Each znode can store a small amount of data and has an associated stat structure that includes version numbers for data changes, ACL changes, and timestamps.

2. **Watches**: Clients can set watches on znodes. A watch is a one-time trigger that notifies the client when the znode changes.

3. **Ephemeral nodes**: Ephemeral nodes are znodes that exist as long as the session that created them is active. When the session ends, the znode is deleted.

4. **Sequential nodes**: Sequential nodes are znodes that are created with a unique monotonically increasing sequence number appended to the path name.

5. **Consistency**: ZooKeeper guarantees that once a write is complete, all subsequent reads will see that write. It also guarantees that updates from a client will be applied in the order that they were sent.

6. **Atomicity**: All updates are atomic. Either all the changes are applied, or none of them are.

7. **Reliability**: ZooKeeper is designed to be highly reliable. It replicates its data over a set of servers, and as long as a majority of the servers are available, ZooKeeper will be available.
