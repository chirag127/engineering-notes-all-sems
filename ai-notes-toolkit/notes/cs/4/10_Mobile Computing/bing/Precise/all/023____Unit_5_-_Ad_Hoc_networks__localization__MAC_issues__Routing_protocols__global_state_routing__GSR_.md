## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

### Ad Hoc Networks
- An ad hoc network is a decentralized type of wireless network.
- The network is ad hoc because it does not rely on a pre-existing infrastructure, such as routers in wired networks or access points in managed (infrastructure) wireless networks.
- Instead, each node participates in routing by forwarding data for other nodes, so the determination of which nodes forward data is made dynamically on the basis of network connectivity and the routing algorithm in use.

### Localization
- Localization is the process of determining the physical location of a device or user in a network.
- In wireless networks, localization techniques can be used to determine the location of a device based on the strength of the signals it receives from multiple access points.
- Localization can also be achieved through the use of GPS or other satellite-based positioning systems.

### MAC Issues
- The medium access control (MAC) layer is responsible for controlling access to the shared communication medium in a network.
- In wireless networks, the MAC layer must address issues such as interference, hidden and exposed terminal problems, and the near-far problem.
- Various MAC protocols have been developed to address these issues, including CSMA/CA, TDMA, and FDMA.

### Routing Protocols
- Routing protocols are used to determine the best path for data to travel from one node to another in a network.
- In ad hoc networks, routing protocols must be able to handle the dynamic nature of the network, where nodes can join, leave, or move within the network at any time.
- Examples of routing protocols used in ad hoc networks include AODV, DSR, and OLSR.

### Global State Routing (GSR)
- Global State Routing (GSR) is a type of routing protocol used in ad hoc networks.
- GSR is a table-driven protocol, where each node maintains a table containing the complete topology of the network.
- The tables are updated periodically through the exchange of control messages between nodes.
- GSR can provide optimal routes, but the overhead of maintaining the routing tables can be high in large or highly dynamic networks.