The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet. The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to. The link layer is also known as the data link layer, or layer 2, in the OSI model of computer networking. The data link layer transfers data between nodes on a network segment across the physical layer and provides error control and addressing functions.

A diagram for the link layer in computer networks is shown below. The diagram is drawn using ASCII characters and markdown syntax. The diagram shows the data link layer encapsulating the network layer packet into a frame with a header and a trailer. The header contains the source and destination MAC addresses, the type of the network layer protocol, and other control information. The trailer contains a checksum or a cyclic redundancy check (CRC) to detect errors in the frame. The frame is then transmitted over the physical layer as a stream of bits.

#### Link layer in Computer Networks

```
+-----------------+-----------------+-----------------+-----------------+
|  Source MAC     | Destination MAC | Type            | Control         |
|  Address        | Address         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                         Network Layer Packet                  |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
|                                                               |
+-----------------+-----------------+-----------------+-----------------+
|  Checksum or    |                 |                 |                 |
|  CRC            |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
```