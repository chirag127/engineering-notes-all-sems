# TCP/IP Server Sockets

- TCP/IP server sockets are used to create servers that listen for either local or remote client programs to connect to them on published ports.
- TCP/IP server sockets use the Transmission Control Protocol (TCP), which is a connection-oriented protocol that ensures reliable and ordered delivery of data .
- TCP/IP server sockets require three packets to set up a connection: the SYN packet, the SYN-ACK packet, and the ACK packet. This is called the three-way handshake .
- TCP/IP server sockets are defined by the IP address of the machine and the port it uses. A port is a 16-bit number that identifies a specific application or service on a host.
- TCP/IP server sockets use the ServerSocket class in Java, which has methods to create, bind, listen, and accept connections from client sockets .
- TCP/IP server sockets can handle multiple concurrent connections from clients by creating a new thread for each accepted connection .