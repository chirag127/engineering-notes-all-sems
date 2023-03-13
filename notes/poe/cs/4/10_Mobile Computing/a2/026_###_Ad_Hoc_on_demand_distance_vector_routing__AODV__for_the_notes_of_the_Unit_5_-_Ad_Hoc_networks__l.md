 Here are the notes for ### Ad Hoc on demand distance vector routing (AODV) for the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing:

### Ad Hoc on demand distance vector routing (AODV)
- AODV is a reactive routing protocol for mobile ad hoc networks (MANETs).
- It uses destination sequence numbers to determine freshness of routes and minimize routing loops.
- It maintains routing tables with next hop information for each destination.
- Routes are created on demand and destination sequence numbers are used to determine the freshness of routes and minimize routing loops.
- Route maintenance and route error handling are also included in the protocol.

Working:
- When a source node wants to send data packets to a destination node and does not already have a valid route to the destination, it initiates a route discovery process to locate the destination node.
- The source node broadcasts a ROUTE REQUEST (RREQ) packet to its neighbors.
- Each node receiving this packet updates its information for the source node and sets up a reverse path to the source node.
- If the node receiving the RREQ packet is the destination or has a fresh enough route to the destination, it sends a ROUTE REPLY (RREP) packet to the source node.
- Otherwise, it rebroadcasts the RREQ packet.
- Once the source node receives the RREP packet, it can begin sending data packets to the destination node.

Advantages:
- Reactive - creates routes only on demand, reducing bandwidth overhead.
- Loop free - uses sequence numbers to determine freshness of routes.
- Unidirectional link support - can handle unidirectional links.
- Low processing and memory overhead.

Disadvantages:
- Slow convergence - can lead to higher latency in obtaining a route.
- High control overhead - can lead to high network utilization during route acquisition.
- Count to infinity problem - possible but avoided with sequence numbers.