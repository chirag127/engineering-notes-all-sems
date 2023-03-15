#### TCP/IP protocol suite in computer networks

- TCP/IP stands for Transmission Control Protocol/Internet Protocol and is a suite of communication protocols used to interconnect network devices on the internet or a private network .
- TCP/IP is also known as the internet protocol suite, as it defines the standards and rules for data transmission over the internet .
- TCP/IP consists of four layers: application, transport, internet, and network interface .
- The application layer provides the interface for the user or the application to access the network services, such as email, web browsing, file transfer, etc. Some of the common protocols in this layer are HTTP, SMTP, FTP, DNS, etc .
- The transport layer provides the end-to-end data delivery between the source and the destination hosts, by ensuring reliable, ordered, and error-free transmission. The two main protocols in this layer are TCP and UDP .
- TCP (Transmission Control Protocol) is a connection-oriented protocol that establishes a logical connection between the sender and the receiver, and uses sequence numbers, acknowledgements, and retransmissions to ensure reliable data transfer .
- UDP (User Datagram Protocol) is a connectionless protocol that does not guarantee reliable data delivery, but is faster and more efficient than TCP. UDP is suitable for real-time applications, such as video streaming, voice over IP, etc .
- The internet layer is responsible for the routing and forwarding of packets across different networks, by using the IP (Internet Protocol) address of the source and the destination hosts. The IP address is a unique identifier for each host on the internet, and is usually written in dotted decimal notation, such as 192.168.1.1 .
- The IP (Internet Protocol) is the core protocol of the internet layer, and defines the format and structure of the packets, as well as the rules for addressing and fragmenting them. The current version of IP is IPv4, which uses 32-bit addresses, but a newer version, IPv6, which uses 128-bit addresses, is being deployed to overcome the address space limitation .
- The network interface layer is the lowest layer of the TCP/IP suite, and interacts with the physical network devices, such as the network interface card (NIC), the cable, the hub, the switch, etc. This layer is also known as the link layer or the data link layer, and handles the framing, encoding, and error detection of the data bits .
- The network interface layer can use different protocols depending on the type and topology of the network, such as Ethernet, Wi-Fi, Bluetooth, etc .

- A mnemonic to remember the four layers of the TCP/IP suite is **A** **T**ea **I**n **N**ovember, where A stands for Application, T stands for Transport, I stands for Internet, and N stands for Network interface.
- A diagram to illustrate the TCP/IP suite and its protocols is shown below:

```
+--------------------------+--------------------------+--------------------------+--------------------------+
|        Application       |        Transport         |         Internet         |     Network interface    |
+--------------------------+--------------------------+--------------------------+--------------------------+
| HTTP | SMTP | FTP | DNS  | TCP | UDP                | IP | ICMP | ARP | RARP   | Ethernet | Wi-Fi | etc.  |
+--------------------------+--------------------------+--------------------------+--------------------------+
```