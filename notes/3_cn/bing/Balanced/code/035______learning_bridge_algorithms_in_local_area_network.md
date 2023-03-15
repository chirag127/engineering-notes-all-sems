#### Learning bridge algorithms in local area network

- A bridge is a device that connects two or more local area networks (LANs) at the data link layer and forwards frames based on the destination MAC address.
- A bridge algorithm is a method that determines how a bridge learns and updates its forwarding table and how it handles loops and congestion in the network.
- There are two main types of bridge algorithms: spanning tree (ST) and source routing (SR), which are specified by the IEEE 802 standards committee .
- Spanning tree algorithm:
  - It creates a loop-free logical topology of the network by disabling some of the bridge ports and forming a tree of active ports.
  - It uses a distributed protocol that elects a root bridge and assigns a cost to each port based on the bandwidth and distance to the root.
  - It updates the forwarding table by learning the MAC addresses from the incoming frames and aging out the entries that are not used for a certain time.
  - It handles topology changes by sending and receiving bridge protocol data units (BPDUs) that notify other bridges about the status of the ports and the root bridge.
- Source routing algorithm:
  - It allows the source station to specify the path of the frame through the network by appending a routing information field (RIF) to the frame header.
  - It uses a discovery process that involves sending and receiving explorer frames that collect the information about the available paths and bridges.
  - It updates the forwarding table by caching the RIFs from the incoming frames and using them to forward the frames with the same destination.
  - It handles topology changes by sending and receiving ring purge frames that invalidate the cached RIFs and trigger a new discovery process.