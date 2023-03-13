## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They consist of mobile nodes that communicate with each other over wireless links.
- Localization is the process of determining the position of a node in an ad hoc network, either relative to other nodes or to a global coordinate system. Localization can be achieved by using GPS, signal strength, angle of arrival, time of arrival, or other techniques.
- MAC issues refer to the challenges of designing a medium access control protocol for ad hoc networks, such as collision avoidance, channel access, power control, fairness, and scalability. Some of the MAC protocols for ad hoc networks are CSMA/CA, MACA, MACAW, FAMA, IEEE 802.11, and Bluetooth.
- Routing protocols are the algorithms that enable the nodes in an ad hoc network to discover and maintain routes to other nodes. Routing protocols can be classified into proactive, reactive, and hybrid protocols.
  - Proactive protocols maintain fresh routing information for all destinations by periodically exchanging routing tables or link state information. Examples of proactive protocols are DSDV, OLSR, and GSR.
  - Reactive protocols find routes on demand by flooding the network with route request packets and waiting for route reply packets. Examples of reactive protocols are DSR, AODV, and TORA.
  - Hybrid protocols combine the features of proactive and reactive protocols to achieve a balance between routing overhead and latency. Examples of hybrid protocols are ZRP, CEDAR, and EIGRP.
- Global state routing (GSR) is a proactive routing protocol for ad hoc networks that is based on link state routing. In GSR, each node maintains a global view of the network topology by periodically exchanging link state packets with its neighbors. GSR uses a hierarchical structure to reduce the routing overhead and improve scalability. GSR divides the network into clusters, and each cluster has a cluster head that acts as a gateway to other clusters. GSR also uses multipoint relays (MPRs) to optimize the flooding of link state packets.

Some of the mnemonics and learning tricks for Unit 5 are:

- To remember the types of routing protocols, use the acronym **PAR** (Proactive, Active, Reactive).
- To remember the examples of proactive protocols, use the acronym **DOG** (DSDV, OLSR, GSR).
- To remember the examples of reactive protocols, use the acronym **DAT** (DSR, AODV, TORA).
- To remember the examples of hybrid protocols, use the acronym **ZCE** (ZRP, CEDAR, EIGRP).
- To remember the components of GSR, use the acronym **CLAM** (Cluster, Link state, MPR).