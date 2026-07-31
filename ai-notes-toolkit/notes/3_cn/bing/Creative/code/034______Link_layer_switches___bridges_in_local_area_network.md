#### Link layer switches & bridges in local area network

- Link layer switches and bridges are network devices that operate at the data link layer (layer 2) of the OSI model.
- They are used to connect multiple LANs (local area networks) together to form a larger LAN or a single broadcast domain.
- They can also interconnect LANs that use different data link layer technologies, such as Ethernet and FDDI.
- They perform switching or bridging by forwarding frames based on the MAC (media access control) addresses of the source and destination devices.
- They use a forwarding table or a MAC address table to store the mappings between MAC addresses and ports or interfaces.
- They learn the MAC addresses of the devices connected to their ports by observing the source MAC addresses of the incoming frames.
- They can operate in different modes, such as store-and-forward, cut-through, or fragment-free, depending on how they process the frames.
- They can also perform filtering, segmentation, or aggregation functions to improve the performance or security of the network.
- They are transparent to the upper layer protocols, such as IP or TCP, and do not modify the frames except for updating the frame check sequence (FCS) field.
- They are different from routers, which operate at the network layer (layer 3) of the OSI model and forward packets based on the IP addresses of the source and destination devices.