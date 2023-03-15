## Experiment 9 - Applications using TCP and UDP Sockets

TCP and UDP are two protocols that are used to send and receive data over the internet. They are part of the transport layer of the internet protocol suite, which provides end-to-end communication between applications. TCP and UDP have different characteristics and use cases, depending on the requirements of the applications.

### TCP (Transmission Control Protocol)

TCP is a connection-oriented protocol, which means that it establishes a reliable and ordered communication channel between two endpoints before sending any data. TCP uses a three-way handshake to create a connection, and a four-way handshake to terminate it. TCP also provides mechanisms for error detection, congestion control, and flow control, to ensure that the data is delivered correctly and efficiently.

Some of the applications that use TCP are:

- Web browsers and servers, which use HTTP (Hypertext Transfer Protocol) to exchange web pages and files.
- Email clients and servers, which use SMTP (Simple Mail Transfer Protocol) to send and receive emails.
- File transfer applications, which use FTP (File Transfer Protocol) or SCP (Secure Copy Protocol) to upload and download files.
- Remote login applications, which use SSH (Secure Shell) or Telnet to access remote computers.
- Streaming media applications, which use RTSP (Real Time Streaming Protocol) to control the playback of audio and video.

### UDP (User Datagram Protocol)

UDP is a connectionless protocol, which means that it does not establish or maintain any connection between the endpoints. UDP simply sends datagrams, which are packets of data, without any guarantee of delivery, order, or error correction. UDP is faster and more efficient than TCP, but it also has more risks of data loss, duplication, or corruption.

Some of the applications that use UDP are:

- Domain name system (DNS), which resolves domain names to IP addresses.
- Dynamic host configuration protocol (DHCP), which assigns IP addresses to devices on a network.
- Network time protocol (NTP), which synchronizes the clocks of devices on a network.
- Voice over IP (VoIP), which transmits voice calls over the internet.
- Online gaming, which requires low latency and high responsiveness.

### Sockets

Sockets are the endpoints of a communication channel between two applications. Sockets are identified by a combination of an IP address and a port number, which specify the source and destination of the data. Sockets can be either TCP or UDP, depending on the protocol used by the applications.

Sockets are used by applications to send and receive data over the network. Sockets can be either blocking or non-blocking, depending on how they handle the data. Blocking sockets wait for the data to be available before returning, while non-blocking sockets return immediately even if the data is not ready.

Some of the functions that are used to create and manipulate sockets are:

- socket(), which creates a new socket and returns a file descriptor.
- bind(), which assigns a local address and port to a socket.
- listen(), which marks a socket as ready to accept incoming connections.
- accept(), which accepts a connection request from a remote socket and returns a new socket.
- connect(), which initiates a connection to a remote socket.
- send(), which sends data to a connected socket.
- recv(), which receives data from a connected socket.
- sendto(), which sends data to a specific socket address.
- recvfrom(), which receives data from a specific socket address.
- close(), which closes a socket and releases its resources.