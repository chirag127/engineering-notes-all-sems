### Temporary ordered routing algorithm (TORA) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

- TORA (Temporally Ordered Routing Algorithm) is a source initiated on-demand routing protocol for wireless mobile ad hoc networks .
- TORA is based on link reversal algorithm and aims to achieve a high degree of scalability, efficiency, adaptability, and loop-free routing .
- TORA does not use a shortest path solution, but rather builds and maintains a Directed Acyclic Graph (DAG) rooted at a destination.
- TORA uses a height metric to establish the DAG, such that information can only flow from nodes with higher heights to nodes with lower heights.
- TORA performs three basic functions: route creation, route maintenance, and route erasure .
- Route creation: A node that requires a route to a destination broadcasts a QRY (query) packet and sets its route-required flag. A node that receives a QRY packet either replies with an UPD (update) packet containing its height quintuple, or forwards the QRY packet if it has no route to the destination .
- Route maintenance: When a link failure occurs, the nodes adjacent to the link adjust their heights to restore the DAG. If the link failure causes a partition, the nodes in the partition that have no downstream neighbors generate a new reference level and propagate it to the other nodes in the partition .
- Route erasure: When a route is no longer valid, a node broadcasts a CLR (clear) packet to erase the invalid routes. The CLR packet contains the destination id and the height of the node that initiated the route erasure .
- TORA supports multiple routes to a destination and localizes the control messages to a small set of nodes near the topological change .
- TORA can operate smoothly in a highly dynamic mobile environment and exhibits multipath routing capability.
- TORA's height quintuple consists of: logical time of link failure, unique id of the node that defines the new reference level, a reflection indicator bit, a propagation ordering parameter, and unique id of the node .
- TORA's operation can be compared to that of water flowing downhill toward a sink node through a grid of tubes that model the routes in the network. The tube junctions represent the nodes, the tubes represent the links, and the water represents the packets.

: https://en.wikipedia.org/wiki/Temporally_ordered_routing_algorithm
: https://www.javatpoint.com/temporally-ordered-routing-algorithm