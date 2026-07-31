### Point-to-point networks in network layer

- A point-to-point network is a network topology that connects two nodes directly using a single link.
- A point-to-point link can be either physical (such as a cable) or logical (such as a tunnel).
- A point-to-point network can be used to connect two routers, two hosts, or a router and a host.
- A point-to-point network can provide dedicated bandwidth, security, and reliability for the communication between the two nodes.
- A point-to-point network can use different protocols at the data link layer (layer 2) to encapsulate the network layer (layer 3) packets for transmission over the link.
- One of the most common protocols for point-to-point networks is the Point-to-Point Protocol (PPP), which can provide authentication, encryption, and compression features.
- PPP consists of three main components:
  - A way to encapsulate multiprotocol datagrams into frames.
  - A Link Control Protocol (LCP) to establish, configure, and test the data link connection.
  - A set of Network Control Protocols (NCPs) to negotiate the network layer parameters for different protocols (such as IP, IPX, or AppleTalk).
- PPP can operate over various types of physical media, such as serial ports, modems, ISDN, Ethernet, or wireless.
- PPP can also operate over logical media, such as Point-to-Point Tunneling Protocol (PPTP), which creates a virtual point-to-point link over an IP network.
- A mnemonic to remember the components of PPP is **ELN** (Encapsulation, Link Control, Network Control).
- A diagram to illustrate the structure of PPP is:

```
+-----------------+-----------------+
| Network Layer   | Network Layer   |
| Packet          | Packet          |
+-----------------+-----------------+
| PPP Header      | PPP Header      |
| PPP Payload     | PPP Payload     |
| PPP Trailer     | PPP Trailer     |
+-----------------+-----------------+
| Data Link Layer | Data Link Layer |
| Frame           | Frame           |
+-----------------+-----------------+
| Physical Layer  | Physical Layer  |
| Bit Stream      | Bit Stream      |
+-----------------+-----------------+
| Node A          | Node B          |
+-----------------+-----------------+
```