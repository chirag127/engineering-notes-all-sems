 Here is the content written in markdown format on the topic #### TCP Transport layer protocol:

#### TCP Transport layer protocol

- TCP stands for Transmission Control Protocol. It is a transport layer protocol in the OSI model.
- It provides reliable, ordered, and error-checked delivery of transmitted data over IP networks.
- TCP is a connection-oriented protocol, which means it requires a logical connection to be established between two endpoints before any data is exchanged. This connection is defined by a socket and is provided through a three-way handshake process.
- The three-way handshake process:

1. SYN: The client sends a SYN request to the server to synchronize sequence numbers and establish a connection.
2. SYN-ACK: The server sends a SYN-ACK response to the client to acknowledge the SYN request and also to synchronize its own sequence number with the client's sequence number.
3. ACK: The client sends an ACK confirmation to the server to complete the handshake and establish a connection.

- Once a connection is established, TCP uses sequencing numbers to ensure that data sent from each endpoint is delivered in the same order in which it was sent. Data is also checked for errors using a cyclic redundancy check (CRC) or checksum.
- If there is data loss or corruption, TCP will retransmit the data until it is successfully delivered. This makes TCP a reliable but slower protocol compared to UDP which does not guarantee delivery or check for errors.
- Some key features of TCP are:

- Reliability: Uses sequencing numbers and retransmissions to ensure all data is delivered.
- Ordered: Data is delivered in the same order in which it was sent.
- Error-checked: CRC or checksum is used to check for data errors.
- Flow controlled: Sender will not overwhelm receiver with too much data at once.
- Congestion controlled: TCP has mechanisms to reduce transmission rate in the event of network congestion.

- Example applications that use TCP are web browsing, email, and file transfer.

[Diagrams and examples can be added here for learning aid.]