Process-to-process delivery in transport layer is the delivery of a packet, part of a message, from one process to another. A process is an entity of the application layer that uses the services of the transport layer. A transport layer protocol needs two identifiers, IP address and port number, at each end to make a connection. The IP address defines the host, and the port number defines the process on the host.

### Process-to-process delivery in transport layer

The following diagram illustrates the basic architecture of process-to-process delivery in transport layer using ASCII art:

```
+-----------------+      +-----------------+
| Application     |      | Application     |
| Layer           |      | Layer           |
+-----------------+      +-----------------+
| Transport       |      | Transport       |
| Layer           |      | Layer           |
+-----------------+      +-----------------+
| Network         |      | Network         |
| Layer           |      | Layer           |
+-----------------+      +-----------------+
| Data Link       |      | Data Link       |
| Layer           |      | Layer           |
+-----------------+      +-----------------+
| Physical        |      | Physical        |
| Layer           |      | Layer           |
+-----------------+      +-----------------+
|                 |      |                 |
|    Host A       |      |    Host B       |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|    IP Address   |      |    IP Address   |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|    Port Number  |      |    Port Number  |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|    Process      |      |    Process      |
|                 |      |                 |
+-----------------+      +-----------------+
```

The transport layer receives data from the application layer and divides it into segments. Each segment has a header that contains the source and destination port numbers. The segments are then passed to the network layer, which adds the source and destination IP addresses in the header of each packet. The packets are then sent to the data link layer, which adds the source and destination MAC addresses in the header of each frame. The frames are then transmitted over the physical layer to the destination host.

At the destination host, the data link layer removes the MAC addresses and passes the packets to the network layer. The network layer removes the IP addresses and passes the segments to the transport layer. The transport layer removes the port numbers and reassembles the segments into the original data. The data is then delivered to the appropriate process in the application layer.