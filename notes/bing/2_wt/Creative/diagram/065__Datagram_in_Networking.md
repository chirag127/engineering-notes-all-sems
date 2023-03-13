A datagram is a basic transfer unit associated with a packet-switched network. Datagrams are data packets which contain adequate header information so that they can be individually routed by all intermediate network switching devices to the destination. Datagrams provide a connectionless communication service across a packet-switched network. A datagram is an independent, self-contained message sent over the network whose arrival, arrival time, and content are not guaranteed.

#### Datagram in Networking

The following diagram illustrates the basic architecture of a datagram network:

```
+-----------------+      +-----------------+      +-----------------+
|   Source Host   |      |   Intermediate  |      |  Destination    |
|                 |      |   Switching     |      |  Host           |
|                 |      |   Device        |      |                 |
|                 |      |                 |      |                 |
|                 |      |                 |      |                 |
|                 |      |                 |      |                 |
|                 |      |                 |      |                 |
|                 |      |                 |      |                 |
|                 |      |                 |      |                 |
|                 |      |                 |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |<---------------------->|<---------------------->|
       |      Datagram         |      Datagram         |
       |      Segment          |      Segment          |
       |      (Header +        |      (Header +        |
       |      Payload)         |      Payload)         |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       +------------------------+------------------------+
```

The source host divides the data into smaller parts called datagrams and adds a header to each datagram. The header contains information such as the source and destination addresses, the length of the datagram, the sequence number, and the checksum. The source host then sends the datagrams to the intermediate switching device, which may be a router, a switch, or a gateway. The intermediate switching device examines the header of each datagram and forwards it to the next hop along the route to the destination host. The intermediate switching device does not maintain any state information about the datagrams or the connection. The destination host receives the datagrams and reassembles them into the original data. The destination host may also perform error checking and retransmission requests if some datagrams are lost or corrupted. The destination host does not send any acknowledgment to the source host for the received datagrams. The datagram network does not guarantee the order, delivery, or integrity of the datagrams. The datagram network is suitable for applications that can tolerate some loss or delay of data, such as voice or video streaming. The datagram network is also scalable and robust, as it does not require any connection establishment or termination, and can handle network congestion and failures. The datagram network is also known as the connectionless network or the best-effort network.