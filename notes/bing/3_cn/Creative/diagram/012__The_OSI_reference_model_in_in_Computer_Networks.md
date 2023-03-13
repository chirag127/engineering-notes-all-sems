The OSI reference model is a seven-layered architecture that describes how information from a software application in one computer moves through a physical medium to the software application in another computer. Each layer performs a particular network function and communicates with the adjacent layers through interfaces .

The following diagram illustrates the basic architecture of the OSI reference model in Computer Networks using ASCII art:

```
+------------------------+ +------------------------+
| Application Layer      | | Application Layer      |
| (Layer 7)              | | (Layer 7)              |
+------------------------+ +------------------------+
| Presentation Layer     | | Presentation Layer     |
| (Layer 6)              | | (Layer 6)              |
+------------------------+ +------------------------+
| Session Layer          | | Session Layer          |
| (Layer 5)              | | (Layer 5)              |
+------------------------+ +------------------------+
| Transport Layer        | | Transport Layer        |
| (Layer 4)              | | (Layer 4)              |
+------------------------+ +------------------------+
| Network Layer          | | Network Layer          |
| (Layer 3)              | | (Layer 3)              |
+------------------------+ +------------------------+
| Data Link Layer        | | Data Link Layer        |
| (Layer 2)              | | (Layer 2)              |
+------------------------+ +------------------------+
| Physical Layer         | | Physical Layer         |
| (Layer 1)              | | (Layer 1)              |
+------------------------+ +------------------------+
|                        | |                        |
|      Computer A        | |      Computer B        |
|                        | |                        |
+------------------------+ +------------------------+
```

The layers are:

- **Application Layer (Layer 7)**: This layer provides the interface between the user application and the network. It handles high-level functions such as authentication, encryption, file transfer, email, web browsing, etc. Some examples of application layer protocols are HTTP, FTP, SMTP, POP3, etc.
- **Presentation Layer (Layer 6)**: This layer is responsible for the format and syntax of the data exchanged between the application layer and the network. It performs functions such as data compression, encryption, decryption, translation, etc. Some examples of presentation layer standards are JPEG, GIF, MPEG, SSL, etc.
- **Session Layer (Layer 5)**: This layer manages the communication sessions between the application layer entities. It establishes, maintains, and terminates the sessions. It also provides services such as synchronization, dialog control, error recovery, etc. Some examples of session layer protocols are NFS, SQL, RPC, etc.
- **Transport Layer (Layer 4)**: This layer provides reliable and efficient data transfer between the network layer and the application layer. It performs functions such as segmentation, reassembly, error detection, error correction, flow control, congestion control, etc. Some examples of transport layer protocols are TCP, UDP, SCTP, etc.
- **Network Layer (Layer 3)**: This layer is responsible for the routing and forwarding of data packets across the network. It performs functions such as addressing, routing, fragmentation, reassembly, etc. Some examples of network layer protocols are IP, ICMP, ARP, RIP, OSPF, etc.
- **Data Link Layer (Layer 2)**: This layer provides the physical transmission of data frames between the network layer and the physical layer. It performs functions such as framing, error detection, error correction, medium access control, etc. Some examples of data link layer protocols are Ethernet, Wi-Fi, PPP, HDLC, etc.
- **Physical Layer (Layer 1)**: This layer is responsible for the physical characteristics of the transmission medium. It performs functions such as modulation, demodulation, encoding, decoding, signaling, etc. Some examples of physical layer standards are RS-232, USB, Bluetooth, etc.