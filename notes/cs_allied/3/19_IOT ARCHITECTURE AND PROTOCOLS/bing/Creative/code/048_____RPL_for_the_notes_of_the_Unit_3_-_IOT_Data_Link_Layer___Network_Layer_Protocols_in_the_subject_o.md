Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS:

### RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for Routing Protocol for Low-Power and Lossy Networks  .
- Low-power and lossy networks (LLNs) are resource-constrained networks that have limited bandwidth, memory, processing power, and battery life  .
- LLNs are typically used for IoT applications such as smart grid, smart city, industrial automation, environmental monitoring, etc.
- RPL is designed to provide efficient and scalable routing for LLNs, by constructing a tree-like topology called a Destination Oriented Directed Acyclic Graph (DODAG)  .
- A DODAG is a directed graph that has no cycles and has a single root node that represents the destination or sink of the network  .
- RPL uses a metric called the Objective Function (OF) to select the best path from a source node to the root node, based on various criteria such as hop count, energy consumption, link quality, etc  .
- RPL operates in two modes: storing mode and non-storing mode  .
- In storing mode, each node maintains a routing table that contains the next hop information for all the nodes in the DODAG  .
- In non-storing mode, only the root node maintains a routing table that contains the full path information for all the nodes in the DODAG  .
- RPL uses two types of control messages: DODAG Information Object (DIO) and DODAG Information Solicitation (DIS)  .
- DIO messages are used to advertise the DODAG parameters, such as the root ID, the OF, the rank, etc  .
- DIS messages are used to request DIO messages from neighboring nodes  .
- RPL also uses two types of data messages: Destination Advertisement Object (DAO) and Destination Advertisement Object Acknowledgment (DAO-ACK)  .
- DAO messages are used to propagate the reachability information from the leaf nodes to the root node  .
- DAO-ACK messages are used to acknowledge the receipt of DAO messages  .
- RPL supports multiple DODAGs within a network, each with a different OF or application  .
- RPL also supports local repair mechanisms, such as poison reverse and local rerouting, to cope with link failures or topology changes  .
