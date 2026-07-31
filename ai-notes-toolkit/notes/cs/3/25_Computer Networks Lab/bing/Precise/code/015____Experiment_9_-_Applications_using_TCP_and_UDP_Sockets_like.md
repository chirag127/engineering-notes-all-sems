## Experiment 9 - Applications using TCP and UDP Sockets

TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two of the core protocols in the Internet Protocol Suite. Both protocols are used to send data over the internet, but they have different characteristics and use cases.

1. **TCP** is a connection-oriented protocol, which means that it establishes a connection between the sender and receiver before transmitting data. This connection ensures that data is transmitted reliably and in the correct order. TCP is used by applications that require reliable data transmission, such as web browsing, email, and file transfers.

2. **UDP** is a connectionless protocol, which means that it does not establish a connection before transmitting data. Instead, it sends data in individual packets, called datagrams, without checking if they are received correctly or in the correct order. UDP is used by applications that require fast data transmission and can tolerate some data loss, such as online gaming, video streaming, and voice over IP (VoIP).

Some common applications that use TCP and UDP sockets include:

- **Web browsing:** Web browsers use TCP to establish a connection to a web server and request web pages.

- **Email:** Email clients use TCP to send and receive emails from an email server.

- **File transfers:** File transfer protocols such as FTP and SFTP use TCP to reliably transfer files between computers.

- **Online gaming:** Online games often use UDP to send fast, real-time updates between players.

- **Video streaming:** Video streaming services such as YouTube and Netflix use UDP to quickly transmit video data.

- **Voice over IP (VoIP):** VoIP applications such as Skype and WhatsApp use UDP to transmit voice data in real-time.

In summary, TCP and UDP are two core protocols in the Internet Protocol Suite, used by various applications to transmit data over the internet. TCP is used by applications that require reliable data transmission, while UDP is used by applications that require fast data transmission and can tolerate some data loss. Some common applications that use TCP and UDP sockets include web browsing, email, file transfers, online gaming, video streaming, and VoIP.