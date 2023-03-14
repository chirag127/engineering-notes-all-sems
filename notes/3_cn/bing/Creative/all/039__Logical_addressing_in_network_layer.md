### Logical addressing in network layer

- Logical addressing is a method of identifying hosts and routers in a network using numerical values that are independent of the physical addresses.
- Logical addresses are also called network addresses or IP addresses, and they are assigned by the network administrator or the Internet service provider (ISP).
- Logical addressing enables communication between hosts and routers across different physical networks, as long as they share a common logical address space.
- Logical addressing is implemented by the network layer, which is responsible for routing packets from the source to the destination based on the logical addresses.
- Logical addressing is different from physical addressing, which is a method of identifying hosts and routers in a network using their hardware addresses or MAC addresses. Physical addressing is implemented by the data link layer, which is responsible for transmitting frames from one node to another within the same physical network.
- Logical addressing and physical addressing work together to enable end-to-end communication in a network. The network layer uses the logical addresses to determine the best path for the packets, and the data link layer uses the physical addresses to deliver the frames to the next hop along the path.

Some points to remember about logical addressing are:

- Logical addresses are hierarchical, meaning they consist of two parts: a network part and a host part. The network part identifies the network to which the host belongs, and the host part identifies the host within the network.
- Logical addresses are variable-length, meaning they can have different sizes depending on the network class or the subnetting scheme. The most common logical address format is the IPv4 address, which is 32 bits long and divided into four octets separated by dots. For example, 192.168.1.100 is an IPv4 address.
- Logical addresses are dynamic, meaning they can change over time depending on the network configuration or the host location. For example, a host can obtain a different logical address when it connects to a different network or when it renews its lease from a DHCP server.
- Logical addresses are globally unique, meaning they are not repeated in the entire Internet. However, some logical addresses are reserved for private networks, which are not connected to the Internet and can use the same logical addresses internally. For example, 192.168.x.x is a private network address range.