#### Learning bridge algorithms in local area network

- A bridge is a device that connects two or more local area networks (LANs) at the data link layer and forwards frames between them based on their MAC addresses.
- A bridge algorithm is a set of rules that determines how a bridge learns the MAC addresses of the devices connected to the LANs and how it decides which frames to forward or discard.
- There are two main types of bridge algorithms: spanning tree and source routing.
- Spanning tree algorithm :
  - It creates a loop-free logical topology of the interconnected LANs by disabling some of the bridge ports.
  - It elects a root bridge among all the bridges and assigns a priority to each bridge port based on the distance from the root bridge.
  - It forwards frames based on the destination MAC address and the port priority.
  - It dynamically adapts to changes in the network topology by exchanging configuration messages with other bridges.
  - It is simple and transparent to the end devices, but it may cause delays and waste bandwidth due to the disabled ports and the configuration messages.
- Source routing algorithm :
  - It allows the source device to specify the path of the frame through the interconnected LANs by adding a routing information field to the frame header.
  - It learns the MAC addresses of the devices and the bridges by listening to the frames that pass through it.
  - It forwards frames based on the routing information field and the destination MAC address.
  - It does not require any configuration messages or topology changes, but it may cause overhead and complexity due to the routing information field and the source device's knowledge of the network topology.
- A mnemonic to remember the difference between spanning tree and source routing is: **S**panning **T**ree **S**elects **T**he **P**ath, **S**ource **R**outing **S**pecifies **T**he **P**ath.