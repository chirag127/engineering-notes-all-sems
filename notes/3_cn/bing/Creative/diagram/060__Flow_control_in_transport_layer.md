Flow control in transport layer is a mechanism that regulates the amount of data that can be sent by a sender to a receiver, to avoid congestion and data loss. It is an end-to-end service that operates between the transport layer protocols of the source and destination hosts.  

The following diagram illustrates the basic architecture of flow control in transport layer using TCP as an example:

```
+----------------+       +----------------+
| Application    |       | Application    |
| layer          |       | layer          |
+----------------+       +----------------+
| Transport      |       | Transport      |
| layer          |       | layer          |
+----------------+       +----------------+
| Network        |       | Network        |
| layer          |       | layer          |
+----------------+       +----------------+
| Data link      |       | Data link      |
| layer          |       | layer          |
+----------------+       +----------------+
| Physical       |       | Physical       |
| layer          |       | layer          |
+----------------+       +----------------+
|                |       |                |
|     Sender     |       |    Receiver    |
|                |       |                |
+----------------+       +----------------+

+----------------+       +----------------+
|                |       |                |
|  Segment       |       |  Segment       |
|  +------+      |       |  +------+      |
|  | Port |      |       |  | Port |      |
|  +------+      |       |  +------+      |
|  | Seq  |      |       |  | Seq  |      |
|  +------+      |       |  +------+      |
|  | Ack  |      |       |  | Ack  |      |
|  +------+      |       |  +------+      |
|  | Win  |      |       |  | Win  |      |
|  +------+      |       |  +------+      |
|  | Data |      |       |  | Data |      |
|  +------+      |       |  +------+      |
|                |       |                |
+----------------+       +----------------+
```

The sender and receiver use TCP segments to exchange data. Each segment has a header that contains the following fields:

- Port: The source and destination port numbers that identify the processes on the hosts.
- Seq: The sequence number that indicates the position of the data in the byte stream.
- Ack: The acknowledgment number that indicates the next expected byte from the sender.
- Win: The window size that indicates the number of bytes that the receiver can accept.
- Data: The payload that contains the actual information.

The sender and receiver use a sliding window protocol to control the flow of data. The sender maintains a send window that indicates the range of bytes that can be sent without acknowledgment. The receiver maintains a receive window that indicates the range of bytes that can be received without overflowing the buffer. The sender adjusts the send window based on the acknowledgment and window size received from the receiver. The receiver adjusts the receive window based on the data received and the buffer availability.   

Flow control in transport layer ensures that the sender and receiver can communicate at a compatible rate, and that the network resources are not wasted or overwhelmed.