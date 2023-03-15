#### protocols and standards in networks architecture in Computer Networks

- Network protocols are the rules and procedures that define how devices communicate and exchange data over a network .
- Network standards are the specifications and guidelines that ensure compatibility and interoperability among different network devices, systems, and applications .
- Network architecture is the design and structure of a network, including its components, protocols, standards, and topology.
- Some of the common network protocols and standards are:

  - TCP/IP: Transmission Control Protocol/Internet Protocol is the most widely used protocol suite that provides end-to-end data transmission and addressing over the Internet and other networks .
  - UDP: User Datagram Protocol is a connectionless protocol that provides fast and unreliable data delivery over the Internet and other networks .
  - ARP: Address Resolution Protocol is a protocol that maps network layer addresses (such as IP addresses) to data link layer addresses (such as MAC addresses) on a local area network (LAN) .
  - DHCP: Dynamic Host Configuration Protocol is a protocol that assigns network configuration parameters (such as IP addresses, subnet masks, and default gateways) to devices on a network dynamically .
  - FTP: File Transfer Protocol is a protocol that allows users to transfer files between devices over a network .
  - DNS: Domain Name System is a protocol that translates domain names (such as www.google.com) to IP addresses (such as 172.217.14.206) on the Internet and other networks .
  - HTTP: Hypertext Transfer Protocol is a protocol that defines how web browsers and web servers communicate and exchange web pages and other resources over the Internet and other networks .
  - SMTP: Simple Mail Transfer Protocol is a protocol that defines how email messages are sent and received over the Internet and other networks .
  - IEEE 802: A family of standards that define various aspects of data link layer and physical layer protocols for different types of networks, such as Ethernet, Wi-Fi, Bluetooth, and ZigBee.
  - OSI: Open Systems Interconnection is a reference model that defines seven layers of network protocols and functions, from the physical layer to the application layer.

- A mnemonic to remember the seven layers of the OSI model is: **Please Do Not Throw Sausage Pizza Away**.

  - Physical layer: deals with the transmission and reception of raw bits over a physical medium, such as cables, wires, or radio waves.
  - Data link layer: deals with the framing, error detection, and flow control of data packets over a physical medium, such as Ethernet or Wi-Fi.
  - Network layer: deals with the routing, addressing, and fragmentation of data packets over a network, such as IP or ICMP.
  - Transport layer: deals with the end-to-end delivery, reliability, and congestion control of data segments over a network, such as TCP or UDP.
  - Session layer: deals with the establishment, maintenance, and termination of sessions between applications over a network, such as RPC or SSL.
  - Presentation layer: deals with the representation, encryption, and compression of data between applications over a network, such as ASCII or JPEG.
  - Application layer: deals with the user interface, functionality, and protocols of applications over a network, such as HTTP or FTP.

- An example of network architecture is the client/server model, where one or more devices (clients) request and receive services from another device (server) over a network.

  - A client is a device that initiates a communication and requests a service from a server, such as a web browser or an email client.
  - A server is a device that responds to a communication and provides a service to a client, such as a web server or an email server.
  - A network is a collection of devices that are connected by communication links and protocols, such as the Internet or a LAN.
  - A client/server network architecture can be illustrated as follows:

```
    +--------+        +--------+        +--------+
    | Client | <----> | Server | <----> | Client |
    +--------+        +--------+        +--------+
          ^                ^                ^
          |                |                |
          |                |                |
          v                v