### Logical addressing in network layer

- Logical addressing is a method of identifying hosts and routers in a network using addresses that are independent of the physical location and connection of the devices.
- Logical addresses are assigned by the network layer protocol, such as IP (Internet Protocol), and are used to route packets from the source to the destination across multiple networks.
- Logical addresses are also called network addresses or layer 3 addresses, as they belong to the network layer of the OSI model.
- Logical addresses have two components: a network ID and a host ID. The network ID identifies the network to which the device belongs, and the host ID identifies the device within that network.
- Logical addresses are hierarchical, meaning that they can be divided into subnets of different sizes, depending on the network requirements. Subnetting allows more efficient use of the address space and reduces the size of the routing tables.
- Logical addresses are usually represented in a human-readable format, such as dotted decimal notation for IPv4 (e.g., 192.168.1.1) or hexadecimal notation for IPv6 (e.g., 2001:db8::1).
- Logical addresses are mapped to physical addresses, such as MAC addresses, using address resolution protocols, such as ARP (Address Resolution Protocol) for IPv4 or NDP (Neighbor Discovery Protocol) for IPv6. This allows the data link layer to deliver the packets to the correct device on the same network.
- Logical addressing is essential for the functioning of the internet, as it enables communication between devices that are not directly connected or located in different networks. Logical addressing also provides flexibility and scalability for network growth and changes.