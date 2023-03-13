A distributed system is a collection of independent computers that appear to the users as a single coherent system. Distributed systems can have different architectures, such as client-server, peer-to-peer, or hybrid. Some examples of distributed systems are:

- Telecommunication networks: These are networks of devices that communicate with each other using protocols such as TCP/IP, HTTP, or SMTP. Telephone networks, cellular networks, and the Internet are examples of telecommunication networks. They are distributed systems because they consist of many nodes that exchange messages and coordinate actions.

- Real-time systems: These are systems that have strict timing constraints and must respond to events within a certain deadline. Examples of real-time systems are air traffic control systems, industrial control systems, and multimedia systems. They are distributed systems because they involve multiple sensors, actuators, and processors that interact with the physical environment and each other.

- Distributed database systems: These are systems that store and manage data across multiple servers, locations, or both. Examples of distributed database systems are Google's Bigtable, Amazon's Dynamo, and MongoDB. They are distributed systems because they provide data consistency, availability, and scalability by using techniques such as replication, partitioning, and caching.

The following diagram illustrates the basic architecture of a distributed database system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Application   |     |   Application   |     |   Application   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Middleware    |     |   Middleware    |     |   Middleware    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Database     |     |    Database     |     |    Database     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```