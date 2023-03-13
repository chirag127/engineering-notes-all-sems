### Point-to-point networks in network layer

- Point-to-point networks are networks that connect two devices directly without any intermediate devices or networks.
- Point-to-point networks are commonly used for wide area network (WAN) connections between routers or between a router and a host.
- Point-to-point networks require a data link layer protocol to encapsulate network layer packets into frames for transmission over the link.
- One of the most widely used data link layer protocols for point-to-point networks is the Point-to-Point Protocol (PPP).
- PPP has the following features and functions:
  - It can support multiple network layer protocols, such as IP, IPX, or AppleTalk, by using a field in the frame header to indicate the type of the encapsulated packet.
  - It can provide authentication, encryption, and compression of the data transmitted over the link, by using optional extensions and subprotocols.
  - It can dynamically negotiate and configure the parameters of the link, such as the maximum transmission unit (MTU), the quality of service (QoS), or the network layer address, by using the Link Control Protocol (LCP).
  - It can support multiple logical connections over the same physical link, by using the Multilink Protocol (MP).
  - It can support tunneling of point-to-point connections over other networks, such as the Internet, by using the Point-to-Point Tunneling Protocol (PPTP) or the Layer 2 Tunneling Protocol (L2TP).