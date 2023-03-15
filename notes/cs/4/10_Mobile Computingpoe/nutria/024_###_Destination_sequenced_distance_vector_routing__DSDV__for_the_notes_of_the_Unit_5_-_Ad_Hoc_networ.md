
### Destination sequenced distance vector routing (DSDV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

Destination sequenced distance vector routing (DSDV) is a routing protocol for mobile ad hoc networks (MANETs) that was developed in 1994 by Charles E. Perkins and Pravin Bhagwat. It is an extension of the distance vector routing (DV) algorithm, which is based on the Bellman–Ford algorithm.

DSDV is a proactive routing protocol, meaning that it continuously updates its routing tables, even when there is no data to send. It uses sequence numbers to ensure that the most recent information is used to update the routing table. It also uses hop counts to determine the best route.

DSDV is a loop-free algorithm, meaning that it does not suffer from routing loops. It also ensures that the data is delivered in the correct order.

Advantages:
- DSDV is a proactive routing protocol, meaning that it continuously updates its routing tables, even when there is no data to send. 
- It uses sequence numbers to ensure that the most recent information is used to update the routing table. 
- It also uses hop counts to determine the best route. 
- DSDV is a loop-free algorithm, meaning that it does not suffer from routing loops. 
- It also ensures that the data is delivered in the correct order.

Disadvantages:
- DSDV has a high overhead due to the frequent updates of the routing table. 
- It is also not well suited for networks with a large number of nodes, as the routing table size increases exponentially with the number of nodes. 
- DSDV is also not well suited for dynamic networks, as the routing table must be updated whenever a node moves or leaves the network. 

Applications:
- DSDV is used in mobile ad hoc networks, where nodes are constantly changing their position. 
- It is also used in wireless sensor networks, where it can be used to route data from the sensor nodes to the base station. 
- DSDV is also used in vehicular ad hoc networks, where it is used to route data from the vehicles to the base station.

Mnemonic:
- DSDV: Destination Sequenced Distance Vector Routing