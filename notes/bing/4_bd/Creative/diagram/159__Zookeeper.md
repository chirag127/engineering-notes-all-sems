Zookeeper is a distributed coordination service for distributed systems. It has a simple client-server model in which clients are nodes (i.e. machines) and servers are nodes. Zookeeper maintains a hierarchical namespace of znodes, which are data nodes that can store data and have permissions. Clients can read and write data from znodes, and also set watches on them to get notified of changes. Servers form a quorum, which is a majority of servers that agree on the state of the system. One of the servers acts as a leader, which handles write requests and coordinates the followers. The followers handle read requests and sync with the leader.

### Zookeeper

    +-----------------+      +-----------------+      +-----------------+
    |    Client 1     |      |    Client 2     |      |    Client 3     |
    +-----------------+      +-----------------+      +-----------------+
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             +-----------------------+-----------------------+
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
    +-----------------+      +-----------------+      +-----------------+
    |    Server 1     |      |    Server 2     |      |    Server 3     |
    |    (Leader)     |      |   (Follower)    |      |   (Follower)    |
    +-----------------+      +-----------------+      +-----------------+
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             +-----------------------+-----------------------+
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
                                 |
    +-----------------+      +-----------------+      +-----------------+
    |    Znode 1      |      |    Znode 2      |      |    Znode 3      |
    +-----------------+      +-----------------+      +-----------------+
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             |                       |                       |
             +-----------------------+-----------------------+
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
    +-----------------+      +-----------------+      +-----------------+
    |    Znode 4      |      |    Znode 5      |      |    Znode 6      |
    +-----------------+      +-----------------+      +-----------------+