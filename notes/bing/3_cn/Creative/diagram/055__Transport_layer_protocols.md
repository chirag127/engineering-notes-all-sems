Transport layer protocols are the protocols that provide end-to-end communication services for applications. They lie between the user applications and the network layer. The most common transport layer protocols are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP). TCP provides reliable, connection-oriented, and stream-oriented communication, while UDP provides unreliable, connectionless, and datagram-oriented communication. Other transport layer protocols that have been defined and implemented include the Datagram Congestion Control Protocol (DCCP) and the Stream Control Transmission Protocol (SCTP).

### Transport layer protocols

The following diagram shows the basic structure of a transport layer protocol header. The header contains information such as the source and destination port numbers, the sequence and acknowledgment numbers, the checksum, and the flags. The header is followed by the payload, which is the data that the protocol is carrying.

```
+---------------------+---------------------+
|  Source Port        |  Destination Port   |
+---------------------+---------------------+
|  Sequence Number    |  Acknowledgment No. |
+---------------------+---------------------+
|  Data Offset |Flags |  Window Size        |
+---------------------+---------------------+
|  Checksum           |  Urgent Pointer     |
+---------------------+---------------------+
|  Options (if any)   |  Padding (if any)   |
+---------------------+---------------------+
|                     |                     |
|        Payload      |                     |
|                     |                     |
+---------------------+---------------------+
```