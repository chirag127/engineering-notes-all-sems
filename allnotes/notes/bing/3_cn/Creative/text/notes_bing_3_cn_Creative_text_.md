

# Computer Networks

- A computer network is a system that connects two or more computing devices for transmitting and sharing information.
- Computing devices include everything from a mobile phone to a server. They can be connected using physical wires such as fiber optics, but they can also be wireless .
- Computer networking refers to connected computing devices and an ever-expanding array of IoT devices (such as cameras, door locks, doorbells, refrigerators, audio/visual systems, thermostats, and various sensors) that communicate with one another.
- The main objectives of computer networking are to:
  - Facilitate communication and collaboration among users, such as email, chat, video conferencing, etc.
  - Share resources and services, such as printers, scanners, files, databases, web servers, etc.
  - Enhance security and reliability, such as encryption, authentication, backup, redundancy, etc.
  - Improve performance and efficiency, such as load balancing, caching, compression, etc.
- The main types of computer networks are:
  - Local Area Network (LAN): A network that connects devices within a small geographic area, such as a home, office, or building.
  - Wide Area Network (WAN): A network that connects devices across a large geographic area, such as a city, country, or the world.
  - Metropolitan Area Network (MAN): A network that connects devices within a metropolitan area, such as a city or a campus.
  - Personal Area Network (PAN): A network that connects devices within a personal range, such as a few meters, using wireless technologies such as Bluetooth or infrared.
  - Wireless Local Area Network (WLAN): A network that connects devices using wireless technologies such as WiFi or WiMAX within a LAN range.
  - Wireless Wide Area Network (WWAN): A network that connects devices using wireless technologies such as cellular or satellite within a WAN range.



## Unit 1 - Introductory Concepts of Computer Networks and Physical Layer

- A computer network is any group of interconnected computing devices capable of sending or receiving data.
- A computing device is not just a computer, but any device that can run a program, such as a tablet, phone, or smart sensor.
- Computer networks can be classified by their size, topology, architecture, and protocols.
- The most common network models are the Open Systems Interconnection (OSI) model and the Transmission Control Protocol/Internet Protocol (TCP/IP) model.
- The OSI model consists of seven layers: application, presentation, session, transport, network, data link, and physical.
- The TCP/IP model consists of four layers: application, transport, internet, and network access.
- The physical layer is the lowest layer of both models and is responsible for defining the hardware, cabling, wiring, frequencies, pulses, and encoding used to transmit and receive data bits over a physical medium .
- The physical layer provides its services to the data link layer, which is responsible for reading and writing data from and onto the line and detecting link errors .
- The physical layer can use different types of transmission media, such as copper wires, optical fibers, radio waves, or infrared signals .
- The physical layer can also use different types of modulation techniques, such as amplitude modulation, frequency modulation, or phase modulation, to encode the data bits into analog or digital signals .
- The physical layer can be further divided into two sublayers: the physical medium dependent (PMD) sublayer and the physical medium independent (PMI) sublayer.
- The PMD sublayer deals with the characteristics of the physical medium, such as the voltage levels, the connectors, the cable types, etc.
- The PMI sublayer deals with the encoding and decoding of the data bits, the synchronization of the sender and receiver, and the error detection and correction.



### Introductory Concepts of Computer Networks

A computer network is a group of two or more interconnected computer systems that can communicate and share information and resources . Computer networks have many applications, such as email, web browsing, file transfer, online gaming, video conferencing, etc.

Some of the basic concepts and fundamentals of computer networks are:

- **Essential components of the computer network**: A computer network consists of four main components: end devices, media, protocols, and networking devices.
  - **End devices**: An end device is a device that sends or receives the data in the network, such as a computer, a printer, a smartphone, a camera, etc.
  - **Media**: The media provides connectivity between the end devices. It can be either wired, such as cables and fiber optics, or wireless, such as radio waves and infrared signals .
  - **Protocols**: Protocols are the rules and standards that define how the data is formatted, transmitted, and received in the network. They ensure that the devices can communicate and understand each other. Some of the common protocols are TCP/IP, HTTP, FTP, SMTP, etc .
  - **Networking devices**: Networking devices are the devices that facilitate the data transmission and routing in the network, such as switches, routers, hubs, bridges, firewalls, etc .
- **Classification of the computer network**: Computer networks can be classified based on different criteria, such as size, topology, architecture, etc .
  - **Size**: The size of a network refers to the geographical area and the number of devices that it covers. Some of the common network sizes are LAN (Local Area Network), WAN (Wide Area Network), MAN (Metropolitan Area Network), PAN (Personal Area Network), etc .
  - **Topology**: The topology of a network refers to the physical or logical arrangement of the devices and the media in the network. It affects the performance, reliability, and cost of the network. Some of the common network topologies are bus, ring, star, mesh, tree, etc .
  - **Architecture**: The architecture of a network refers to the design and structure of the network, such as the layers, the protocols, the addressing, the routing, etc. It affects the functionality, scalability, and security of the network. Some of the common network architectures are TCP/IP, OSI, peer-to-peer, client-server, etc .



#### Goals and applications of networks and protocols

- A network is a collection of devices that can communicate with each other over a shared medium, such as wires, cables, radio waves or optical fibers.
- A protocol is a set of rules, conventions or data structures that allows communication between devices in a network. They are essential for allowing two or more devices to identify and connect with each other. The protocols also specify how the devices communicate within the network package, send, receive and interpret data.
- The main goals of networks are :
  - **Resource sharing**: Networks enable multiple users or devices to share common hardware and software resources, such as printers, scanners, modems, files, databases, applications, etc. This reduces the cost and increases the efficiency of resource utilization.
  - **High reliability**: Networks provide multiple sources of supply and backup for data and services, such as redundancy, fault tolerance, load balancing, etc. This increases the availability and reliability of the network and reduces the risk of data loss or service interruption.
  - **Greater flexibility**: Networks allow devices to connect and communicate with each other regardless of their physical location, type or configuration. This enables users to access data and services from anywhere, anytime and from any device. Networks also support dynamic and scalable network architectures, such as peer-to-peer, client-server, cloud, etc.
  - **Increased productivity**: Networks facilitate data exchange and collaboration among users and devices, such as email, chat, video conferencing, file transfer, etc. This improves the speed and quality of information processing and decision making. Networks also enable automation and optimization of various tasks and processes, such as scheduling, monitoring, security, etc.
- The main applications of networks are:
  - **Internet**: The Internet is the global network of networks that connects billions of devices and users around the world. It supports various applications and services, such as web browsing, online shopping, social media, online gaming, streaming, etc. The Internet uses a set of protocols, such as TCP/IP, HTTP, DNS, SMTP, etc. to enable communication and data exchange among different networks and devices.
  - **Intranet**: An intranet is a private network that is accessible only to authorized users or devices within an organization or a group. It is used for internal communication and collaboration, such as email, file sharing, document management, etc. An intranet may use the same protocols as the Internet, such as TCP/IP, HTTP, etc. but with additional security and access control measures.
  - **Extranet**: An extranet is a network that connects an intranet with external networks or devices, such as customers, suppliers, partners, etc. It is used for business-to-business communication and transactions, such as e-commerce, supply chain management, customer relationship management, etc. An extranet may use the same protocols as the Internet or the intranet, but with different levels of security and access control depending on the nature and purpose of the connection.
  - **Wireless network**: A wireless network is a network that uses radio waves or other wireless technologies, such as Wi-Fi, Bluetooth, cellular, satellite, etc. to connect devices without wires or cables. It is used for mobile and remote communication and access, such as smartphones, laptops, tablets, smart watches, etc. A wireless network may use the same protocols as the wired network, such as TCP/IP, HTTP, etc. but with additional challenges and considerations, such as interference, signal strength, battery life, etc.
  - **Sensor network**: A sensor network is a network that consists of a large number of small and low-power devices, such as sensors, actuators, cameras, etc. that can collect, process and transmit data about the physical environment or phenomena. It is used for monitoring and control applications, such as smart home, smart city, smart grid, health care, agriculture, etc. A sensor network may use different protocols than the traditional network, such as ZigBee, LoRaWAN, MQTT, etc. to address the specific requirements and constraints of the network, such as energy efficiency, scalability, reliability, etc.



#### Categories of networks in computer networks

A computer network is a system of two or more computers that are connected to each other and can share data, resources, and applications. Computer networks can be classified based on several criteria, such as the transmission medium, the network size, the topology, and the organizational intent. Based on the network size, the most common types of computer networks are:

- **Personal Area Network (PAN)**: A PAN is the smallest and simplest type of network. It connects devices within the range of an individual, such as a smartphone, a laptop, a printer, or a smartwatch. A PAN is usually wireless and can use technologies such as Bluetooth, Wi-Fi, or infrared. A PAN can enable personal communication, data synchronization, and device control.   

- **Local Area Network (LAN)**: A LAN is a network that connects devices within a limited geographical area, such as a home, an office, a school, or a building. A LAN can use wired or wireless technologies, such as Ethernet, Wi-Fi, or fiber optics. A LAN can enable file sharing, printer sharing, internet access, and local communication. A LAN can have a single or multiple subnets, depending on the network design and the number of devices.   

- **Wide Area Network (WAN)**: A WAN is a network that connects devices across a large geographical area, such as a city, a country, or the world. A WAN can use wired or wireless technologies, such as telephone lines, satellite links, cellular networks, or the internet. A WAN can enable remote access, data transfer, and global communication. A WAN can have a single or multiple domains, depending on the network architecture and the level of control.   

- **Metropolitan Area Network (MAN)**: A MAN is a network that connects devices within a metropolitan area, such as a city or a town. A MAN can use wired or wireless technologies, such as cable, DSL, WiMAX, or 5G. A MAN can enable regional communication, internet service, and public access. A MAN can have a single or multiple providers, depending on the network ownership and the service agreement.   

- **Campus Area Network (CAN)**: A CAN is a network that connects devices within a campus, such as a university, a hospital, or a military base. A CAN can use wired or wireless technologies, such as Ethernet, Wi-Fi, or fiber optics. A CAN can enable academic, medical, or military communication, data sharing, and security. A CAN can have a single or multiple LANs, depending on the network size and the functional requirements.  

- **Storage Area Network (SAN)**: A SAN is a network that connects storage devices, such as hard disks, tape drives, or optical disks. A SAN can use wired or wireless technologies, such as SCSI, Fibre Channel, or iSCSI. A SAN can enable data backup, data recovery, data replication, and data management. A SAN can have a single or multiple servers, depending on the network performance and the storage capacity.  

- **Virtual Private Network (VPN)**: A VPN is a network that connects devices over a public network, such as the internet, using encryption and authentication. A VPN can use wired or wireless technologies, such as SSL, IPSec, or L2TP. A VPN can enable secure, private, and remote communication, data transfer, and access. A VPN can have a single or multiple tunnels, depending on the network security and the user needs.



#### Organization of the Internet

- The Internet is a global network of interconnected computers and devices that communicate using standardized protocols and procedures.
- The Internet is composed of many smaller networks, called internets, that are connected by routers and gateways. Some internets are isolated and do not connect to the global Internet, but use the same Internet standards.
- The Internet is organized at different levels, such as hardware, access, navigation, and governance. Each level involves different actors and entities that control and regulate the Internet.
- The hardware level consists of the physical devices and infrastructure that enable data transmission and processing, such as computers, servers, cables, satellites, and wireless networks.
- The access level involves the Internet service providers (ISPs) and network operators that provide connectivity and bandwidth to users and organizations. ISPs can be commercial, public, or community-based, and they can have different policies and prices for their services.
- The navigation level refers to the methods and tools that help users find and access information and resources on the Internet, such as domain names, IP addresses, search engines, browsers, and applications.
- The governance level encompasses the rules, norms, and institutions that shape the development and operation of the Internet, such as laws, regulations, standards, policies, and organizations. Some of the organizations that influence the Internet are the Internet Society, the Internet Engineering Task Force, the Internet Corporation for Assigned Names and Numbers, the World Wide Web Consortium, and the United Nations.



#### ISP

- ISP stands for **Internet Service Provider**  , a company that provides access to the internet and other related services to its customers .
- ISPs make it possible for their customers to surf the web, shop online, conduct business, and connect with family and friends—all for a fee.
- ISPs may also provide software packages (such as browsers), e-mail accounts, and a personal website or home page.
- ISPs can host websites for businesses and can also build the websites themselves.
- ISPs can be classified into different types based on the technology they use to deliver internet access, such as dial-up, DSL, cable, fiber, satellite, wireless, or mobile.
- ISPs can also be categorized based on the scale and scope of their services, such as regional, national, or global ISPs, or specialized ISPs that cater to specific markets or niches.
- ISPs are regulated by different laws and policies depending on the country or region they operate in, such as net neutrality, data privacy, censorship, or taxation.



#### Network structure with reference to Computer Networks

- A computer network is a structure that makes available to a data processing user at one place some data processing function or service performed at another place.
- Computer network architecture defines the physical and logical framework of a computer network. It outlines how computers are organized in the network and what tasks are assigned to those computers.
- Network architecture components include hardware, software, transmission media (wired or wireless), network topology, and communications protocols.
- Network topology is the arrangement of the elements of a network, such as nodes, links, and switches. It affects the performance, reliability, and scalability of the network.
- Communications protocols are the rules and conventions that govern the exchange of information between network devices. They specify the format, timing, and error control of the data packets.
- One of the most common and widely used communications protocols is TCP/IP, which stands for Transmission Control Protocol/Internet Protocol. It is the predominant model for today’s Internet structure and presents this standard layer configuration for communication links:
  - Network access layer: Defines how the data gets physically transferred.
  - Internet layer: Packages the data into understandable packets so it can be sent and received.
  - Transport layer: Allows the network devices to maintain conversations.
  - Application layer: Establishes how high-level applications access the network for purposes of data transfer.
- Computer networks can be classified on the basis of architecture into different types, such as LAN, WAN, MAN, PAN, CAN, SAN, etc. Each type has its own characteristics, advantages, and disadvantages .
  - LAN (local area network): A LAN connects computers over a relatively short distance, allowing them to share data, files, resources, and services. A LAN can be wired or wireless. Examples of LANs are home networks, office networks, and school networks.
  - WAN (wide area network): A WAN connects computers over a large geographical area, such as a country or a continent. A WAN can use different transmission media, such as cables, satellites, or radio waves. Examples of WANs are the Internet, telephone networks, and cellular networks.
  - MAN (metropolitan area network): A MAN connects computers within a city or a metropolitan area. A MAN can use optical fibers, coaxial cables, or wireless links. Examples of MANs are cable TV networks, city-wide Wi-Fi networks, and campus networks.
  - PAN (personal area network): A PAN connects devices within a very short range, such as a few meters. A PAN can be wired or wireless. Examples of PANs are Bluetooth networks, infrared networks, and USB networks.
  - CAN (campus area network): A CAN connects computers within a limited area, such as a university or a corporate campus. A CAN can use LAN or MAN technologies. Examples of CANs are university networks, corporate networks, and hospital networks.
  - SAN (storage area network): A SAN connects storage devices, such as hard disks, tape drives, and optical disks, to servers or other computers. A SAN can use fiber channels, SCSI, or iSCSI protocols. Examples of SANs are data centers, backup systems, and disaster recovery systems.



#### Network architecture with reference to Computer Networks

- Network architecture is the design of a computer network    .
- It is a framework for the specification of a network's physical components and their functional organization and configuration, its operational principles and procedures, as well as communication protocols used   .
- Network architecture components include hardware, software, transmission media (wired or wireless), network topology, and communications protocols  .
- Network architecture can be classified based on the network's size and purpose, such as:
  - LAN (local area network): A LAN connects computers over a relatively short distance, allowing them to share data, files, printers, and other resources .
  - WLAN (wireless local area network): A WLAN is just like a LAN but connections between devices on the network are wireless, using radio waves or infrared signals .
  - MAN (metropolitan area network): A MAN covers a larger area than a LAN, such as a city or a campus, and interconnects several LANs .
  - WAN (wide area network): A WAN spans a large geographic area, such as a country or a continent, and connects multiple LANs or MANs .
  - PAN (personal area network): A PAN is a small network that connects personal devices, such as smartphones, laptops, or wearable devices, usually over Bluetooth or Wi-Fi .
  - SAN (storage area network): A SAN is a dedicated network that provides access to consolidated, block-level data storage, usually for high-performance applications .
  - CAN (controller area network): A CAN is a serial bus network that connects devices or controllers in vehicles, industrial machinery, or embedded systems .
- Network architecture can also be classified based on the network's topology, which is the arrangement of nodes and links in the network, such as:
  - Bus: A bus network has a single cable that connects all the nodes, and data is transmitted in both directions .
  - Star: A star network has a central node, such as a switch or a hub, that connects all the other nodes, and data is transmitted through the central node .
  - Ring: A ring network has a circular arrangement of nodes, and data is transmitted in one direction along the ring .
  - Mesh: A mesh network has multiple paths between any pair of nodes, and data is routed through the best available path .
  - Tree: A tree network has a hierarchical structure of nodes, and data is transmitted from the root node to the leaf nodes or vice versa .
  - Hybrid: A hybrid network combines two or more of the above topologies, and data is transmitted according to the rules of each topology .



#### Layering Principles with reference to Network Architecture in Computer Networks

Layering is a design principle that divides a complex system into smaller and simpler components, called layers, that can be managed independently. Each layer has a specific function and interacts with the adjacent layers through well-defined interfaces. Layering allows for modularity, interoperability, scalability, and flexibility of network systems.

Some of the benefits of layering are:

- It reduces the complexity of the system by hiding the details of lower layers from higher layers.
- It enables the reuse of common functions and protocols across different applications and network technologies.
- It allows for the development and evolution of each layer independently, without affecting the other layers.
- It facilitates the standardization and interoperability of network components from different vendors and organizations.

One of the most widely used models of layered network architecture is the Open Systems Interconnection (OSI) model, which defines seven layers of network functions:

- Physical layer: This layer is responsible for the transmission and reception of raw bits over a physical medium, such as cables, wires, or wireless signals. It defines the characteristics of the physical devices, connectors, and encoding schemes.
- Data link layer: This layer is responsible for the reliable and error-free delivery of data frames between adjacent nodes on a network. It defines the protocols for framing, addressing, error detection, and flow control.
- Network layer: This layer is responsible for the routing and forwarding of data packets across different networks. It defines the protocols for addressing, routing, congestion control, and fragmentation.
- Transport layer: This layer is responsible for the end-to-end delivery of data segments between applications on different hosts. It defines the protocols for connection establishment, reliability, multiplexing, and quality of service.
- Session layer: This layer is responsible for the management and coordination of sessions between applications. It defines the protocols for authentication, authorization, synchronization, and checkpointing.
- Presentation layer: This layer is responsible for the representation and transformation of data formats between applications. It defines the protocols for encryption, compression, translation, and serialization.
- Application layer: This layer is responsible for the provision and support of application-specific services and functions. It defines the protocols for various network applications, such as email, web, file transfer, remote access, and network management.



#### Services in Networks Architecture in Computer Networks

- Services in networks architecture are applications that run at the network application layer and above, and provide various capabilities to the users and devices in the network .
- Services in networks architecture can be classified into two types: connection-oriented and connectionless.
  - Connection-oriented services require the establishment of a logical connection between the sender and the receiver before any data can be exchanged. Examples of connection-oriented services are TCP, FTP, and Telnet.
  - Connectionless services do not require a logical connection between the sender and the receiver, and data can be sent without any prior arrangement. Examples of connectionless services are UDP, IP, and DNS.
- Services in networks architecture can also be classified into two types: reliable and unreliable.
  - Reliable services guarantee that the data sent by the sender will be delivered to the receiver without any errors or losses. Examples of reliable services are TCP, FTP, and SMTP.
  - Unreliable services do not guarantee that the data sent by the sender will be delivered to the receiver without any errors or losses. Examples of unreliable services are UDP, IP, and SNMP.
- Services in networks architecture can be implemented using different architectures, such as client-server or peer-to-peer .
  - Client-server architecture is a model where one or more servers provide services to multiple clients. The servers are usually centralized and have more resources than the clients. Examples of client-server services are HTTP, FTP, and SMTP .
  - Peer-to-peer architecture is a model where each node in the network can act as both a client and a server, and provide services to other nodes. The nodes are usually distributed and have equal resources. Examples of peer-to-peer services are BitTorrent, Skype, and Bitcoin .
- Services in networks architecture typically use application layer protocols to communicate with each other and with the lower layers of the network. Examples of application layer protocols are HTTP, FTP, SMTP, DNS, and DHCP  .



#### Protocols and Standards in Networks Architecture in Computer Networks

- Network protocols are a set of guidelines governing the exchange of information in a simple, dependable and secure way.
- Network protocols define how devices communicate within a network, including the formats, procedures, and rules of data transmission.
- Network standards are formal specifications that ensure compatibility and interoperability among different devices, systems, and applications in a network.
- Network standards are usually developed by standard organizations, such as IEEE, ISO, IETF, etc., or by industry consortia, such as W3C, Bluetooth SIG, etc.
- Network protocols and standards usually come in groups that work well together and constitute protocol suites or protocol stacks, such as TCP/IP, OSI, etc.
- Network architecture is the design and structure of a network, including its components, connections, and functions.
- Network architecture components include hardware, software, transmission media (wired or wireless), network topology, and communications protocols.
- Network architecture can be classified into two main types: peer-to-peer (P2P) and client/server.
- In a P2P network, each device can act as both a client and a server, and communicate directly with each other without a central authority.
- In a client/server network, each device has a specific role: a client requests services or resources from a server, and a server provides services or resources to a client.
- Network protocols and standards are essential for network architecture, as they enable the exchange of information across different devices, systems, and applications in a network.



#### The OSI reference model in Computer Networks

The OSI reference model is a conceptual framework that describes how information from a software application in one computer moves through a physical medium to another computer. It was developed by the International Organization for Standardization (ISO) in the early 1980s to facilitate interoperability and standardization of network protocols and devices .

The OSI reference model consists of seven layers, each with its own function and responsibility. The layers are:

- **Physical layer**: This layer defines the physical characteristics of the transmission medium, such as voltage levels, connectors, cables, etc. It also handles the conversion of digital signals to analog signals and vice versa. The physical layer is responsible for transmitting and receiving raw bits of data over the network.
- **Data link layer**: This layer provides reliable and error-free transmission of data frames between two nodes on the same network. It also handles the addressing, framing, and flow control of data packets. The data link layer is divided into two sublayers: the logical link control (LLC) and the media access control (MAC). The LLC sublayer provides services such as error detection and correction, while the MAC sublayer regulates the access to the shared medium, such as Ethernet or Wi-Fi.
- **Network layer**: This layer provides the routing and forwarding of data packets across different networks. It also handles the addressing, fragmentation, and reassembly of data packets. The network layer uses logical addresses, such as IP addresses, to identify the source and destination of each packet. The network layer is responsible for the end-to-end delivery of data across the network.
- **Transport layer**: This layer provides the reliable and error-free transmission of data segments between two processes on different computers. It also handles the segmentation, reassembly, and flow control of data segments. The transport layer uses port numbers to identify the source and destination processes of each segment. The transport layer is responsible for the process-to-process delivery of data across the network. The transport layer can provide different types of services, such as connection-oriented (TCP) or connectionless (UDP).
- **Session layer**: This layer provides the establishment, management, and termination of sessions between two applications on different computers. It also handles the synchronization, checkpointing, and recovery of data exchange. The session layer allows different applications to communicate with each other using different protocols, such as HTTP, FTP, or SMTP.
- **Presentation layer**: This layer provides the translation, encryption, and compression of data between two applications on different computers. It also handles the formatting, representation, and interpretation of data. The presentation layer ensures that the data is compatible and understandable by both applications, regardless of their internal formats or structures.
- **Application layer**: This layer provides the interface and services for the user applications to access the network. It also handles the authentication, authorization, and accounting of users and applications. The application layer defines the protocols and standards for different types of applications, such as web browsers, email clients, file transfer programs, etc.

The OSI reference model is a useful tool for understanding and designing network systems, as it provides a common language and framework for describing the functions and interactions of different network components. However, it is not a strict specification or implementation of network protocols, as some protocols may span across multiple layers or omit some layers altogether. For example, the TCP/IP protocol suite, which is the most widely used network protocol today, does not follow the OSI reference model exactly, as it combines the data link and physical layers into one layer, and the session, presentation, and application layers into another layer. Therefore, the OSI reference model should be seen as a guideline rather than a rule for network communication.



#### TCP/IP protocol suite in in Computer Networks

- TCP/IP stands for Transmission Control Protocol/Internet Protocol and is a suite of communication protocols used to interconnect network devices on the internet or in a private network.
- TCP/IP is also known as the internet protocol suite, as it defines the rules and methods for data transmission over the internet .
- TCP/IP consists of four layers: application, transport, internet, and network interface .
- The application layer provides the interface for the user or the application to access the network services, such as email, web browsing, file transfer, etc. Some of the protocols in this layer are HTTP, SMTP, FTP, DNS, etc .
- The transport layer provides reliable or unreliable data delivery between the source and the destination hosts, using protocols such as TCP or UDP. TCP ensures reliable and ordered data delivery, while UDP provides fast and unordered data delivery .
- The internet layer is responsible for routing the data packets across different networks, using protocols such as IP, ICMP, ARP, etc. IP assigns a unique address to each host and device on the network, and routes the packets based on the destination address. ICMP is used for error reporting and diagnostic purposes. ARP is used for resolving the physical address of a host from its IP address .
- The network interface layer is responsible for transmitting and receiving the data packets over the physical medium, such as Ethernet, Wi-Fi, etc. It also handles the framing, error detection, and flow control of the data. Some of the protocols in this layer are Ethernet, Wi-Fi, MAC, etc .



#### Network devices in Computer Networks

Network devices are physical devices that enable communication and interaction between hardware on a computer network. Each networking device operates in a distinct computer network segment and performs distinct functions. A network may require hundreds or thousands of different network devices to maintain and build out various LAN and WAN.

Some of the common types of network devices are:

- **Repeater**: A repeater is a device that operates at the physical layer and regenerates the signal over the same network. It can extend the transmission distance of a network by amplifying the weak signals.
- **Hub**: A hub is a device that operates at the physical layer and connects multiple wires coming from different branches. It broadcasts the data to all the connected devices, regardless of the destination address. It is a passive device that does not perform any filtering or routing.
- **Bridge**: A bridge is a device that operates at the data link layer and connects two or more network segments. It filters the data based on the MAC addresses and forwards only the relevant data to the destination segment. It can also reduce network congestion by dividing a large network into smaller segments.
- **Switch**: A switch is a device that operates at the data link layer or the network layer and connects multiple devices on the same network. It has a buffer and a design that can improve its efficiency. It can store the MAC addresses of the connected devices in a table and forward the data only to the intended device. It can also perform routing functions based on the IP addresses .
- **Router**: A router is a device that operates at the network layer and routes data packets based on their IP addresses. It can connect different networks with different protocols and architectures. It can also perform filtering, security, and network management functions .
- **Gateway**: A gateway is a device that operates at the application layer and connects two or more networks with different protocols and data formats. It can perform protocol conversion, data translation, and encryption functions. It can also act as a proxy server or a firewall.
- **Brouter**: A brouter is a device that combines the functions of a bridge and a router. It can filter and route data packets based on both the MAC addresses and the IP addresses. It can also switch between the two functions depending on the network configuration.
- **NIC**: A NIC (network interface card) is a device that operates at the physical layer and the data link layer and enables a computer to connect to a network. It has a unique MAC address and can send and receive data over the network. It can also perform error detection and correction functions .

: https://www.scaler.com/topics/computer-network/network-devices/
: https://www.geeksforgeeks.org/network-devices-hub-repeater-bridge-switch-router-gateways/
: https://testbook.com/learn/types-of-computer-network-devices/



#### Network components in Computer Networks

A computer network is a system of interconnected devices that can communicate and share data. The network components are the hardware and software elements that enable this communication and data transfer. Some of the common network components are:

- **Nodes**: Nodes are the devices that participate in the network, such as computers, laptops, smartphones, printers, servers, routers, switches, etc. Nodes have network interfaces that allow them to send and receive data over the network.
- **Media**: Media are the physical or wireless means that carry the data signals between the nodes. Examples of media are copper wires, fiber-optic cables, radio waves, infrared beams, etc. Media have different characteristics, such as bandwidth, latency, noise, interference, etc., that affect the network performance.
- **Protocols**: Protocols are the rules and standards that govern how the nodes communicate and exchange data over the network. Protocols define the format, structure, timing, and error control of the data packets. Examples of protocols are TCP/IP, Ethernet, Wi-Fi, HTTP, FTP, etc. Protocols are organized into layers, such as the OSI model or the TCP/IP model, that specify the functions and responsibilities of each layer.
- **Network devices**: Network devices are the specialized hardware that facilitate the network operation and management. Examples of network devices are routers, switches, hubs, bridges, repeaters, firewalls, modems, etc. Network devices perform different functions, such as forwarding, filtering, amplifying, converting, or securing the data packets.
- **Network services**: Network services are the software applications that provide various functionalities and resources to the network users. Examples of network services are DNS, DHCP, email, web, file, print, etc. Network services run on servers or cloud platforms that can be accessed by the network clients.



### Physical Layer in Computer Networks

The physical layer is the lowest and first layer of the OSI model of computer networking. It is responsible for sending and receiving bits of data between devices through a physical medium, such as a cable, a fiber, or a wireless channel. The physical layer provides an electrical, mechanical, and procedural interface to the transmission medium, and defines how the bits are encoded, modulated, and demodulated into signals. The physical layer also determines the data rate, the synchronization, the transmission mode, and the physical topology of the network. Some of the functions and components of the physical layer are:

- Data encoding: The physical layer converts the binary data into signals that can be transmitted over the medium. The signals can be electrical, optical, or electromagnetic, depending on the type of medium. The encoding scheme can be analog or digital, and can use different techniques such as NRZ, Manchester, or QAM.
- Data modulation: The physical layer modulates the signals to adapt them to the characteristics and limitations of the medium. Modulation is the process of changing the amplitude, frequency, or phase of a carrier signal according to the data signal. Modulation can increase the data rate, the range, and the reliability of the transmission.
- Data demodulation: The physical layer demodulates the signals received from the medium and converts them back into binary data. Demodulation is the inverse process of modulation, and it recovers the original data signal from the carrier signal.
- Data transmission: The physical layer transmits and receives the signals over the medium, using different devices and connectors. The devices can be transmitters, receivers, transceivers, repeaters, hubs, or switches. The connectors can be RJ-45, BNC, or SC, depending on the type of cable or fiber used.
- Data rate: The physical layer maintains the data rate, which is the number of bits that can be sent or received per second. The data rate depends on the bandwidth, the signal-to-noise ratio, and the modulation scheme of the medium. The data rate can be fixed or variable, and can be measured in bits per second (bps), kilobits per second (kbps), megabits per second (Mbps), or gigabits per second (Gbps).
- Synchronization: The physical layer performs synchronization of bits, which is the process of aligning the sender and the receiver clocks to ensure that the bits are correctly interpreted. Synchronization can be achieved by using a common clock source, a preamble, or a start and stop bit for each data frame.
- Transmission mode: The physical layer helps in transmission mode decision, which is the direction of data transfer between devices. The transmission mode can be simplex, half-duplex, or full-duplex. Simplex mode allows data to flow in one direction only, such as from a keyboard to a monitor. Half-duplex mode allows data to flow in both directions, but not at the same time, such as in a walkie-talkie. Full-duplex mode allows data to flow in both directions simultaneously, such as in a telephone.
- Physical topology: The physical layer helps in physical topology decision, which is the arrangement of devices and cables in a network. The physical topology can be mesh, star, bus, ring, or hybrid. Mesh topology connects every device to every other device, providing high reliability and redundancy. Star topology connects every device to a central hub or switch, providing easy installation and management. Bus topology connects every device to a single cable, providing low cost and simplicity. Ring topology connects every device to a closed loop of cable, providing equal access and fault tolerance. Hybrid topology combines two or more of the above topologies, providing flexibility and scalability.



#### Network topology design in Computer Networks

- Network topology is the arrangement of the nodes and links in a network, both physically and logically .
- Physical topology refers to the actual layout of the cables and devices, while logical topology refers to how data flows between the nodes .
- Network topology affects the performance, cost, reliability, scalability and security of a network .
- There are different types of network topologies, such as bus, ring, star, mesh, tree, hybrid, etc. Each type has its own advantages and disadvantages .
- Network topology design is the process of choosing the best topology for a given network, based on the requirements and constraints of the network .
- Network topology design involves the following steps:
  - Identify the network objectives, such as speed, reliability, security, scalability, etc.
  - Analyze the network environment, such as the number and location of nodes, the type and amount of traffic, the available resources, etc.
  - Select the appropriate topology, such as bus, ring, star, mesh, tree, hybrid, etc., based on the network objectives and environment.
  - Implement the topology, such as installing the cables and devices, configuring the settings, testing the functionality, etc.
  - Monitor and evaluate the topology, such as measuring the performance, detecting and resolving the problems, updating and modifying the topology, etc.



#### Types of connections in Computer Networks

A computer network is a group of interconnected computing devices that can communicate and share data, files, and resources. There are different types of connections in computer networks, depending on how the devices are linked and what kind of data they can exchange. Some of the common types of connections are:

- **Point-to-point connections**: These connections allow one device to communicate with one other device. For example, two phones may pair with each other using Bluetooth to exchange files or make calls. Point-to-point connections are usually simple and secure, but they can only support two devices at a time.

- **Broadcast/multicast connections**: These connections allow a device to send one message out to the network and have copies of that message delivered to multiple recipients. For example, a radio station may broadcast its signal to many listeners, or a video conferencing app may multicast its stream to many viewers. Broadcast/multicast connections are useful for reaching a large audience, but they can also cause network congestion and interference.

- **Multipoint connections**: These connections allow one device to connect and deliver messages to multiple devices in parallel. For example, a router may connect to several computers and forward packets to them based on their destination addresses. Multipoint connections are efficient and flexible, but they can also introduce delays and errors.

- **Local area network (LAN)**: A LAN connects computers over a relatively short distance, allowing them to share data, files, and resources. For example, a LAN may connect all the computers in an office building, school, or hospital. LANs are usually fast and reliable, but they can also be expensive and difficult to maintain.

- **Metropolitan area network (MAN)**: A MAN connects computers over a larger area, such as a city or a campus. For example, a MAN may connect several LANs using fiber optic cables or wireless bridges. MANs are usually faster and more secure than WANs, but they can also be costly and complex.

- **Personal area network (PAN)**: A PAN connects devices over a very short distance, usually within a few meters. For example, a PAN may connect a laptop, a mouse, a keyboard, and a printer using USB cables or wireless signals. PANs are usually convenient and portable, but they can also be limited and vulnerable.

- **Wide area network (WAN)**: A WAN connects computers over a very large area, such as a country or a continent. For example, the Internet is the world's largest WAN, connecting billions of devices across the globe. WANs are usually powerful and scalable, but they can also be slow and insecure.



#### Transmission media in Computer Networks

- Transmission media is the physical medium that carries data from one device to another in a computer network.
- Transmission media can be classified into two types: guided media and unguided media.
- Guided media, also known as wired or bounded media, are those that provide a physical path for the data signals, such as cables or wires.
- Unguided media, also known as wireless or unbounded media, are those that do not require a physical medium, but use electromagnetic waves to transmit data, such as radio waves, microwaves, infrared, or optical signals.
- The choice of transmission media depends on several factors, such as the distance, bandwidth, cost, reliability, security, and interference of the communication channel.
- Some examples of guided media are twisted pair cable, coaxial cable, and fiber optic cable.
- Some examples of unguided media are radio waves, microwaves, infrared, and optical signals.
- The properties of different transmission media determine the speed of data transfer from one endpoint to another.
- Transmission media is an essential component of network architecture, along with hardware, software, network topology, and communication protocols.



#### Signal transmission and encoding in Computer Networks

- Signal transmission is the process of sending digital or analog data over a physical medium such as a wire, a cable, or a wireless channel.
- Encoding is the process of converting data into a specific format that can be recognized and interpreted by the receiver.
- There are different types of encoding techniques depending on the nature of the data and the medium used for transmission.
- Some of the common encoding techniques are:

  - Digital-to-digital encoding: This is the conversion of binary data (0s and 1s) into a series of voltage pulses or electromagnetic waves that can be transmitted over a wire or a wireless channel. Examples of digital-to-digital encoding are Non-return-to-zero (NRZ), Manchester, and 4B/5B encoding.
  - Analog-to-digital encoding: This is the conversion of analog data (such as sound or video) into a digital format that can be transmitted over a digital medium. This involves sampling, quantization, and encoding of the analog signal. Examples of analog-to-digital encoding are Pulse code modulation (PCM) and Delta modulation (DM).
  - Digital-to-analog encoding: This is the conversion of digital data into an analog signal that can be transmitted over an analog medium. This involves modulating the digital data onto a carrier wave using techniques such as Amplitude shift keying (ASK), Frequency shift keying (FSK), or Phase shift keying (PSK).
  - Analog-to-analog encoding: This is the conversion of analog data into another analog signal that can be transmitted over an analog medium. This involves changing the amplitude, frequency, or phase of the analog signal using techniques such as Amplitude modulation (AM), Frequency modulation (FM), or Phase modulation (PM).

- The choice of encoding technique depends on factors such as the bandwidth, the noise, the error rate, the cost, and the complexity of the transmission medium and the devices involved.



#### Network performance and transmission impairments in Computer Networks

- Network performance is a measure of how well a network can deliver data and services to its users. It can be evaluated by various metrics, such as:

  - Network throughput - Amount of data successfully transferred over the network in a given time
  - Network delay, latency and jittering - Any network issue causing packet transfer to be slower than usual
  - Data loss and network errors - Packets dropped or lost in transmission and delivery

- Transmission impairments are any factors that degrade the quality of a signal as it travels through a transmission medium. They can cause distortion, attenuation, noise, and interference in the signal. Some common types of transmission impairments are:

  - Attenuation - The gradual loss of signal strength as it travels over a distance. It can be caused by absorption, reflection, scattering, or dispersion of the signal by the medium or the environment
  - Distortion - The alteration of the shape or form of the signal due to the characteristics of the medium or the devices. It can be caused by non-linearities, frequency-dependent attenuation, or delay distortion
  - Noise - The unwanted or random signals that are added to the original signal and reduce its signal-to-noise ratio (SNR). There are several types of noise, such as induced noise, crosstalk noise, thermal noise, and impulse noise, which may corrupt the signal 
  - Interference - The unwanted signals that are generated by other sources and affect the desired signal. It can be caused by electromagnetic interference (EMI), radio frequency interference (RFI), or intermodulation distortion

- The impact of transmission impairments on network performance depends on the type, severity, and frequency of the impairments, as well as the characteristics of the network and the signal. Some possible impacts are:

  - Reduced network throughput - Transmission impairments can cause errors, retransmissions, or congestion in the network, which can lower the effective data rate of the network
  - Increased network delay, latency, and jittering - Transmission impairments can cause variations in the propagation time, processing time, or queuing time of the packets, which can affect the timeliness and quality of the network services
  - Degraded network reliability and availability - Transmission impairments can cause failures, disruptions, or outages in the network, which can affect the continuity and dependability of the network services



#### Switching techniques and multiplexing in Computer Networks

Switching techniques are methods of connecting multiple devices in a network and transferring data between them. There are three main types of switching techniques: circuit switching, message switching, and packet switching.

- Circuit switching: In circuit switching, two nodes communicate with each other over a dedicated communication path. The path is established before the data transmission and remains active until the communication is over. The advantage of circuit switching is that it provides a guaranteed and continuous connection between the nodes. The disadvantage is that it wastes bandwidth when there is no data to transmit and it is vulnerable to failures in the path. Examples of circuit switching are telephone networks and ISDN.
- Message switching: In message switching, the whole message is treated as a data unit. The message is stored and forwarded by intermediate nodes until it reaches the destination. The advantage of message switching is that it does not require a dedicated path and it can overcome failures in the network. The disadvantage is that it introduces delays and overheads due to the storage and forwarding process. Examples of message switching are email and bulletin board systems.
- Packet switching: The packet switching technique is derived from message switching where the message is broken down into smaller chunks called packets. The packets are transmitted independently and may follow different routes to reach the destination. The advantage of packet switching is that it optimizes the use of bandwidth and it can adapt to dynamic network conditions. The disadvantage is that it may cause packet loss, duplication, or reordering due to congestion or errors in the network. Examples of packet switching are TCP/IP and ATM.

Multiplexing is a technique of combining multiple signals into one signal over a shared medium. Multiplexing allows the efficient utilization of bandwidth and the sharing of network resources among multiple sources and receivers. There are different methods of multiplexing, such as frequency division multiplexing (FDM), time division multiplexing (TDM), and statistical multiplexing.

- Frequency division multiplexing (FDM): In FDM, the bandwidth of the medium is divided into several frequency bands, and each signal is assigned a different band. The signals are modulated by their respective frequencies and then combined into one signal. The advantage of FDM is that it is simple and robust. The disadvantage is that it may cause interference and crosstalk among the signals. Examples of FDM are radio and television broadcasting.
- Time division multiplexing (TDM): In TDM, the time of the medium is divided into several time slots, and each signal is assigned a different slot. The signals are transmitted one after another in a cyclic manner and then combined into one signal. The advantage of TDM is that it can avoid interference and crosstalk among the signals. The disadvantage is that it may cause synchronization and latency issues. Examples of TDM are PCM and DSL.
- Statistical multiplexing: Statistical multiplexing is a communication link sharing technique, which is used in packet switching. The shared linking is variable in statistical multiplexing, whereas it is fixed in TDM or FDM. This is a strategic application for maximizing the utilization of bandwidth. This can increase the efficiency of network, as well. The advantage of statistical multiplexing is that it can adapt to the varying demands and traffic patterns of the sources. The disadvantage is that it may cause congestion and packet loss in the network. Examples of statistical multiplexing are Ethernet and IP.



## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

- The link layer is the lowest layer in the TCP/IP model. It is responsible for sending and receiving frames between nodes on the same physical link.
- A frame is a unit of data that contains a header, a payload, and a trailer. The header contains information such as the source and destination addresses, the type of payload, and error detection codes. The trailer contains a checksum or a cyclic redundancy check (CRC) to verify the integrity of the frame.
- The link layer can be divided into two sublayers: the logical link control (LLC) sublayer and the media access control (MAC) sublayer.
- The LLC sublayer provides services such as flow control, error control, and multiplexing to the upper layers. It can use different protocols such as HDLC, PPP, or Ethernet to encapsulate the data from the network layer.
- The MAC sublayer is responsible for controlling the access to the shared medium. It can use different techniques such as contention-based, reservation-based, or polling-based to coordinate the transmission of frames among multiple nodes.
- A local area network (LAN) is a network that connects devices within a limited geographic area, such as a building or a campus. A LAN can use different technologies such as Ethernet, Wi-Fi, or Token Ring to implement the link layer.
- Ethernet is the most widely used LAN technology. It uses a bus or a star topology to connect nodes. It uses the CSMA/CD protocol to resolve collisions on the shared medium. It can operate at different speeds such as 10 Mbps, 100 Mbps, 1 Gbps, or 10 Gbps.
- Wi-Fi is a wireless LAN technology that uses radio waves to transmit and receive data. It uses the CSMA/CA protocol to avoid collisions on the shared medium. It can operate at different frequencies such as 2.4 GHz or 5 GHz, and different standards such as 802.11a, 802.11b, 802.11g, 802.11n, or 802.11ac.
- Token Ring is a LAN technology that uses a ring topology to connect nodes. It uses a token-passing protocol to grant access to the medium. It can operate at 4 Mbps or 16 Mbps. It is less popular than Ethernet or Wi-Fi.



#### Link layer in Computer Networks

- The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet.
- The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to.
- The link layer is responsible for transferring data between nodes on a network segment across the physical layer.
- The link layer may also provide the means to detect and possibly correct errors that can occur in the physical layer.
- The link layer is concerned with local delivery of frames between nodes on the same level of the network.
- The link layer provides and gives data reliability and provides various tools to establish, maintain, and also release data link connections between network nodes.
- The link layer performs the following functions:
  - Framing: The packet received from the Network layer is known as a frame in the Data link layer. At the sender’s side, the Data link layer encapsulates the packet with a header and a trailer. At the receiver’s side, the Data link layer decapsulates the packet and sends it to the Network layer.
  - Addressing: The data link layer encapsulates the source and destination’s MAC address / physical address in the header of the frame. The MAC address is used to identify the nodes on the same network segment.
  - Error Control: Data link layer detects and corrects the errors that can occur in the transmission of frames. The errors can be detected by using techniques such as parity check, checksum, or cyclic redundancy check (CRC). The errors can be corrected by using techniques such as stop-and-wait ARQ, go-back-N ARQ, or selective repeat ARQ.
  - Flow Control: Data link layer controls the flow of data between the sender and the receiver to avoid congestion and data loss. The flow control can be implemented by using techniques such as stop-and-wait, sliding window, or backpressure.
  - Media Access Control: Data link layer regulates the access of multiple nodes to the shared medium. The media access control can be implemented by using techniques such as contention-based (e.g., CSMA/CD, CSMA/CA) or reservation-based (e.g., token ring, token bus) protocols.



#### Framing in link layer in Computer Networks

- Framing is a function of the data link layer that provides a way for a sender to transmit a set of bits that are meaningful to the receiver   .
- Framing uses frames to send or receive data. A frame is the unit of transmission in a link layer protocol, and consists of a link layer header followed by a packet.
- The data link layer receives packets from the network layer and converts them into frames. The frames have headers that contain information such as error-checking codes, source and destination addresses, and control information  .
- Framing is necessary because the physical layer only accepts and transfers a stream of bits without any regard to meaning or structure. The frames help the receiver to identify the start and end of each packet, and to detect and correct any errors that may occur during transmission .
- There are various kinds of framing methods used in data link layer, such as character count, byte stuffing, bit stuffing, and physical layer coding violations. Each method has its own advantages and disadvantages, and is suitable for different types of data and transmission media.



#### Error Detection and Correction in link layer in Computer Networks

- Error detection and correction are techniques that allow reliable delivery of data over unreliable communication channels.
- Error detection is the process of detecting the presence of errors in the transmitted data.
- Error correction is the process of correcting the errors in the transmitted data by either retransmitting the corrupted data or using extra information to recover the original data.
- There are two types of errors that can occur in the link layer: bit errors and frame errors.
- Bit errors are single or multiple changes in the value of one or more bits in the transmitted data.
- Frame errors are errors that affect the entire frame, such as missing, duplicated, or reordered frames.
- The link layer can use different methods to detect and correct errors, such as parity check, checksum, cyclic redundancy check (CRC), and automatic repeat request (ARQ).
- Parity check is a simple method that adds an extra bit to each data unit to make the number of 1s in the data unit even (even parity) or odd (odd parity). The receiver can detect a single bit error by checking the parity bit, but cannot correct it or detect multiple bit errors.
- Checksum is a method that calculates a value based on the sum of the data unit and appends it to the end of the data unit. The receiver can detect errors by recalculating the checksum and comparing it with the received value, but cannot correct them or identify the location of the errors.
- CRC is a method that generates a code based on the division of the data unit by a predefined polynomial and appends it to the end of the data unit. The receiver can detect errors by performing the same division and comparing the remainder with the received code, but cannot correct them or identify the location of the errors. CRC can detect more errors than checksum and is widely used in practice.
- ARQ is a method that uses feedback from the receiver to the sender to indicate the status of the received data. The sender can retransmit the data if the receiver detects errors or does not receive the data within a certain time. There are different types of ARQ, such as stop-and-wait ARQ, go-back-N ARQ, and selective repeat ARQ, that differ in how they handle the retransmission and buffering of the data. ARQ can provide error correction by retransmission, but it requires more bandwidth and delay than other methods.



#### Flow control in link layer in Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- It regulates the amount of data that a sender can send so that a fast sender does not overwhelm a slow receiver .
- It makes the sender wait until an acknowledgment is received from the receiver's end.
- Methods of flow control are Stop-and-wait, and Sliding window.
- Stop-and-wait is a simple method where the sender sends one frame and waits for an acknowledgment before sending the next frame.
- Sliding window is a more efficient method where the sender can send multiple frames without waiting for acknowledgments, but the number of frames is limited by a window size.
- Flow control on Ethernet can be implemented at the data link layer using pause frames, which are defined by the IEEE standard 802.3x.



#### Elementary Data Link Protocols in link layer in Computer Networks

- Data link layer protocols are designed to perform the basic functions of the data link layer, such as framing, error control and flow control.
- Framing is the process of dividing the bit-streams from the physical layer into data frames whose size ranges from a few hundred to a few thousand bytes.
- Error control is the process of detecting and correcting errors that may occur during transmission or reception of data frames.
- Flow control is the process of regulating the rate of data transmission between the sender and the receiver to avoid congestion or buffer overflow.
- Elementary data link layer protocols are divided into three different subcategories, as follows:
  - Protocol 1: Unrestricted simplex protocol
    - This protocol allows the sender to transmit data frames continuously without any feedback from the receiver.
    - This protocol is suitable for simplex channels, where data can only flow in one direction.
    - This protocol does not provide any error control or flow control mechanisms.
    - This protocol is simple and efficient, but it may waste bandwidth and cause data loss if the receiver is not ready or the channel is noisy.
  - Protocol 2: Simplex stop-and-wait protocol
    - This protocol requires the sender to wait for an acknowledgment (ACK) from the receiver before sending the next data frame.
    - This protocol is suitable for half-duplex channels, where data can flow in both directions, but not at the same time.
    - This protocol provides error control by using sequence numbers and retransmission of lost or corrupted frames.
    - This protocol provides flow control by using a single buffer at the receiver and blocking the sender if the buffer is full.
    - This protocol is reliable and simple, but it may cause low utilization and long delay if the channel is long or noisy.
  - Protocol 3: Simplex protocol for noisy channels
    - This protocol is an improvement of protocol 2 by adding a timer at the sender and a negative acknowledgment (NAK) at the receiver.
    - This protocol is suitable for noisy channels, where errors may occur frequently.
    - This protocol provides error control by using sequence numbers, retransmission of lost or corrupted frames, and timeout of unacknowledged frames.
    - This protocol provides flow control by using a single buffer at the receiver and blocking the sender if the buffer is full.
    - This protocol is reliable and efficient, but it may cause unnecessary retransmissions if the ACK or NAK is lost or delayed.
- Some examples of data link layer protocols are:
  - Synchronous Data Link Control (SDLC): a bit-oriented protocol that uses flags, bit stuffing, and cyclic redundancy check (CRC) for framing and error control.
  - High-Level Data Link Control (HDLC): a bit-oriented protocol that is based on SDLC and uses three types of frames: information, supervisory, and unnumbered.
  - Serial Line Internet Protocol (SLIP): a character-oriented protocol that uses end-of-frame markers and checksum for framing and error control.
  - Point-to-Point Protocol (PPP): a byte-oriented protocol that uses flags, byte stuffing, and CRC for framing and error control, and supports multiple network layer protocols.
  - Link Control Protocol (LCP): a protocol that negotiates and establishes the parameters of a PPP link.
  - Link Access Procedure (LAP): a protocol that implements the stop-and-wait mechanism for flow and error control.
  - Network Control Protocol (NCP): a protocol that negotiates and establishes the parameters of a network layer protocol over a PPP link.



#### Sliding Window protocols in link layer in Computer Networks

- The sliding window protocol is a data link layer protocol that is useful for the sequential and reliable delivery of data frames between two network nodes  .
- The sliding window protocol allows the sender to send multiple frames at a time before receiving an acknowledgment from the receiver  .
- The sliding window protocol uses a window size to control the number of frames that can be sent or received at a time. The window size is the number of frames that fit in the buffer of the sender or the receiver  .
- The sliding window protocol has two variants: stop-and-wait and go-back-N  .
- In the stop-and-wait protocol, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The window size is one for both the sender and the receiver  .
- In the go-back-N protocol, the sender can send up to N frames at a time, where N is the window size of the sender. The receiver can only send cumulative acknowledgments for the frames it has received in order. If the receiver detects a missing or corrupted frame, it discards all the subsequent frames and sends a negative acknowledgment to the sender. The sender then retransmits all the frames from the last unacknowledged frame  .
- The sliding window protocol improves the efficiency and throughput of data transmission by reducing the idle time of the sender and the receiver  .
- The sliding window protocol also ensures that the receiver can handle the incoming data without being overwhelmed by the sender  .
- The sliding window protocol is also used in the transport layer by the Transmission Control Protocol (TCP), which manages the flow of packets between two computers or network hosts.



#### Medium Access Control and Local Area Networks

- Medium access control (MAC) is a sublayer of the data link layer that regulates the access of multiple devices to a shared medium, such as a wireless channel or a wired network.
- MAC protocols are designed to avoid or resolve collisions, which occur when two or more devices transmit data at the same time on the same medium.
- There are two main approaches to MAC protocols: contention-based and token-passing.
  - Contention-based protocols allow any device to transmit data whenever the medium is idle, but require a mechanism to detect and recover from collisions. Examples of contention-based protocols are carrier sense multiple access/collision detection (CSMA/CD), used in Ethernet networks, and carrier sense multiple access/collision avoidance (CSMA/CA), used in wireless networks.
  - Token-passing protocols use a special frame, called a token, that circulates among the devices in a logical ring or bus topology. Only the device that holds the token can transmit data, and it must release the token after a certain time or amount of data. Examples of token-passing protocols are token ring and token bus, used in some wired networks, and IEEE 802.11, used in some wireless networks.
- Local area networks (LANs) are networks that connect devices within a limited geographic area, such as a building or a campus. LANs typically use MAC protocols to coordinate the access of devices to a shared medium, such as a coaxial cable, a twisted pair, a fiber optic cable, or a radio frequency band.
- LANs can be classified into different types based on their topology, transmission technology, and performance. Some common types of LANs are:
  - Ethernet: A wired LAN that uses CSMA/CD as the MAC protocol and operates at speeds ranging from 10 Mbps to 10 Gbps. Ethernet can use different physical media, such as coaxial cable, twisted pair, or fiber optic cable, and different topologies, such as bus, star, or mesh.
  - Wireless LAN (WLAN): A wireless LAN that uses CSMA/CA as the MAC protocol and operates at frequencies in the 2.4 GHz or 5 GHz bands. WLANs can use different standards, such as IEEE 802.11, Wi-Fi, or Bluetooth, and different topologies, such as infrastructure, ad hoc, or mesh.
  - Token ring: A wired LAN that uses token-passing as the MAC protocol and operates at speeds of 4 Mbps or 16 Mbps. Token ring uses a logical ring topology and a physical star topology, where each device is connected to a hub or a switch.
  - Token bus: A wired LAN that uses token-passing as the MAC protocol and operates at speeds of 5 Mbps or 10 Mbps. Token bus uses a logical bus topology and a physical tree topology, where each device is connected to a branch of a coaxial cable.
  - FDDI: A wired LAN that uses token-passing as the MAC protocol and operates at speeds of 100 Mbps. FDDI uses a dual ring topology and a fiber optic cable as the physical medium. FDDI can support long distances and high reliability.



#### Channel allocation in medium access control

- Channel allocation is the process of assigning different frequency bands or time slots to different users or transmitters in a wireless network.
- Channel allocation aims to maximize the network throughput, fairness, and spectrum efficiency while minimizing the interference, latency, and energy consumption.
- Medium access control (MAC) is the mechanism that coordinates the access to the channel among multiple users or transmitters.
- MAC protocols can be classified into two main categories: single-channel and multi-channel.
- Single-channel MAC protocols use only one common channel for all the users or transmitters in the network. They can be further divided into contention-based and contention-free protocols.
- Contention-based protocols allow users or transmitters to compete for the channel access using random or deterministic methods. Examples of contention-based protocols are ALOHA, CSMA, and TDMA.
- Contention-free protocols allocate the channel access to users or transmitters in advance using a centralized or distributed scheme. Examples of contention-free protocols are FDMA, CDMA, and OFDMA.
- Multi-channel MAC protocols use more than one channel for the users or transmitters in the network. They can be further divided into fixed and dynamic protocols.
- Fixed protocols assign a fixed number of channels to each user or transmitter based on their traffic demand or priority. Examples of fixed protocols are FAMA and DCA.
- Dynamic protocols allow users or transmitters to switch between different channels based on the channel availability or quality. Examples of dynamic protocols are SSCH and MC-LMAC.



#### Multiple access protocols in medium access control

Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model  . These protocols allow a number of nodes or users to access a shared network channel.

Some of the design criteria for multiple access protocols are:

- Efficiency: The protocol should maximize the utilization of the channel and minimize the overhead and delay.
- Fairness: The protocol should allocate the channel fairly among the competing nodes or users and avoid starvation or domination.
- Robustness: The protocol should be able to handle different traffic patterns and network conditions and adapt to changes in the network topology or size.
- Simplicity: The protocol should be easy to implement and maintain and have low cost and complexity.

Multiple access protocols can be classified into three main categories :

- Random access protocols: In these protocols, all stations have equal priority and can send data depending on the medium's state (idle or busy). There is no fixed time for sending data and collisions may occur. Examples of random access protocols are ALOHA, Carrier Sense Multiple Access (CSMA), CSMA with Collision Avoidance (CSMA/CA) and CSMA with Collision Detection (CSMA/CD).
- Controlled access protocols: In these protocols, a station needs to obtain permission from a central authority or follow a predefined order before sending data. There is a fixed time for sending data and collisions are avoided. Examples of controlled access protocols are Reservation, Polling and Token Passing.
- Channelization protocols: In these protocols, the channel is divided into smaller sub-channels that are assigned to different stations or users. There is no contention for the channel and collisions are avoided. Examples of channelization protocols are Frequency Division Multiple Access (FDMA), Time Division Multiple Access (TDMA) and Code Division Multiple Access (CDMA).



#### LAN standards in local area network

- LAN standards are a set of rules and specifications that define how devices communicate and share resources in a local area network (LAN).
- LAN standards are developed and maintained by various organizations, such as the Institute of Electrical and Electronics Engineers (IEEE), the International Organization for Standardization (ISO), and the Internet Engineering Task Force (IETF).
- LAN standards cover various aspects of network design and operation, such as physical layer, data link layer, network layer, transport layer, and application layer protocols, as well as network topology, media access control, addressing, routing, security, and quality of service.
- Some of the most common and widely used LAN standards are:

  - **IEEE 802**: A family of standards for LANs, personal area networks (PANs), and metropolitan area networks (MANs), such as Ethernet, Wi-Fi, Bluetooth, and WiMAX  .
  - **Ethernet**: A standard for wired LANs that uses a bus or star topology and a carrier sense multiple access with collision detection (CSMA/CD) protocol to transmit data over twisted pair, coaxial, or optical fiber cables .
  - **Wi-Fi**: A standard for wireless LANs that uses radio frequency (RF) signals to transmit data over the air using various modulation and coding schemes, such as orthogonal frequency-division multiplexing (OFDM) and quadrature amplitude modulation (QAM) .
  - **Bluetooth**: A standard for wireless PANs that uses short-range RF signals to connect devices, such as smartphones, laptops, headphones, and speakers, using a frequency-hopping spread spectrum (FHSS) technique and a master-slave network topology .
  - **WiMAX**: A standard for wireless MANs that uses microwave signals to provide broadband wireless access to devices, such as modems, routers, and laptops, using a point-to-multipoint network topology and a time division multiple access (TDMA) protocol .

- LAN standards are important for ensuring interoperability, compatibility, and reliability of network devices and applications, as well as facilitating network management, maintenance, and troubleshooting.



#### Link layer switches & bridges in local area network

- A **link layer switch** is a network device that operates at the data link layer (layer 2) of the OSI model and forwards Ethernet frames between devices on a local area network (LAN).
- A **bridge** is a similar device that can also connect multiple LANs or different types of LANs, such as Ethernet and token ring, using MAC addresses to forward frames.
- Both switches and bridges use a **MAC address table** to store the mappings between MAC addresses and ports, and update the table dynamically by learning from the source addresses of incoming frames.
- Switches and bridges can **reduce collisions** and increase the available bandwidth on a LAN by dividing it into smaller segments or collision domains. Each port on a switch or a bridge is a separate collision domain.
- Switches and bridges can also perform **filtering** and **forwarding** decisions based on the destination MAC address of a frame. If the destination MAC address is not in the MAC address table, the device broadcasts the frame to all ports except the incoming port. If the destination MAC address is in the MAC address table, the device forwards the frame to the corresponding port. If the destination MAC address is the same as the incoming port, the device discards the frame.
- Switches and bridges can improve the **security** and **performance** of a LAN by isolating traffic and preventing unauthorized access. However, they cannot prevent broadcast storms or loops, which can cause network congestion and instability. To prevent loops, switches and bridges use a protocol called **Spanning Tree Protocol (STP)**, which dynamically disables some ports and creates a loop-free logical topology.



#### Learning bridge algorithms in local area network

A bridge is a device that connects two or more local area networks (LANs) at the data link layer and forwards packets based on the destination MAC address. Bridge algorithms are the methods that bridges use to learn the MAC addresses of the devices connected to the LANs and to decide which packets to forward or discard.

There are two main types of bridge algorithms that are commonly used in interconnected LANs: Spanning Tree (ST) and Source Routing (SR). Both of them are specified by the IEEE 802 standards committee .

- Spanning Tree (ST) algorithm: This algorithm creates a loop-free logical topology of the interconnected LANs by disabling some of the bridge ports. It uses a distributed protocol to elect a root bridge and assign a cost to each bridge port based on the distance from the root. Then, it selects the ports that are part of the shortest path from each bridge to the root and enables them, while blocking the others. The ST algorithm also handles topology changes by detecting link failures or additions and updating the port states accordingly. The ST algorithm is transparent to the end devices, meaning that they do not need to know about the existence of bridges or the logical topology.

- Source Routing (SR) algorithm: This algorithm requires the end devices to know about the existence of bridges and the physical topology of the interconnected LANs. It uses a special field in the MAC header of the packets to store the route information, which is a sequence of bridge identifiers that the packet needs to traverse. The end devices obtain the route information by sending special packets called explorer packets, which are broadcasted by the bridges and returned to the source with the route information. The SR algorithm does not create a loop-free logical topology, but relies on the end devices to avoid loops and select the best route. The SR algorithm is more flexible and efficient than the ST algorithm, but also more complex and costly.

Some of the factors that affect the performance of the bridge algorithms are:

- The size and topology of the network: Larger and more complex networks may require more bridge ports, more explorer packets, and more updates to maintain the logical topology.
- The traffic pattern and load: Different types of traffic, such as unicast, multicast, or broadcast, may have different impacts on the bridge algorithms. For example, broadcast traffic may cause more congestion and overhead in the SR algorithm, while unicast traffic may benefit from the route optimization. The traffic load may also affect the delay and throughput of the packets.
- The bridge design and implementation: The bridge algorithms may have different hardware and software requirements, such as memory, processing power, and protocol support. The bridge design may also affect the reliability and scalability of the network.



#### Spanning Tree Algorithms in Local Area Network

- Spanning tree algorithms are used to prevent loops and broadcast storms in Ethernet networks that have redundant links between switches or bridges.
- Spanning tree algorithms work by selecting one switch or bridge as the root of the network, and then disabling some of the links that are not part of the shortest path from the root to the other nodes.
- The most common spanning tree algorithm is the Spanning Tree Protocol (STP), which is standardized by IEEE 802.1D. STP uses a set of parameters, such as bridge ID, port priority, and path cost, to determine the best link for each node to reach the root.
- STP also has a mechanism to detect and recover from link failures, by enabling the backup links that were previously disabled. STP can take up to 50 seconds to converge after a topology change, which can cause temporary network disruptions.
- A variant of STP is the Rapid Spanning Tree Protocol (RSTP), which is standardized by IEEE 802.1w. RSTP reduces the convergence time by using a faster handshake process between switches, and by designating some ports as alternate or backup ports that can quickly take over in case of a failure.
- Another variant of STP is the Multiple Spanning Tree Protocol (MSTP), which is standardized by IEEE 802.1s. MSTP allows the creation of multiple spanning trees for different VLANs, which can improve the load balancing and fault tolerance of the network. MSTP also supports RSTP features for faster convergence.



## Unit 3 - Network Layer in Computer Networks

- The network layer is the third layer of the OSI reference model     .
- The network layer controls the operation of the subnet   .
- The main aim of this layer is to deliver packets from source to destination across multiple links (networks)    .
- The network layer is involved both at the source host and the destination host .
- The network layer manages options pertaining to host and network addressing, managing sub-networks, and internetworking  .
- The network layer takes the responsibility for routing packets from source to destination within or outside a subnet   .
- The network layer also handles packet fragmentation and reassembly, error control, congestion control, and quality of service  .
- The network layer can be divided into two sub-layers: the logical network sub-layer and the internet sub-layer.
- The logical network sub-layer provides network layer services to the transport layer and handles network layer addressing and routing.
- The internet sub-layer handles the encapsulation and decapsulation of packets, and interacts with the data link layer.
- Some of the protocols used at the network layer are: IP, ICMP, ARP, RARP, IGMP, etc  .



### Point-to-point networks in network layer

- Point-to-point networks are networks that connect two devices directly without any intermediate devices or networks.
- Point-to-point networks are commonly used for wide area network (WAN) connections between routers or between a router and a host.
- Point-to-point networks require a data link layer protocol to encapsulate network layer packets into frames for transmission over the link.
- One of the most widely used data link layer protocols for point-to-point networks is the Point-to-Point Protocol (PPP).
- PPP has the following features and functions:
  - It can support multiple network layer protocols, such as IP, IPX, or AppleTalk, by using a field in the frame header to indicate the type of the encapsulated packet.
  - It can provide authentication, encryption, and compression of the data transmitted over the link, by using optional extensions and subprotocols.
  - It can dynamically negotiate and configure the parameters of the link, such as the maximum transmission unit (MTU), the quality of service (QoS), or the network layer address, by using the Link Control Protocol (LCP).
  - It can support multiple logical connections over the same physical link, by using the Multilink Protocol (MP).
  - It can support tunneling of point-to-point connections over other networks, such as the Internet, by using the Point-to-Point Tunneling Protocol (PPTP) or the Layer 2 Tunneling Protocol (L2TP).



### Logical addressing in network layer

- Logical addressing is a way of identifying devices on a network using addresses that are assigned by a network layer protocol, such as IP or IPX.
- Logical addresses are different from physical addresses, which are the hardware addresses of the network interface cards (NICs) in the devices.
- Logical addresses are also called network addresses or layer 3 addresses, as they are used by the network layer of the OSI model.
- Logical addresses are independent of the underlying physical network and can be changed or reconfigured without affecting the physical connectivity of the devices.
- Logical addresses allow devices to communicate across different types of networks, such as LANs, WANs, or the Internet, by providing a uniform addressing scheme that can be routed and translated by network devices, such as routers and gateways.
- Logical addresses consist of two parts: a network identifier and a host identifier. The network identifier specifies the network to which the device belongs, and the host identifier specifies the device within that network.
- The format and size of the logical addresses depend on the network layer protocol that is used. For example, IPv4 addresses are 32 bits long and are usually written in dotted decimal notation, such as 192.168.1.1. IPv6 addresses are 128 bits long and are usually written in hexadecimal notation, such as 2001:db8::1.
- Logical addresses are assigned to devices either statically or dynamically. Static addressing means that the logical address is manually configured on the device and does not change. Dynamic addressing means that the logical address is automatically obtained from a server, such as DHCP, and may change over time.



### Basic internetworking in network layer

- Internetworking is the process of connecting different types of networks using routers and other devices to form a larger network that can exchange data across different protocols and architectures .
- The network layer is responsible for providing logical addressing, routing, and packet forwarding between networks .
- The standard reference model for internetworking is the Open Systems Interconnection (OSI) model, which defines seven layers of communication functions .
- The network layer is the third layer in the OSI model and corresponds to the internetwork layer in the Internet reference model.
- The network layer uses network-layer addresses, also known as IP addresses, to identify and locate hosts and routers in an internetwork .
- The network layer also uses data-link layer addresses, also known as MAC addresses, to identify and locate physical network interfaces of a network device.
- The network layer relies on protocols such as the Internet Protocol (IP), the Internet Control Message Protocol (ICMP), and the Internet Group Management Protocol (IGMP) to perform its functions.
- The network layer can be divided into two sublayers: the network layer core and the network layer interface.
- The network layer core is responsible for routing packets across multiple networks using algorithms and tables.
- The network layer interface is responsible for encapsulating and decapsulating packets with the appropriate headers and trailers for the data-link layer.
- The network layer can support different types of internetworks, such as the Internet, intranets, and extranets .
- The Internet is a global network of networks that uses the TCP/IP protocol suite and the IP addressing scheme  .
- An intranet is a private network of networks that uses the same technologies as the Internet but is accessible only to authorized users within an organization .
- An extranet is a network of networks that extends an intranet to include authorized users from outside the organization, such as customers, suppliers, or partners .



#### IP

IP can have different meanings depending on the context:

- In the context of **network communication**, IP stands for **Internet Protocol**, which is a set of specifications that standardize how data packets move through a network. IP is the defining set of protocols that enable the modern internet. Every device that connects to the internet has a unique IP address, which enables users to find it. IP is often used with TCP (Transmission Control Protocol), which ensures reliable and ordered delivery of data packets. The combination of IP and TCP is known as TCP/IP.
- In the context of **commerce and innovation**, IP stands for **Intellectual Property**, which refers to creations of the mind, such as inventions, literary and artistic works, designs, symbols, names and images used in commerce. IP is protected in law by, for example, patents, copyright and trademarks, which enable people to earn recognition or financial benefit from what they invent or create.
- In the context of **sports**, IP stands for **Innings Pitched**, which is a statistic that measures how many innings a pitcher has completed in a game or a season. An inning is a unit of play in baseball and softball, in which each team has a turn to bat and score runs. IP is used to calculate other pitching statistics, such as earned run average (ERA) and strikeouts per nine innings (K/9).



#### CIDR
- CIDR stands for Classless Inter-Domain Routing, a method for allocating IP addresses and for IP routing .
- CIDR replaces the previous classful network addressing architecture on the Internet, which was based on fixed-length network prefixes.
- CIDR allows blocks of IP addresses to be grouped into single routing table entries, which reduces the size and complexity of routing tables on routers across the Internet .
- CIDR also enables more efficient use of the available IP address space, especially for IPv4, which has been exhausted since 2011.
- CIDR notation is a compact representation of an IP address and its associated routing prefix. It consists of an IP address, a slash (/), and a number that indicates the length of the prefix in bits .
- For example, 192.168.1.0/24 is a CIDR notation that represents the IP address 192.168.1.0 and its prefix of 24 bits, which corresponds to the network mask 255.255.255.0. This means that the network has 256 possible host addresses, from 192.168.1.0 to 192.168.1.255.
- CIDR notation can also be used to specify a range of IP addresses, by using a hyphen (-) to indicate the lower and upper bounds of the range. For example, 192.168.1.0-192.168.1.255/24 is equivalent to 192.168.1.0/24.
- CIDR notation is widely used in network configuration, routing protocols, firewall rules, and access control lists .



#### ARP

- ARP stands for Address Resolution Protocol .
- It is a protocol or procedure that connects an ever-changing Internet Protocol (IP) address to a fixed physical machine address, also known as a media access control (MAC) address, in a local-area network (LAN).
- It is used to resolve the IP address, specially IPV4, to the hardware address.
- It is a dynamic mapping technique that accepts the logical address from the IP protocol and maps the address to the corresponding physical address and then passes it to the data link layer.
- It operates in two modes: request and reply.
- In request mode, a host sends an ARP request packet to the broadcast address of the network, asking for the MAC address of the host with a specific IP address.
- In reply mode, the host with the requested IP address sends an ARP reply packet to the host that sent the request, providing its MAC address.
- ARP maintains a cache or table of IP-MAC address mappings in each host to reduce the number of ARP requests and replies.
- ARP is a stateless protocol, meaning it does not keep track of the status or availability of the hosts in the network.
- ARP is vulnerable to various attacks, such as ARP spoofing, ARP poisoning, and ARP flooding, that can compromise the network security and performance.



#### RARP

- RARP stands for Reverse Address Resolution Protocol, which is a network protocol used to obtain an IP address from a MAC address.
- RARP operates on the Network Access Layer of the TCP/IP protocol stack, which is the lowest layer that deals with data transmission between two points in a network.
- RARP works by sending a broadcast message to a RARP server on the same local area network (LAN), containing the MAC address of the requesting device. The RARP server then looks up its table or cache of MAC-to-IP mappings and replies with the corresponding IP address, if found.
- RARP was published in 1984 and was used for address assignment for network hosts that did not have a permanent IP address, such as diskless workstations. However, RARP had some limitations, such as:
  - It required a RARP server on each LAN segment, which increased the network administration overhead.
  - It could not provide any additional information, such as subnet mask, default gateway, or domain name server, that a host might need to configure its network interface.
  - It could not handle dynamic address allocation or address reuse, which are essential for large-scale networks.
- RARP was eventually replaced by BOOTP and DHCP, which are more advanced and flexible protocols for address assignment and configuration. RARP is now considered obsolete and is rarely used in modern networks.



#### DHCP

- DHCP stands for Dynamic Host Configuration Protocol .
- It is a network management protocol that automatically assigns IP addresses and other communication parameters to devices connected to a network using a client-server architecture  .
- It simplifies the configuration and administration of IP networks, as it eliminates the need for manual intervention or pre-allocation of IP resources   .
- It operates on four basic steps: discover, offer, request, and acknowledge  .
  - Discover: The client broadcasts a DHCPDISCOVER message to find a DHCP server on the network  .
  - Offer: The DHCP server responds with a DHCPOFFER message that contains an IP address and other configuration information for the client  .
  - Request: The client sends a DHCPREQUEST message to accept the offer and request the IP address and configuration information from the server  .
  - Acknowledge: The server sends a DHCPACK message to confirm the IP address and configuration information to the client  .
- It supports different types of IP address allocation methods, such as static, dynamic, and automatic .
  - Static: The DHCP server assigns a fixed IP address to a specific client based on its MAC address .
  - Dynamic: The DHCP server assigns an IP address from a pool of available addresses for a limited period of time (called a lease) .
  - Automatic: The DHCP server assigns an IP address from a pool of available addresses for an indefinite period of time (until the client releases it) .
- It is based on the Bootstrap Protocol (BOOTP), which is an older protocol for IP address allocation .
- It is defined by RFCs 2131 and 2132, and has been extended by several other RFCs to support additional features and options .



#### ICMP

- ICMP stands for Internet Control Message Protocol.
- It is a network layer protocol that devices use to communicate problems or errors with data transmission .
- It is part of the Internet protocol suite as defined in RFC 792.
- It is mainly used to determine whether data is reaching its intended destination in a timely manner .
- Some common types of ICMP messages are:
  - Echo request and echo reply: used to test the connectivity and latency between two devices (e.g. ping command).
  - Destination unreachable: sent when a device cannot reach the destination IP address or port.
  - Time exceeded: sent when a packet has exceeded its time-to-live (TTL) value and has been discarded.
  - Parameter problem: sent when a device detects an error in the header of an IP packet.
  - Source quench: sent when a device is experiencing congestion and requests the sender to reduce the transmission rate.
  - Redirect: sent when a device knows a better route for a packet and advises the sender to use it.
- ICMP messages have a fixed header of 8 bytes, followed by a variable length data field that contains information relevant to the message type.
- The header consists of four fields:
  - Type: 8 bits, identifies the type of ICMP message.
  - Code: 8 bits, provides more details about the type of ICMP message.
  - Checksum: 16 bits, used to verify the integrity of the ICMP message.
  - Rest of header: 32 bits, varies depending on the type and code of the ICMP message.
- ICMP messages are encapsulated within IP datagrams and have a protocol number of 1 in the IP header.
- ICMP messages are not reliable, meaning they may be lost, delayed, or reordered during transmission.
- ICMP messages are not secured, meaning they may be spoofed, altered, or intercepted by malicious actors.
- ICMP messages may be filtered or blocked by firewalls or routers for security or performance reasons.



### Routing in network layer

- Routing is the process of finding the best path for a packet to reach its destination in a network .
- Routing is performed by a special device known as a router, which works at the network layer in the OSI model and internet layer in TCP/IP model.
- A router is a networking device that forwards the packet based on the information available in the packet header and forwarding table. The forwarding table is a data structure that maps destination addresses to outgoing interfaces or next-hop routers.
- The routing algorithms are used for calculating the optimal routes and updating the forwarding tables. Routing algorithms can be classified into two types: static and dynamic.
- Static routing algorithms use fixed routes that are manually configured or rarely changed. Static routing is simple, fast, and secure, but it cannot adapt to network changes or failures.
- Dynamic routing algorithms use current network conditions, such as traffic load, link failures, or topology changes, to update the routes periodically or on demand. Dynamic routing is more flexible and scalable, but it requires more computation, communication, and memory resources.
- Some examples of dynamic routing algorithms are distance vector, link state, and path vector.
- Distance vector algorithms use the hop count or the total distance to the destination as the metric to find the shortest path. Each router exchanges its distance vector with its neighbors and updates its own vector based on the Bellman-Ford equation. An example of distance vector algorithm is the Routing Information Protocol (RIP).
- Link state algorithms use the link cost or the delay to the destination as the metric to find the lowest cost path. Each router broadcasts its link state to all other routers in the network and builds a complete map of the network topology. Then, each router applies Dijkstra's algorithm to find the shortest path tree. An example of link state algorithm is the Open Shortest Path First (OSPF).
- Path vector algorithms use the entire path to the destination as the metric to find the loop-free path. Each router exchanges its path vector with its neighbors and updates its own vector based on the path selection criteria. An example of path vector algorithm is the Border Gateway Protocol (BGP).



### Forwarding and Delivery in Network Layer

- The network layer is the third layer of the OSI model that is responsible for source-to-destination or host-to-host delivery of packets across multiple networks.
- The delivery of a packet is called **direct** if the deliverer (host or router) and the destination are on the same network; the delivery of a packet is called **indirect** if the deliverer (host or router) and the destination are on different networks.
- The network layer supervises the handling of the packets by the underlying physical networks. This handling is defined as the **delivery**.
- The network layer takes the data from the transport layer, adds its header, and forwards it to the data link layer.
- The network layer header contains the source and destination network addresses, which are used to route the packet through the network.
- The network layer provides two main functions: **forwarding** and **routing**.
- **Forwarding** refers to the router-local action of transferring a packet from an input link interface to the appropriate output link interface.
- **Routing** refers to the network-wide process that determines the end-to-end paths that packets take from source to destination.
- Forwarding is based on the routing table that is stored in each router. The routing table maps a destination network address to an output link interface.
- Routing is based on the routing algorithms that are used to compute the routing tables. Routing algorithms can be classified into two types: **static** and **dynamic**.
- **Static routing** algorithms use fixed routing tables that are manually configured by the network administrator. Static routing is simple and reliable, but it cannot adapt to network changes or failures.
- **Dynamic routing** algorithms use routing protocols that exchange information among routers to update their routing tables. Dynamic routing is more flexible and robust, but it requires more computation and communication overhead.
- Some examples of routing protocols are: **Distance Vector Routing**, **Link State Routing**, **Hierarchical Routing**, **Broadcast Routing**, **Multicast Routing**, and **Anycast Routing** .



### Static and dynamic routing in computer networks

- Static routing and dynamic routing are two methods used to determine how to send a packet toward its destination.
- Static routes are configured in advance of any network communication. Static routing is often used for small networks or as a backup for dynamic routing.
- Dynamic routing, on the other hand, requires routers to exchange information with other routers to learn about paths through the network. Dynamic routing is often used for large networks or to adapt to changing network conditions.
- Some of the key differences between static and dynamic routing are  :
  - Path selection: Static routing uses a single preconfigured route to send traffic to its destination, while dynamic routing uses complex routing algorithms to select the best route based on various factors such as hop count, bandwidth, load, etc.
  - Ability to update routes: Network administrators must manually reconfigure static routes in order to adjust routes or add new destinations, while dynamic routing automatically updates routes based on the information received from other routers.
  - Routing overhead: Static routing does not generate any routing overhead, as no routing messages are exchanged between routers, while dynamic routing consumes some network bandwidth and router resources to exchange routing information and maintain routing tables.
  - Security: Static routing provides more security, as the routes are not exposed to other routers or potential attackers, while dynamic routing provides less security, as the routing information can be intercepted or manipulated by malicious actors.
  - Scalability: Static routing is not scalable, as it becomes difficult and error-prone to manage static routes for large networks, while dynamic routing is scalable, as it can handle network growth and changes without manual intervention.



### Routing algorithms and protocols in computer networks

- Routing is the process of finding and selecting the best path for data transmission from source to destination in a computer network .
- Routing algorithms are the software programs that implement the logic of routing, i.e., deciding the optimal path for each packet based on various factors such as distance, cost, congestion, etc .
- Routing protocols are the set of rules and messages that routers use to communicate with each other and exchange routing information .
- There are three major classes of routing protocols in IP networks:
  - Interior gateway protocols (IGPs) are used within a single autonomous system (AS), which is a group of routers under the same administrative control. IGPs can be further divided into two types:
    - Link-state routing protocols, such as OSPF and IS-IS, which maintain a complete map of the network topology and calculate the shortest path to each destination using an algorithm like Dijkstra's.
    - Distance-vector routing protocols, such as RIP, RIPv2, and IGRP, which exchange information about the distance and direction to each destination with their neighboring routers and update their routing tables accordingly.
  - Exterior gateway protocols (EGPs) are used between different autonomous systems, which are usually owned by different organizations or ISPs. EGPs enable inter-domain routing and exchange network reachability information. The most common EGP is the Border Gateway Protocol (BGP).
  - Hybrid routing protocols, such as EIGRP and Babel, which combine the features of both link-state and distance-vector routing protocols and can operate in both intra-domain and inter-domain scenarios.
- Routing algorithms and protocols are essential for the efficient and reliable operation of computer networks. They enable data to flow between different parts of the network and adapt to changing network conditions and demands .



### Congestion control algorithms in computer networks

- Congestion control algorithms are mechanisms that control the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse.
- Congestive collapse is a situation where the network performance degrades drastically due to excessive traffic and congestion.
- Congestion control algorithms can be broadly classified into two categories: open loop and closed loop.
- Open loop congestion control policies are applied to prevent congestion before it happens. They involve designing the network and choosing the appropriate protocols and parameters to avoid congestion.
- Closed loop congestion control policies are applied to detect and mitigate congestion after it happens. They involve monitoring the network state and adjusting the transmission rate or window size of the senders based on feedback signals such as packet losses and delays.
- Some examples of open loop congestion control techniques are admission control, traffic shaping, and resource reservation.
- Some examples of closed loop congestion control techniques are congestion avoidance, congestion recovery, and congestion pricing.
- Congestion avoidance algorithms are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network. They use additive increase/multiplicative decrease (AIMD) scheme, along with other schemes such as slow start and congestion window (CWND), to achieve congestion avoidance.
- Congestion recovery algorithms are implemented at the TCP layer as the mechanism to recover from congestion after it happens. They use fast retransmit, fast recovery, and selective acknowledgment (SACK) schemes to recover from packet losses and retransmit the missing data.
- Congestion pricing algorithms are implemented at the network layer as the mechanism to allocate network resources based on the demand and supply of bandwidth. They use economic principles such as marginal cost pricing, smart market, and progressive second price auction to charge users for using the network resources.



### IPv6 in China

- IPv6 is the latest version of the Internet Protocol, which provides virtually unlimited IP addresses for electronic devices to communicate online.
- China is one of the leading countries in IPv6 deployment and adoption, with over 400 million active IPv6 users as of January 2023.
- China has set a goal of running a single-stack IPv6 network by 2030, which means that all devices and applications will use IPv6 only and not rely on IPv4.
- China has also issued a notice to accelerate the large-scale deployment and application of IPv6, which requires all government agencies, public institutions, enterprises, and internet service providers to implement IPv6 transition plans and report their progress regularly.
- China's motivation for embracing IPv6 is to cope with the increasing demand for internet access, especially from mobile devices, and to enhance its network security, innovation, and global competitiveness .
- China also wants to shape the IPv6 standards and promote its own technologies and solutions in the global market.



## Unit 4 - Transport Layer in Computer Networks

The transport layer is the fourth layer of the OSI model and the third layer of the TCP/IP model. It is responsible for providing end-to-end communication between applications running on different hosts in a network. The transport layer performs the following functions:

- **Segmentation and reassembly**: The transport layer divides the data received from the application layer into smaller units called segments, and adds a header to each segment with information such as source and destination port numbers, sequence numbers, and checksums. The transport layer at the receiving end reassembles the segments into the original data and delivers it to the application layer.
- **Connection management**: The transport layer establishes, maintains, and terminates logical connections between applications. Some transport layer protocols, such as TCP, use a three-way handshake to establish a connection-oriented service, while others, such as UDP, provide a connectionless service that does not require any connection setup or teardown.
- **Flow control**: The transport layer regulates the rate of data transmission between the sender and the receiver to avoid congestion and buffer overflow. Flow control can be implemented using mechanisms such as sliding window, stop-and-wait, or backpressure.
- **Error control**: The transport layer detects and corrects errors that may occur during data transmission. Error control can be implemented using mechanisms such as checksum, acknowledgment, retransmission, or forward error correction.
- **Multiplexing and demultiplexing**: The transport layer enables multiple applications to share the same network resources by using port numbers to identify different processes. Multiplexing is the process of combining data from multiple sources into a single stream, while demultiplexing is the process of separating data from a single stream into multiple destinations.
- **Quality of service**: The transport layer can provide different levels of service to different applications based on their requirements. Quality of service can be measured by parameters such as bandwidth, delay, jitter, or reliability.

The transport layer protocols can be classified into two categories: reliable and unreliable. Reliable protocols, such as TCP, guarantee the delivery of data in the correct order and without any loss or duplication. Unreliable protocols, such as UDP, do not provide any guarantee of data delivery and may lose, reorder, or duplicate data. Reliable protocols are suitable for applications that require high accuracy and consistency, such as web browsing, email, or file transfer. Unreliable protocols are suitable for applications that can tolerate some loss or delay, such as video streaming, voice over IP, or online gaming.



### Process-to-process delivery in transport layer

- The transport layer is the fourth layer of the OSI model, which provides services to the application layer.
- The transport layer is responsible for **process-to-process delivery**, which means the delivery of a packet, part of a message, from one process to another.
- A process is an entity of the application layer that uses the services of the transport layer. Two processes can communicate in a client/server or a peer-to-peer relationship.
- To achieve process-to-process delivery, the transport layer needs to perform the following tasks:
  - **Addressing**: The transport layer assigns a unique identifier, called a **port number**, to each process that wants to communicate with another process. A port number is a 16-bit integer that ranges from 0 to 65535. The port number is added to the packet header by the transport layer protocol .
  - **Multiplexing and demultiplexing**: The transport layer can handle multiple processes at the same time, each with a different port number. This is called **multiplexing**, which means combining data from several processes into one packet. The reverse process, which means separating data for different processes from one packet, is called **demultiplexing** .
  - **Segmentation and reassembly**: The transport layer can divide a long message into smaller units, called **segments**, and add a header to each segment. The header contains information such as the source and destination port numbers, the sequence number, the acknowledgment number, and the checksum. The segments are then sent to the network layer, which encapsulates them into datagrams. At the receiver side, the transport layer reassembles the segments into the original message. This is called **reassembly** .
  - **Connection control**: The transport layer can establish, maintain, and terminate a logical connection between two processes. A logical connection is a set of rules and parameters that define how the communication will take place. The transport layer can use either a **connection-oriented** or a **connectionless** protocol to provide connection control. A connection-oriented protocol requires a three-way handshake to establish a connection before data transfer, and a four-way handshake to terminate a connection after data transfer. A connectionless protocol does not require any connection establishment or termination, and sends data as independent packets .
  - **Flow control**: The transport layer can regulate the amount of data that a sender can transmit to a receiver, to prevent the receiver from being overwhelmed. The transport layer can use either a **stop-and-wait** or a **sliding window** mechanism to provide flow control. A stop-and-wait mechanism requires the sender to wait for an acknowledgment from the receiver before sending the next segment. A sliding window mechanism allows the sender to send multiple segments without waiting for acknowledgments, as long as the number of segments does not exceed the size of the window .
  - **Error control**: The transport layer can detect and correct errors that may occur during the transmission of data. The transport layer can use either a **checksum** or a **cyclic redundancy check (CRC)** to provide error control. A checksum is a value that is calculated from the data in the segment, and added to the header. The receiver can verify the checksum and request a retransmission if there is a mismatch. A CRC is a more complex and reliable method that uses a polynomial function to generate a code from the data in the segment, and append it to the end of the segment. The receiver can use the same polynomial function to check the code and request a retransmission if there is an error .
  - **Reliable delivery**: The transport layer can ensure that the data is delivered to the destination process without any loss, duplication, or corruption. The transport layer can use a combination of sequence numbers, acknowledgments, timers, and retransmissions to provide reliable delivery. A sequence number is a value that indicates the order of the segments in the message. An acknowledgment is a message that confirms the receipt of a segment. A timer is a device that measures the time elapsed since the sending of a segment. A retransmission is the sending of a segment again if there is no acknowledgment or if there is an error .
- The transport layer can use different protocols to provide different levels of service to the application layer. Some of the common transport layer protocols are:
  -



### Transport layer protocols

- Transport layer protocols are responsible for providing end-to-end communication services for applications over a network .
- Transport layer protocols use port numbers to identify different applications or processes that communicate with each other.
- Transport layer protocols can be classified into two categories: connection-oriented and connectionless .
  - Connection-oriented protocols establish a logical connection between the sender and the receiver before exchanging data, and maintain the connection until the data transfer is complete. They also provide reliable data delivery, error detection and correction, flow control, and congestion control. An example of a connection-oriented protocol is the Transmission Control Protocol (TCP) .
  - Connectionless protocols do not establish or maintain a connection between the sender and the receiver, and do not guarantee reliable data delivery, error detection and correction, flow control, or congestion control. They are suitable for applications that require fast and efficient data transfer, but can tolerate some data loss or corruption. An example of a connectionless protocol is the User Datagram Protocol (UDP) .
- Some transport layer protocols that have been defined and implemented for specific purposes include the Datagram Congestion Control Protocol (DCCP) and the Stream Control Transmission Protocol (SCTP).



#### UDP Transport layer protocol

- UDP stands for User Datagram Protocol. It is a transport layer protocol that provides process-to-process communication in the internet protocol suite .
- UDP is a connectionless and unreliable protocol. It does not establish a connection before sending data, and it does not guarantee that the data will be delivered or received in order or without errors .
- UDP is a simple protocol with minimum overhead. It adds only four fields to the data: source port, destination port, length, and checksum. The source and destination ports identify the processes that send and receive the data. The length indicates the size of the UDP header and data. The checksum is used to detect errors in the header and data .
- UDP is suitable for applications that require fast and efficient transmission of small amounts of data, such as real-time audio and video streaming, online gaming, and DNS queries. UDP does not incur the overhead of connection establishment, congestion control, flow control, or retransmission of lost or corrupted packets .
- UDP is also used by some protocols that run on top of it, such as the Trivial File Transfer Protocol (TFTP), the Simple Network Management Protocol (SNMP), and the Routing Information Protocol (RIP). These protocols implement their own reliability and error recovery mechanisms on top of UDP.



#### TCP Transport layer protocol

- TCP stands for Transmission Control Protocol  .
- It is a transport layer protocol that facilitates the transmission of packets from source to destination   .
- It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network  .
- TCP is a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data  .
- TCP provides reliable, ordered, and error-checked delivery of a stream of octets between applications running on hosts communicating via an IP network.
- TCP has three main steps: establish connection, send packets of data, and close the connection.
  - Establish connection: When two computers want to send data to each other over TCP, they first need to establish a connection using a three-way handshake .
  - Send packets of data: When a packet of data is sent over TCP, the recipient must always acknowledge what they received. If the sender does not receive an acknowledgment within a certain time, it will resend the packet. This ensures that no data is lost or corrupted .
  - Close the connection: When the data transmission is complete, the sender and the receiver exchange messages to terminate the connection gracefully .
- TCP is used by many applications that require reliable and ordered delivery of data, such as web browsing, email, file transfer, and remote login .



### Multiplexing in transport layer

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver.
- Multiplexing at the transport layer involves adding transport headers to the data chunks received from different sockets and passing them to the network layer.
- The transport headers contain information such as source port number, destination port number, sequence number, acknowledgment number, etc. that help to identify the corresponding application processes at the receiver side.
- The transport layer can use either connection-oriented or connectionless multiplexing, depending on the protocol used (TCP or UDP).
- Connection-oriented multiplexing requires establishing a connection between the sender and the receiver before exchanging data, and maintaining the state of the connection throughout the communication.
- Connectionless multiplexing does not require any connection establishment or state maintenance, and relies on the port numbers to deliver the data to the correct socket.
- Demultiplexing is the reverse process of multiplexing, which is delivering the data to the correct socket by the transport layer at the receiver side.
- Demultiplexing at the transport layer involves extracting the transport headers from the segments received from the network layer, and using the information in the headers to direct the data to the appropriate socket.
- The transport layer can use either connection-oriented or connectionless demultiplexing, depending on the protocol used (TCP or UDP).
- Connection-oriented demultiplexing uses the source and destination port numbers, as well as the source and destination IP addresses, to identify the correct socket.
- Connectionless demultiplexing uses only the destination port number to identify the correct socket.
- Multiplexing and demultiplexing are the services facilitated by the transport layer to extend the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts.



### Connection management in transport layer

- The transport layer is responsible for creating and managing the end-to-end connections between hosts for data transmission.
- The transport layer uses two main protocols: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
- TCP is a reliable, connection-oriented protocol that uses a three-way handshake to establish a connection between two hosts . TCP ensures that the data is delivered in order and without errors, and also provides flow control and congestion control mechanisms.
- UDP is an unreliable, connectionless protocol that does not guarantee the delivery, order, or integrity of the data. UDP is faster and simpler than TCP, and is used for applications that do not require reliability, such as streaming media or online games.
- Connection management in TCP involves three phases: connection establishment, data transfer, and connection termination.
- Connection establishment is initiated by the client, which sends a SYN segment to the server, requesting a connection. The server responds with a SYN-ACK segment, acknowledging the request and sending its own sequence number. The client then sends an ACK segment, confirming the connection and sending its initial window size. This completes the three-way handshake and the connection is established.
- Data transfer is the phase where the actual data is exchanged between the hosts. TCP uses a sliding window protocol to control the amount of data that can be sent and received at a time. TCP also uses acknowledgments, retransmissions, and timers to ensure the reliability of the data transfer. TCP also adapts to the network conditions by adjusting the window size and the congestion window, which are parameters that determine how much data can be sent without causing congestion.
- Connection termination is the phase where the hosts close the connection gracefully. Either host can initiate the connection termination by sending a FIN segment, indicating that it has no more data to send. The other host responds with an ACK segment, acknowledging the FIN. The host that sent the FIN then waits for a FIN from the other host, and sends an ACK when it receives it. This completes the four-way handshake and the connection is terminated.



### Flow control in transport layer

- Flow control is a mechanism that regulates the amount of data that can be sent and received between two communicating nodes.
- Flow control is needed in transport layer because it provides end-to-end communication services for applications across different networks.
- Flow control in transport layer prevents data loss due to congestion, buffer overflow, or mismatched speeds between the sender and the receiver.
- Flow control in transport layer can be implemented using different techniques, such as:
  - Sliding window: The sender and the receiver maintain a window of acceptable sequence numbers that indicate how much data can be sent or received at a time. The window size can be adjusted dynamically based on the feedback from the receiver or the network conditions.
  - Stop-and-wait: The sender sends one data unit at a time and waits for an acknowledgment from the receiver before sending the next one. This technique is simple but inefficient, as it wastes the bandwidth and introduces delays.
  - Go-back-N: The sender can send multiple data units without waiting for acknowledgments, but it has to keep a copy of each one in case of retransmission. The receiver sends cumulative acknowledgments for the last received data unit in order. If the sender does not receive an acknowledgment within a timeout period, it retransmits all the data units from the last acknowledged one.
  - Selective repeat: The sender can send multiple data units without waiting for acknowledgments, but it only retransmits the ones that are lost or corrupted. The receiver sends selective acknowledgments for each received data unit individually. This technique reduces the number of retransmissions and improves the efficiency.



### etransmission in transport layer

- The transport layer is a layer in the network stack that provides end-to-end communication services for applications.
- The transport layer is responsible for ensuring that the data transmitted by the application layer is delivered reliably, efficiently, and in the correct order to the destination application layer.
- One of the functions of the transport layer is error control, which involves detecting and correcting errors that may occur during data transmission.
- Error control is achieved through retransmission of the packet, which means sending the packet again if it is lost, delayed, corrupted, or duplicated .
- The transport layer uses two mechanisms to trigger retransmission of packets: duplicate acknowledgements (ACK) and retransmission timers.
- Duplicate ACKs are sent by the receiver when it detects a gap in the sequence of received packets, indicating that some packets are missing or out of order.
- Retransmission timers are set by the sender for each packet, and if the timer expires before receiving an ACK, the sender assumes that the packet is lost and retransmits it.
- The transport layer also provides congestion control, which involves preventing or removing congestion in the network, which can cause packet loss, delay, and reduced throughput.
- Congestion control can be open loop or closed loop, depending on whether it acts before or after congestion occurs.
- Open loop congestion control involves avoiding congestion by regulating the rate of data transmission or the number of packets in the network.
- Closed loop congestion control involves detecting congestion by measuring the network parameters, such as packet loss, delay, or queue length, and adjusting the data transmission accordingly.
- The transport layer can use different protocols to perform its functions, such as Transmission Control Protocol (TCP) or User Datagram Protocol (UDP).
- TCP is a reliable, connection-oriented, and stream-oriented protocol that provides error control, congestion control, flow control, and in-order delivery of data.
- UDP is an unreliable, connectionless, and datagram-oriented protocol that provides minimal error control, no congestion control, no flow control, and no guarantee of in-order delivery of data.
- The choice of protocol depends on the requirements of the application layer, such as reliability, efficiency, or real-time communication.



### Window management in transport layer

- The transport layer is the layer that provides end-to-end communication between applications on different hosts in a network.
- The transport layer uses protocols such as Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) to ensure reliable and efficient data transfer.
- Window management is a technique used by TCP to control the flow of data between the sender and the receiver.
- A window is a buffer that stores the data packets that are sent or received by TCP.
- The sender has a send window that indicates how many packets it can send before waiting for an acknowledgment from the receiver.
- The receiver has a receive window that indicates how many packets it can receive before sending an acknowledgment to the sender.
- The size of the send and receive windows can vary depending on the network conditions and the available buffer space.
- The sender and the receiver use a sliding window technique to adjust the window size dynamically.
- The sliding window technique involves moving the window forward as the packets are sent or received, and acknowledging the packets that are successfully delivered.
- The sliding window technique allows TCP to achieve optimal throughput and avoid congestion and packet loss.
- The sliding window technique can be implemented using different algorithms, such as stop-and-wait, go-back-N, and selective repeat.



### TCP Congestion Control in Transport Layer

- TCP (Transmission Control Protocol) is a connection-oriented transport layer protocol that provides reliable and ordered delivery of data packets between source and destination.
- TCP congestion control is a mechanism that prevents the network from being overloaded by regulating the amount of data that a TCP sender can inject into the network.
- TCP congestion control consists of three main components: congestion window, congestion avoidance algorithm, and congestion detection and recovery.
- Congestion window (cwnd) is a variable that limits the number of unacknowledged packets that a TCP sender can have in the network at any time. It is dynamically adjusted by the congestion avoidance algorithm based on the network conditions.
- Congestion avoidance algorithm is a set of rules that determines how the cwnd is increased or decreased. There are different variants of congestion avoidance algorithms, such as AIMD (Additive Increase Multiplicative Decrease), Reno, NewReno, Vegas, Cubic, etc. The most common one is AIMD, which increases the cwnd by one segment per round trip time (RTT) when there is no congestion, and halves the cwnd when congestion is detected .
- Congestion detection and recovery is a process that identifies the occurrence of congestion and takes appropriate actions to recover from it. TCP uses two main indicators of congestion: packet loss and delay. Packet loss is detected by the absence of acknowledgments (ACKs) from the receiver, and delay is measured by the round trip time (RTT) of the packets. TCP uses different mechanisms to handle packet loss and delay, such as retransmission timeout (RTO), fast retransmit, fast recovery, selective acknowledgment (SACK), etc .
- TCP congestion control has three phases: slow start, congestion avoidance, and congestion detection.
  - Slow start is the initial phase of congestion control, where the sender starts with a small cwnd (usually one or two segments) and doubles it every RTT until it reaches a threshold (ssthresh) or detects congestion.
  - Congestion avoidance is the phase where the sender increases the cwnd more slowly (by one segment per RTT) to avoid causing congestion. This phase continues until congestion is detected or the cwnd reaches the receiver's advertised window (rwnd), which is the maximum amount of data that the receiver can accept.
  - Congestion detection is the phase where the sender detects congestion by packet loss or delay and reduces the cwnd accordingly. Depending on the mechanism used, the sender may also enter a fast recovery phase, where it tries to recover the lost packets without reducing the cwnd too much.



### Quality of service in transport layer

- Quality of service (QoS) is the use of mechanisms or technologies that work on a network to control traffic and ensure the performance of critical applications with limited network capacity.
- The transport layer is responsible for enhancing the QoS provided by the network layer by offering reliable, end-to-end data delivery services to the application layer.
- The transport layer can provide QoS in terms of throughput, delay, jitter, reliability, security, etc. depending on the requirements of the application layer.
- The transport layer can use different protocols and techniques to achieve QoS, such as:
  - Transport connection: The transport layer establishes the transport connection by sending a request and specifying the transport addresses, QoS requirements, and collect addresses services.
  - Reliable data transport: The transport layer can use error detection, retransmission, acknowledgment, and flow control mechanisms to ensure the correct and timely delivery of data packets.
  - Congestion control and rate control: The transport layer can adjust the sending rate and window size of the sender to avoid network congestion and packet loss.
  - Single packet delivery or block delivery: The transport layer can deliver data packets individually or in blocks depending on the application needs.
- The transport layer can also use different QoS models, such as:
  - Integrated services (IntServ): This model requires the reservation of network resources along the path of the data flow using signaling protocols such as RSVP.
  - Differentiated services (DiffServ): This model assigns different priorities to different types of traffic using packet marking and classification techniques.
  - Multiprotocol label switching (MPLS): This model uses labels to route packets along predetermined paths with guaranteed QoS.
- The transport layer and QoS are especially important in wireless sensor networks, where the network capacity, energy, and reliability are limited.



## Unit 5 - Application Layer in Computer Networks

- The application layer is the **topmost layer** of the Open Systems Interconnection (OSI) model and the Internet Protocol Suite (TCP/IP) model.
- The application layer **specifies** the shared communications protocols and interface methods used by hosts in a communications network.
- The application layer is **not** an application, but a set of services that support applications across different computer systems and networks.
- The application layer is where users **interact** with the network, download information and send data.
- The application layer **ensures** that an application can effectively communicate with other applications on different computer systems and networks.
- The application layer **provides** various functions and benefits, such as:
  - Email services: This layer allows users to forward several emails and it also provides a storage facility.
  - File transfer: This layer allows users to access, retrieve and manage files in a remote computer.
  - Remote login: This layer allows users to log on as a remote host.
  - Directory services: This layer provides access to global information about various objects and resources.
  - Web browsing: This layer enables users to access and view web pages using hypertext transfer protocol (HTTP).
  - Voice over IP: This layer enables users to make and receive voice calls over the internet using H.323 protocol.
  - Digital currency: This layer enables users to exchange and verify transactions using Bitcoin protocol.
- The application layer **uses** various protocols to perform its functions, such as:
  - HTTP: Hypertext Transfer Protocol is used for web browsing and message communications.
  - SMTP: Simple Mail Transfer Protocol is used for sending and receiving emails.
  - FTP: File Transfer Protocol is used for transferring files between hosts.
  - Telnet: Telnet is used for remote login and terminal emulation.
  - LDAP: Lightweight Directory Access Protocol is used for queries of user information.
  - DNS: Domain Name System is used for resolving host names to IP addresses.
  - H.323: H.323 is used for packet-based communications, such as voice over IP.
  - Bitcoin: Bitcoin is used for digital currency and peer-to-peer transactions.



### Domain Name System

- The Domain Name System (DNS) is a service that translates domain names into Internet Protocol (IP) addresses. Domain names are the human-readable names of websites, such as google.com or wikipedia.org. IP addresses are the numerical identifiers of computers or devices on the internet, such as 142.250.64.78 or 198.35.26.96.
- DNS works like a phone book that contains all the public domains and their corresponding IP addresses. When a user types a domain name in a web browser or an app, the request is sent to a DNS server, which looks up the domain name and returns the matching IP address. The browser or app then connects to the IP address and loads the website or resource.
- DNS is a hierarchical and distributed system that consists of various components and levels. The main components of DNS are:

  - **Root servers**: These are the servers that store the information about the top-level domains (TLDs), such as .com, .org, .net, etc. There are 13 root servers in the world, each with multiple copies and locations for redundancy and performance.
  - **TLD servers**: These are the servers that store the information about the second-level domains (SLDs), such as google.com, wikipedia.org, etc. Each TLD server is responsible for a specific TLD or a group of TLDs.
  - **Authoritative servers**: These are the servers that store the information about the subdomains and records of a specific SLD, such as mail.google.com, en.wikipedia.org, etc. Each authoritative server is managed by the owner or administrator of the SLD.
  - **Recursive servers**: These are the servers that act as intermediaries between the user and the DNS system. They receive the user's query and perform a series of requests to the root, TLD, and authoritative servers until they find the answer. They also cache the results for future queries to improve efficiency and speed.
  - **Resolver**: This is the software component that runs on the user's device and initiates the DNS query. It communicates with the recursive server and returns the IP address to the browser or app.

- DNS uses various types of records to store different kinds of information. Some of the common record types are:

  - **A record**: This is the most basic type of record that maps a domain name to an IPv4 address, such as google.com -> 142.250.64.78.
  - **AAAA record**: This is similar to an A record, but maps a domain name to an IPv6 address, such as google.com -> 2607:f8b0:4006:80a::200e.
  - **CNAME record**: This is a type of record that maps a domain name to another domain name, such as mail.google.com -> googlemail.l.google.com. This is useful for creating aliases or redirecting traffic.
  - **MX record**: This is a type of record that specifies the mail server that handles the email for a domain name, such as google.com -> aspmx.l.google.com. This is useful for sending and receiving email.
  - **NS record**: This is a type of record that specifies the authoritative server that is responsible for a domain name, such as google.com -> ns1.google.com. This is useful for delegating authority and maintaining consistency.
  - **TXT record**: This is a type of record that stores arbitrary text information for a domain name, such as google.com -> "v=spf1 include:_spf.google.com ~all". This is useful for verifying ownership, providing security, or adding metadata.



### World Wide Web

- The World Wide Web (WWW) is an information system that enables documents and other web resources to be accessed over the Internet.
- The WWW is not the same as the Internet, which is a global network of computers that can communicate with each other. The WWW is a service that operates over the Internet, just as email and Usenet do.
- The WWW consists of webpages that are linked by hyperlinks, which are references to other webpages or web resources. Users can click on hyperlinks to navigate from one webpage to another.
- The WWW was invented by Tim Berners-Lee, a British computer scientist, in 1989 at CERN, a European research organization. He proposed a system to share and organize information among researchers using hypertext, a way of presenting text with embedded links.
- The first web browser, called WorldWideWeb, was also created by Berners-Lee in 1990. It was a graphical user interface that allowed users to view and edit webpages. The first web server, which stored and delivered webpages, was also set up by Berners-Lee at CERN.
- The WWW gained rapid acceptance with the creation of a web browser called Mosaic, which was developed in the United States by Marc Andreessen and others at the National Center for Supercomputing Applications at the University of Illinois and was released in September 1993. Mosaic was the first web browser to display images and multimedia content along with text, making the WWW more attractive and accessible to the general public.
- The WWW has grown exponentially since its inception, becoming the dominant source of information and communication on the Internet. The WWW has enabled the development of many applications and services, such as e-commerce, social media, online education, entertainment, and news. The WWW has also transformed various fields and industries, such as science, business, politics, and culture.



### Hyper Text Transfer Protocol

- Hyper Text Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML .
- HTTP is the underlying protocol used by the World Wide Web, developed by Tim Berners-Lee .
- HTTP defines how messages are formatted and transmitted, and what actions Web servers and browsers should take in response to various commands .
- HTTP is a stateless protocol, meaning that each request is independent of the previous one and does not store any information about the client or the server .
- HTTP uses a client-server model, where the client initiates a request and the server responds with a status code and a message body .
- HTTP requests and responses have a common structure, consisting of a start-line, zero or more headers, an empty line, and an optional message body .
- HTTP requests have a method, a Uniform Resource Identifier (URI), and a version. The method indicates the action to be performed on the resource, such as GET, POST, PUT, DELETE, etc .
- HTTP responses have a version, a status code, and a reason phrase. The status code indicates the outcome of the request, such as 200 OK, 404 Not Found, 500 Internal Server Error, etc .
- HTTP headers provide additional information about the request or the response, such as the content type, the content length, the date, the server name, the cookies, etc .
- HTTP message body contains the actual data to be sent or received, such as HTML documents, images, forms, etc .
- HTTP supports different types of content negotiation, such as language, encoding, media type, etc., to allow the client and the server to agree on the best format for the data exchange .
- HTTP also supports different types of authentication, caching, compression, redirection, and security mechanisms to enhance the functionality and performance of the protocol .



### Electronic mail in application layer

- Electronic mail (or e-mail) is an application layer service that allows users to exchange messages and information over the internet .
- E-mail is one of the most popular and widely used services of the internet.
- E-mail has a client-server architecture, where the clients are the user agents that send and receive e-mails, and the servers are the mail servers that store and forward e-mails .
- E-mail uses several application layer protocols to perform different functions, such as:
  - Simple Mail Transfer Protocol (SMTP) is used to transfer e-mails from the sender's mail server to the receiver's mail server  .
  - Post Office Protocol (POP) and Internet Message Access Protocol (IMAP) are used to retrieve e-mails from the receiver's mail server to the receiver's user agent  .
  - Multipurpose Internet Mail Extensions (MIME) is used to encode and decode e-mails that contain multimedia content, such as images, audio, video, etc  .
- E-mail has a standard format that consists of two parts: the header and the body  .
  - The header contains information such as the sender's address, the receiver's address, the subject, the date, etc  .
  - The body contains the actual message or content of the e-mail  .
- E-mail provides several benefits, such as:
  - It is fast, convenient, and inexpensive .
  - It can support multiple recipients and attachments  .
  - It can store and manage e-mails on the remote server or the local user agent  .
  - It can access global information and services through the internet.



### File Transfer Protocol in application layer

- File Transfer Protocol (FTP) is an application layer protocol that is used to transfer files between local and remote devices over the Internet .
- FTP runs on top of TCP, which provides reliable and ordered delivery of data packets .
- FTP uses two parallel TCP connections for each file transfer: a control connection and a data connection  .
- The control connection is used to exchange commands and responses between the FTP client and the FTP server. It remains open throughout the file transfer session .
- The data connection is used to transfer the actual file data between the FTP client and the FTP server. It is opened and closed for each file transfer .
- FTP supports both text and binary files, and can handle different types of file systems and formats .
- FTP requires a plaintext (unencrypted) sign-in process, which involves a username and a password. This makes FTP vulnerable to eavesdropping and unauthorized access .
- FTP can operate in two modes: active mode and passive mode. In active mode, the FTP client initiates both the control and data connections. In passive mode, the FTP client initiates the control connection, but the FTP server initiates the data connection .
- FTP can be used for various applications, such as uploading and downloading files, updating websites, backing up data, transferring large files, and sharing files among users.
- FTP best practices include using secure FTP (SFTP) or FTP over SSL (FTPS) to encrypt the data and sign-in process, choosing strong passwords, limiting the number of concurrent connections, restricting the access permissions, and scanning the files for malware.



### Remote login in application layer

- Remote login is a service that allows a user to access a remote system over a network, such as the Internet, and execute commands on that system.
- Remote login is an example of an application layer protocol, which is a set of rules and formats that define how data is exchanged between applications on different systems.
- Remote login protocols typically use a client-server model, where the client is the user's system and the server is the remote system. The client initiates a connection request to the server, and the server responds by asking for authentication credentials, such as a username and password. If the credentials are valid, the server grants access to the client and establishes a virtual terminal session, where the client can send commands and receive responses from the server.
- Some common remote login protocols are:

  - Telnet: A simple and widely used protocol that allows a user to access a remote system over a TCP/IP network. Telnet does not provide any encryption or security features, so the data exchanged between the client and the server is vulnerable to eavesdropping and tampering.
  - Secure Shell (SSH): A more secure and advanced protocol that provides encryption, authentication, and compression for remote login sessions. SSH also supports features such as port forwarding, file transfer, and tunneling, which allow a user to access other network services through the SSH connection.
  - Remote Desktop Protocol (RDP): A protocol that allows a user to access the graphical user interface (GUI) of a remote system over a network. RDP enables a user to see and control the desktop, applications, and files of the remote system, as if they were sitting in front of it. RDP also supports features such as audio, video, and printer redirection, which allow a user to use the local devices on the remote system.



### Network management in application layer

- Network management is the process of monitoring, controlling, and optimizing the performance and security of a network system.
- The application layer is the topmost layer in the Open System Interconnection (OSI) model, which defines how different devices communicate over a network.
- The application layer provides the interface and protocols for users and applications to access network services, such as file transfer, email, web browsing, remote login, etc.
- Network management in the application layer involves the following functions and benefits:
  - Identifying communication partners: The application layer helps to establish the identity and availability of the network entities that want to communicate, such as hosts, servers, routers, etc. This can be done using name resolution, which maps human-readable names to IP addresses, or using directory services, which store information about network resources and users.
  - Synchronizing communication: The application layer helps to coordinate the timing and sequencing of data exchange between the communication partners, such as by using timestamps, acknowledgments, flow control, etc. This ensures that the data is delivered reliably and efficiently.
  - Representing data: The application layer helps to format and encode the data in a way that is understandable and compatible for both the sender and the receiver, such as by using character sets, compression, encryption, etc. This ensures that the data is transmitted securely and accurately.
  - Providing network services: The application layer helps to implement the specific functions and features of the network applications, such as by using protocols, standards, and APIs. For example, HTTP is a protocol that defines how web servers and browsers communicate, SMTP is a protocol that defines how email servers and clients communicate, etc.
  - Managing network resources: The application layer helps to monitor and control the network resources that are used by the network applications, such as by using Simple Network Management Protocol (SNMP), which allows network administrators to collect and modify information about network devices, or by using CiscoWorks2000, which allows network administrators to manage the configuration, inventory, and syslog of network devices.



### Data compression in application layer

- Data compression is the function of presentation layer in OSI reference model.
- Data compression allows to reduce the number of bits that needs to be transmitted on the network.
- Data compression can optimize disk space when saving data.
- Data compression can be performed by various algorithms, such as Huffman coding, Lempel-Ziv coding, run-length encoding, etc.
- Data compression can be lossless or lossy, depending on whether the original data can be recovered exactly or not.
- Data compression can improve the performance and efficiency of network applications, such as email, file transfer, web browsing, etc.
- Data compression can also reduce the bandwidth consumption and network congestion.
- Data compression can be combined with other functions of presentation layer, such as data encryption, character set conversion, interpretation of graphics commands, etc .
- Data compression can be implemented by various protocols, such as GZIP, ZIP, JPEG, MP3, etc.



### Cryptography in application layer

- Cryptography is the process of converting plain text into cipher text, which is unintelligible and vice-versa. It provides secure communication in the presence of adversaries.
- Application layer encryption is a data-security solution that encrypts nearly any type of data passing through an application. When encryption occurs at this level, data is encrypted across multiple (including disk, file, and database) layers .
- Application layer encryption increases security by reducing the number of potential attack vectors. It also gives developers more control over what gets encrypted and who gets the keys for decryption.
- End-to-end encryption is an increasingly popular type of application-layer encryption. This type of encryption lets organizations enforce access control using key management as well as policy. In some cases, the users themselves may be the only parties with the keys.
- Some examples of applications that use application layer encryption are messaging apps, email clients, cloud storage services, and web browsers. These applications use various cryptographic algorithms and protocols to protect the data from unauthorized access, modification, or disclosure.



### Basic concepts of cryptography in application layer

Cryptography is the science of securing communications from unauthorized parties. It involves the use of mathematical techniques to transform plain text into cipher text, which is unintelligible, and vice versa. Cryptography can provide confidentiality, integrity and authenticity to the data transmitted or stored in applications.

Some of the basic concepts of cryptography in application layer are:

- **Symmetric key cryptography**: This is a type of cryptography where the same key is used for both encryption and decryption. The key must be shared securely between the communicating parties. Symmetric key cryptography is fast and efficient, but it suffers from the key distribution problem. Examples of symmetric key algorithms are AES, DES, RC4, etc.

- **Asymmetric key cryptography**: This is a type of cryptography where a pair of keys is used for encryption and decryption. One key is called the public key, which can be shared openly, and the other is called the private key, which must be kept secret. The public key can be used to encrypt a message, which can only be decrypted by the corresponding private key, and vice versa. Asymmetric key cryptography solves the key distribution problem of symmetric key cryptography, but it is slower and more complex. Examples of asymmetric key algorithms are RSA, ECC, DSA, etc.

- **Hash functions**: These are mathematical functions that map an arbitrary input to a fixed-length output, called the hash or digest. Hash functions are one-way, meaning that it is easy to compute the hash from the input, but hard to find the input from the hash. Hash functions can be used to verify the integrity of data, by comparing the hash of the original data with the hash of the received data. Examples of hash functions are SHA, MD5, etc.

- **Digital signatures**: These are a way of using asymmetric key cryptography to provide authenticity and non-repudiation to data. A digital signature is generated by applying a hash function to the data, and then encrypting the hash with the private key of the sender. The receiver can verify the signature by decrypting the hash with the public key of the sender, and comparing it with the hash of the data. Digital signatures can prove that the data was sent by the sender, and that it was not altered in transit.

- **Public key infrastructure (PKI)**: This is a system of managing the public keys and digital certificates of the entities involved in a cryptographic communication. A digital certificate is a document that binds the identity of an entity to its public key, and is issued by a trusted authority, called the certificate authority (CA). PKI can be used to establish the trustworthiness of the public keys and the identities of the entities, and to revoke the certificates if they are compromised. Examples of PKI standards are X.509, PGP, etc.

