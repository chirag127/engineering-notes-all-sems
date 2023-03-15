## Unit 4 - Transport Layer in Computer Networks

- The transport layer is a conceptual division of methods in the layered architecture of protocols in the network stack in the Internet protocol suite and the OSI model.
- The protocols of this layer provide end-to-end communication services for applications.
- The transport layer takes data from the application layer and then breaks it into smaller size segments, numbers each byte, and hands over to the network layer for delivery.
- The transport layer also reassembles the segments at the destination and delivers them to the application layer.
- The transport layer is responsible for the following functions   :
  - **Addressing**: The transport layer provides the user address which is specified as a station or port. The port variable represents a specific process running on a host. The transport layer protocols need to know the port number of the application layer protocol to deliver the data to the correct process.
  - **Multiplexing and Demultiplexing**: The transport layer can multiplex multiple application layer processes on a single host by using different port numbers for each process. Similarly, the transport layer can demultiplex the incoming segments from the network layer by using the port numbers in the header and deliver them to the appropriate application layer process.
  - **Reliable Delivery**: The transport layer ensures the reliable arrival of messages across a network and provides error-checking mechanisms and data flow controls. The transport layer can detect and correct errors, retransmit lost or corrupted segments, and acknowledge the received segments. The transport layer can also use sequence numbers and timers to ensure the correct order and timing of the segments.
  - **Flow Control**: The transport layer can regulate the amount of data that a sender can transmit to a receiver, to avoid overwhelming the receiver or the network. The transport layer can use techniques such as sliding window, stop-and-wait, or backpressure to control the flow of data.
  - **Congestion Control**: The transport layer can monitor the network conditions and adjust the rate of data transmission to avoid congestion and packet loss. The transport layer can use techniques such as additive increase multiplicative decrease (AIMD), slow start, congestion avoidance, or congestion recovery to control the congestion.
  - **Quality of Service**: The transport layer can provide different levels of service to different applications, depending on their requirements. The transport layer can use parameters such as bandwidth, delay, jitter, or reliability to specify the quality of service. The transport layer can also use techniques such as reservation, prioritization, or differentiation to allocate the network resources accordingly.
- The transport layer can be classified into two types of protocols: connection-oriented and connectionless.
  - **Connection-oriented protocols**: These protocols establish a logical connection between the sender and the receiver before transmitting the data. The connection-oriented protocols provide reliable, ordered, and error-free delivery of data. The connection-oriented protocols use a three-way handshake to establish and terminate the connection. An example of a connection-oriented protocol is the Transmission Control Protocol (TCP).
  - **Connectionless protocols**: These protocols do not establish a logical connection between the sender and the receiver before transmitting the data. The connectionless protocols provide fast, unordered, and unreliable delivery of data. The connectionless protocols do not use any handshake or acknowledgment mechanism. An example of a connectionless protocol is the User Datagram Protocol (UDP).
- The transport layer can be represented by the following diagram:

```
+-----------------+-----------------+-----------------+
| Application     | Application     | Application     |
| Layer           | Layer           | Layer           |
+-----------------+-----------------+-----------------+
| Transport       | Transport       | Transport       |
| Layer           | Layer           | Layer           |
+-----------------+-----------------+-----------------+
| Network         | Network         | Network         |
| Layer           | Layer           | Layer           |
+-----------------+-----------------+-----------------+
| Data Link       | Data Link       | Data Link       |
| Layer           | Layer           | Layer           |
+-----------------+-----------------+-----------------+
| Physical        | Physical        | Physical        |
| Layer           | Layer           | Layer           |
+-----------------+-----------------+-----------------+
```

- The transport layer can be studied by using the following mnemonics and learning tricks:
  - To remember the functions of the transport layer, use the acronym **ARM F