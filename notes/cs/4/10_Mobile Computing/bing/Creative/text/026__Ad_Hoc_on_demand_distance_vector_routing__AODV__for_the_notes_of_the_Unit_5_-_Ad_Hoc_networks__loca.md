### Ad Hoc On Demand Distance Vector Routing (AODV)

- AODV is a routing protocol for mobile ad hoc networks (MANETs) and other wireless ad hoc networks. 
- AODV is based on the principle of on-demand route discovery, which means that routes are established only when needed by the source node.  
- AODV uses sequence numbers to ensure loop-free and fresh routes.  
- AODV uses three types of control messages: route request (RREQ), route reply (RREP), and route error (RERR).  
- AODV supports both unicast and multicast routing.  
- AODV has the following advantages: 
  - It adapts quickly to dynamic network topology and link failures.
  - It has low processing and memory overhead at each node.
  - It has low network utilization for route maintenance.
  - It can handle high mobility and large network size.
- AODV has the following disadvantages: 
  - It may cause high latency for route discovery due to flooding of RREQs.
  - It may suffer from route breaks and frequent route repairs due to mobility.
  - It may generate excessive control overhead in large and dense networks.
  - It may not scale well to high traffic load and network congestion.