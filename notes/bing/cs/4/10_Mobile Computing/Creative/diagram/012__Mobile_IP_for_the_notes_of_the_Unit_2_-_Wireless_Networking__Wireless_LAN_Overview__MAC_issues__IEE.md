Mobile IP is a protocol that allows a mobile node to maintain its IP address and connectivity while moving across different networks. Mobile IP consists of three main components: a home agent, a foreign agent, and a mobile node. The home agent is a router on the mobile node's home network that keeps track of the mobile node's current location and forwards packets to it. The foreign agent is a router on the visited network that provides a temporary address and services to the mobile node. The mobile node is the device that changes its point of attachment to the Internet.

The following diagram illustrates the basic architecture of Mobile IP using ASCII characters:

```
+-----------------+      +-----------------+      +-----------------+
| Internet Host   |      | Home Agent      |      | Foreign Agent   |
|                 |      |                 |      |                 |
| IP: 10.1.1.1    |      | IP: 10.2.2.2    |      | IP: 10.3.3.3    |
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
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
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
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+      +-----------------+      +-----------------+
| Mobile Node     |      | Mobile Node     |      | Mobile Node     |
|                 |      |                 |      |                 |
| IP: 10.2.2.100  |      | IP: 10.2.2.100  |      | IP: 10.2.2.100  |
| CoA: N/A        |      | CoA: 10.3.3.100 |      | CoA: 10.4.4.100 |
+-----------------+      +-----------------+      +-----------------+
| Home Network    |      | Foreign Network |      | Foreign Network |
```

The diagram shows three scenarios of the mobile node's movement. In the first scenario, the mobile node is on its home network and does not need a care-of address (CoA). In the second scenario, the mobile node moves to a foreign network and obtains a CoA from the foreign agent. The home agent and the foreign agent exchange registration messages to establish a binding between the mobile node's IP address and its CoA. The home agent then tunnels packets destined to the mobile node to its CoA, and the foreign agent decapsulates them and delivers them to the mobile node. In the third scenario, the mobile node moves to another foreign network and obtains a new CoA from the new foreign agent. The mobile node updates its registration with the home agent and the old foreign agent, and the packet forwarding process continues as before.