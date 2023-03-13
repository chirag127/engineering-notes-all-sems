Resource sharing is one of the key characteristics of distributed systems. It means that the existing resources in a distributed system can be accessed or remotely accessed across multiple computers in the system. Resources may include hardware (such as disks and printers), software (such as files, windows and data objects) and data. Resource sharing can vary widely in scope and in how close users collaborate together. For example, search engines and computer-supported cooperative work (CSCW) are two extremes of resource sharing.

A possible ascii diagram for resource sharing in a distributed system is shown below. It illustrates how different types of resources can be shared by different types of components (such as clients, servers and objects) through a network and a distribution middleware. The distribution middleware is a software layer that provides services and abstractions to enable resource sharing and coordination among the components. The network is a communication medium that connects the components and allows data exchange.

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Client 1     |       |    Client 2     |       |    Client 3     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
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
       |                       |                       |
       |                       |                       |
+---------------------------------------------------------------+
|                                                               |
|                      Distribution Middleware                  |
|                                                               |
+---------------------------------------------------------------+
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
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Server 1     |       |    Server 2     |       |    Server 3     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Object 1     |       |    Object 2     |       |    Object 3     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows that clients can access resources from servers and objects, and that servers and objects can also access resources from each other. The distribution middleware provides services such as naming, communication, synchronization, replication, fault tolerance, security and consistency to facilitate resource sharing. The network may be heterogeneous, unreliable and dynamic, and may have different protocols and topologies.

This is a simplified and abstract diagram of resource sharing in a distributed system. There may be more types of components, resources and services involved in a real distributed system. The diagram is not meant to be exhaustive or precise, but to illustrate the general idea of resource sharing.