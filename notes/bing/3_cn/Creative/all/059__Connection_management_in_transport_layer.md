### Connection management in transport layer

- Connection management is the process of establishing, maintaining, and terminating a logical connection between two or more end points in a network.
- Connection management is one of the responsibilities of the transport layer, which provides end-to-end communication services for applications.
- Connection management can be classified into two types: connection-oriented and connectionless.
- Connection-oriented connection management requires the establishment of a connection before any data can be exchanged, and the termination of the connection after the data transfer is completed. Connection-oriented connection management ensures reliable, ordered, and error-free delivery of data, but it also introduces overhead and delay in the communication.
- Connectionless connection management does not require the establishment or termination of a connection, and data can be exchanged at any time without any prior agreement. Connectionless connection management is faster and more efficient, but it does not guarantee reliable, ordered, or error-free delivery of data.
- The most common protocols used for connection management in the transport layer are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
- TCP is a connection-oriented protocol that uses a three-way handshake to establish a connection, and a four-way handshake to terminate a connection. TCP also uses sequence numbers, acknowledgments, timers, and retransmission mechanisms to ensure reliable data transfer. TCP is used for applications that require high reliability and accuracy, such as web browsing, email, file transfer, etc.
- UDP is a connectionless protocol that does not use any handshake or termination procedures, and does not provide any reliability or error control mechanisms. UDP simply sends datagrams to the destination without any guarantee of delivery, order, or integrity. UDP is used for applications that require low latency and high efficiency, such as video streaming, voice over IP, online gaming, etc.

- A possible mnemonic to remember the difference between TCP and UDP is:

  - TCP: Trustworthy, Careful, and Polite
  - UDP: Unreliable, Daring, and Pragmatic

- A possible ascii diagram to illustrate the connection management in TCP is:

```
Client                          Server
  |                              |
  |  SYN (seq=x)                 |
  |--------------------------->  |
  |                              |
  |  SYN-ACK (seq=y, ack=x+1)    |
  |  <---------------------------|
  |                              |
  |  ACK (seq=x+1, ack=y+1)      |
  |--------------------------->  |
  |                              |
  |  Connection established      |
  |<============================>|
  |                              |
  |  Data transfer               |
  |<============================>|
  |                              |
  |  FIN (seq=z, ack=w)          |
  |--------------------------->  |
  |                              |
  |  ACK (seq=w+1, ack=z+1)      |
  |  <---------------------------|
  |                              |
  |  FIN (seq=v, ack=z+1)        |
  |  <---------------------------|
  |                              |
  |  ACK (seq=z+1, ack=v+1)      |
  |--------------------------->  |
  |                              |
  |  Connection terminated       |
  |                              |
```