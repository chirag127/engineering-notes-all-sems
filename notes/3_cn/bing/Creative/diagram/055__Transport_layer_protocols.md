Transport layer protocols are protocols that lie between user applications and the network. They provide end-to-end communication services for applications, such as connection-oriented communication, reliability, flow control, and multiplexing.  

The most common transport layer protocols in the Internet protocol suite are the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP). TCP is a connection-oriented protocol that ensures reliable and ordered delivery of data, while UDP is a connectionless protocol that provides simple and fast messaging.  

Other transport layer protocols that have been defined and implemented include the Datagram Congestion Control Protocol (DCCP) and the Stream Control Transmission Protocol (SCTP). DCCP is a connection-oriented protocol that provides congestion control for unreliable datagrams, while SCTP is a connection-oriented protocol that supports multiple streams of data within a single connection. 

The following diagram illustrates the basic architecture of a transport layer protocol:

```
+-----------------+-----------------+-----------------+
| Application     | Application     | Application     |
| layer           | layer           | layer           |
+-----------------+-----------------+-----------------+
| Transport layer | Transport layer | Transport layer |
| protocol        | protocol        | protocol        |
+-----------------+-----------------+-----------------+
| Network layer   | Network layer   | Network layer   |
| protocol        | protocol        | protocol        |
+-----------------+-----------------+-----------------+
| Data link layer | Data link layer | Data link layer |
| protocol        | protocol        | protocol        |
+-----------------+-----------------+-----------------+
| Physical layer  | Physical layer  | Physical layer  |
| protocol        | protocol        | protocol        |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Computer A   |    Computer B   |    Computer C   |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
```

The transport layer protocol takes data from the application layer and adds a header that contains information such as the source and destination port numbers, the sequence and acknowledgement numbers, and the control bits. The transport layer protocol then passes the data to the network layer protocol, which adds another header that contains information such as the source and destination IP addresses. The network layer protocol then passes the data to the data link layer protocol, which adds another header that contains information such as the source and destination MAC addresses. The data link layer protocol then passes the data to the physical layer protocol, which converts the data into electrical signals or electromagnetic waves that can be transmitted over the physical medium.  

The process is reversed at the receiving end, where the physical layer protocol converts the signals or waves back into data, and the data link layer protocol, the network layer protocol, and the transport layer protocol remove their respective headers and pass the data to the upper layer. The transport layer protocol checks the data for errors, reorders the data if necessary, and acknowledges the receipt of the data to the sender. The transport layer protocol then delivers the data to the application layer protocol that matches the port number in the header.  

### Transport layer protocols

```
+-----------------+-----------------+-----------------+
| Application     | Application     | Application     |
| layer           | layer           | layer           |
+-----------------+-----------------+-----------------+
| Transport layer | Transport layer | Transport layer |
| protocol        | protocol        | protocol        |
+-----------------+-----------------+-----------------+
| Network layer   | Network layer   | Network layer   |
| protocol        | protocol        | protocol        |
+-----------------+-----------------+-----------------+
| Data link layer | Data link layer | Data link layer |
| protocol        | protocol        | protocol        |
+-----------------+-----------------+-----------------+
| Physical layer  | Physical layer  | Physical layer  |
| protocol        | protocol        | protocol        |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Computer A   |    Computer B   |    Computer C   |
|                 |                 |                 |
+-----------------+-----------------+-----------------+

+-----------------+-----------------+-----------------+
| Application     | Application     | Application     |
| layer           | layer           | layer           |
+-----------------+-----------------+-----------------+
| Transport layer | Transport layer | Transport layer |
| protocol        | protocol        | protocol        |