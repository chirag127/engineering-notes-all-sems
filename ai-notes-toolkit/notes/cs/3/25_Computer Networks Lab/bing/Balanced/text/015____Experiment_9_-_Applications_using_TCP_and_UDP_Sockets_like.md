## Experiment 9 - Applications using TCP and UDP Sockets

- TCP and UDP are two protocols that provide reliable and unreliable data transmission over the Internet Protocol (IP) network.
- TCP stands for Transmission Control Protocol and it guarantees that the data sent by one end is received by the other end in the same order and without any loss or corruption.
- UDP stands for User Datagram Protocol and it does not guarantee any reliability or ordering of the data. It is faster and more efficient than TCP for some applications that do not require reliability.
- Sockets are the endpoints of a bidirectional communication channel between two processes running on different machines over a network.
- A socket is identified by a combination of an IP address and a port number. An IP address is a unique identifier for a machine on the network and a port number is a logical identifier for a specific process or service on that machine.
- A socket can be either a TCP socket or a UDP socket, depending on the protocol used for data transmission.
- Some common applications that use TCP and UDP sockets are:

  - Web browsers and web servers use TCP sockets to exchange HTTP requests and responses over the World Wide Web.
  - Email clients and servers use TCP sockets to send and receive emails using SMTP, POP3 or IMAP protocols.
  - File transfer applications use TCP sockets to transfer files between machines using FTP or SCP protocols.
  - Streaming media applications use UDP sockets to deliver audio and video data over the Internet using RTP or RTSP protocols.
  - Online games use UDP sockets to exchange real-time information between players using custom protocols.
  - Voice over IP applications use UDP sockets to transmit voice data over the Internet using SIP or H.323 protocols.