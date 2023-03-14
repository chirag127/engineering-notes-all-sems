## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet. It is responsible for transferring data between nodes on a network segment across the physical layer. The link layer can be divided into two sublayers: the media access control (MAC) layer and the logical link control (LLC) layer. The MAC layer handles the access to the shared medium, such as Ethernet or Wi-Fi, and the LLC layer provides error detection and flow control. 

The link layer also includes multiple access protocols, which are methods to coordinate the use of a shared medium by multiple nodes. Some examples of multiple access protocols are:

- ALOHA: A simple protocol that allows nodes to transmit frames whenever they have data to send, without checking the channel status. This can result in collisions, which are detected by the lack of acknowledgments. Nodes then retransmit the frames after a random delay. 
- CSMA: A protocol that requires nodes to sense the channel before transmitting. If the channel is busy, the node defers its transmission until the channel is idle. This can reduce collisions, but not eliminate them completely. 
- CSMA/CA: A protocol that uses a collision avoidance mechanism, such as a random backoff algorithm, to reduce the probability of collisions. This protocol is used in wireless networks, where collision detection is difficult. 
- CSMA/CD: A protocol that uses a collision detection mechanism, such as a jamming signal, to abort the transmission as soon as a collision is detected. This protocol is used in wired networks, where collision detection is feasible. 

The following diagram illustrates the basic architecture of a link layer in a computer network:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|      Node A     |     |      Node B     |     |      Node C     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Application    |     |  Application    |     |  Application    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Transport     |     |   Transport     |     |   Transport     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Network      |     |    Network      |     |    Network      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     LLC         |     |     LLC         |     |     LLC         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     MAC         |     |     MAC         |     |     MAC         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Physical      |     |   Physical      |     |   Physical      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Medium       |<--->|    Medium       |<--->|    Medium       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```