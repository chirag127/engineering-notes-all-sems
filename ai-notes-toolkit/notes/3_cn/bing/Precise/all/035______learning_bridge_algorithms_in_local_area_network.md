#### Learning bridge algorithms in local area network

A bridge is a device that connects two or more local area networks (LANs) or segments of the same LAN. A bridge operates at the data link layer (layer 2) of the OSI model and uses MAC addresses to determine where to forward traffic.

Bridge algorithms are used to determine the best path for forwarding traffic between different segments of a LAN. Some common bridge algorithms include:

1. **Transparent Bridging:** This is the most common type of bridging used in Ethernet networks. In transparent bridging, the bridge learns the MAC addresses of the devices connected to each of its ports by examining the source addresses of incoming frames. The bridge then uses this information to build a forwarding table, which it uses to determine where to forward traffic.

2. **Source Route Bridging:** This type of bridging is used in Token Ring networks. In source route bridging, the source device specifies the entire path that the frame should take through the network. The bridge uses this information to forward the frame to its destination.

3. **Spanning Tree Protocol (STP):** This is a protocol used to prevent loops in a network with redundant paths. STP is used in conjunction with transparent bridging to ensure that there is only one active path between any two network segments.

Mnemonics and learning tricks:
- To remember the three types of bridge algorithms, you can use the acronym **TSS**: **T**ransparent Bridging, **S**ource Route Bridging, **S**panning Tree Protocol.
- To remember the order of the OSI model layers, you can use the mnemonic **Please Do Not Throw Sausage Pizza Away**: **P**hysical, **D**ata Link, **N**etwork, **T**ransport, **S**ession, **P**resentation, **A**pplication.