#### Link layer switches & bridges in local area network

- Link layer switches and bridges are network devices that operate at the data link layer (layer 2) of the OSI model.
- They connect multiple LANs (local area networks) together to form a larger LAN or a single broadcast domain.
- They use MAC addresses to forward Ethernet frames from one device to another device in an Ethernet standard based LAN.
- They store and forward frames, meaning they receive the entire frame, check for errors, and then forward it to the appropriate destination or drop it if it is not valid.
- They can also filter frames based on MAC addresses, preventing unnecessary traffic from reaching other segments of the network.
- They can learn MAC addresses dynamically by observing the source addresses of the incoming frames and updating their MAC address table accordingly.
- They can also handle different data link layer technologies, such as Ethernet, FDDI, or Token Ring, by converting the frame format and adjusting the maximum frame size if needed.

Some advantages of using link layer switches and bridges are:

- They reduce the collision domain size, improving the network performance and efficiency.
- They increase the network security, as they can isolate traffic based on MAC addresses or VLANs (virtual LANs).
- They enable network segmentation, allowing different groups of devices to communicate within their own LAN without interfering with other LANs.
- They are transparent to the network layer protocols, such as IP, meaning they do not affect the routing or addressing of the packets.

Some disadvantages of using link layer switches and bridges are:

- They increase the broadcast domain size, which can cause network congestion and latency if there are too many broadcasts or multicasts.
- They are vulnerable to MAC address spoofing or flooding attacks, which can compromise the network security or performance.
- They are not scalable for large networks, as they can create loops or bottleneecs if not configured properly with spanning tree protocol (STP) or other mechanisms.

Some examples of link layer switches and bridges are:

- Ethernet switch: a device that connects multiple Ethernet devices and forwards frames based on MAC addresses.
- Wireless access point: a device that connects wireless devices to a wired network and forwards frames based on MAC addresses.
- Transparent bridge: a device that connects two or more LANs with the same data link layer technology and forwards frames based on MAC addresses.
- Translational bridge: a device that connects two or more LANs with different data link layer technologies and forwards frames by converting the frame format and size.

Some applications of link layer switches and bridges are:

- Home network: a network that connects multiple devices, such as computers, smartphones, printers, and smart TVs, within a household using a wireless router or a switch.
- Campus network: a network that connects multiple buildings, such as classrooms, offices, labs, and dormitories, within a university or a company using switches and access points.
- Data center network: a network that connects multiple servers, storage devices, and switches within a data center using high-performance switches and routers.