#### Zookeeper concepts

Zookeeper is a term that can refer to two different concepts:

- A zookeeper is a person who manages zoo animals that are kept in captivity for conservation or to be displayed to the public. They are usually responsible for the feeding and daily care of the animals. As part of their routine, the zookeepers may clean the exhibits and report health problems.

- ZooKeeper is a distributed application on its own while being a coordination service for distributed systems. It has a simple client-server model in which clients are nodes (i.e. machines) and servers are nodes. As a function, ZooKeper Clients make use of the services and servers provides the services . Some of the services that ZooKeeper provides are:

  - Naming: ZooKeeper allows clients to register and discover services using a hierarchical namespace.
  - Configuration management: ZooKeeper allows clients to store and update configuration data in a centralized manner.
  - Synchronization: ZooKeeper allows clients to coordinate their actions using locks, barriers, queues, and other primitives.
  - Group services: ZooKeeper allows clients to form and maintain groups of nodes, such as leader election, membership, and broadcast .

ZooKeeper is designed to be reliable, scalable, and fast. It uses a consensus protocol called Zab to ensure that all the servers have the same view of the data. It also uses a hierarchical data model, similar to a file system, to store the data in znodes, which are the basic units of data in ZooKeeper. Each znode can have data, children, and metadata, such as version, timestamp, and access control list .