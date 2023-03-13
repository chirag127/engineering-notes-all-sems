### Applications for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They are composed of mobile nodes that can communicate with each other directly or through intermediate nodes. Some of the applications of ad hoc networks are:

  - Military scenarios: Ad hoc networks can provide secure and robust communication among soldiers, vehicles, and command centers in the battlefield.
  - Disaster relief: Ad hoc networks can facilitate rescue operations and coordination among emergency workers in areas where the existing communication infrastructure is damaged or unavailable.
  - Vehicular networks: Ad hoc networks can enable information exchange among vehicles and roadside units for traffic management, safety, and entertainment purposes.
  - Sensor networks: Ad hoc networks can connect a large number of sensors that monitor various physical phenomena such as temperature, humidity, pressure, etc.
  - Personal area networks: Ad hoc networks can enable wireless communication among personal devices such as laptops, smartphones, tablets, etc.

- Localization is the process of determining the position of a node in an ad hoc network. Localization is important for many applications that require location-awareness, such as navigation, routing, tracking, etc. Some of the techniques for localization are:

  - GPS-based: Nodes use the global positioning system (GPS) to obtain their coordinates from satellites. This technique requires GPS receivers on the nodes and a clear view of the sky.
  - Range-based: Nodes use the distance or angle measurements from other nodes or landmarks to estimate their position. This technique requires specialized hardware such as radio, ultrasound, or infrared transceivers on the nodes.
  - Range-free: Nodes use the connectivity or proximity information from other nodes or landmarks to estimate their position. This technique does not require specialized hardware on the nodes, but it may be less accurate than range-based techniques.

- MAC issues refer to the challenges of designing a medium access control (MAC) protocol for ad hoc networks. A MAC protocol is responsible for coordinating the access of multiple nodes to the shared wireless channel. Some of the MAC issues are:

  - Hidden terminal problem: A node may not be able to sense the transmission of another node that is out of its range, but within the range of the intended receiver. This may cause a collision at the receiver and degrade the network performance.
  - Exposed terminal problem: A node may refrain from transmitting to its intended receiver because it senses the transmission of another node that is within its range, but out of the range of the intended receiver. This may cause a waste of channel resources and reduce the network throughput.
  - Fading and interference: The wireless channel may vary in quality and availability due to the effects of fading and interference from other sources. This may cause packet loss, delay, and errors in the network.
  - Mobility and topology changes: The nodes in an ad hoc network may move and join or leave the network dynamically. This may cause frequent changes in the network topology and connectivity, and require the MAC protocol to adapt accordingly.

- Routing protocols are algorithms that enable the nodes in an ad hoc network to discover and maintain routes to other nodes. Routing protocols can be classified into two main categories:

  - Proactive routing protocols: Nodes maintain up-to-date routing information to all other nodes in the network by periodically exchanging control messages. This reduces the route discovery latency, but increases the overhead and bandwidth consumption. Examples of proactive routing protocols are Destination-Sequenced Distance Vector (DSDV), Optimized Link State Routing (OLSR), and Global State Routing (GSR).
  - Reactive routing protocols: Nodes discover routes to other nodes on demand, when they have data to send. This reduces the overhead and bandwidth consumption, but increases the route discovery latency. Examples of reactive routing protocols are Ad hoc On-Demand Distance Vector (AODV), Dynamic Source Routing (DSR), and Temporally Ordered Routing Algorithm (TORA).

- Global State Routing (GSR) is a proactive routing protocol for ad hoc networks that aims to reduce the overhead of link state routing protocols. In GSR, each node maintains a local topology table that contains the link state information of its neighbors. The nodes periodically exchange their local topology tables with their neighbors, and use the information to construct a global topology table that contains the link state information of the whole network. The nodes then use the global topology table to compute the shortest paths to all other nodes using Dijkstra's algorithm. GSR has the following advantages and disadvantages:

  - Advantages: GSR can provide optimal routes to all destinations, and