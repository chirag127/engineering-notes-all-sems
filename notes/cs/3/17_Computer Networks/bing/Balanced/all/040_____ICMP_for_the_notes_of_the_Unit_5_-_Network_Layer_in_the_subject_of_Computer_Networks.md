# ICMP

ICMP stands for Internet Control Message Protocol. It is a protocol that devices within a network use to communicate problems with data transmission. It is also used for reporting errors and management queries. ICMP messages are encapsulated in IP datagrams, which means that they don’t use higher level protocols (such as TCP or UDP) for transmission. ICMP is an integral part of IP and all IP modules must support the ICMP protocol.

Some of the main functions of ICMP are:

- Allow routers to inform a source when an IP packet sent by the source is undeliverable.
- Allow a source to discover all available paths to the destination device.
- Allow a source to test the reachability of a destination device.
- Allow a source to measure the round-trip time to a destination device.
- Allow a source to adjust the packet size to avoid fragmentation.

Some of the common ICMP messages are:

- Echo request and echo reply: These messages are used to test the reachability of a destination device. The source sends an echo request message to the destination and expects an echo reply message back. This is the basis of the ping command.
- Destination unreachable: This message is sent by a router or a host to the source when an IP packet sent by the source cannot be delivered to the destination. There are different codes for different reasons of unreachability, such as network unreachable, host unreachable, protocol unreachable, port unreachable, etc.
- Time exceeded: This message is sent by a router or a host to the source when an IP packet sent by the source has expired its time to live (TTL) value. This is used to prevent packets from looping indefinitely in the network.
- Parameter problem: This message is sent by a router or a host to the source when an IP packet sent by the source has an invalid or missing field in the IP header. This is used to notify the source of the error and the pointer to the problematic field.
- Source quench: This message is sent by a router or a host to the source when an IP packet sent by the source causes congestion in the network. This is used to request the source to reduce its sending rate.
- Redirect: This message is sent by a router to the source when an IP packet sent by the source can be delivered more efficiently by using a different router. This is used to update the source's routing table with a better route.
- Router advertisement and router solicitation: These messages are used by routers to advertise their presence and capabilities to hosts in the network. They are also used by hosts to solicit router information from routers in the network. This is the basis of the router discovery protocol.