### TCP/IP Server Sockets

- TCP/IP server sockets are used to create servers that listen for either local or remote client programs to connect to them on published ports.
- TCP/IP server sockets use the Transmission Control Protocol (TCP), which is a connection-oriented protocol that ensures reliable and ordered delivery of data .
- TCP/IP server sockets require three packets to set up a connection: the SYN packet, the SYN-ACK packet, and the ACK packet. This is called the three-way handshake .
- TCP/IP server sockets are defined by the IP address of the machine and the port number they use. A port is a logical endpoint that identifies a specific service or process .
- TCP/IP server sockets can accept multiple connections from different clients by creating a new socket for each connection and delegating the communication to a separate thread or process .
- TCP/IP server sockets can send and receive data over the connection using the read and write methods of the socket object .
- TCP/IP server sockets can close the connection by sending a FIN packet and waiting for an ACK packet from the client. This is called the four-way handshake .

#### Diagram

```
+-----------------+             +-----------------+
|  Server Socket  |             |  Client Socket  |
+-----------------+             +-----------------+
|                 |             |                 |
|  listen(port)   |             |                 |
|                 |             |                 |
|                 |<---SYN----->|  connect(addr)  |
|                 |             |                 |
|                 |<--SYN-ACK---|                 |
|                 |             |                 |
|                 |---ACK-----> |                 |
|                 |             |                 |
|  accept()       |             |                 |
|                 |             |                 |
|  new Socket()   |             |                 |
|                 |             |                 |
|  read/write     |<--DATA----->|  read/write     |
|                 |             |                 |
|  close()        |             |                 |
|                 |             |                 |
|                 |<---FIN----->|  close()        |
|                 |             |                 |
|                 |---ACK-----> |                 |
|                 |             |                 |
|                 |<---ACK------|                 |
|                 |             |                 |
+-----------------+             +-----------------+
```