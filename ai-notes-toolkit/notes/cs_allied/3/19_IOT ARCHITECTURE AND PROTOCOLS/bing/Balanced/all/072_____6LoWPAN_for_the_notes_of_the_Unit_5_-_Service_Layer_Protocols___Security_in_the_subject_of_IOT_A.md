# 6LoWPAN

- 6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks.
- It is an open standard defined by the Internet Engineering Task Force (IETF) that enables low-power devices with limited processing capabilities to participate in the Internet of Things (IoT) by using IPv6 over IEEE 802.15.4 based networks .
- 6LoWPAN defines mechanisms for:
  - Encapsulation: how to fragment and reassemble IPv6 datagrams over the IEEE 802.15.4 frame size limit of 127 bytes.
  - Header compression: how to reduce the size of IPv6 and UDP headers to fit in the IEEE 802.15.4 frame payload.
  - Neighbor discovery: how to discover and register IPv6 addresses and prefixes of other nodes in the network.
  - Routing: how to forward IPv6 datagrams over multiple hops using different routing protocols, such as RPL (Routing Protocol for Low-Power and Lossy Networks).
- 6LoWPAN networks can be connected to other IPv6 networks, such as the Internet, through edge routers that support IPv6 transition mechanisms, such as NAT64, which allows IPv6 nodes to communicate with IPv4 nodes.
- 6LoWPAN networks can support various applications that require wireless internet connectivity at lower data rates, such as residential and office automation, smart grid, industrial monitoring, etc.