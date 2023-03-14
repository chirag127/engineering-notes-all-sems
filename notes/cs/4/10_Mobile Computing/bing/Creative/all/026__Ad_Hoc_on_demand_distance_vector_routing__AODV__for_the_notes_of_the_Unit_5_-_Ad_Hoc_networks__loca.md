### Ad Hoc on demand distance vector routing (AODV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

- Ad Hoc on demand distance vector routing (AODV) is a routing protocol designed for wireless and mobile ad hoc networks .
- Ad hoc networks are networks that do not have any fixed infrastructure or centralized access point, and consist of mobile nodes that cooperate to communicate with each other.
- AODV establishes routes to destinations on demand, meaning that it only initiates a route discovery process when a node needs to send data to a destination and does not have a valid route to it .
- AODV supports both unicast and multicast routing, meaning that it can send data to a single destination or to a group of destinations .
- AODV uses destination sequence numbers to ensure loop freedom at all times, avoiding problems such as "counting to infinity" that are associated with classical distance vector protocols .
- AODV has low processing and memory overhead, as it does not require periodic routing advertisements or maintaining routes that are not in use .
- AODV offers quick adaptation to dynamic link conditions, as it can repair broken links locally or globally, depending on the situation .
- AODV determines unicast routes to destinations within the ad hoc network by using a route discovery process that involves sending route request (RREQ) packets and receiving route reply (RREP) packets .
- AODV determines multicast routes to destinations within the ad hoc network by using a multicast route discovery process that involves sending multicast route request (MRREQ) packets and receiving multicast route reply (MRREP) packets.
- AODV maintains routing tables at each node, where each entry contains the destination address, the next hop address, the destination sequence number, the hop count, and the lifetime of the route.
- AODV uses hello messages to detect link failures and update the routing tables accordingly.
- AODV uses route error (RERR) packets to notify the affected nodes of a link failure and invalidate the routes that use the broken link.
- AODV scales to large populations of mobile nodes, as it reduces the network utilization and avoids the broadcast storm problem by using an expanding ring search technique and a route request ID .

Some possible mnemonics and learning tricks for AODV are:

- AODV stands for Ad hoc On Demand Distance Vector, which can be remembered as **A**d hoc **O**n **D**emand **D**istance **V**ector.
- AODV uses destination sequence numbers to avoid loops, which can be remembered as **D**estination **S**equence **N**umbers for **D**eleting **S**illy **N**odes.
- AODV uses RREQ and RREP packets for unicast route discovery, which can be remembered as **R**equest and **R**eply for **R**eaching **R**emote **E**ndpoints.
- AODV uses MRREQ and MRREP packets for multicast route discovery, which can be remembered as **M**ulticast **R**equest and **R**eply for **M**ultiple **R**eceiving **E**ndpoints.
- AODV uses hello messages to detect link failures, which can be remembered as **H**ello for **H**ealthy **L**inks.
- AODV uses RERR packets to notify link failures, which can be remembered as **R**oute **E**rror for **R**eporting **R**otten **L**inks.