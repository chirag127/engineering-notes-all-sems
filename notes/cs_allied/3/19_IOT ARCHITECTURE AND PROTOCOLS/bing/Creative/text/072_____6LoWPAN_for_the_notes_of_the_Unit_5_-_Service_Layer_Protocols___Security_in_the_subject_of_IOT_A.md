### 6LoWPAN

- 6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks.
- It is an open standard defined by the Internet Engineering Task Force (IETF) that enables low-power devices with limited processing capabilities to participate in the Internet of Things (IoT) by using IPv6 over IEEE 802.15.4 based networks .
- 6LoWPAN defines mechanisms for:
  - Encapsulation: how to fragment and reassemble IPv6 datagrams over the IEEE 802.15.4 frame size limit of 127 bytes.
  - Header compression: how to reduce the size of IPv6 and UDP headers to fit in the IEEE 802.15.4 frame payload.
  - Neighbor discovery: how to discover and register IPv6 addresses and prefixes of other nodes in the network.
  - Routing: how to forward IPv6 datagrams over multiple hops using mesh-under or route-over approaches.
- 6LoWPAN also supports IPv6 transition mechanisms to connect 6LoWPAN networks to IPv4 networks, such as NAT64, which allows IPv6-only nodes to communicate with IPv4-only nodes by translating the IPv6 addresses to IPv4 addresses and vice versa.
- 6LoWPAN is suitable for applications that require wireless internet connectivity at lower data rates, such as residential and office automation, smart grid, industrial monitoring, and environmental sensing.