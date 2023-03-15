# Experiment 9 - Applications using TCP and UDP Sockets

## Introduction

TCP and UDP are two of the most common transport layer protocols used for sending and receiving data over the Internet. They are both based on the IP protocol, which provides the basic mechanism for delivering packets from one node to another. However, they have different characteristics and features that make them suitable for different types of applications.

## TCP Sockets

TCP stands for Transmission Control Protocol. It is a connection-oriented protocol, which means that it establishes a reliable and ordered communication channel between two nodes before exchanging data. TCP sockets are the endpoints of a TCP connection, identified by a combination of IP address and port number. A TCP socket can only send and receive data to and from the remote node that it is connected to.

Some of the features of TCP sockets are:

- They use a three-way handshake to establish a connection, which involves sending and acknowledging SYN, SYN-ACK, and ACK packets.
- They use sequence numbers and acknowledgments to ensure that all data is delivered correctly and in order.
- They use flow control and congestion control mechanisms to adjust the sending rate and window size according to the network conditions.
- They use a four-way handshake to terminate a connection, which involves sending and acknowledging FIN, FIN-ACK, ACK, and RST packets.

Some of the applications that use TCP sockets are:

- Web browsers and servers, which use HTTP over TCP to exchange web pages and other resources.
- Email clients and servers, which use SMTP over TCP to send and receive emails.
- File transfer clients and servers, which use FTP over TCP to upload and download files.
- Remote login clients and servers, which use SSH or Telnet over TCP to execute commands on remote machines.

## UDP Sockets

UDP stands for User Datagram Protocol. It is a connectionless protocol, which means that it does not establish or maintain a communication channel between two nodes. UDP sockets are the endpoints of a UDP communication, identified by a combination of IP address and port number. A UDP socket can send and receive data to and from any node at any time with the same socket.

Some of the features of UDP sockets are:

- They do not use any handshake to establish or terminate a communication, which makes them faster and simpler than TCP sockets.
- They do not use any sequence numbers or acknowledgments to ensure that data is delivered correctly and in order. They rely on the application layer to handle any errors or losses.
- They do not use any flow control or congestion control mechanisms to adjust the sending rate or window size. They send data as fast as possible, regardless of the network conditions.
- They do not guarantee any ordering or reliability of data. They may deliver data out of order, duplicate, or drop data.

Some of the applications that use UDP sockets are:

- Streaming media clients and servers, which use RTP over UDP to transmit audio and video data in real time.
- Online gaming clients and servers, which use UDP to exchange game state and events with low latency and high responsiveness.
- Voice over IP clients and servers, which use SIP over UDP to establish and manage voice calls over the Internet.
- Domain name system clients and servers, which use DNS over UDP to resolve domain names to IP addresses.