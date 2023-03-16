### Ad Hoc On-Demand Distance Vector Routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations on demand and supports both unicast and multicast routing .
- AODV is based on the principle of distance vector routing, where each node maintains a routing table with the next hop and the distance (in terms of hops) to each destination .
- AODV uses three types of control messages: route request (RREQ), route reply (RREP) and route error (RERR)  .
- AODV uses sequence numbers to ensure loop-free and up-to-date routes  .
- AODV uses two timers: active route timeout and hello interval. Active route timeout is the time after which a route is considered invalid if no data packets are sent or received through it. Hello interval is the time between two consecutive hello messages that are used to detect link failures  .
- AODV is the routing protocol used in Zigbee – a low power, low data rate wireless ad hoc network. There are various implementations of AODV such as MAD-HOC, Kernel-AODV, AODV-UU, AODV-UCSB and AODV-UIUC.
- AODV has some advantages such as low overhead, quick adaptation to network changes, loop-free routes and scalability . AODV also has some disadvantages such as high latency, vulnerability to attacks, lack of quality of service (QoS) support and frequent route breaks .