#### Goals and applications of networks and protocols

A network consists of two or more nodes (e.g. computers) that are linked in order to share resources (such as printers and CDs), exchange files, or allow electronic communications. The computers on a network may be linked through cables, telephone lines, radio waves, satellites, or infrared light beams. 

The main goals of a network are :

- Cost reduction by sharing hardware and software resources
- High reliability by having multiple sources of supply
- Greater flexibility because of the possibility to connect devices
- Increased productivity by making it easier to access data by several users
- Enhanced performance by adding more processors as the workload increases
- Powerful communication medium for various purposes

Some of the applications of networks in different fields are :

- Marketing and sales
- Financial services
- Manufacturing (e.g. CAD, CAM, etc.)
- Information services
- Cellular telephone
- Cable television
- Teleconferencing
- Electronic data interchange (EDI)
- E-mail, etc.

The following diagram illustrates the basic architecture of a network using the TCP/IP protocol suite, which is the most widely used protocol for internet communication. TCP/IP stands for Transmission Control Protocol/Internet Protocol, and it consists of four layers: application, transport, internet, and network access. Each layer has a specific function and communicates with the adjacent layers through interfaces.

```
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|   Application   |   Application   |   Application   |   Application   |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|    Transport    |    Transport    |    Transport    |    Transport    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|    Internet     |    Internet     |    Internet     |    Internet     |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
| Network Access  | Network Access  | Network Access  | Network Access  |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|    Physical     |    Physical     |    Physical     |    Physical     |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|    Node A       |    Node B       |    Node C       |    Node D       |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
```

The application layer provides the interface for the user applications to access the network services, such as e-mail, web browsing, file transfer, etc. The transport layer provides end-to-end communication between the source and destination nodes, and ensures reliable and ordered delivery of data packets. The internet layer handles the routing of data packets across different networks, and assigns unique addresses to each node. The network access layer defines the physical and data link protocols for the transmission medium, such as Ethernet, Wi-Fi, etc. The physical layer deals with the actual transmission of bits over the medium.