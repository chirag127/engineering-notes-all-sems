#### Learning bridge algorithms in local area network

- A bridge is a device that connects two or more local area networks (LANs) at the data link layer and forwards frames based on the destination MAC address.
- A bridge algorithm is a method that determines how a bridge learns and updates its forwarding table and how it handles loops and broadcast storms in the network.
- There are two main types of bridge algorithms: spanning tree (ST) and source routing (SR), which are specified by the IEEE 802 standards committee .
- Spanning tree algorithm:
  - It creates a loop-free logical topology of the network by disabling some of the bridge ports and forming a tree of active ports.
  - It uses a distributed protocol that elects a root bridge and assigns a cost to each port based on the bandwidth and distance to the root bridge.
  - It updates the forwarding table by learning the MAC addresses from the incoming frames and aging out the entries that are not used for a certain period of time.
  - It handles topology changes by sending and receiving special frames called bridge protocol data units (BPDUs) that inform other bridges about the new status of the ports.
  - It has the advantages of simplicity, transparency, and compatibility with any LAN technology.
  - It has the disadvantages of slow convergence, suboptimal routing, and wasted bandwidth on disabled ports.
- Source routing algorithm:
  - It embeds the route information in the frame header and lets the source node decide the path to the destination node.
  - It uses a discovery mechanism that sends special frames called explorer frames to find all possible routes to the destination node and stores them in a routing information field (RIF).
  - It updates the forwarding table by caching the RIFs from the incoming frames and discarding the entries that are not used for a certain period of time.
  - It handles topology changes by sending and receiving special frames called ring purge frames (RPFs) that inform other nodes about the new status of the links.
  - It has the advantages of fast convergence, optimal routing, and load balancing.
  - It has the disadvantages of complexity, overhead, and incompatibility with some LAN technologies.

- A mnemonic to remember the difference between ST and SR is: ST is Simple and Transparent, SR is Smart and Resourceful.