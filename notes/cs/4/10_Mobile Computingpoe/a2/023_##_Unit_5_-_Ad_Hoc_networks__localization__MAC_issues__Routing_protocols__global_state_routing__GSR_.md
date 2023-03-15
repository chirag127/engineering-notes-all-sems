 Here is the content in markdown format for Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR):

## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

Ad Hoc networks:
- Self organizing wireless networks without any pre-existing infrastructure
- Nodes act as routers and communicate via wireless links
- Applications: Emergency rescue operations, military battlefields, conferences

Localization:
- Determining the position of nodes in an Ad Hoc network
- Methods: Received signal strength indication (RSSI), Time of arrival (ToA), Time difference of arrival (TDoA), Angle of arrival (AoA)
- Challenges: Inaccurate distance estimates, Node mobility, Limited resources

MAC issues:
- Hidden terminal problem: When a node is out of range of an ongoing transmission and causes collision
- Exposed terminal problem: When a node defers transmission even when the channel is idle due to inadequate sensing of carrier
- Solutions: RTS/CTS, Scheduling, Directional antennas

Routing protocols:
- Proactive: Each node maintains routing info to every other node. Low latency but high overhead. Eg: Destination Sequenced Distance Vector (DSDV)
- Reactive: Routes are discovered on demand. Lower overhead but higher latency. Eg: Ad hoc On-demand Distance Vector (AODV), Dynamic Source Routing (DSR)
- Hybrid: Combines proactive and reactive approaches. Eg: Zone Routing Protocol (ZRP)

Global state routing (GSR):
- Maintains global knowledge of the network to determine efficient routes
- Challenges: Scalability, message complexity, single point of failure
- Examples: FloodNET, Geographic Random Forwarding (GeRaF)