TCP stands for Transmission Control Protocol. It is a transport layer protocol that facilitates the transmission of packets from source to destination. It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network .

TCP provides reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications running on hosts communicating via an IP network. Major internet applications such as the World Wide Web, email, remote administration, and file transfer rely on TCP, which is part of the Transport Layer of the TCP/IP suite.

TCP employs network congestion avoidance and error recovery mechanisms. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data.

#### TCP Transport layer protocol

The following diagram illustrates the basic architecture of a TCP segment:

```
  0                   1                   2                   3   
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
 +---------------------------------------------------------------+
 |          Source Port          |       Destination Port        |
 +---------------------------------------------------------------+
 |                        Sequence Number                        |
 +---------------------------------------------------------------+
 |                    Acknowledgment Number                      |
 +---------------------------------------------------------------+
 |  Data |           |U|A|P|R|S|F|                               |
 | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
 |       |           |G|K|H|T|N|N|                               |
 +---------------------------------------------------------------+
 |           Checksum            |         Urgent Pointer        |
 +---------------------------------------------------------------+
 |                    Options                    |    Padding    |
 +---------------------------------------------------------------+
 |                             data                              |
 +---------------------------------------------------------------+
```

The TCP header contains the following fields:

- Source Port: The 16-bit port number of the sender.
- Destination Port: The 16-bit port number of the receiver.
- Sequence Number: The 32-bit number that identifies the byte in the stream of data that the segment carries.
- Acknowledgment Number: The 32-bit number that acknowledges the receipt of the previous segment.
- Data Offset: The 4-bit number that indicates the size of the TCP header in 32-bit words.
- Reserved: The 6-bit field that is reserved for future use and must be set to zero.
- Control Bits: The 6-bit field that contains the flags that control the operation of TCP. The flags are:
  - URG: Urgent pointer field is significant.
  - ACK: Acknowledgment field is significant.
  - PSH: Push function.
  - RST: Reset the connection.
  - SYN: Synchronize sequence numbers.
  - FIN: No more data from sender.
- Window: The 16-bit number that indicates the size of the receive window in bytes.
- Checksum: The 16-bit number that is used for error detection of the header and data.
- Urgent Pointer: The 16-bit number that points to the byte following the urgent data in the segment.
- Options: The variable-length field that may contain additional information for TCP.
- Padding: The variable-length field that is used to make the TCP header a multiple of 32 bits.
- Data: The variable-length field that contains the actual data being transferred.