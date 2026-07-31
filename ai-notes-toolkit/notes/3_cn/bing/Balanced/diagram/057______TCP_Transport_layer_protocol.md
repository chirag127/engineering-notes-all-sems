TCP Transport layer protocol
#### TCP Transport layer protocol
TCP stands for Transmission Control Protocol. It is a transport layer protocol that facilitates the transmission of packets from source to destination. It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network.

TCP is a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data.

TCP operates in three main steps: connection establishment, data transfer, and connection termination.

The following diagram shows the basic structure of a TCP segment, which is the unit of data exchanged between TCP endpoints.

```
  0                   1                   2                   3   
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
 +---------------+---------------+-------------------------------+
 |     Source    |   Destination |          Sequence             |
 |      Port     |      Port     |           Number              |
 +---------------+---------------+-------------------------------+
 |        Acknowledgment Number  |            Data               |
 |                               |           Offset             |
 +---------------+---------------+-------------------------------+
 |  Reserved |N|C|E|U|A|P|R|S|F| |         Window Size          |
 |           |S|W|C|R|C|S|S|Y|I| |                               |
 |           | |R|E|G|K|H|T|N|N| |                               |
 +---------------+---------------+-------------------------------+
 |         Checksum              |         Urgent Pointer       |
 +---------------+---------------+-------------------------------+
 |                    Options                    |    Padding    |
 +-----------------------------------------------+---------------+
 |                             data                              |
 +---------------------------------------------------------------+
```

The fields in the TCP segment header are as follows:

- Source Port: The 16-bit port number of the sender.
- Destination Port: The 16-bit port number of the receiver.
- Sequence Number: The 32-bit number that identifies the byte in the stream of data from the sender that the first byte of data in this segment represents.
- Acknowledgment Number: The 32-bit number that acknowledges the receipt of the previous segment by specifying the next expected sequence number from the sender.
- Data Offset: The 4-bit number that indicates the size of the TCP header in 32-bit words. The minimum value is 5, which means that the header has no options.
- Reserved: The 6-bit field that is reserved for future use and should be set to zero.
- Flags: The 9-bit field that contains control flags for the TCP segment. The flags are as follows:
  - NS: Nonce Sum. A flag used for Explicit Congestion Notification (ECN).
  - CWR: Congestion Window Reduced. A flag used to indicate that the sender has reduced its congestion window due to network congestion.
  - ECE: ECN-Echo. A flag used to indicate that the receiver has received a packet with the CE (Congestion Experienced) bit set in the IP header.
  - URG: Urgent. A flag used to indicate that the segment contains urgent data that should be processed immediately by the receiver.
  - ACK: Acknowledgment. A flag used to indicate that the acknowledgment number field is valid and that the receiver should send an acknowledgment for this segment.
  - PSH: Push. A flag used to indicate that the sender requests the receiver to push the data to the application layer as soon as possible, without buffering.
  - RST: Reset. A flag used to indicate that the sender wants to abort the connection due to an error or a security violation.
  - SYN: Synchronize. A flag used to indicate that the sender wants to establish a connection and that the sequence number field is the initial sequence number for the connection.
  - FIN: Finish. A flag used to indicate that the sender has no more data to send and wants to terminate the connection gracefully.
- Window Size: The 16-bit number that specifies the size of the receive window, which is the amount of data that the receiver can accept at a time.
- Checksum: The 16-bit number that is used to verify the integrity of the TCP header and data. It is computed as the 16-bit one's complement