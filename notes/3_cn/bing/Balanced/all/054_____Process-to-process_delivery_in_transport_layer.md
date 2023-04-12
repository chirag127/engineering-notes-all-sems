### Process-to-process delivery in transport layer

- The transport layer is responsible for delivering data from one process to another process on different hosts.
- A process is an entity of the application layer that uses the services of the transport layer.
- The transport layer uses the host-to-host delivery service of the network layer to send data between hosts, and then adds its own functionality to enable process-to-process delivery.
- The transport layer uses two methods to identify the processes on the source and destination hosts: port numbers and socket addresses.

#### Port numbers
- A port number is a 16-bit integer that identifies a specific process on a host.
- The port numbers are divided into three ranges: well-known ports (0 to 1023), registered ports (1024 to 49151), and dynamic or private ports (49152 to 65535).
- Well-known ports are assigned by the Internet Assigned Numbers Authority (IANA) to standard services, such as HTTP (80), FTP (21), and Telnet (23).
- Registered ports are assigned by IANA to user applications, such as email clients, web browsers, and chat applications.
- Dynamic or private ports are used by processes that need temporary communication, such as client processes that initiate a connection to a server.

#### Socket addresses
- A socket address is a combination of an IP address and a port number that uniquely identifies a process on a host.
- A socket address is written as IP address:port number, such as 192.168.1.1:80.
- The transport layer uses the socket address to deliver data to the correct process on the destination host.

#### Process-to-process delivery example
- Suppose a web browser on host A wants to request a web page from a web server on host B.
- The web browser is a client process that uses a dynamic port number, such as 5000, to communicate with the web server.
- The web server is a server process that uses a well-known port number, such as 80, to listen for incoming requests.
- The web browser creates a socket address by combining its own IP address and port number, such as 192.168.1.1:5000.
- The web browser also creates a socket address for the web server by combining its IP address and port number, such as 192.168.1.2:80.
- The web browser sends a request to the web server using the socket addresses as the source and destination addresses.
- The transport layer on host A adds the socket addresses to the data and passes it to the network layer.
- The network layer on host A adds the IP addresses to the data and passes it to the data link layer.
- The data link layer on host A adds the MAC addresses to the data and sends it over the link to host B.
- The data link layer on host B removes the MAC addresses and passes the data to the network layer.
- The network layer on host B removes the IP addresses and passes the data to the transport layer.
- The transport layer on host B checks the destination socket address and delivers the data to the web server process on port 80.
- The web server process sends a response to the web browser using the same socket addresses as the source and destination addresses.
- The transport layer on host B adds the socket addresses to the data and passes it to the network layer.
- The network layer on host B adds the IP addresses to the data and passes it to the data link layer.
- The data link layer on host B adds the MAC addresses to the data and sends it over the link to host A.
- The data link layer on host A removes the MAC addresses and passes the data to the network layer.
- The network layer on host A removes the IP addresses and passes the data to the transport layer.
- The transport layer on host A checks the destination socket address and delivers the data to the web browser process on port 5000.

#### ASCII diagram of process-to-process delivery

```
+----------------+      +----------------+
| Web browser    |      | Web server     |
| Port: 5000     |      | Port: 80       |
+----------------+      +----------------+
| Transport layer|      | Transport layer|
| Socket address |      | Socket address |
| 192.168.1.1:5000|     | 192.168.1.2:80 |
+----------------+      +----------------+
| Network layer  |      | Network layer  |
| IP address     |      | IP address     |
| 192.168.1.1    |      | 192.168.1

```
