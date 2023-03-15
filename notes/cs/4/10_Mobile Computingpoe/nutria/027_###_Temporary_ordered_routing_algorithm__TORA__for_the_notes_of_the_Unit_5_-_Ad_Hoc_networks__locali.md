
### Temporary Ordered Routing Algorithm (TORA) for the Notes of the Unit 5 - Ad Hoc Networks, Localization, MAC Issues, Routing Protocols, Global State Routing (GSR), in the Subject of Mobile Computing

- **TORA** is an on-demand routing protocol used in ad hoc mobile networks. It is based on the idea of creating routing paths by flooding the network with **Query** packets. 

- **Query** packets are sent out by a source node and contain information such as the source and destination addresses, as well as the number of hops the packet has traveled. 

- When a node receives a **Query** packet, it will forward the packet to all of its neighbors, thus creating a **temporary ordered routing path** from the source node to the destination node. 

- **TORA** has two main components: **Directed Diffusion** and **Link Reversal**. 

- **Directed Diffusion** is used to create the temporary ordered routing path, while **Link Reversal** is used to maintain the routing path. 

- **Link Reversal** works by having the nodes on the routing path periodically send out **Update** packets. These packets contain information about the link quality of the path and are used to maintain the routing path. 

- **TORA** is a distributed routing protocol and does not require any centralized control. It is also highly scalable and can handle large networks. 

- **TORA** has several advantages, such as low latency, low overhead, and robustness to link failures. It is also suitable for dynamic networks, as it can quickly adapt to changes in the network topology. 

- **TORA** is used in several applications, such as military networks, vehicular networks, and wireless sensor networks. 

- Mnemonics and learning tricks for TORA: 
    - **T**emporarily **O**rdered **R**outing **A**lgorithm
    - **T**opology **O**bservation **R**eversal **A**lgorithm 
    - **T**ime **O**riented **R**outing **A**lgorithm