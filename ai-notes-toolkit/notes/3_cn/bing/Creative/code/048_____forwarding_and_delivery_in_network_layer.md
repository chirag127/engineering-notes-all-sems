### Forwarding and Delivery in Network Layer

The network layer is responsible for delivering packets from the source host to the destination host across multiple networks. The network layer supervises the handling of packets by the underlying physical networks and defines the route that packets take from source to destination.

Forwarding is the process of moving a packet from an input link interface to the appropriate output link interface of a router. Forwarding requires a routing table that maps the destination address of a packet to the output interface. Forwarding can be done in two ways: datagram approach and virtual-circuit approach. In datagram approach, each packet is treated independently and forwarded based on its destination address. In virtual-circuit approach, a connection is established between the source and the destination before any packets are sent, and each packet carries a virtual-circuit identifier that determines the output interface.

Routing is the process of determining the end-to-end paths that packets take from source to destination. Routing involves two main activities: path determination and packet switching. Path determination is the algorithm that computes the optimal path for each source-destination pair based on some criteria, such as shortest path, least cost, or load balancing. Packet switching is the technique that transfers packets from one router to another along the path until they reach the destination. Packet switching can be done in two ways: store-and-forward and cut-through. In store-and-forward, a router receives the entire packet before forwarding it to the next router. In cut-through, a router forwards a packet as soon as it receives the header of the packet.

Address aggregation is a technique that reduces the size of the routing table by grouping multiple destinations that share a common prefix into a single entry. For example, if there are four destinations with addresses 200.23.16.0/24, 200.23.17.0/24, 200.23.18.0/24, and 200.23.19.0/24, they can be aggregated into one entry with address 200.23.16.0/22. Address aggregation reduces the memory and processing requirements of routers and improves the scalability of the network.

Some tools and utilities that can be used to test and troubleshoot the packet delivery and routing are:

- ping: a command that sends an echo request packet to a destination and waits for an echo reply packet. It measures the round-trip time and packet loss rate between the source and the destination.
- traceroute: a command that sends a series of packets with increasing time-to-live (TTL) values to a destination and records the routers that the packets pass through. It shows the path and the delay of each hop between the source and the destination.
- ipconfig: a command that displays the IP address, subnet mask, default gateway, and DNS server of a host.
- route: a command that displays or modifies the routing table of a host or a router.
- arp: a command that displays or modifies the address resolution protocol (ARP) cache of a host or a router. ARP is a protocol that maps an IP address to a physical address, such as a MAC address .

: Network Layer – Understanding Packet Delivery and Routing, https://bing.com/search?q=forwarding+and+delivery+in+network+layer
: Network Layer Delivery Forwarding and Routing, https://vdocument.in/network-layer-delivery-forwarding-and-routing.html
: Data Communication and Networking – Network Layer: Delivery, Forwarding, and Routing Study Notes, https://examradar.com/network-layer-delivery-forwarding-routing-short-notes/
: Forwarding and Routing in Network Layer, https://electronicspost.com/forwarding-and-routing-in-network-layer/
: Network Layer Services- Packetizing, Routing and Forwarding, https://www.geeksforgeeks.org/network-layer-services-packetizing-routing-and-forwarding/