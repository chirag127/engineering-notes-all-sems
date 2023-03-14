#### Link layer switches & bridges in local area network

- Link layer switches and bridges are network devices that interconnect different segments of a local area network (LAN) at the data link layer (layer 2) of the OSI model.
- They operate in store-and-forward mode, which means they receive a complete frame, check its integrity, and then forward it to the appropriate destination based on the MAC address of the frame.
- They can interconnect LAN segments that use different data link layer technologies, such as Ethernet and FDDI, as long as the upper layers are compatible.
- They can also regenerate the signal and reduce the collision domain, which improves the performance and reliability of the network.
- They extend the broadcast domain, which means they forward broadcast frames to all ports, unless they are configured with filtering rules.

Some of the advantages of using link layer switches and bridges are:

- They can increase the bandwidth of the network by dividing it into smaller segments and reducing the number of competing nodes.
- They can isolate traffic and improve security by creating separate collision domains and applying filtering rules based on MAC addresses.
- They can reduce the latency and error rate by regenerating the signal and checking the frame integrity before forwarding it.
- They can support different data link layer technologies and allow interoperability between them.

Some of the disadvantages of using link layer switches and bridges are:

- They cannot prevent broadcast storms, which can overload the network and cause congestion.
- They cannot perform routing functions, which means they cannot interconnect different network layer protocols or logical networks.
- They cannot handle frames that are larger than the maximum transmission unit (MTU) of the destination segment, which can cause fragmentation or discarding of frames.
- They can create loops in the network topology, which can cause instability and inconsistency in the forwarding tables, unless they are configured with a loop prevention protocol such as spanning tree protocol (STP).

A possible mnemonic to remember the difference between link layer switches and bridges is:

- Switches have many ports and can create many collision domains, while bridges have few ports and can create few collision domains.
- Switches are faster and smarter than bridges, because they use hardware-based switching and can learn MAC addresses dynamically, while bridges are slower and simpler, because they use software-based switching and have static MAC addresses.