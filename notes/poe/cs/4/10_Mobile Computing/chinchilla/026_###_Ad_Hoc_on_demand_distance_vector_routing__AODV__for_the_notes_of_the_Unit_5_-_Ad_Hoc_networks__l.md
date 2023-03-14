### Ad Hoc on demand distance vector routing (AODV)

Ad Hoc On-demand Distance Vector Routing (AODV) is a reactive routing protocol designed for mobile ad hoc networks (MANETs). It is a distance vector protocol that uses a hop-by-hop approach to find the shortest path between nodes. The protocol is capable of handling both unicast and multicast traffic.

#### How AODV works

AODV is an on-demand routing protocol, which means that it only establishes a route when it is necessary. When a node wants to send data to another node, it first checks its routing table to see if it already has a route to the destination. If it does not have a route, it broadcasts a Route Request (RREQ) message to its neighbors. The RREQ message contains the source and destination addresses and a unique identifier. When a neighbor receives the RREQ message, it checks its routing table to see if it can satisfy the request. If it cannot, it forwards the message to its neighbors. The process continues until the RREQ message reaches the destination node or a node that has a route to the destination. When the destination node receives the RREQ message, it sends a Route Reply (RREP) message back to the source node. The RREP message contains the route from the source to the destination. The source node caches the route in its routing table for future use.

#### Advantages of AODV

- AODV is a reactive protocol, which means that it only establishes a route when it is necessary. This reduces the overhead of route discovery and maintenance.
- AODV supports both unicast and multicast traffic.
- AODV is capable of handling dynamic network topologies, which makes it suitable for mobile ad hoc networks.

#### Disadvantages of AODV

- AODV may suffer from route loops and broken routes due to the lack of global state information.
- AODV does not support hierarchical routing, which makes it difficult to scale to large networks.
- AODV may suffer from the "black hole" problem, where a malicious node falsely claims to have a route to a destination, causing other nodes to send data to it, which it then drops.

#### Mnemonic and Learning Trick

AODV can be remembered as "Always On Demand Vector" or "Aha, On-demand Vector!".

To remember how AODV works, you can use the acronym RREQ, which stands for "Route REQuest". RREQ messages are sent by nodes to request a route to a destination. Similarly, you can use the acronym RREP, which stands for "Route REPlY". RREP messages are sent by the destination node to reply with a route to the source node.

Overall, AODV is a popular routing protocol for mobile ad hoc networks due to its reactive nature and support for both unicast and multicast traffic. However, it may suffer from route loops and broken routes, and it does not support hierarchical routing. By using the mnemonic and learning trick, you can remember the key concepts of AODV for exams and real-world applications.