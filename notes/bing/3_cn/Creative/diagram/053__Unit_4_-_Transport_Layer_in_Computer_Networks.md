## Unit 4 - Transport Layer in Computer Networks

The transport layer is a conceptual division of methods in the layered architecture of protocols in the network stack in the Internet protocol suite and the OSI model. The protocols of this layer provide end-to-end communication services for applications.

The transport layer takes data from the upper layer (i.e. application layer) and then breaks it into smaller size segments, numbers each byte, and hands over to the lower layer (network layer) for delivery.

The transport layer also provides the user address which is specified as a station or port. The port variable represents a specific process within a host machine that is the source or destination of the data.

The transport layer is responsible for the following functions :

- Service-point addressing: The transport layer provides the user address which is specified as a station or port. The port variable represents a specific process within a host machine that is the source or destination of the data.
- Segmentation and reassembly: The transport layer divides the data received from the application layer into smaller units called segments, and adds a header to each segment. The header contains information such as source and destination port numbers, sequence numbers, checksums, etc. The transport layer also reassembles the segments at the destination and checks for errors.
- Connection control: The transport layer can establish, maintain, and terminate a logical connection between the source and destination hosts. The connection can be either connection-oriented or connectionless, depending on the protocol used. Connection-oriented protocols, such as TCP, use a three-way handshake to establish a connection, and a four-way handshake to terminate a connection. Connectionless protocols, such as UDP, do not use any handshaking mechanism, and simply send the segments without any acknowledgment.
- Flow control: The transport layer regulates the flow of data between the source and destination hosts, to avoid congestion and buffer overflow. Flow control can be either end-to-end or hop-by-hop, depending on the protocol used. End-to-end flow control, such as TCP, uses a sliding window mechanism to control the amount of data that can be sent by the sender before receiving an acknowledgment from the receiver. Hop-by-hop flow control, such as X.25, uses a credit-based mechanism to control the amount of data that can be sent by the sender before receiving a permission from the next hop.
- Error control: The transport layer detects and corrects errors that may occur during the transmission of data. Error control can be either end-to-end or hop-by-hop, depending on the protocol used. End-to-end error control, such as TCP, uses checksums, sequence numbers, acknowledgments, and timers to detect and correct errors. Hop-by-hop error control, such as X.25, uses cyclic redundancy checks (CRC), acknowledgments, and retransmissions to detect and correct errors.

The following diagram illustrates the basic architecture of the transport layer in computer networks:

```
+-----------------+     +-----------------+
| Application     |     | Application     |
| Layer           |     | Layer           |
+-----------------+     +-----------------+
| Transport       |     | Transport       |
| Layer           |     | Layer           |
+-----------------+     +-----------------+
| Network         |     | Network         |
| Layer           |     | Layer           |
+-----------------+     +-----------------+
| Data Link       |     | Data Link       |
| Layer           |     | Layer           |
+-----------------+     +-----------------+
| Physical        |     | Physical        |
| Layer           |     | Layer           |
+-----------------+     +-----------------+
|                 |     |                 |
|      Host A     |     |      Host B     |
|                 |     |                 |
+-----------------+     +-----------------+
```

The transport layer header contains the following fields:

```
+-----------------+-----------------+-----------------+-----------------+
| Source Port     | Destination Port| Sequence Number | Acknowledgment  |
| (16 bits)       | (16 bits)       | (32 bits)       | Number (32 bits)|
+-----------------+-----------------+-----------------+-----------------+
| Data Offset     | Reserved        | Control Bits    | Window Size     |
| (4 bits)        | (6 bits)        | (6 bits)        | (16 bits)       |
+-----------------+-----------------+-----------------+-----------------+
| Checksum        | Urgent Pointer  | Options         | Padding         |
| (16 bits)       | (16 bits