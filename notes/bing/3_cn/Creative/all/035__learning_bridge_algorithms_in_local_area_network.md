#### Learning bridge algorithms in local area network

- A bridge is a device that connects two or more local area networks (LANs) at the data link layer and forwards frames between them based on the destination address.
- A bridge algorithm is a set of rules that determines how a bridge learns the addresses of the devices connected to the LANs and how it decides which frames to forward or discard.
- There are two main types of bridge algorithms: spanning tree and source routing.
- Spanning tree algorithm :
  - It creates a loop-free logical topology of the network by disabling some of the bridge ports.
  - It elects a root bridge and assigns a cost to each bridge port based on the bandwidth of the link.
  - It uses the Bridge Protocol Data Units (BPDUs) to exchange information among bridges and to detect topology changes.
  - It forwards frames based on the destination address and the port cost.
  - It has the advantages of simplicity, transparency, and adaptability to topology changes.
  - It has the disadvantages of slow convergence, suboptimal routing, and limited scalability.
- Source routing algorithm :
  - It allows the source device to specify the path of the frame through the network by adding a routing information field (RIF) to the frame header.
  - It uses the All Routes Explorer (ARE) and the Spanning Tree Explorer (STE) frames to discover and update the routes in the network.
  - It forwards frames based on the RIF and the destination address.
  - It has the advantages of fast convergence, optimal routing, and high scalability.
  - It has the disadvantages of complexity, overhead, and security risks.

- A mnemonic to remember the difference between spanning tree and source routing is: **ST** stands for **S**imple and **T**ransparent, while **SR** stands for **S**pecific and **R**apid.