### Multiplexing in transport layer

- Multiplexing is the process of combining multiple data streams from different sources into one single stream for transmission over a shared medium.
- Multiplexing in transport layer is done by using port numbers to identify different applications or processes that send or receive data over the network.
- Port numbers are 16-bit integers that range from 0 to 65535. They are divided into three categories: well-known ports (0-1023), registered ports (1024-49151), and dynamic or private ports (49152-65535).
- Well-known ports are assigned by the Internet Assigned Numbers Authority (IANA) to standard protocols or services, such as HTTP (80), FTP (21), SSH (22), etc.
- Registered ports are allocated by IANA to specific applications or organizations, such as Skype (49175), Minecraft (25565), etc.
- Dynamic or private ports are used by applications or processes that do not need a fixed port number, such as ephemeral ports for temporary connections or client ports for initiating connections.
- Multiplexing in transport layer allows multiple applications or processes to share the same network interface and IP address, without interfering with each other's data.
- Multiplexing in transport layer also enables communication between different hosts on the network, by using the combination of IP address and port number to uniquely identify each end point of a connection.
- Multiplexing in transport layer is performed by the transport layer protocols, such as TCP or UDP, which add a header to each data segment that contains the source and destination port numbers, along with other information.
- Multiplexing in transport layer is illustrated by the following diagram:

```
    +-----------------+      +-----------------+
    | Application 1   |      | Application 1   |
    | Port: 5000      |      | Port: 5000      |
    +-----------------+      +-----------------+
    | Application 2   |      | Application 2   |
    | Port: 6000      |      | Port: 6000      |
    +-----------------+      +-----------------+
    | Application 3   |      | Application 3   |
    | Port: 7000      |      | Port: 7000      |
    +-----------------+      +-----------------+
    | Transport layer |      | Transport layer |
    | Port: 80        |      | Port: 80        |
    +-----------------+      +-----------------+
    | Network layer   |      | Network layer   |
    | IP: 192.168.1.1 |      | IP: 192.168.1.2 |
    +-----------------+      +-----------------+
    | Data link layer |      | Data link layer |
    | MAC: AA:BB:CC   |      | MAC: DD:EE:FF   |
    +-----------------+      +-----------------+
    | Physical layer  |      | Physical layer  |
    | Medium: Ethernet|<---->| Medium: Ethernet|
    +-----------------+      +-----------------+
```

- In this example, three applications are running on each host, using different port numbers. The transport layer protocol (TCP or UDP) adds a header to each data segment that contains the port number of the application that sent or received the data. The network layer protocol (IP) adds a header to each data segment that contains the IP address of the source and destination hosts. The data link layer protocol (Ethernet) adds a header and a trailer to each data segment that contains the MAC address of the source and destination hosts. The physical layer transmits the data segments over the shared medium (Ethernet cable).
- Multiplexing in transport layer allows the hosts to communicate with each other, by using the combination of IP address and port number to identify each end point of a connection. For example, if application 1 on host 192.168.1.1 wants to send data to application 2 on host 192.168.1.2, it will use the following address: 192.168.1.2:6000. Similarly, if application 3 on host 192.168.1.2 wants to send data to application 1 on host 192.168.1.1, it will use the following address: 192.168.1.1:5000. The transport layer protocol will use these addresses to multiplex and demultiplex the data segments accordingly.