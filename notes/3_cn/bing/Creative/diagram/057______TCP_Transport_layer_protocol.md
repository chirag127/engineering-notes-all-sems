TCP Transport layer protocol is a standard that defines how to establish and maintain a network conversation through which application programs can exchange data. It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network. It is also a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data.

A detailed ASCII diagram for TCP Transport layer protocol is as follows:

#### TCP Transport layer protocol

```
+-----------------+ +-----------------+
| Application     | | Application     |
| Layer           | | Layer           |
+-----------------+ +-----------------+
| TCP             | | TCP             |
| Segment         | | Segment         |
+-----------------+ +-----------------+
| IP              | | IP              |
| Datagram        | | Datagram        |
+-----------------+ +-----------------+
| Data Link       | | Data Link       |
| Frame           | | Frame           |
+-----------------+ +-----------------+
| Physical        | | Physical        |
| Layer           | | Layer           |
+-----------------+ +-----------------+
|                 | |                 |
|                 | |                 |
|                 | |                 |
|                 | |                 |
|                 | |                 |
|                 | |                 |
|                 | |                 |
|                 | |                 |
|                 | |                 |
|                 | |                 |
|                 | |                 |
|                 | |                 |
+-----------------+ +-----------------+
| Physical        | | Physical        |
| Layer           | | Layer           |
+-----------------+ +-----------------+
| Data Link       | | Data Link       |
| Frame           | | Frame           |
+-----------------+ +-----------------+
| IP              | | IP              |
| Datagram        | | Datagram        |
+-----------------+ +-----------------+
| TCP             | | TCP             |
| Segment         | | Segment         |
+-----------------+ +-----------------+
| Application     | | Application     |
| Layer           | | Layer           |
+-----------------+ +-----------------+
```

The diagram shows the TCP segment structure and how it is encapsulated in an IP datagram and a data link frame. It also shows how the TCP segment is decapsulated at the destination. The TCP segment contains the following fields:

- Source port: The port number of the sender application
- Destination port: The port number of the receiver application
- Sequence number: The number of the first byte in the segment
- Acknowledgment number: The number of the next byte expected from the sender
- Header length: The number of 32-bit words in the header
- Flags: Control bits that indicate the state of the connection
- Window size: The number of bytes that the receiver can accept
- Checksum: A value that verifies the integrity of the segment
- Urgent pointer: A pointer to the urgent data in the segment
- Options: Optional fields that provide additional information
- Data: The payload of the segment

The TCP segment is then encapsulated in an IP datagram, which contains the source and destination IP addresses, the protocol number (6 for TCP), and other fields. The IP datagram is then encapsulated in a data link frame, which contains the source and destination MAC addresses, the type field (0x0800 for IP), and other fields. The data link frame is then transmitted over the physical layer, which can be a wired or wireless medium.

At the destination, the data link frame is decapsulated and the IP datagram is extracted. The IP datagram is then decapsulated and the TCP segment is extracted. The TCP segment is then processed by the TCP layer, which checks the checksum, the sequence number, the acknowledgment number, and the flags. The TCP layer then passes the data to the application layer, which is the final destination of the segment.