### Ad Hoc on demand distance vector routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations on demand and supports both unicast and multicast routing .
- AODV is based on the principle of distance vector routing, which means that each node maintains a routing table with the next hop and the distance (in terms of hops) to each destination .
- AODV uses three types of control messages to discover and maintain routes: route request (RREQ), route reply (RREP) and route error (RERR) .
- AODV is a reactive protocol, which means that it only initiates a route discovery process when a node needs to send data to a destination and does not have a valid route to it .
- AODV avoids routing loops by using sequence numbers to indicate the freshness of a route .
- AODV is the routing protocol used in Zigbee – a low power, low data rate wireless ad hoc network.
- AODV has various implementations such as MAD-HOC, Kernel-AODV, AODV-UU, AODV-UCSB and AODV-UIUC.
- AODV has some advantages such as low network overhead, quick adaptation to network changes, scalability and support for multicast .
- AODV has some disadvantages such as high latency for route discovery, vulnerability to malicious attacks, frequent route breaks and excessive flooding in large networks .