A Beowulf cluster is a computer cluster of what are normally identical, commodity-grade computers networked into a small local area network with libraries and programs installed which allow processing to be shared among them. The result is a high-performance parallel computing cluster from inexpensive personal computer hardware. 

The following diagram illustrates the basic architecture of a Beowulf cluster:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Server Node    |      |  Client Node    |      |  Client Node    |
|                 |      |                 |      |                 |
|  - Master       |      |  - Slave        |      |  - Slave        |
|  - Scheduler    |      |  - Worker       |      |  - Worker       |
|  - File Server  |      |  - File Client  |      |  - File Client  |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
      |                       |                       |
      |                       |                       |
      +-----------------------+-----------------------+
                            |
                            |
                      +-----+-----+
                      |           |
                      |   Switch  |
                      |           |
                      +-----+-----+
                            |
                            |
                      +-----+-----+
                      |           |
                      |   Router  |
                      |           |
                      +-----+-----+
                            |
                            |
                      +-----+-----+
                      |           |
                      | Internet  |
                      |           |
                      +-----------+
```

The server node is the master node that controls the cluster. It is responsible for scheduling tasks, distributing data, and managing the file system. The client nodes are the slave nodes that perform the computations. They are workers that receive tasks and data from the server node, and return the results. The file server is a service that provides a shared file system for the cluster. The file client is a software that allows the client nodes to access the file server. The switch is a device that connects the nodes in the cluster and enables fast data transfer. The router is a device that connects the cluster to the Internet and allows external access.  

: Beowulf cluster - Wikipedia
: Beowulf.org: Overview
: Introduction to Beowulf Cluster - GeeksforGeeks