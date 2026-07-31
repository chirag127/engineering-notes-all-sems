#### Link layer switches & bridges in local area network

- Link layer switches and bridges are network devices that operate at the data link layer (layer 2) of the OSI model.
- They connect multiple LANs (local area networks) together to form a larger LAN or a single broadcast domain.
- They use MAC addresses to forward Ethernet frames from one device to another device in an Ethernet standard based LAN.
- They can also interconnect data link layer domains that have different technologies, such as Ethernet to FDDI, by converting the frame formats and adjusting the maximum frame size.
- They store and forward the frames, which means they receive the entire frame, check for errors, and then transmit it to the destination or drop it if there is no destination.
- They can learn the MAC addresses of the devices connected to their ports by examining the source address of the incoming frames, and build a MAC address table to store the mappings of MAC addresses and ports.
- They can filter the frames by only forwarding them to the ports that belong to the destination MAC address, or broadcast them to all ports if the destination MAC address is unknown or multicast.
- They can improve the network performance by reducing the collision domain and increasing the bandwidth for each device.
- They can also perform some advanced functions, such as VLANs, spanning tree protocol, link aggregation, and quality of service.