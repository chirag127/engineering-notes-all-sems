### Link layer switches & bridges

- Link layer switches and bridges are network devices that operate at the data link layer (layer 2) of the OSI model and forward data frames based on MAC addresses .
- Link layer switches and bridges can connect multiple LANs (local area networks) together to form a larger LAN. This process of aggregating networks is called network bridging .
- Link layer switches and bridges can also filter and isolate traffic within a LAN, reducing collisions and increasing bandwidth efficiency .
- Link layer switches and bridges can learn the MAC addresses of the devices connected to their ports by examining the source addresses of the incoming frames. They can then build a forwarding table that maps each MAC address to a port .
- Link layer switches and bridges can also perform error detection and correction on the frames they receive and transmit, using techniques such as CRC (cyclic redundancy check) or checksum .
- Link layer switches and bridges can be classified into different types based on their functionality and features, such as:
  - Transparent bridges: These are the simplest and most common type of bridges, which forward frames based on the destination MAC address and do not modify the frames in any way.
  - Source routing bridges: These are bridges that use a special field in the frame header to indicate the path that the frame should follow through the network. They are mainly used in Token Ring networks.
  - Remote bridges: These are bridges that connect LANs over a wide area network (WAN) using a protocol such as PPP (point-to-point protocol) or HDLC (high-level data link control).
  - Wireless bridges: These are bridges that connect a wired LAN to a wireless LAN or vice versa, using a wireless access point as a bridge device.
  - Layer 3 switches: These are switches that can also forward data at the network layer (layer 3) of the OSI model by incorporating routing functionality. They can use IP addresses or other network layer protocols to make forwarding decisions .