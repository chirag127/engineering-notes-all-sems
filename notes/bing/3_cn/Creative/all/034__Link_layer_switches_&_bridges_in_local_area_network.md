#### Link layer switches & bridges in local area network

- Link layer switches and bridges are network devices that operate at the data link layer (layer 2) of the OSI model.
- They connect multiple LANs (local area networks) together to form a larger LAN or a single broadcast domain.
- They use MAC addresses to forward Ethernet frames from one device to another device in an Ethernet standard based LAN.
- They store and forward frames, which means they receive the entire frame, check for errors, and then forward it to the appropriate destination or drop it if it is not valid.
- They can also filter frames based on MAC addresses, which reduces the network congestion and improves the performance.
- They can learn MAC addresses dynamically by observing the source addresses of the incoming frames and updating their MAC address table accordingly.
- They can also handle different data link layer technologies, such as Ethernet, FDDI, Token Ring, etc. by converting the frame format and adjusting the maximum frame size.
- They can be classified into two types: transparent bridges and source routing bridges.
  - Transparent bridges are the most common type of bridges. They use the destination MAC address of the frame to determine the outgoing port. They use the spanning tree protocol (STP) to avoid loops in the network topology.
  - Source routing bridges are used in Token Ring networks. They use the source MAC address of the frame and a routing information field (RIF) to determine the path to the destination. They do not use STP, but rely on the source device to avoid loops.
- Link layer switches are similar to bridges, but they have some advantages over them, such as:
  - They have multiple ports and can forward frames in parallel, which increases the bandwidth and reduces the latency.
  - They have larger MAC address tables and can handle more devices and traffic.
  - They can perform more advanced functions, such as VLANs, QoS, security, etc. by using additional information in the frame header or payload.