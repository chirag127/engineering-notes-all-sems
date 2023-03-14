## Unit 4 - Transport Layer in Computer Networks

The transport layer is the fourth layer in the OSI model and the Internet protocol suite. It provides end-to-end communication services for applications, such as connection-oriented communication, reliability, flow control, and multiplexing. The transport layer protocols are implemented in the end systems but not in the network routers. The transport layer protocols can be divided into two categories: connection-oriented and connectionless. The connection-oriented protocols, such as TCP, establish a logical connection between the source and destination before transmitting data. The connectionless protocols, such as UDP, do not require a connection and send data as independent datagrams.

The following diagram illustrates the basic architecture of the transport layer in computer networks:

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
|      Host A     |      |      Host B     |
|                 |      |                 |
+-----------------+      +-----------------+
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
+-----------------+      +-----------------+
| Data Link       |      | Data Link       |
| Layer           |      | Layer           |
+-----------------+      +-----------------+
| Physical        |      | Physical        |
| Layer           |      | Layer           |
+-----------------+      +-----------------+
|                 |      |                 |
|    Router 1     |      |    Router 2     |
|                 |      |                 |
+-----------------+      +-----------------+
```

The transport layer receives data from the application layer and divides it into segments, each with a sequence number and a checksum. The transport layer then passes the segments to the network layer, which adds source and destination IP addresses and encapsulates them into packets. The network layer then sends the packets to the data link layer, which adds source and destination MAC addresses and encapsulates them into frames. The data link layer then sends the frames to the physical layer, which converts them into bits and transmits them over the physical medium.

The transport layer at the destination host receives the segments from the network layer and checks the sequence number and the checksum. If the segments are in order and not corrupted, the transport layer delivers them to the application layer. If the segments are out of order or corrupted, the transport layer may request a retransmission from the source host, depending on the protocol used. The transport layer also performs flow control and congestion control to regulate the rate of data transmission and avoid network congestion.