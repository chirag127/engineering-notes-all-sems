 Here is the content in markdown format for Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR):

## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

Ad hoc networks:
- Self organizing networks without any infrastructure
- Nodes act as routers and hosts
- Dynamic topology - links may change frequently
- Limited bandwidth and power
- Challenges: Routing, MAC, security, localization, power management

Localization:
- Determining position of nodes
- Uses ranging techniques like RSSI, AOA, TDOA
- Lateration and trilateration to compute positions
- Applications: tracking, navigation, location based services

MAC issues:
- Hidden terminal problem - nodes out of range of each other causing collisions
- Exposed terminal problem - nodes deferring unnecessarily reducing channel utilization
- Deafness - hidden terminals causing failure of RTS-CTS scheme
- Solutions: scheduling, directional antennas, busy tone, etc.

Routing protocols:
- Proactive: table driven -Destination sequenced distance vector (DSDV), Wireless routing protocol (WRP), Optimized link state routing (OLSR)
- Reactive: on demand - Ad hoc on demand distance vector (AODV), Dynamic source routing (DSR)
- Hybrid - Zone routing protocol (ZRP)

Global state routing (GSR):
- Maintaining and using global knowledge for efficient routing
- Periodically nodes broadcast and share topology, connectivity and traffic information
- Based on global knowledge, shortest paths and best routes are computed
- Need for scaling to large networks and overhead of maintaining global state