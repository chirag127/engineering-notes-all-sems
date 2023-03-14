### Temporary ordered routing algorithm (TORA) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

- TORA is a source initiated on-demand routing protocol for wireless mobile ad hoc networks .
- TORA is based on link reversal algorithm and aims to achieve a high degree of scalability, efficiency, adaptability and loop-freeness .
- TORA does not use a shortest path solution, but builds and maintains a directed acyclic graph (DAG) rooted at a destination.
- TORA assigns a height metric to each node, such that information can only flow from nodes with higher heights to nodes with lower heights.
- TORA performs three basic functions: route creation, route maintenance and route erasure .
- Route creation: A node that requires a route to a destination broadcasts a query (QRY) packet and sets its route-required flag. A node that receives a QRY packet either replies with an update (UPD) packet containing its height quintuple, or forwards the QRY packet if it has no route to the destination.
- Route maintenance: When a link failure occurs, the nodes adjacent to the link adjust their heights to restore the DAG. If the link failure causes a partition, the nodes in the partition that have no downstream neighbors generate a new reference level and propagate it to the other nodes in the partition.
- Route erasure: When a node detects that a route to a destination is invalid, it broadcasts a clear (CLR) packet to erase the invalid routes. The CLR packet contains the destination id and the height of the node that initiated the erasure.
- TORA supports multiple routes and localizes the control messages to a small set of nodes near the topological change .
- TORA's height quintuple consists of: logical time of link failure, unique id of the node that defines the new reference level, a reflection indicator bit, a propagation ordering parameter, and unique id of the node .