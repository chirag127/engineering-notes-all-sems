### Routing algorithms and protocols for the notes of the Unit 5 - Network Layer in the subject of Computer Networks

- Routing is the process of finding and selecting the best path for data transmission from source to destination in a computer network.
- Routing algorithms are the software programs that implement the logic of routing, i.e., deciding the optimal path for each packet.
- Routing protocols are the set of rules and messages that routers use to communicate with each other and exchange routing information.
- Routing algorithms and protocols can be classified into two main categories: static and dynamic.
  - Static routing algorithms and protocols are fixed and do not change with the network conditions. They are usually configured manually by the network administrator. They are simple, fast, and secure, but they cannot adapt to network failures or congestion. Examples of static routing protocols are RIP and IGRP.
  - Dynamic routing algorithms and protocols are adaptive and change with the network conditions. They are usually configured automatically by the routers using routing messages. They are complex, slow, and less secure, but they can cope with network failures or congestion. Examples of dynamic routing protocols are OSPF, EIGRP, and BGP.
- Routing algorithms and protocols can also be classified based on the scope of their operation: intra-domain and inter-domain.
  - Intra-domain routing algorithms and protocols are used within a single administrative domain or network, such as a LAN or a WAN. They are also called interior gateway protocols (IGPs). They are usually based on distance vector or link state algorithms. Examples of intra-domain routing protocols are RIP, OSPF, and EIGRP.
  - Inter-domain routing algorithms and protocols are used between different administrative domains or networks, such as the Internet. They are also called exterior gateway protocols (EGPs). They are usually based on path vector algorithms. Examples of inter-domain routing protocols are BGP and EGP.
- Routing algorithms and protocols use various metrics to measure the cost or quality of a path, such as distance, hop count, bandwidth, delay, reliability, or load. They also use various techniques to optimize the routing performance, such as shortest path, flooding, broadcasting, multicasting, or anycasting.
- Routing algorithms and protocols have three basic functions: discovery, route management, and path determination.
  - Discovery is the process of identifying other routers on the network and establishing connections with them.
  - Route management is the process of keeping track of the possible destinations and the associated paths for each destination.
  - Path determination is the process of making dynamic decisions for where to send each packet based on the routing information and the network conditions.