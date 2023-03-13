 Here is the content in markdown format:

### Applications for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

Ad Hoc networks:
- Self-configuring network of mobile devices connected by wireless links
- No fixed infrastructure (no access points)
- Decentralized control (no centralized administration)
- Nodes act as routers and hosts
- Topology changes frequently and unpredictably
- Challenges: Routing, MAC, power consumption, security

Localization:
- Determining the position of a node in an ad hoc network
- Uses connectivity/proximity and signal strength information
- Methods: Triangulation (angle/distance), Scene analysis, RF fingerprinting
- Applications: Emergency response, tracking, location-based services

MAC issues:
- Hidden terminal problem: Nodes can't sense ongoing transmissions of other nodes, leading to collisions
- Exposed terminal problem: Nodes refrain from transmitting even when the channel is free due to possibility of collisions
- Solutions: RTS/CTS, scheduling-based protocols (TDMA), directional antennas

Routing protocols:
- Proactive: Consistently maintain routes to all destinations (DSR, OLSR)
- Reactive: Find routes on-demand when needed (AODV, DSDV)
- Hybrid: Combination of proactive and reactive (ZRP)
- Challenges: Frequent topology changes, limited bandwidth and power

Global state routing (GSR):
- Maintains overall view of network topology and link states
- Nodes exchange topology information and compute optimal routes
- Robust to topology changes but incurs high overhead
- Example: Link state routing

Advantages: Always has route to destination (if exists), considers entire topology
Disadvantages: Slow reaction to changes, high communication overhead

Examples of ad hoc networks: Vehicular ad hoc networks, mobile ad hoc networks, wireless mesh networks, sensor networks, etc.

Applications: Emergency/rescue operations, disaster relief, battlefield surveillance, smart spaces, etc.