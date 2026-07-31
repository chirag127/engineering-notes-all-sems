## Unit 4 - Transport Layer in Computer Networks

The transport layer is responsible for establishing end-to-end communication between applications running on different hosts. It provides a reliable and efficient data transfer mechanism by breaking the data into smaller units called segments and ensuring that they are delivered error-free and in order.

Some important concepts related to the transport layer are:

- **Multiplexing and Demultiplexing**: The transport layer can handle multiple applications running on the same host and send their data over the network. This is achieved through multiplexing, which combines data from different applications into a single stream, and demultiplexing, which separates the data at the receiving end and delivers it to the correct application.

- **Connection-oriented versus connectionless**: Transport layer protocols can be either connection-oriented or connectionless. Connection-oriented protocols establish a logical connection between the sender and receiver before transmitting data, while connectionless protocols do not establish such a connection and simply send data to the destination.

- **Flow control**: The transport layer uses flow control mechanisms to ensure that the sender does not overwhelm the receiver with too much data. The receiver can send feedback to the sender indicating how much data it can handle at a time, and the sender adjusts its transmission accordingly.

- **Reliable data transfer**: The transport layer provides reliable data transfer by using acknowledgments and retransmissions. When a segment is sent, the sender waits for an acknowledgment from the receiver before sending the next segment. If an acknowledgment is not received within a certain time frame, the sender retransmits the segment.

- **Congestion control**: The transport layer also has mechanisms to prevent network congestion, which can occur when too much data is sent over a network that cannot handle it. Congestion control mechanisms slow down the rate of transmission when congestion is detected, and gradually increase it as the network conditions improve.

Overall, the transport layer plays a crucial role in ensuring that data is transmitted reliably and efficiently over computer networks. Understanding its concepts and mechanisms is essential for anyone working in the field of computer networking.