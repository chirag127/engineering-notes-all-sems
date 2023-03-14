#### Learning bridge algorithms in local area network

- A bridge is a device that connects two or more local area networks (LANs) at the data link layer and forwards packets based on the MAC addresses of the destination nodes.
- A bridge algorithm is a method that determines how a bridge learns and updates its forwarding table and how it handles broadcast and multicast packets.
- There are two main types of bridge algorithms: spanning tree and source routing.
- Spanning tree algorithm:
  - It is based on the IEEE 802.1 standard and uses a distributed algorithm to create a loop-free logical topology of the bridges and LANs in the network.
  - It elects a root bridge and assigns a cost to each link based on the bandwidth and delay. Then, it computes the shortest path from each bridge to the root bridge and selects the links that are part of the shortest path as the forwarding links. The rest of the links are blocked to prevent loops.
  - It handles broadcast and multicast packets by flooding them on the forwarding links, except the link from which they were received.
  - It adapts to topology changes by exchanging configuration messages called bridge protocol data units (BPDUs) and updating the forwarding table accordingly.
  - It has the advantages of simplicity, robustness, and compatibility with any LAN technology.
  - It has the disadvantages of inefficiency, slow convergence, and lack of load balancing.
- Source routing algorithm:
  - It is based on the IEEE 802.5 standard and uses a centralized algorithm to create a routing table for each source node in the network.
  - It requires each source node to discover the topology of the network by sending a special packet called an explorer packet, which is broadcasted on all links and collects the information of the bridges and LANs it traverses.
  - It uses the information collected by the explorer packet to compute the optimal path to each destination node and stores it in the routing table. Then, it appends the path information to each data packet as a source routing field, which is used by the bridges to forward the packet along the specified path.
  - It handles broadcast and multicast packets by sending them on multiple paths or by using a special field called the broadcast indicator, which is recognized by the bridges and causes them to forward the packet on all links, except the link from which they were received.
  - It adapts to topology changes by periodically sending new explorer packets and updating the routing table accordingly.
  - It has the advantages of efficiency, fast convergence, and load balancing.
  - It has the disadvantages of complexity, overhead, and scalability.

- A mnemonic to remember the difference between the two algorithms is: STAB (Spanning Tree Algorithm is Based on BPDUs) and SORC (Source Routing Algorithm is based on ORC, which stands for Optimal Routing Computation).