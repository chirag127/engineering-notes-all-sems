## Experiment 9 - Applications using TCP and UDP Sockets

TCP and UDP are two protocols that are used for sending data over the Internet. They are both part of the transport layer, which is responsible for establishing connections and ensuring reliable data transfer. TCP and UDP have different characteristics and are suitable for different types of applications.

### TCP Sockets

TCP stands for Transmission Control Protocol. It is a connection-oriented protocol, which means that it establishes a connection between two endpoints before sending data. TCP ensures that the data is delivered reliably, in order, and without errors. TCP also provides flow control and congestion control mechanisms to avoid overloading the network or the receiver.

A TCP socket is an endpoint of a TCP connection. It is identified by a combination of an IP address and a port number. A TCP socket can only communicate with the socket that it is connected to. To create a TCP connection, a client socket initiates a three-way handshake with a server socket, which is listening for incoming connections. The three-way handshake involves sending and acknowledging SYN, SYN-ACK, and ACK packets. Once the connection is established, the sockets can exchange data using send and receive functions. To terminate the connection, the sockets use a four-way handshake, which involves sending and acknowledging FIN and ACK packets.

Some examples of applications that use TCP sockets are:

- Web browsers and web servers, which use HTTP over TCP to exchange web pages and files.
- Email clients and servers, which use SMTP over TCP to send and receive emails.
- File transfer clients and servers, which use FTP over TCP to upload and download files.
- Remote login clients and servers, which use SSH or Telnet over TCP to execute commands on remote machines.

### UDP Sockets

UDP stands for User Datagram Protocol. It is a connectionless protocol, which means that it does not establish a connection before sending data. UDP does not guarantee that the data is delivered reliably, in order, or without errors. UDP also does not provide flow control or congestion control mechanisms. UDP is faster and more efficient than TCP, but it may lose or reorder some packets.

A UDP socket is an endpoint of a UDP communication. It is also identified by a combination of an IP address and a port number. A UDP socket can send and receive data to and from any socket, without establishing a connection. To send data, a UDP socket simply attaches the destination IP address and port number to the data and sends it as a datagram. To receive data, a UDP socket simply listens for incoming datagrams and extracts the data from them.

Some examples of applications that use UDP sockets are:

- Voice over IP (VoIP) and video conferencing applications, which use RTP over UDP to stream audio and video data in real time.
- Online gaming applications, which use UDP to exchange fast and frequent updates of the game state.
- Domain name system (DNS) servers and clients, which use UDP to resolve domain names to IP addresses.
- Network time protocol (NTP) servers and clients, which use UDP to synchronize the clocks of different machines.