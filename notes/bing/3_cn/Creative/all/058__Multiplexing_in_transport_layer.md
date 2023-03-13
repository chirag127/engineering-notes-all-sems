### Multiplexing in transport layer

- Multiplexing is the process of combining multiple data streams from different sources into a single data stream for transmission over a shared medium.
- Multiplexing in transport layer is done by using port numbers to identify the source and destination applications of each data stream.
- Port numbers are 16-bit integers that range from 0 to 65535. They are divided into three categories: well-known ports (0-1023), registered ports (1024-49151), and dynamic or private ports (49152-65535).
- Well-known ports are assigned by the Internet Assigned Numbers Authority (IANA) to standard protocols and services, such as HTTP (80), FTP (21), and SSH (22).
- Registered ports are allocated by IANA to specific applications or organizations, such as Skype (49175), Minecraft (25565), and Apache Tomcat (8080).
- Dynamic or private ports are used by applications for temporary or ephemeral communication, such as web browsers and email clients. They are randomly chosen by the operating system from the available range.
- Multiplexing in transport layer allows multiple applications to share the same network interface and IP address, without interfering with each other's data.
- Multiplexing in transport layer also enables end-to-end communication between applications across different hosts, by using a combination of IP address and port number to uniquely identify each data stream.
- Multiplexing in transport layer is supported by both TCP and UDP protocols, but they use different methods to perform it.
- TCP multiplexing is based on the concept of a socket, which is a combination of an IP address, a port number, and a protocol. A socket uniquely identifies an endpoint of a TCP connection. TCP uses a four-tuple of (source IP, source port, destination IP, destination port) to multiplex and demultiplex data streams.
- UDP multiplexing is based on the concept of a datagram, which is a self-contained unit of data that contains an IP header, a UDP header, and a payload. A datagram does not establish a connection or maintain a state with the destination. UDP uses a two-tuple of (destination IP, destination port) to multiplex and demultiplex data streams.

A simple ASCII diagram to illustrate multiplexing in transport layer is:

```
    Host A                          Host B
+------------+                  +------------+
| Application|                  | Application|
+------------+                  +------------+
|    Port    |                  |    Port    |
+------------+                  +------------+
|   TCP/UDP  |                  |   TCP/UDP  |
+------------+                  +------------+
|    IP      |                  |    IP      |
+------------+                  +------------+
|  Network   |------------------|  Network   |
+------------+                  +------------+
```

Some mnemonics and learning tricks for multiplexing in transport layer are:

- Remember that multiplexing is like a **multi**-tasking **plex** movie theater, where different movies are shown on different screens to different audiences.
- Remember that port numbers are like **door** numbers of different rooms in a building, where different applications are running in different rooms.
- Remember that well-known ports are like **well-known** celebrities, who have fixed and famous names or numbers, such as Tom Cruise (80) or Brad Pitt (21).
- Remember that registered ports are like **registered** trademarks, who have specific and official names or numbers, such as Nike (49175) or Lego (25565).
- Remember that dynamic or private ports are like **dynamic** or **private** individuals, who have random and temporary names or numbers, such as Alice (54321) or Bob (12345).
- Remember that TCP multiplexing is like a **TCP**hone call, where you need to dial a four-digit number (source IP, source port, destination IP, destination port) to connect to another person.
- Remember that UDP multiplexing is like a **UD**eliver**P**izza service, where you only need to give a two-digit number (destination IP, destination port) to send a pizza to another person.