### Process-to-process delivery in transport layer

```
+---------------------+
| Application Layer   |
+---------------------+
          |
          |
          V
+---------------------+
| Transport Layer     |
+---------------------+
|                     |
|  +---------------+  |
|  |    Process    |  |
|  |   Multiplexing|  |
|  +---------------+  |
|                     |
|  +---------------+  |
|  |   Flow and    |  |
|  | Congestion    |  |
|  |   Control     |  |
|  +---------------+  |
|                     |
|  +---------------+  |
|  |   Error       |  |
|  |   Control     |  |
|  +---------------+  |
|                     |
+---------------------+
          |
          |
          V
+---------------------+
| Network Layer       |
+---------------------+
```

The transport layer is responsible for process-to-process delivery of the entire message. It provides services such as connection-oriented data transfer, reliability, flow control, and multiplexing. The transport layer ensures that the whole message arrives intact and in order, overseeing both error control and flow control at the source-to-destination level. It also provides the acknowledgment of the successful data transmission and sends the next data if no errors occurred. The transport layer creates segments out of the message received from the application layer. Segmentation is the process of dividing a long message into smaller messages. These smaller messages are easier to transmit and manage. The transport layer header is then added to each segment, and the resulting segment is passed to the network layer. The transport layer header contains the source and destination port numbers, which are used for multiplexing and demultiplexing data from multiple applications. The transport layer is also responsible for flow control and congestion control. Flow control is the process of adjusting the rate of data transmission between two nodes based on the network's capacity. Congestion control is the process of preventing network congestion by reducing the rate of data transmission when the network is congested. The transport layer can use various mechanisms to control the flow of data and prevent congestion, such as sliding window protocols and congestion avoidance algorithms. The transport layer also provides error control by detecting and correcting errors that may occur during transmission. Error control mechanisms include checksums, acknowledgments, and retransmissions. If an error is detected, the transport layer can request that the data be retransmitted. The transport layer is responsible for ensuring that the data is delivered correctly and in the correct order. It provides a reliable, process-to-process communication service between applications running on different hosts. The transport layer is a crucial component of the OSI model, providing the necessary services for end-to-end communication between applications.