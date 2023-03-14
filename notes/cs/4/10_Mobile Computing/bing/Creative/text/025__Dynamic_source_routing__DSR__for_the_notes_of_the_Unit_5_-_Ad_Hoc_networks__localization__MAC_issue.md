### Dynamic Source Routing (DSR) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

- Dynamic Source Routing (DSR) is a routing protocol for wireless mesh networks .
- It is an on-demand protocol that does not require periodic table-update messages or hello packets .
- It uses source routing instead of relying on the routing table at each intermediate device .
- It has two major phases: Route Discovery and Route Maintenance .
- Route Discovery is initiated when a source node needs to send a packet to a destination node and does not have a route to it .
- The source node floods the network with Route Request packets that contain the source and destination addresses and a route record of the traversed nodes .
- The Route Request packets are forwarded by intermediate nodes until they reach the destination node or a node that has a route to the destination in its cache .
- The destination node or the intermediate node sends a Route Reply packet back to the source node along the reverse path or the cached path .
- The Route Reply packet contains the complete route from the source to the destination .
- The source node caches the route and uses it to send data packets to the destination node .
- The data packets carry the source route in their headers, which specifies the sequence of nodes to be traversed .
- Route Maintenance is performed when a link break or a node failure occurs in the source route .
- The node that detects the error sends a Route Error packet to the source node, indicating the failed link or node .
- The source node removes the invalid route from its cache and initiates a new Route Discovery if needed .
- DSR has some advantages such as low overhead, loop-free routing, and support for asymmetric and unidirectional links .
- DSR also has some disadvantages such as high header size, scalability issues, and vulnerability to malicious nodes .

: Dynamic Source Routing - Wikipedia
: Dynamic Routing Protocols: OSPF, EIGRP, RIPv2, IS-IS, BGP - Cisco Community
: Dynamic Source Routing Protocol - Carnegie Mellon University