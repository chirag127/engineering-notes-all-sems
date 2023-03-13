#### TCP Transport layer protocol

- TCP stands for Transmission Control Protocol  .
- It is a transport layer protocol that facilitates the transmission of packets from source to destination   .
- It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network  .
- TCP is a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data  .
- TCP provides reliable, ordered, and error-checked delivery of a stream of octets between applications running on hosts communicating via an IP network.
- TCP has three main steps: establish connection, send packets of data, and close the connection.
  - Establish connection: When two computers want to send data to each other over TCP, they first need to establish a connection using a three-way handshake .
  - Send packets of data: When a packet of data is sent over TCP, the recipient must always acknowledge what they received. If the sender does not receive an acknowledgment within a certain time, it will resend the packet. This ensures that no data is lost or corrupted .
  - Close the connection: When the data transmission is complete, the sender and the receiver exchange messages to terminate the connection gracefully .
- TCP is used by many applications that require reliable and ordered delivery of data, such as web browsing, email, file transfer, and remote login .