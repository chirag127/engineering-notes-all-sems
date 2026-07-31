## Experiment 9 - Applications using TCP and UDP Sockets

- A socket is an endpoint of communication between two processes or devices over a network.
- A socket is identified by a combination of an IP address and a port number.
- A port is a logical number that identifies a specific application or service on a device.
- There are two types of sockets: stream sockets and datagram sockets.
- Stream sockets use TCP (Transmission Control Protocol), which is a reliable, stream-oriented protocol that ensures that all data is delivered in order and without errors.
- Datagram sockets use UDP (User Datagram Protocol), which is an unreliable, message-oriented protocol that does not guarantee delivery, order, or error detection.
- TCP and UDP are both protocols that operate on top of the IP protocol, which is responsible for routing packets across the Internet.
- TCP and UDP sockets can use the same port number, but they are not related to each other. TCP ports are interpreted by the TCP stack, while the UDP stack interprets UDP ports.
- TCP and UDP sockets have different characteristics and applications, depending on the requirements of the communication.
- TCP sockets are suitable for applications that need reliable and ordered data transfer, such as web browsing, file transfer, email, etc.
- UDP sockets are suitable for applications that need fast and lightweight data transfer, such as video streaming, online gaming, voice over IP, etc.

Some examples of applications using TCP and UDP sockets are:

- A web browser uses a TCP socket to connect to a web server and request a web page. The web server uses another TCP socket to send the web page back to the browser.
- A video conferencing application uses a UDP socket to send and receive audio and video data between the participants. The UDP socket allows for low latency and high bandwidth communication, but some packets may be lost or out of order.
- A chat application uses a TCP socket to establish a connection between the sender and the receiver, and then uses another TCP socket to send and receive text messages. The TCP socket ensures that the messages are delivered reliably and in order.
- A DNS (Domain Name System) client uses a UDP socket to send a query to a DNS server, asking for the IP address of a domain name. The DNS server uses another UDP socket to send the response back to the client. The UDP socket allows for fast and simple communication, but the query or the response may be lost or corrupted.