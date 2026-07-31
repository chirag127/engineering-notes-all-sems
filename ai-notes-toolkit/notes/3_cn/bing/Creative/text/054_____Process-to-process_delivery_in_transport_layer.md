### Process-to-process delivery in transport layer

- The transport layer is the fourth layer of the OSI model, which provides services to the application layer.
- The transport layer is responsible for process-to-process delivery, which means the delivery of a packet, part of a message, from one process to another.
- A process is an entity of the application layer that uses the services of the transport layer. Two processes can communicate in a client/server relationship.
- The transport layer uses two methods to identify the processes: port numbers and service access points (SAPs).
- A port number is a 16-bit number that uniquely identifies a process on a host. There are two types of port numbers: well-known ports and registered ports.
- A well-known port is a port number assigned to a common service, such as HTTP (80), FTP (21), or Telnet (23). These port numbers are standardized by the Internet Assigned Numbers Authority (IANA).
- A registered port is a port number assigned to a specific service or application by the IANA upon request. These port numbers range from 1024 to 49151.
- A service access point (SAP) is a logical address that identifies a process on a host. A SAP consists of a network address and a port number. For example, a SAP for a web server on a host with IP address 192.168.1.10 and port number 80 is 192.168.1.10:80.
- The transport layer uses two protocols to provide process-to-process delivery: TCP and UDP.
- TCP (Transmission Control Protocol) is a connection-oriented, reliable, and full-duplex protocol that provides error control, flow control, and congestion control. TCP establishes a logical connection between two processes before exchanging data, and ensures that the data is delivered in the same order and without errors.
- UDP (User Datagram Protocol) is a connectionless, unreliable, and simplex protocol that provides no error control, flow control, or congestion control. UDP does not establish a connection between two processes, and does not guarantee the delivery, order, or integrity of the data. UDP is used for applications that require speed and efficiency, such as streaming media or online gaming.