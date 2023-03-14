## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They consist of mobile nodes that communicate with each other using wireless links. Localization is the process of determining the position of a node in an ad hoc network, which is essential for many applications and services. MAC issues refer to the challenges of coordinating the access to the shared wireless medium among the nodes, such as avoiding collisions, reducing interference, and saving energy. Routing protocols are the algorithms that enable the nodes to discover and maintain routes to other nodes in the network. Global state routing (GSR) is a routing protocol that uses link state information to make routing decisions.

The following diagram illustrates the basic architecture of an ad hoc network with localization, MAC, and GSR components.

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Node A         |     |  Node B         |     |  Node C         |
|                 |     |                 |     |                 |
|  +-----------+  |     |  +-----------+  |     |  +-----------+  |
|  |  GSR      |  |     |  |  GSR      |  |     |  |  GSR      |  |
|  +-----------+  |     |  +-----------+  |     |  +-----------+  |
|  |  MAC      |  |     |  |  MAC      |  |     |  |  MAC      |  |
|  +-----------+  |     |  +-----------+  |     |  +-----------+  |
|  |  Localization|     |  |  Localization|     |  |  Localization|
|  +-----------+  |     |  +-----------+  |     |  +-----------+  |
|  |  Wireless |  |     |  |  Wireless |  |     |  |  Wireless |  |
|  |  Interface|  |     |  |  Interface|  |     |  |  Interface|  |
|  +-----------+  |     |  +-----------+  |     |  +-----------+  |
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
       +-----------------------+-----------------------+
                 Wireless Link
```

In this diagram, each node has a wireless interface that enables it to communicate with other nodes within its transmission range. Each node also has a localization component that uses various techniques, such as GPS, signal strength, or angle of arrival, to estimate its own position and the positions of its neighbors. Each node also has a MAC component that implements a protocol, such as CSMA/CA, TDMA, or CDMA, to coordinate the access to the wireless channel and avoid collisions. Each node also has a GSR component that maintains a global view of the network topology by exchanging link state vectors with its neighbors. The link state vectors contain information about the status and quality of the links between the nodes. Based on the link state vectors, each node can compute the best route to any destination node using a shortest path algorithm, such as Dijkstra's algorithm. The GSR component also updates the link state vectors periodically or when there is a change in the network topology. The GSR protocol is designed to reduce the overhead of routing information exchange and to cope with the dynamic and unpredictable nature of ad hoc networks.