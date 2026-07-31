# Destination Sequenced Distance Vector Routing (DSDV)

Destination Sequenced Distance Vector Routing (DSDV) is a proactive routing protocol for ad hoc networks. It is based on the Bellman-Ford algorithm and was developed to solve the routing loop problem. In DSDV, each node maintains a routing table that contains the shortest distance and the first node on the shortest path to every other node in the network. The routing table is updated periodically to maintain the most recent route information.

Some key features of DSDV are:
- Each node maintains a routing table that contains the shortest distance and the first node on the shortest path to every other node in the network.
- The routing table is updated periodically to maintain the most recent route information.
- Each entry in the routing table is marked with a sequence number that is originated by the destination node.
- The sequence numbers are used to distinguish stale routes from new ones and to prevent routing loops.
- Each node transmits updates containing its routing table information to its neighbors.
- The updates are both time-driven and event-driven.
- If there is a change in the network topology, the affected nodes transmit updates immediately, instead of waiting for the next periodic update.

DSDV is a simple and efficient routing protocol for ad hoc networks. However, it has some limitations, such as the overhead of periodic updates and the slow convergence in the face of network topology changes. These limitations have led to the development of other routing protocols for ad hoc networks, such as Ad hoc On-Demand Distance Vector (AODV) and Dynamic Source Routing (DSR).