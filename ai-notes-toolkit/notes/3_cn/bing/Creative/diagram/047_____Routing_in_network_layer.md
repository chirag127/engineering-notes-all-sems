### Routing in network layer

- Routing is the process of finding the best path from the source to the destination in a network.
- Routing is performed by a special device known as a router, which works at the network layer in the OSI model and internet layer in TCP/IP model.
- A router forwards packets based on the information available in the packet header and the forwarding table, which contains the next hop for each destination.
- Routing can be based on static tables that are rarely changed, or dynamic tables that are updated automatically depending on network conditions.
- Routing algorithms are used to determine the optimal routes for packets. Some examples of routing algorithms are distance vector, link state, and path vector.
- Routing can be classified into two types: intra-domain routing and inter-domain routing.
  - Intra-domain routing is the routing within a single network or autonomous system (AS), which is a group of networks under the same administrative control. Intra-domain routing protocols are also called interior gateway protocols (IGPs). Some examples of IGPs are RIP, OSPF, and EIGRP.
  - Inter-domain routing is the routing between different networks or autonomous systems. Inter-domain routing protocols are also called exterior gateway protocols (EGPs). The most widely used EGP is BGP, which exchanges routing information between ASes on the internet.