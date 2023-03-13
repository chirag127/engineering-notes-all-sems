

A computer network is a system of interconnected devices that can communicate and share data. There are different types of computer networks, such as local area network (LAN), wide area network (WAN), personal area network (PAN), metropolitan area network (MAN), and wireless network. Each type of network has its own characteristics, such as size, speed, security, and topology.

A network topology is the arrangement of the nodes and connections in a network. It determines how the data flows between the devices and how the network can be managed and maintained. There are several common network topologies, such as bus, ring, star, mesh, tree, and hybrid. Each topology has its advantages and disadvantages, depending on the network requirements and constraints.

The following diagram illustrates the basic architecture of a computer network, using the star topology as an example. In a star network, each device is connected to a central hub or switch, which acts as the point of communication and control. The hub or switch can be a router, a server, or a dedicated device. The star topology is simple, easy to install and troubleshoot, and allows for high performance and scalability. However, it also has some drawbacks, such as high cost, dependency on the central device, and vulnerability to single point of failure.

# Computer Networks

```
    +--------+          +--------+
    | Device |          | Device |
    +--------+          +--------+
        |                   |
        |                   |
        |                   |
        |                   |
        |                   |
        |                   |
+--------+--------+ +--------+--------+
|      Hub/Switch | |      Hub/Switch |
+--------+--------+ +--------+--------+
        |                   |
        |                   |
        |                   |
        |                   |
        |                   |
        |                   |
    +--------+          +--------+
    | Device |          | Device |
    +--------+          +--------+
```



## Unit 1 - Introductory Concepts of Computer Networks and Physical Layer

A computer network is any group of interconnected computing devices capable of sending or receiving data. A computing device can be a computer, a tablet, a phone, or a smart sensor. Computer networks can be classified by their size, topology, architecture, and protocols.

The physical layer is the lowest layer of the OSI model of computer networking . It is responsible for the actual physical connection between the devices . It defines the hardware equipment, cabling, wiring, frequencies, pulses, and binary signals used to transmit and receive data. It also coordinates the functions required to carry a bit stream over a physical medium. It provides its services to the data-link layer, which is the next higher layer in the OSI model .

The following diagram illustrates the basic architecture of a computer network and the physical layer using ASCII art:

```
+--------+    +--------+    +--------+    +--------+
| Device |----| Device |----| Device |----| Device |
+--------+    +--------+    +--------+    +--------+
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
+--------+    +--------+    +--------+    +--------+
| Router |----| Router |----| Router |----| Router |
+--------+    +--------+    +--------+    +--------+
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
+--------+    +--------+    +--------+    +--------+
| Switch |----| Switch |----| Switch |----| Switch |
+--------+    +--------+    +--------+    +--------+
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
+--------+    +--------+    +--------+    +--------+
| Hub    |----| Hub    |----| Hub    |----| Hub    |
+--------+    +--------+    +--------+    +--------+
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
+--------+    +--------+    +--------+    +--------+
| Cable  |----| Cable  |----| Cable  |----| Cable  |
+--------+    +--------+    +--------+    +--------+
    |             |             |             |
    |             |             |             |
    |             |             |             |
    |             |             |             |
+--------+    +--------+    +--------+    +--------+
| Device |----| Device |----| Device |----| Device |
+--------+    +--------+    +--------+    +--------+

```

The devices can be any computing devices that can send or receive data. The routers, switches, hubs, and cables are examples of physical layer devices that facilitate the data transmission and reception . The routers are responsible for routing the data packets to the correct destination. The switches are responsible for connecting multiple devices in a network and forwarding the data packets to the appropriate device. The hubs are responsible for connecting multiple devices in a network and broadcasting the data packets to all the devices. The cables are responsible for carrying the electrical or optical signals between the devices.



### Introductory Concepts of Computer Networks

A computer network is a group of computers that are connected to each other using cables, wireless signals, or other media, for the purpose of transmitting, exchanging, or sharing data and resources . Computer networks follow protocols, which are rules that define how communications are sent and received.

There are several essential components of a computer network, such as:

- End devices: These are the devices that send or receive the data in the network, such as computers, printers, scanners, etc.
- Media: These are the physical or logical means that provide connectivity between the end devices, such as cables, fiber optics, radio waves, etc.
- Protocols: These are the sets of rules that enable communication between two or more end devices, such as TCP/IP, HTTP, FTP, etc.
- Networking devices: These are the devices that facilitate the transmission and routing of data in the network, such as routers, switches, hubs, etc.

Computer networks can be classified based on different criteria, such as:

- Size: The geographical area covered by the network, such as LAN (Local Area Network), WAN (Wide Area Network), MAN (Metropolitan Area Network), etc.
- Topology: The physical or logical arrangement of the network nodes and links, such as bus, ring, star, mesh, etc.
- Architecture: The design and structure of the network, such as peer-to-peer, client-server, etc.

The following diagram illustrates the basic architecture of a computer network using ASCII art:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    End device   |       |    End device   |       |    End device   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Networking     |-------|  Networking     |-------|  Networking     |
|    device       |       |    device       |       |    device       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Media        |       |    Media        |       |    Media        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```



#### Goals and applications of networks and protocols

A network consists of two or more nodes (e.g. computers) that are linked in order to share resources (such as printers and CDs), exchange files, or allow electronic communications. The computers on a network may be linked through cables, telephone lines, radio waves, satellites, or infrared light beams.

A protocol is a set of rules that governs the communication between nodes on a network. Protocols specify the format, timing, sequencing, and error control of data packets that are sent and received by the nodes.

The main goals of networks are  :

- Cost reduction by sharing hardware and software resources.
- High reliability by having multiple sources of supply and backup.
- Greater flexibility by allowing devices to connect and communicate with each other.
- Increased productivity by making it easier to access and process data by multiple users.
- Enhanced security by protecting data from unauthorized access and modification.

Some of the applications of networks are:

- Email: Allows users to send and receive messages across the network.
- World Wide Web: Allows users to access and view web pages hosted on different servers across the network.
- File Transfer Protocol (FTP): Allows users to upload and download files from remote servers across the network.
- Voice over Internet Protocol (VoIP): Allows users to make and receive voice calls over the network using digital signals.
- Streaming: Allows users to watch and listen to audio and video content over the network without downloading it.

The following diagram illustrates the basic architecture of a network using ASCII art:

```
    +-----------------+       +-----------------+       +-----------------+
    |     Node 1      |       |     Node 2      |       |     Node 3      |
    |                 |       |                 |       |                 |
    |  +-----------+  |       |  +-----------+  |       |  +-----------+  |
    |  |   Email   |  |       |  |    Web    |  |       |  |   FTP    |  |
    |  +-----------+  |       |  +-----------+  |       |  +-----------+  |
    |  +-----------+  |       |  +-----------+  |       |  +-----------+  |
    |  |   VoIP    |  |       |  | Streaming |  |       |  |   VoIP    |  |
    |  +-----------+  |       |  +-----------+  |       |  +-----------+  |
    |                 |       |                 |       |                 |
    +-----------------+       +-----------------+       +-----------------+
            |                       |                       |
            |                       |                       |
            |                       |                       |
            |                       |                       |
            |                       |                       |
            |                       |                       |
            |                       |                       |
            |                       |                       |
            |                       |                       |
            |                       |                       |
            |                       |                       |
            +-----------------------+-----------------------+
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                |

```




Categories of networks in computer networks are classifications based on the size, scope, and purpose of the network. There are different types of networks, such as LAN, MAN, WAN, PAN, WLAN, CAN, SAN, POLAN, VPN, etc. Each type of network has its own characteristics, advantages, and disadvantages.

The following is a detailed ASCII diagram for categories of networks in computer networks:

```
+-----------------+    +-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |    |                 |
|      PAN        |    |      LAN        |    |      MAN        |    |      WAN        |
|                 |    |                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+    +-----------------+
| Personal Area   |    | Local Area      |    | Metropolitan    |    | Wide Area       |
| Network         |    | Network         |    | Area Network    |    | Network         |
|                 |    |                 |    |                 |    |                 |
| A network that  |    | A network that  |    | A network that  |    | A network that  |
| connects        |    | connects        |    | connects        |    | connects        |
| devices within  |    | devices within  |    | devices within  |    | devices across  |
| a short range,  |    | a small area,   |    | a city or a     |    | a large area,   |
| such as         |    | such as a home, |    | region, such as |    | such as a       |
| Bluetooth       |    | office, or      |    | a campus or a   |    | country or a    |
| devices,        |    | school, using   |    | town, using     |    | continent,      |
| smartphones,    |    | wired or        |    | wired or        |    | using wired or  |
| smartwatches,   |    | wireless        |    | wireless        |    | wireless        |
| etc.            |    | technologies,   |    | technologies,   |    | technologies,   |
|                 |    | such as         |    | such as         |    | such as         |
|                 |    | Ethernet, Wi-Fi,|    | Ethernet, Wi-Fi,|    | Ethernet,       |
|                 |    | etc.            |    | etc.            |    | satellite,      |
|                 |    |                 |    |                 |    | cellular, etc.  |
+-----------------+    +-----------------+    +-----------------+    +-----------------+
| Example:        |    | Example:        |    | Example:        |    | Example:        |
|                 |    |                 |    |                 |    |                 |
| A wireless      |    | A wired network |    | A wireless      |    | A wired network |
| keyboard and    |    | connecting      |    | network         |    | connecting      |
| mouse           |    | computers and   |    | connecting      |    | offices and     |
| connecting to a |    | printers in an  |    | buildings in a  |    | branches in     |
| laptop via      |    | office via      |    | campus via      |    | different       |
| Bluetooth.      |    | Ethernet cables.|    | Wi-Fi routers.  |    | countries via   |
|                 |    |                 |    |                 |    | submarine       |
|                 |    |                 |    |                 |    | cables.         |
+-----------------+    +-----------------+    +-----------------+    +-----------------+
```



The organization of the Internet can be understood at different levels, such as the physical infrastructure, the access providers, the navigation tools, and the online communities. Each level has its own actors, rules, and protocols that enable the functioning and governance of the Internet.

#### Organization of the Internet

```
+-----------------+    +-----------------+    +-----------------+
| Online          |    | Online          |    | Online          |
| Communities     |    | Communities     |    | Communities     |
+-----------------+    +-----------------+    +-----------------+
| Navigation      |    | Navigation      |    | Navigation      |
| Tools           |    | Tools           |    | Tools           |
+-----------------+    +-----------------+    +-----------------+
| Access          |    | Access          |    | Access          |
| Providers       |    | Providers       |    | Providers       |
+-----------------+    +-----------------+    +-----------------+
| Physical        |    | Physical        |    | Physical        |
| Infrastructure  |    | Infrastructure  |    | Infrastructure  |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
                               |
                               |
                               v
                        +-----------------+
                        | Internet        |
                        | Standards       |
                        +-----------------+
```

The following is a brief explanation of each level of the organization of the Internet:

- Physical infrastructure: This level consists of the hardware and software components that enable the transmission of data over the Internet, such as routers, switches, cables, satellites, servers, computers, and mobile devices. The physical infrastructure is owned and operated by various entities, such as governments, corporations, universities, and individuals.
- Access providers: This level consists of the organizations that provide access to the Internet for users, such as Internet service providers (ISPs), mobile network operators, and public Wi-Fi providers. The access providers are regulated by different laws and policies in different countries, and they may charge fees, impose restrictions, or offer incentives for using their services.
- Navigation tools: This level consists of the applications and platforms that help users find, access, and use information and services on the Internet, such as browsers, search engines, social media, and e-commerce. The navigation tools are developed and maintained by various companies, organizations, and individuals, and they may have their own terms of use, privacy policies, and business models.
- Online communities: This level consists of the groups and networks of users who interact and communicate on the Internet, such as forums, blogs, wikis, chat rooms, and online games. The online communities are formed and governed by their own rules, norms, and cultures, and they may have different purposes, interests, and values.



An ISP (Internet Service Provider) is a company that provides access to the internet and other related services, such as email, web hosting, and domain name registration. An ISP typically has a network of routers, switches, servers, and other devices that connect to the backbone of the internet and to other ISPs. An ISP may also have regional or local networks that serve customers in a specific area.

The following diagram illustrates the basic architecture of an ISP using ASCII characters:

#### ISP

```
+-----------------+       +-----------------+       +-----------------+
| Backbone ISP    |       | Backbone ISP    |       | Backbone ISP    |
| (Level 1)       |       | (Level 1)       |       | (Level 1)       |
+-----------------+       +-----------------+       +-----------------+
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
+-----------------+       +-----------------+       +-----------------+
| Regional ISP    |       | Regional ISP    |       | Regional ISP    |
| (Level 2)       |       | (Level 2)       |       | (Level 2)       |
+-----------------+       +-----------------+       +-----------------+
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
+-----------------+       +-----------------+       +-----------------+
| Local ISP       |       | Local ISP       |       | Local ISP       |
| (Level 3)       |       | (Level 3)       |       | (Level 3)       |
+-----------------+       +-----------------+       +-----------------+
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
         |                         |                         |
+-----------------+       +-----------------+       +-----------------+
| Customer        |       | Customer        |       | Customer        |
| (Level 4)       |       | (Level 4)       |       | (Level 4)       |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows three levels of ISPs:

- Level 1: Backbone ISPs are large international networks that connect to each other and to other ISPs through high-speed fiber optic links. They are the core of the internet and store enormous amounts of data in data centers.
- Level 2: Regional ISPs are smaller networks that connect to one or more backbone ISPs and to other regional or local ISPs. They provide access to customers in a specific geographic area, such as a country or a state.
- Level 3: Local ISPs are the smallest networks that connect to one or more regional ISPs and to customers in a specific location, such as a city or a town. They may use different technologies, such as telephone lines, cable, wireless, or fiber optics, to deliver internet services to customers.

The diagram also shows the level 4 customers, who are the end users of the internet. They may be individuals, households, businesses, or organizations that use the internet for various purposes, such as browsing, emailing, gaming, streaming, or online shopping. Customers may use different devices, such as computers, laptops, smartphones, tablets, or smart TVs, to connect to the internet through their local ISP.



Network structure with reference to Computer Networks is the way network devices and services are structured to serve the connectivity needs of client devices. Network devices typically include switches and routers. Types of services include DHCP and DNS. Client devices comprise end-user devices, servers, and smart things.

One way to represent the network structure is by using the OSI model, which stands for Open System Interconnection. It is a reference model that specifies standards for communications protocols and also the functionalities of each layer. OSI consists of seven layers, and each layer performs a particular network function. The layers are:

- Application layer: Provides services to the user applications, such as email, web browsing, file transfer, etc.
- Presentation layer: Translates data between different formats, such as encryption, compression, character encoding, etc.
- Session layer: Establishes, maintains, and terminates sessions between applications, such as authentication, synchronization, dialog control, etc.
- Transport layer: Provides reliable and error-free data transfer between end systems, such as TCP and UDP protocols.
- Network layer: Routes data packets across different networks, such as IP protocol and routing algorithms.
- Data link layer: Transfers data frames between adjacent nodes, such as Ethernet and MAC addresses.
- Physical layer: Transmits and receives raw bits over a physical medium, such as cables, connectors, modems, etc.

The following diagram illustrates the basic architecture of a network using the OSI model:

```
+-----------------+     +-----------------+     +-----------------+
| Application     |     | Application     |     | Application     |
+-----------------+     +-----------------+     +-----------------+
| Presentation    |     | Presentation    |     | Presentation    |
+-----------------+     +-----------------+     +-----------------+
| Session         |     | Session         |     | Session         |
+-----------------+     +-----------------+     +-----------------+
| Transport       |     | Transport       |     | Transport       |
+-----------------+     +-----------------+     +-----------------+
| Network         |     | Network         |     | Network         |
+-----------------+     +-----------------+     +-----------------+
| Data link       |     | Data link       |     | Data link       |
+-----------------+     +-----------------+     +-----------------+
| Physical        |     | Physical        |     | Physical        |
+-----------------+     +-----------------+     +-----------------+
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
+-----------------+     +-----------------+     +-----------------+
| Switch          |-----| Router          |-----| Switch          |
+-----------------+     +-----------------+     +-----------------+
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
     |                         |                         |
+-----------------+     +-----------------+     +-----------------+
| Client device   |     | Client device   |     | Client device   |
+-----------------+     +-----------------+     +-----------------+
```

Another way to represent the network structure is by using the network topology, which is the layout arrangement of the different devices in a network. Common examples include: Bus, Star, Mesh, Ring, and Daisy chain. Network topology is used to describe the physical and logical structure of a network. It maps the way different nodes on a network--including switches and routers--are placed and interconnected, as well as how data flows. Diagramming the locations of endpoints and service requirements helps determine the best placement for each node to optimize performance, reliability, and security.

The following diagram illustrates the basic architecture of a network using the star topology:

```
+-----------------+
| Switch          |
+-----------------+
     |     |     |
     |     |     |
     |     |     |
     |     |     |
     |     |     |
     |     |     |
     |     |     |
     |     |     |
     |     |     |

```




Network architecture is the design of a computer network. It is a framework for the specification of a network's physical components and their functional organization and configuration, its operational principles and procedures, as well as communication protocols used .

There are different types of network architectures based on the network's size and purpose, such as LAN, WLAN, WAN, MAN, PAN, etc . Each type of network architecture has its own advantages and disadvantages, such as speed, security, cost, scalability, etc.

The following diagram illustrates the basic architecture of a LAN (local area network), which connects computers over a relatively short distance, allowing them to share data, files, and resources. A LAN typically consists of a switch, which connects the computers and other devices on the network, and a router, which connects the LAN to other networks or the internet. The switch and the router can be separate devices or integrated into one device. The computers and other devices on the LAN can communicate with each other using Ethernet cables or wireless signals. The communication protocols used on a LAN can vary, but some common ones are TCP/IP, UDP, and HTTP.

#### Network architecture diagram

```
+-----------------+        +-----------------+
|                 |        |                 |
|   Internet      |        |   LAN           |
|                 |        |                 |
+-----------------+        +-----------------+
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
+-----------------+        +-----------------+
|                 |        |                 |
|   Router        |--------|   Switch        |
|                 |        |                 |
+-----------------+        +-----------------+
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
+-----------------+        +-----------------+
|                 |        |                 |
|   Computer 1    |--------|   Computer 2    |
|                 |        |                 |
+-----------------+        +-----------------+
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
          |                         |
+-----------------+        +-----------------+
|                 |        |                 |
|   Printer       |--------|   Scanner       |
|                 |        |                 |
+-----------------+        +-----------------+
```



The layering principles with reference to network architecture in computer networks are based on the idea of dividing the communication process into smaller and manageable parts, each with a specific function and interface. One of the most widely used models of network architecture is the Open Systems Interconnection (OSI) model, which consists of seven layers: physical, data link, network, transport, session, presentation, and application. The following diagram illustrates the basic architecture of the OSI model using ASCII characters:

```
+------------------------+
| Application            |  <---->  Application layer protocols (e.g. HTTP, FTP, SMTP, etc.)
+------------------------+
| Presentation           |  <---->  Data representation and encryption (e.g. ASCII, JPEG, SSL, etc.)
+------------------------+
| Session                |  <---->  Session management and synchronization (e.g. RPC, NFS, SQL, etc.)
+------------------------+
| Transport              |  <---->  Reliable and unreliable data delivery (e.g. TCP, UDP, etc.)
+------------------------+
| Network                |  <---->  Routing and addressing (e.g. IP, ICMP, ARP, etc.)
+------------------------+
| Data Link              |  <---->  Error detection and correction (e.g. Ethernet, PPP, HDLC, etc.)
+------------------------+
| Physical               |  <---->  Transmission medium and signal encoding (e.g. copper, fiber, radio, etc.)
+------------------------+
```



#### Services in networks architecture in Computer Networks

Services in networks architecture are applications that run at the network application layer and above, and provide various capabilities such as data storage, manipulation, presentation, communication, etc. to the client devices . Services are often implemented using a client-server or peer-to-peer architecture based on application layer network protocols. Some examples of services are DHCP, DNS, FTP, HTTP, SMTP, etc.

The following diagram illustrates the basic architecture of a service in a network using a client-server model:

```
+-----------------+      +-----------------+
|                 |      |                 |
|    Client       |      |    Server       |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
| Application     |      | Application     |
| Layer           |      | Layer           |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
| Transport       |      | Transport       |
| Layer           |      | Layer           |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
| Network         |      | Network         |
| Layer           |      | Layer           |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
| Data Link       |      | Data Link       |
| Layer           |      | Layer           |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
| Physical        |      | Physical        |
| Layer           |      | Layer           |
|                 |      |                 |
+-----------------+      +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        +-----------------------+
                Network
```

The client and the server are two devices that communicate over a network. They both have the same network layer stack, consisting of the application, transport, network, data link, and physical layers. The application layer is where the service runs, and it uses the transport layer to send and receive data packets to and from the network layer. The network layer is responsible for routing the packets across the network, and it uses the data link layer to access the physical medium. The physical layer is the lowest layer that deals with the electrical signals and the physical connection.

The client initiates the communication by sending a request to the server, using the service's protocol. The server responds by sending back the requested data or performing the requested action. The communication can be one-way or two-way, depending on the service and the protocol. The communication can also be synchronous or asynchronous, depending on the timing and the order of the messages. The communication can also be stateful or stateless, depending on whether the server maintains information about the client's state or not.



Protocols and standards in networks architecture are used to define the representation and interaction modes within a network and to make certain functions generally available. Protocols are a set of guidelines governing the exchange of information in a simple, dependable and secure way. Standards are formal specifications that ensure compatibility and interoperability among different devices and systems.

Network architecture is the design of a network that includes the hardware, software, transmission media, network topology, and communication protocols. There are two main types of network architecture: peer-to-peer (P2P) and client/server. P2P networks are decentralized and allow each node to communicate directly with each other without a central server. Client/server networks are centralized and rely on a server to provide services and resources to the clients.

The following diagram illustrates the basic architecture of a client/server network using the TCP/IP protocol suite, which is the most widely used network protocol in the internet. TCP/IP consists of four layers: application, transport, internet, and network interface. Each layer performs specific functions and communicates with the adjacent layers using well-defined interfaces.

```
+-----------------+      +-----------------+
|   Application   |      |   Application   |
|      Layer      |      |      Layer      |
+-----------------+      +-----------------+
|    Transport    |      |    Transport    |
|      Layer      |      |      Layer      |
+-----------------+      +-----------------+
|     Internet    |      |     Internet    |
|      Layer      |      |      Layer      |
+-----------------+      +-----------------+
| Network Interface|     | Network Interface|
|      Layer      |      |      Layer      |
+-----------------+      +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        +-----------------------+
                Network
```



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



The TCP/IP protocol suite is a set of communication protocols that are used in the Internet and similar computer networks. It consists of four layers: the application layer, the transport layer, the internet layer, and the network access layer. Each layer has a specific function and interacts with the adjacent layers.

The application layer provides the interface for the user applications, such as web browsers, email clients, file transfer programs, etc. It uses protocols such as HTTP, SMTP, FTP, etc. to exchange data with the transport layer.

The transport layer provides reliable and efficient data transmission between the application layer and the internet layer. It uses protocols such as TCP and UDP to segment, reassemble, and order the data packets. TCP also provides error detection, flow control, and congestion control mechanisms.

The internet layer provides the routing and addressing functions for the data packets. It uses protocols such as IP, ICMP, ARP, etc. to assign unique IP addresses to each device and to determine the best path for the packets to reach their destination.

The network access layer provides the physical and data link functions for the data packets. It uses protocols such as Ethernet, Wi-Fi, PPP, etc. to encode, decode, and transmit the data packets over the network medium.

The following diagram illustrates the basic architecture of the TCP/IP protocol suite in computer networks:

```
+--------------------------+--------------------------+--------------------------+
|        Application       |        Application       |        Application       |
|          Layer           |          Layer           |          Layer           |
+--------------------------+--------------------------+--------------------------+
|        Transport         |        Transport         |        Transport         |
|          Layer           |          Layer           |          Layer           |
+--------------------------+--------------------------+--------------------------+
|         Internet         |         Internet         |         Internet         |
|          Layer           |          Layer           |          Layer           |
+--------------------------+--------------------------+--------------------------+
|      Network Access      |      Network Access      |      Network Access      |
|          Layer           |          Layer           |          Layer           |
+--------------------------+--------------------------+--------------------------+
|          Media           |          Media           |          Media           |
+--------------------------+--------------------------+--------------------------+
```



Network devices are physical devices that enable communication and interaction between hardware on a computer network. Each networking device operates in a distinct computer network segment and performs distinct functions. A network may require hundreds or thousands of different network devices to maintain and build out various LAN and WAN.

Some of the common types of network devices are:

- Repeater: A repeater is a device that operates at the physical layer and regenerates the signal over the same network. It can extend the transmission distance of a network segment.
- Hub: A hub is a device that operates at the physical layer and connects multiple wires coming from different branches. It broadcasts the data to all the connected devices. It is a passive device that does not filter or modify the data.
- Bridge: A bridge is a device that operates at the data link layer and connects two or more network segments. It filters the data based on the MAC addresses and forwards only the relevant data to the destination segment.
- Switch: A switch is a device that operates at the data link layer and connects multiple devices on a network. It has a buffer and a design that can improve its efficiency. It can learn the MAC addresses of the connected devices and forward the data to the specific port .
- Router: A router is a device that operates at the network layer and routes data packets based on their IP addresses. It can connect different networks and choose the best path for data transmission. It can also perform network address translation (NAT) and firewall functions .
- Gateway: A gateway is a device that operates at the application layer and connects two or more networks that use different protocols. It can translate the data between different formats and perform protocol conversion. It can also act as a proxy server and a firewall.
- Brouter: A brouter is a device that combines the functions of a bridge and a router. It can filter and route data packets based on both MAC and IP addresses. It can also switch between broadcast and routing modes depending on the network traffic.
- NIC: A network interface card (NIC) is a device that operates at the physical and data link layers and enables a computer or a device to connect to a network. It has a unique MAC address and can send and receive data over the network.

#### Network devices in Computer Networks

The following diagram illustrates the basic architecture of a network with some of the network devices:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|      NIC        |     |      NIC        |     |      NIC        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Repeater     |-----|      Hub        |-----|    Repeater     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Bridge      |-----|     Switch      |-----|     Bridge      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Router      |-----|    Gateway      |-----|     Router      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|      NIC        |     |      NIC        |     |      NIC        |
|

```




Network components are the devices and media that are used to connect computers and other devices in a network. Some of the common network components are:

- Server: A server is a computer that provides data and services to other computers and users in the network. For example, a web server, a file server, a mail server, etc.
- Client: A client is a computer or device that requests and receives data and services from a server in the network. For example, a web browser, a file explorer, a mail client, etc.
- Transmission media: Transmission media are the physical or wireless means through which data is transferred from one device to another in a network. For example, copper wires, fiber optic cables, radio waves, etc.
- Network interface card (NIC): A NIC is a hardware device that enables a computer or device to communicate with other devices in the network. It provides a physical connection to the transmission media and converts data into signals that can be transmitted over the media.
- Switch: A switch is a device that connects multiple devices in a network and forwards data packets to the appropriate destination based on the MAC address of the device. It operates at the data link layer of the OSI model and can create separate collision domains in a network.
- Router: A router is a device that connects multiple networks and forwards data packets to the appropriate destination based on the IP address of the device. It operates at the network layer of the OSI model and can create separate broadcast domains in a network.
- Hub: A hub is a device that connects multiple devices in a network and broadcasts data packets to all the connected devices. It operates at the physical layer of the OSI model and does not create separate collision or broadcast domains in a network.
- Firewall: A firewall is a device or software that monitors and controls the incoming and outgoing network traffic based on predefined rules. It can protect a network from unauthorized access, malicious attacks, or unwanted traffic.
- Access point: An access point is a device that allows wireless devices to connect to a wired network. It acts as a bridge between the wireless and wired networks and can extend the coverage of a network.
- Software: Software are the programs and applications that enable the network devices to communicate and perform various functions in a network. For example, network operating systems, network protocols, network services, network security, etc.

The following diagram illustrates the basic architecture of a network using ASCII characters:

```
    +-----------------+           +-----------------+
    |                 |           |                 |
    |      Server     |           |      Server     |
    |                 |           |                 |
    +-----------------+           +-----------------+
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
+-----------------+           +-----------------+
|                 |           |                 |
|      Router     |-----------|      Router     |
|                 |           |                 |
+-----------------+           +-----------------+
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
+-----------------+           +-----------------+
|                 |           |                 |
|      Switch     |           |      Switch     |
|                 |           |                 |
+-----------------+           +-----------------+
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |       |       |
+-----------------+           +-----------------+
|                 |           |                 |
|      Hub        |           |      Hub        |
|                 |           |                 |
+-----------------+           +-----------------+
    |       |       |           |       |       |
    |       |       |           |       |       |
    |       |       |           |

```




The physical layer is the lowest layer of the OSI model of computer networking. It is responsible for transmitting and receiving raw bits over a physical medium, such as cables or wireless signals. It also defines the characteristics of the transmission medium, such as the data rate, the synchronization, the encoding, and the topology.

The following ASCII diagram illustrates the basic architecture of a physical layer in a computer network:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Application  |    |   Application  |    |   Application  |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
| Presentation   |    | Presentation   |    | Presentation   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Session      |    |   Session      |    |   Session      |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Transport    |    |   Transport    |    |   Transport    |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Network      |    |   Network      |    |   Network      |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Data Link    |    |   Data Link    |    |   Data Link    |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Physical     |    |   Physical     |    |   Physical     |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       +--------------------+--------------------+
                 Physical Medium
```

The physical layer communicates with the data link layer above it, and with the physical medium below it. The physical medium can be a twisted pair cable, a coaxial cable, a fiber-optic cable, or a wireless signal. The physical layer converts the bits from the data link layer into electrical, optical, or electromagnetic signals that can be transmitted over the physical medium. It also performs the reverse process when receiving signals from the physical medium.

The physical layer also defines the characteristics of the physical medium, such as the data rate, the synchronization, the encoding, and the topology. The data rate is the number of bits that can be transmitted per second over the physical medium. The synchronization is the process of aligning the sender and the receiver clocks to ensure that the bits are correctly interpreted. The encoding is the method of representing the bits as signals on the physical medium. The topology is the shape of the network and the way the devices are connected to the physical medium.

The physical layer is a fundamental layer that enables the communication between devices in a network. It is implemented by various hardware technologies that have different capabilities and limitations. The physical layer is the closest layer to the physical connection between devices.



Network topology design in computer networks is the arrangement of nodes and links in a network, both physically and logically. It determines how data flows between different devices and how network performance can be optimized. There are different types of network topologies, such as bus, ring, star, mesh, tree, etc. Each topology has its own advantages and disadvantages, depending on the network size, complexity, and requirements.

A network topology diagram is a graphical representation of the network structure, showing the nodes, links, and data flow directions. It can help to visualize the network layout, identify potential problems, and plan for future changes. A network topology diagram can be drawn using various symbols and conventions, such as circles, squares, lines, arrows, etc.

The following is an example of a network topology diagram for a star topology, which is one of the most common and simple topologies. In a star topology, all the nodes are connected to a central hub or switch, which acts as the data transmission center. The hub or switch can be either active or passive, depending on whether it amplifies or simply forwards the data signals. A star topology is easy to install and manage, but it can be expensive and vulnerable to a single point of failure.

#### Network topology diagram for a star topology

```
    /----\
   /      \
  /        \
 /          \
|            |
|    HUB     |
|            |
 \          /
  \        /
   \      /
    \----/
     /|\
    / | \
   /  |  \
  /   |   \
 /    |    \
/     |     \
|     |     |
|  N1 |  N2 |
|     |     |
\     |     /
 \    |    /
  \   |   /
   \  |  /
    \ | /
     \|/
    /----\
   /      \
  /        \
 /          \
|            |
|    N3      |
|            |
 \          /
  \        /
   \      /
    \----/
```

N1, N2, N3: Nodes (computers, printers, etc.)
HUB: Hub or switch
----: Cable or wireless link



#### Types of connections in Computer Networks

A connection in a computer network is a link between two or more devices that allows them to communicate and share data, resources, and applications. There are different types of connections in computer networks, depending on the number of devices involved, the topology of the network, and the mode of communication.

According to the number of devices involved, there are three basic types of connections in computer networks:

- **Point-to-point connection**: This type of connection allows one device to communicate with one other device. For example, two phones may pair with each other using Bluetooth to exchange files or make calls. A point-to-point connection can be either wired or wireless, and it can use different protocols, such as Ethernet, PPP, or HDLC. A point-to-point connection is usually simple, reliable, and secure, but it can be expensive and inefficient if there are many devices that need to communicate with each other.

- **Broadcast/multicast connection**: This type of connection allows a device to send one message out to the network and have copies of that message delivered to multiple recipients. For example, a radio station may broadcast its signal to many listeners, or a video streaming service may multicast its content to many subscribers. A broadcast/multicast connection can be either wired or wireless, and it can use different protocols, such as IP, UDP, or RTP. A broadcast/multicast connection is usually efficient and scalable, but it can be unreliable and insecure if there is no feedback or encryption.

- **Multipoint connection**: This type of connection allows one device to connect and deliver messages to multiple devices in parallel. For example, a hub may connect several computers in a local area network (LAN), or a router may connect several networks in a wide area network (WAN). A multipoint connection can be either wired or wireless, and it can use different protocols, such as TCP, HTTP, or FTP. A multipoint connection is usually flexible and versatile, but it can be complex and costly if there are many devices and protocols involved.

The following diagram illustrates the basic architecture of a point-to-point, a broadcast/multicast, and a multipoint connection in a computer network:

```
    Point-to-point connection

    A ------------------------ B

    Broadcast/multicast connection

    A ------------------------ B
    |                          |
    |                          |
    C ------------------------ D
    |                          |
    |                          |
    E ------------------------ F

    Multipoint connection

    A ---- H ---- B
         / | \
        /  |  \
       /   |   \
    C ---- I ---- D
       \   |   /
        \  |  /
         \ | /
    E ---- J ---- F
```

In the diagram, A, B, C, D, E, and F are devices, such as computers, phones, or sensors, that can communicate with each other. H, I, and J are devices, such as hubs, switches, or routers, that can connect multiple devices and forward messages between them. The lines represent the connections, which can be either wired or wireless, and use different protocols.



Transmission media in computer networks are the physical channels that carry data from one device to another using electromagnetic signals. There are two main types of transmission media: guided and unguided. Guided media are those that provide a physical path for the signals, such as wires, cables, or optical fibers. Unguided media are those that do not provide a physical path, but allow the signals to propagate freely in the air, such as radio waves, microwaves, or infrared waves.

#### Transmission media in Computer Networks

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Transmitter   |     |   Receiver      |     |   Transmitter   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Guided Media  |     |   Unguided      |     |   Unguided      |
|                 |     |   Media         |     |   Media         |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Wire          |     |   Radio         |     |   Microwave     |
|   Cable         |     |   Wave          |     |   Wave          |
|   Fiber         |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```



#### Signal transmission and encoding in Computer Networks

Signal transmission is the process of sending digital or analog data over a physical medium such as a wire, a cable, or a wireless channel. Encoding is the process of converting data into a specific format that can be recognized and interpreted by the receiver. Encoding can also help to reduce the errors and the bandwidth required for transmission.

There are different types of encoding techniques depending on the nature of the data and the medium. For example, digital-to-digital encoding converts a stream of bits into a series of voltage pulses that can be transmitted over a wire. Analog-to-digital encoding converts a continuous analog signal into a discrete sequence of bits that can be transmitted over a digital medium. Digital-to-analog encoding converts a stream of bits into a continuous analog signal that can be transmitted over an analog medium. Analog-to-analog encoding converts a continuous analog signal into another continuous analog signal that can be transmitted over an analog medium.

The following diagram illustrates the basic architecture of a signal transmission and encoding system:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Data Source  |----->|   Transmitter  |----->|   Receiver     |----->|   Data Sink    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+

Data Source: The origin of the data to be transmitted, such as a computer, a sensor, a microphone, etc.
Transmitter: The device that encodes the data into a suitable format and sends it over the medium, such as a network adapter, a modem, a radio, etc.
Receiver: The device that receives the encoded data from the medium and decodes it into the original format, such as a network adapter, a modem, a radio, etc.
Data Sink: The destination of the data, such as a computer, a display, a speaker, etc.
Medium: The physical channel that carries the encoded data, such as a wire, a cable, a fiber, a wireless link, etc.
```



Network performance and transmission impairments in Computer Networks

Network performance is the measure of how well a network can deliver data and services to its users. It can be evaluated by various metrics, such as throughput, delay, jitter, packet loss, availability, reliability, etc. Network performance can be affected by various factors, such as network topology, routing protocols, traffic load, congestion control, quality of service, etc.

Transmission impairments are the damages or distortions caused to the signal during its transmission over a medium. They can result in errors, losses, or degradation of the signal quality. Transmission impairments can be classified into three types: attenuation, distortion, and noise.

Attenuation is the gradual loss of signal strength as it travels over a medium. It can be caused by the resistance, capacitance, or inductance of the medium, or by the absorption, reflection, or scattering of the signal by the environment. Attenuation can be measured in decibels (dB), which is the ratio of the input power to the output power of the signal.

Distortion is the change in the shape or form of the signal as it travels over a medium. It can be caused by the non-linear characteristics of the medium, or by the interference of other signals on the same medium. Distortion can affect the amplitude, frequency, or phase of the signal, and can result in errors or losses of information.

Noise is the unwanted or random variation of the signal as it travels over a medium. It can be caused by various sources, such as thermal noise, induced noise, crosstalk noise, impulse noise, etc. Noise can corrupt the signal and make it difficult to distinguish from the original signal.

The following diagram illustrates the basic architecture of a network and the transmission impairments that can affect the signal:

```
+--------+        +--------+        +--------+        +--------+
| Source |        | Router |        | Router |        |Destination|
| Node   |--------| Node   |--------| Node   |--------| Node     |
+--------+        +--------+        +--------+        +--------+
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  V                  V                  V                  V
+--------+        +--------+        +--------+        +--------+
| Signal |        | Signal |        | Signal |        | Signal |
+--------+        +--------+        +--------+        +--------+
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  V                  V                  V                  V
+--------+        +--------+        +--------+        +--------+
| Medium |        | Medium |        | Medium |        | Medium |
+--------+        +--------+        +--------+        +--------+
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  V                  V                  V                  V
+--------+        +--------+        +--------+        +--------+
| Signal |        | Signal |        | Signal |        | Signal |
+--------+        +--------+        +--------+        +--------+
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  |                  |                  |                  |
  V                  V                  V                  V
+--------+        +--------+        +--------+        +--------+
|Attenuation|     |Attenuation|     |Attenuation|     |Attenuation|
+--------

```




Switching techniques and multiplexing are two concepts in computer networks that are related to how data is transmitted over a shared medium. Switching techniques are methods of establishing and maintaining a connection between two nodes in a network, while multiplexing is a method of combining multiple signals into one signal over a shared medium.

There are three main types of switching techniques: circuit switching, message switching, and packet switching. Circuit switching is a technique where a dedicated communication path is established between two nodes for the duration of the communication. Message switching is a technique where the whole message is treated as a data unit and stored and forwarded by intermediate nodes until it reaches the destination. Packet switching is a technique where the message is broken down into smaller chunks called packets and routed independently by intermediate nodes until they reach the destination.

Multiplexing can be done in different ways, such as frequency division multiplexing (FDM), time division multiplexing (TDM), and statistical multiplexing. FDM is a technique where the frequency spectrum of the shared medium is divided into several non-overlapping frequency bands, and each signal is modulated by a different carrier frequency. TDM is a technique where the time axis of the shared medium is divided into several time slots, and each signal is assigned a different time slot. Statistical multiplexing is a technique where the shared medium is dynamically allocated to the signals based on their demand and availability.

The following diagram illustrates the basic architecture of a switching technique and a multiplexing technique in computer networks:

```
+--------+     +--------+     +--------+     +--------+
|        |     |        |     |        |     |        |
| Node A +---->+ Switch +---->+ Mux    +---->+ Node B |
|        |     |        |     |        |     |        |
+--------+     +--------+     +--------+     +--------+
                   |              |
                   |              |
                   |              |
                   |              |
                   |              |
                   |              |
                   |              |
                   |              |
+--------+     +--------+     +--------+     +--------+
|        |     |        |     |        |     |        |
| Node C +---->+ Switch +---->+ Mux    +---->+ Node D |
|        |     |        |     |        |     |        |
+--------+     +--------+     +--------+     +--------+
```

In this diagram, Node A and Node C are sending data to Node B and Node D, respectively. The switch is responsible for establishing and maintaining a connection between the nodes, using one of the switching techniques. The mux is responsible for combining the data from the switch into one signal, using one of the multiplexing techniques. The signal is then transmitted over the shared medium to the destination node, where it is demultiplexed and delivered to the receiver.



The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet. The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to. The link layer is also known as the data link layer, or layer 2, in the seven-layer OSI model of computer networking. The link layer provides the functional and procedural means to transfer data between network entities and may also provide the means to detect and possibly correct errors that can occur in the physical layer. The link layer is concerned with local delivery of frames between nodes on the same level of the network.

The link layer can be divided into two sublayers: the logical link control (LLC) sublayer and the media access control (MAC) sublayer. The LLC sublayer provides services such as flow control, error control, and multiplexing to the upper layers. The MAC sublayer is responsible for controlling the access to the shared medium, such as a cable or a wireless channel. The MAC sublayer defines various protocols for different types of networks, such as Ethernet, Wi-Fi, Bluetooth, etc.

A local area network (LAN) is a network that connects devices within a limited geographical area, such as a home, office, or campus. A LAN typically uses a shared medium, such as a cable or a wireless channel, to communicate between devices. A LAN can have multiple link-layer protocols, such as Ethernet, Wi-Fi, etc., depending on the type of medium and the devices involved.

The following diagram illustrates the basic architecture of a link layer in computer networks and a LAN using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
| Application     |     | Application     |     | Application     |
+-----------------+     +-----------------+     +-----------------+
| Transport       |     | Transport       |     | Transport       |
+-----------------+     +-----------------+     +-----------------+
| Network         |     | Network         |     | Network         |
+-----------------+     +-----------------+     +-----------------+
| Link (LLC)      |     | Link (LLC)      |     | Link (LLC)      |
+-----------------+     +-----------------+     +-----------------+
| Link (MAC)      |     | Link (MAC)      |     | Link (MAC)      |
+-----------------+     +-----------------+     +-----------------+
| Physical        |     | Physical        |     | Physical        |
+-----------------+     +-----------------+     +-----------------+
       |                     |                     |
       |                     |                     |
       +---------------------+---------------------+
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     |                     |
                     +---------------------+
                           Shared Medium
```



The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet. The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to. The link layer is also known as the data link layer or layer 2 in the OSI model of computer networking. The link layer is responsible for transferring data between nodes on a network segment across the physical layer, and for providing error control and addressing functions.

The link layer can be divided into two sublayers: the logical link control (LLC) sublayer and the media access control (MAC) sublayer. The LLC sublayer provides services such as flow control, error detection and correction, and multiplexing to the upper layers. The MAC sublayer handles the access to the shared medium, such as Ethernet, Wi-Fi, or Bluetooth.

The following diagram illustrates the basic architecture of the link layer in computer networks:

```
+-----------------+    +-----------------+    +-----------------+
|   Application   |    |   Application   |    |   Application   |
+-----------------+    +-----------------+    +-----------------+
|    Transport    |    |    Transport    |    |    Transport    |
+-----------------+    +-----------------+    +-----------------+
|    Network      |    |    Network      |    |    Network      |
+-----------------+    +-----------------+    +-----------------+
| Logical Link    |    | Logical Link    |    | Logical Link    |
| Control (LLC)   |    | Control (LLC)   |    | Control (LLC)   |
+-----------------+    +-----------------+    +-----------------+
| Media Access    |    | Media Access    |    | Media Access    |
| Control (MAC)   |    | Control (MAC)   |    | Control (MAC)   |
+-----------------+    +-----------------+    +-----------------+
|    Physical     |    |    Physical     |    |    Physical     |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Node A      |    |     Node B      |    |     Node C      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Link 1      |----|     Link 2      |----|     Link 3      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```



Framing is a function of the data link layer that provides a way for a sender to transmit a set of bits that are meaningful to the receiver. Frames are the result of the final layer of encapsulation before the data is transmitted over the physical layer. Frames have headers that contain information such as error-checking codes, source and destination addresses, and protocols.

There are different types of framing methods used in data link layer, such as character-oriented, bit-oriented, and clock-based. Each method has its own advantages and disadvantages, and uses different techniques to mark the boundaries of frames, such as special characters, bit patterns, or timing signals.

#### Framing in link layer in Computer Networks

The following diagram illustrates the basic architecture of a framing in link layer in computer networks:

```
+----------------+----------------+----------------+----------------+
| Physical layer | Physical layer | Physical layer | Physical layer |
+----------------+----------------+----------------+----------------+
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
+----------------+----------------+----------------+----------------+
| Data link layer| Data link layer| Data link layer| Data link layer|
+----------------+----------------+----------------+----------------+
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
+----------------+----------------+----------------+----------------+
| Network layer  | Network layer  | Network layer  | Network layer  |
+----------------+----------------+----------------+----------------+
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
+----------------+----------------+----------------+----------------+
| Transport layer| Transport layer| Transport layer| Transport layer|
+----------------+----------------+----------------+----------------+
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
|                |                |                |                |
+----------------+----------------+----------------+----------------+
| Application    | Application    | Application    | Application    |
| layer          | layer          | layer          | layer          |
+----------------+----------------+----------------+----------------+

```

The diagram shows four nodes (A, B, C, and D) connected by a physical medium (such as a cable or a wireless channel). Each node has four layers of protocols: application, transport, network, and data link. The data link layer is responsible for framing the data packets received from the network layer and sending them to the physical layer. The physical layer is responsible for transmitting the bits of the frames over the medium.

The data link layer can use different framing methods depending on the type of the physical layer and the network requirements. For example, character-oriented framing uses special characters (such as STX and ETX) to mark the start and end of a frame. Bit-oriented framing uses special bit patterns (such as 01111110) to mark the frame boundaries. Clock-based framing uses timing signals (such as a clock pulse) to synchronize the sender and receiver.

The framing method also determines how the data link layer handles errors, flow control, and addressing. For example, character-oriented framing uses parity bits or checksums to detect errors, and ACK or NAK characters to control the flow. Bit-oriented framing uses CRC or checksum to detect errors, and sliding window or stop-and-wait to control the flow. Clock-based framing uses error-correcting codes or retransmission to handle errors, and feedback or rate control to control the flow.

The framing method also affects the efficiency and reliability of the data transmission. For example, character-oriented framing is simple and easy to implement, but it wastes bandwidth and may cause framing errors if the data contains the special characters. Bit-oriented



#### Error Detection and Correction in link layer in Computer Networks

The data link layer is responsible for ensuring that the data frames transmitted from the source to the destination are free from errors or corrupted bits. To achieve this, the data link layer uses various techniques for error detection and correction.

Error detection is the process of identifying or locating an error in the data frame. Error correction is the process of recovering or correcting the original data frame from the erroneous one.

The basic approach for error detection and correction is the use of redundancy, where additional bits are added to the data frame to facilitate the detection and correction of errors. These additional bits are called error control bits or check bits.

There are three main techniques for error detection and correction in the data link layer:

- Parity check
- Checksum
- Cyclic redundancy check (CRC)

The following diagram illustrates the basic architecture of error detection and correction in the data link layer:

```
+-----------------+       +-----------------+
|                 |       |                 |
|   Data source   |       |   Data sink     |
|                 |       |                 |
+-----------------+       +-----------------+
        |                         ^
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
+-----------------+       +-----------------+
|                 |       |                 |
|   Data link     |       |   Data link     |
|   layer         |       |   layer         |
|                 |       |                 |
+-----------------+       +-----------------+
        |                         ^
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
+-----------------+       +-----------------+
|                 |       |                 |
|   Physical      |       |   Physical      |
|   layer         |       |   layer         |
|                 |       |                 |
+-----------------+       +-----------------+
        |                         ^
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        v                         |
+-----------------+       +-----------------+
|                 |       |                 |
|   Transmission  |       |   Transmission  |
|   medium        |       |   medium        |
|                 |       |                 |
+-----------------+       +-----------------+
```

The data source generates the data frames and passes them to the data link layer. The data link layer adds the error control bits to the data frames and sends them to the physical layer. The physical layer converts the data frames into electrical signals and transmits them over the transmission medium. The transmission medium may introduce errors or noise in the signals due to various factors such as interference, attenuation, distortion, etc. The physical layer at the receiver side receives the signals and converts them back into data frames. The data link layer at the receiver side checks the error control bits and detects any errors in the data frames. If the errors are detected, the data link layer may request the sender to retransmit the data frames or attempt to correct the errors using the error control bits. The data link layer then passes the corrected data frames to the data sink. The data sink receives the data frames and processes them.



Flow control is a technique that allows two stations working at different speeds to communicate with each other. It regulates the amount of data that a sender can send before waiting for an acknowledgment from the receiver. There are two main methods of flow control in the data link layer: stop-and-wait and sliding window.

Stop-and-wait is a simple method where the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment after receiving and processing each frame. This method is easy to implement but has low efficiency and high delay.

Sliding window is a more advanced method where the sender can send multiple frames without waiting for an acknowledgment from the receiver. The sender and the receiver maintain a window of frames that can be sent or received at any time. The window size is determined by the available buffer space and the bandwidth-delay product of the link. The sender slides the window forward when it receives an acknowledgment from the receiver. The receiver slides the window forward when it receives a frame from the sender. This method is more efficient and has lower delay than stop-and-wait.

The following diagram illustrates the basic architecture of a flow control in the data link layer using the sliding window method:

```
Sender                          Receiver
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+


  Frame 1  Frame 2  Frame 3  Frame 4  Frame 5  Frame 6  Frame 7  Frame 8
  |       |       |       |       |       |       |       |       |
  |       |       |       |       |       |       |       |       |
  |       |

```




The data link layer is the second layer of the OSI model that provides reliable and efficient communication between adjacent nodes on a network. The data link layer is responsible for framing, error control and flow control. The data link layer protocols are designed to implement these functions in different scenarios.

The elementary data link layer protocols are the simplest protocols that can be used in the data link layer. They are divided into three categories, based on the assumptions and requirements of the communication channel:

- Protocol 1: Unrestricted simplex protocol. This protocol assumes that the sender can transmit data frames continuously without any feedback from the receiver. The receiver does not send any acknowledgments or control frames. This protocol is suitable for simplex channels that are error-free and have unlimited bandwidth.

- Protocol 2: Simplex stop and wait protocol. This protocol assumes that the sender can transmit only one data frame at a time and must wait for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment for each received frame. This protocol is suitable for simplex channels that are error-prone and have limited bandwidth.

- Protocol 3: Simplex protocol for noisy channels. This protocol assumes that the sender can transmit only one data frame at a time and must wait for a positive acknowledgment from the receiver before sending the next frame. The receiver sends a positive acknowledgment for each correctly received frame and a negative acknowledgment for each corrupted frame. The sender retransmits the frame if it receives a negative acknowledgment or a timeout occurs. This protocol is suitable for simplex channels that are noisy and have limited bandwidth.

The following diagram illustrates the basic architecture of a data link layer protocol:

```
+-----------------+      +-----------------+
|                 |      |                 |
|    Sender       |      |    Receiver     |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
| Data link layer |      | Data link layer |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
| Physical layer  |      | Physical layer  |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|    Channel      |<---->|    Channel      |
|                 |      |                 |
+-----------------+      +-----------------+
```

The following diagram illustrates the frame format of a data link layer protocol:

```
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Header       |    Payload      |    Trailer      |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
| Control | SeqNo |    Data         | Checksum | Flag |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
```

The header contains the control field and the sequence number field. The control field indicates the type of the frame, such as data, acknowledgment, or negative acknowledgment. The sequence number field identifies the frame uniquely and helps in detecting duplicate or lost frames. The payload contains the data to be transmitted. The trailer contains the checksum field and the flag field. The checksum field is used for error detection and correction. The flag field marks the end of the frame and helps in frame synchronization.



The sliding window protocol is a technique for controlling the flow of data between two network nodes. It is used in the data link layer of the OSI model and in the TCP protocol. The sliding window protocol allows the sender to send multiple frames at a time before receiving an acknowledgment from the receiver. The sliding window protocol uses sequence numbers to identify each frame and to keep track of the frames that have been sent and received. The sliding window protocol also uses timers to detect and retransmit lost or corrupted frames.

#### Sliding Window protocols in link layer in Computer Networks

The following diagram illustrates the basic architecture of a sliding window protocol in the data link layer of a computer network.

```
+----------------+      +----------------+
|                |      |                |
|    Sender      |      |    Receiver    |
|                |      |                |
+----------------+      +----------------+
|                |      |                |
|    Data Link   |      |    Data Link   |
|    Layer       |      |    Layer       |
|                |      |                |
+----------------+      +----------------+
|                |      |                |
|    Physical    |      |    Physical    |
|    Layer       |      |    Layer       |
|                |      |                |
+----------------+      +----------------+
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     +----+                  +----+
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          +------------------+
                 Channel
```

The sender and the receiver each have a window of frames that they can send or receive at a time. The window size is determined by the available buffer space and the network conditions. The sender maintains a send window that contains the frames that have been sent but not yet acknowledged. The receiver maintains a receive window that contains the frames that have been received but not yet delivered to the upper layer. The sender and the receiver exchange window information using special control frames.

There are different types of sliding window protocols, such as stop-and-wait, go-back-N, and selective repeat. Each protocol has different rules for managing the window size, the sequence numbers, the acknowledgments, and the retransmissions. The main difference between these protocols is the amount of data that is retransmitted in case of an error. The stop-and-wait protocol retransmits the entire window, the go-back-N protocol retransmits from the first unacknowledged frame, and the selective repeat protocol retransmits only the lost or corrupted frames. The selective repeat protocol is the most efficient but also the most complex of the three.



#### Medium Access Control and Local Area Networks

Medium access control (MAC) is a sublayer of the data link layer that coordinates the access of multiple devices to a shared medium, such as a cable or a wireless channel. MAC protocols can be classified into two categories: contention-based and token-passing.

Contention-based MAC protocols allow any device to transmit data whenever the medium is idle, but they may cause collisions if two or more devices transmit at the same time. A common example of a contention-based MAC protocol is carrier sense multiple access/collision detection (CSMA/CD), which is used in Ethernet networks. In CSMA/CD, a device senses the medium before transmitting and backs off for a random time if a collision is detected.

Token-passing MAC protocols use a special frame, called a token, to grant the right to transmit to one device at a time. The token is passed from one device to another in a predefined order, and only the device that holds the token can transmit data. A common example of a token-passing MAC protocol is token ring, which uses a ring topology and a token that circulates around the ring.

A local area network (LAN) is a network that connects devices within a limited geographic area, such as a building or a campus. LANs typically use MAC protocols to coordinate the access of devices to a shared medium, such as a twisted-pair cable, a coaxial cable, a fiber-optic cable, or a wireless channel. LANs can have different physical and logical topologies, such as bus, star, ring, or mesh.

The following diagram illustrates the basic architecture of a LAN using a contention-based MAC protocol (CSMA/CD) and a bus topology:

```
    +------+      +------+      +------+      +------+
    |Device|      |Device|      |Device|      |Device|
    +------+      +------+      +------+      +------+
       |             |             |             |
       |             |             |             |
       |             |             |             |
       |             |             |             |
       +-------------+-------------+-------------+-------------+
                             Shared medium (bus)
```

The following diagram illustrates the basic architecture of a LAN using a token-passing MAC protocol (token ring) and a ring topology:

```
    +------+      +------+      +------+      +------+
    |Device|      |Device|      |Device|      |Device|
    +------+      +------+      +------+      +------+
       |             |             |             |
       |             |             |             |
       V             V             V             V
       +-------------+-------------+-------------+-------------+
       |             |             |             |             |
       |             |             |             |             |
       +-------------+-------------+-------------+-------------+
       ^             ^             ^             ^
       |             |             |             |
       |             |             |             |
    +------+      +------+      +------+      +------+
    |Device|      |Device|      |Device|      |Device|
    +------+      +------+      +------+      +------+
                             Shared medium (ring)
```



Channel allocation in medium access control is the problem of how to assign a shared communication channel to multiple users who want to transmit data over it. There are different methods of channel allocation, such as fixed, dynamic, and hybrid. A medium access control (MAC) protocol is the set of rules that coordinate the access to the channel and avoid collisions or interference.

#### Channel allocation in medium access control

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   User 1        |       |   User 2        |       |   User 3        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       +-------------------------+-------------------------+
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |

```




Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model. These protocols allow a number of nodes or users to access a shared network channel  .

There are different types of multiple access protocols, such as random access, controlled access, and channelization protocols. Each type has its own advantages and disadvantages, depending on the network scenario and requirements .

#### Multiple access protocols in medium access control

The following diagram illustrates the basic architecture of a multiple access protocol in medium access control:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|     Node 1     |      |     Node 2     |      |     Node 3     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+------------------+
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|     Node 4     |      |     Node 5     |      |     Node 6     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The diagram shows six nodes that want to access a shared network channel. The network channel is represented by the vertical line in the middle. The multiple access protocol is responsible for coordinating the access of the nodes to the channel, avoiding collisions and maximizing the channel utilization .

Some examples of multiple access protocols are:

- ALOHA: A random access protocol that allows nodes to transmit data whenever they have data to send, without checking the channel state. If a collision occurs, the nodes wait for a random time and retransmit the data .
- CSMA: A random access protocol that allows nodes to sense the channel state before transmitting data. If the channel is busy, the nodes wait until it becomes idle. There are different variants of CSMA, such as CSMA/CD and CSMA/CA, that use different methods to handle collisions .
- TDMA: A controlled access protocol that divides the channel into fixed time slots and assigns each slot to a node. The nodes can only transmit data in their assigned slots, avoiding collisions and ensuring fair access .
- FDMA: A channelization protocol that divides the channel into fixed frequency bands and assigns each band to a node. The nodes can only transmit data in their assigned bands, avoiding interference and ensuring orthogonal access .



A local area network (LAN) is a data communication network connecting various terminals or computers within a building or limited geographical area. The connection among the devices could be wired or wireless. LANs use a transmission technology consisting of a cable. Traditional LANs technology transmits at speeds of 10 Mbps to 100 Mbps and makes very few errors.

There are different standards for LANs, such as IEEE 802, which is a family of standards for local area networks (LAN), personal area network (PAN), and metropolitan area networks (MAN). The IEEE 802 family of standards has twelve members, numbered 802.1 through 802.12, with a focus group of the LMSC devoted to each  . The most widely used standards are for Ethernet, Bridging and Virtual Bridged LANs, Wireless LAN, Wireless PAN, Wireless MAN, Wireless Coexistence, Media Independent Handover Services, and Resilient Packet Ring.

The following diagram illustrates the basic architecture of a LAN using IEEE 802 standards:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  IEEE 802.1     |    |  IEEE 802.2     |    |  IEEE 802.3     |
|  Higher Layer   |    |  Logical Link   |    |  Ethernet       |
|  LAN Protocols  |    |  Control        |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  IEEE 802.11    |    |  IEEE 802.15    |    |  IEEE 802.16    |
|  Wireless LAN   |    |  Wireless PAN   |    |  Wireless MAN   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  IEEE 802.21    |    |  IEEE 802.22    |    |  IEEE 802.23    |
|  Media          |    |  Wireless RAN   |    |  Emergency      |
|  Independent    |    |                 |    |  Services        |
|  Handover       |    |                 |    |                 |
|  Services       |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  IEEE 802.24    |    |  IEEE 802.25    |    |  IEEE 802.26    |
|  Smart Grid     |    |  Token Ring     |    |  Energy         |
|  TAG            |    |                 |    |  Efficient      |
|                 |    |                 |    |  Ethernet       |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  IEEE 802.27    |    |  IEEE 802.28    |    |  IEEE 802.29    |
|  Resilient      |    |  Broadband LAN  |    |  Fiber Optic    |
|  Packet Ring    |    |  using Coaxial  |    |  TAG            |
|                 |    |  Cable          |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  IEEE 802.30    |    |  IEEE 802.31    |    |  IEEE 802.32    |
|  Integrated     |    |  Interoperable  |    |  Unused         |
|  Services LAN   |    |  LAN Security   |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```



#### Link layer switches & bridges in local area network

A link layer switch or a bridge is a network device that connects multiple LANs (local area networks) together to form a larger LAN. It operates at the data link layer of the OSI model and uses MAC addresses to forward Ethernet frames from one device to another device. A switch or a bridge can also interconnect different data link layer technologies, such as Ethernet and FDDI.

The following ASCII diagram illustrates the basic architecture of a link layer switch or a bridge in a local area network:

```
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |  LAN Segment 1  |-----|  Switch/Bridge  |-----|  LAN Segment 2  |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
```

In this diagram, the switch or the bridge has two ports, one for each LAN segment. It stores and forwards frames based on the MAC addresses of the source and destination devices. For example, if a device A in LAN segment 1 wants to communicate with a device B in LAN segment 2, it sends a frame with the MAC address of B as the destination address. The switch or the bridge receives the frame on its port 1, looks up the MAC address of B in its forwarding table, and sends the frame out of its port 2 to LAN segment 2. The device B then receives the frame and responds to device A.

A switch or a bridge can also filter frames based on the MAC addresses, to prevent unnecessary traffic from reaching the other LAN segment. For example, if a device C in LAN segment 1 wants to communicate with a device D in LAN segment 1, it sends a frame with the MAC address of D as the destination address. The switch or the bridge receives the frame on its port 1, looks up the MAC address of D in its forwarding table, and finds that D is also connected to port 1. Therefore, the switch or the bridge does not forward the frame to port 2, and only sends it to device D on port 1.

A switch or a bridge can also learn the MAC addresses of the devices connected to its ports by observing the source addresses of the frames it receives. For example, when the switch or the bridge receives a frame from device A on port 1, it adds the MAC address of A and the port number 1 to its forwarding table. This way, the switch or the bridge can dynamically update its forwarding table and improve its performance.



#### Learning bridge algorithms in local area network

A bridge is a device that connects two or more local area networks (LANs) at the data link layer. A bridge operates by learning the MAC addresses of the devices connected to each port and forwarding frames based on the destination MAC address. A bridge maintains a forwarding table that maps each MAC address to the port where it was last seen.

The following diagram illustrates the basic architecture of a bridge:

```
+------+    +------+    +------+
| LAN1 |----| Port1|    | Port2|----| LAN2 |
+------+    +------+    +------+
              |  |
              |  |
              |  +-----------------+
              |                    |
              |                    |
              |                    |
              |                    |
              |                    |
              |                    |
              |                    |
              +--------------------+
              | Forwarding table  |
              +--------------------+
              | MAC address | Port|
              +--------------------+
              | 00:11:22:33 |  1  |
              +--------------------+
              | 00:44:55:66 |  2  |
              +--------------------+
              | 00:77:88:99 |  1  |
              +--------------------+
              | 00:AA:BB:CC |  2  |
              +--------------------+
```

The learning algorithm works as follows:

- When a frame arrives on a port, the bridge examines the source MAC address and adds it to the forwarding table with the port number where it was received.
- The bridge then checks the destination MAC address and looks it up in the forwarding table. If it finds a match, it forwards the frame to the corresponding port. If it does not find a match, it floods the frame to all ports except the one where it was received.
- The bridge periodically updates and deletes the entries in the forwarding table based on the age and activity of the MAC addresses.

The learning algorithm allows the bridge to dynamically adapt to the topology and traffic patterns of the network. It also reduces the amount of unnecessary traffic on the network by filtering out the frames that are destined to the same LAN as the source. However, the learning algorithm can fail when there are loops or multiple paths between LANs, which can cause duplication and inconsistency of frames. To prevent this, bridges use a protocol called spanning tree protocol (STP) to create a loop-free logical topology of the network.



Spanning tree algorithms are used to prevent loops in a local area network (LAN) that has redundant links between switches. They work by selecting one switch as the root bridge and then blocking or disabling some of the links that are not part of the shortest path to the root bridge. This way, a loop-free logical topology is created for the LAN.

The following diagram illustrates the basic architecture of a spanning tree algorithm in a LAN:

```
    +--------+         +--------+         +--------+
    | Switch |---------| Switch |---------| Switch |
    |   A    |         |   B    |         |   C    |
    +--------+         +--------+         +--------+
       |  |              |  |              |  |
       |  |              |  |              |  |
       |  +--------------+  +--------------+  |
       |                    |                 |
       |                    |                 |
       |                    |                 |
    +--------+         +--------+         +--------+
    | Switch |---------| Switch |---------| Switch |
    |   D    |         |   E    |         |   F    |
    +--------+         +--------+         +--------+
```

In this diagram, there are six switches (A, B, C, D, E, F) connected by nine links. If all the links are active, there will be loops in the network, which can cause problems such as broadcast storms, multiple frame copies, and inconsistent MAC address tables. To avoid these problems, a spanning tree algorithm is run on the switches to select a root bridge and block some of the links.

One example of a spanning tree algorithm is the Spanning Tree Protocol (STP), which is based on the following steps:

1. Each switch sends out Bridge Protocol Data Units (BPDUs) to announce its identity and priority to the other switches.
2. The switch with the lowest priority (or the lowest MAC address if there is a tie) becomes the root bridge. In this example, let's assume that switch A is the root bridge.
3. Each switch determines the shortest path to the root bridge based on the cost of the links. The cost is usually proportional to the bandwidth of the link, with lower cost for higher bandwidth.
4. Each switch selects one of its ports as the root port, which is the port that connects to the shortest path to the root bridge. For example, switch B selects the port that connects to switch A as its root port.
5. Each switch also selects one of its ports as the designated port for each LAN segment, which is the port that offers the lowest cost path to the root bridge for that segment. For example, switch B selects the port that connects to switch C as the designated port for the segment between B and C.
6. All the ports that are neither root ports nor designated ports are blocked or disabled, which means they do not forward any traffic. For example, switch B blocks the port that connects to switch E.

The result of the STP algorithm is a spanning tree that covers all the switches in the LAN, as shown in the diagram below. The blocked ports are marked with X.

```
    +--------+         +--------+         +--------+
    | Switch |---------| Switch |---------| Switch |
    |   A    |         |   B    |         |   C    |
    +--------+         +--------+         +--------+
       |  |              |  |              |  |
       |  |              |  |              |  |
       |  +--------------+  +--------------+  |
       |  X                  X              X |
       |                    |                 |
       |                    |                 |
       |                    |                 |
    +--------+         +--------+         +--------+
    | Switch |---------| Switch |---------| Switch |
    |   D    |         |   E    |         |   F    |
    +--------+         +--------+         +--------+
```

The spanning tree provides a loop-free and redundant topology for the LAN. If any of the active links fails, the STP algorithm can detect the failure and unblock one of the blocked ports to restore connectivity. For example, if the link between switch A and switch B fails, switch B can unblock the port that connects to switch E and use it as the new root port. This way, the network can recover from link failures without manual intervention.



## Unit 3 - Network Layer in Computer Networks

The network layer is the third layer of the OSI reference model. The network layer controls the operation of the subnet, which is a collection of networks interconnected by routers. The main aim of this layer is to deliver packets from source to destination across multiple links (networks)  . The network layer is involved both at the source host and the destination host, as well as at the intermediate routers.

The network layer provides the following services :

- Packetizing: The network layer receives data from the transport layer and divides it into smaller units called packets. Each packet has a header that contains information such as source and destination addresses, sequence number, and protocol type.
- Routing: The network layer determines the best path for each packet to reach its destination, based on factors such as network topology, traffic load, and routing algorithms. The network layer maintains routing tables that store information about the available routes and their costs.
- Forwarding: The network layer forwards each packet from one link to another, based on the routing decision. The network layer uses the address in the packet header to find the next hop (the next router or the destination host) and sends the packet to it.

The following diagram illustrates the basic architecture of the network layer:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Transport     |      |  Transport     |      |  Transport     |
|    Layer       |      |    Layer       |      |    Layer       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Network       |      |  Network       |      |  Network       |
|    Layer       |      |    Layer       |      |    Layer       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Data Link     |      |  Data Link     |      |  Data Link     |
|    Layer       |      |    Layer       |      |    Layer       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Physical      |      |  Physical      |      |  Physical      |
|    Layer       |      |    Layer       |      |    Layer       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
     Source             Intermediate            Destination
      Host                Router                  Host
```

The network layer is also responsible for error control, congestion control, and quality of service at the subnet level . The network layer can use different protocols to perform its functions, such as IP, ICMP, ARP, RARP, etc.  .



### Point-to-point networks in network layer

A point-to-point network is a network that connects two devices directly without any intermediate devices or networks. In the network layer, a point-to-point network can use different protocols to encapsulate and transmit data packets over the link. One of the most common protocols is the Point-to-Point Protocol (PPP), which is a data link layer protocol that can provide authentication, encryption, and compression features. PPP can also support multiple network layer protocols, such as IP, IPX, or AppleTalk.

The following diagram illustrates the basic architecture of a point-to-point network using PPP in the network layer:

```
+----------------+    +----------------+
|                |    |                |
|  Network Layer |    |  Network Layer |
|                |    |                |
+----------------+    +----------------+
|                |    |                |
|   PPP Header   |    |   PPP Header   |
|                |    |                |
+----------------+    +----------------+
|                |    |                |
|   Data Link    |    |   Data Link    |
|    Layer       |    |    Layer       |
|                |    |                |
+----------------+    +----------------+
|                |    |                |
|   Physical     |    |   Physical     |
|    Layer       |    |    Layer       |
|                |    |                |
+----------------+    +----------------+
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       +----------------------+
              Point-to-point
                Link
```



Logical addressing in network layer is the process of assigning a unique identifier to each device on an internetwork. The logical address is also known as the IP address, which is a 32-bit or 128-bit number that can be represented in decimal or hexadecimal format. The logical address is used by the network layer protocols, such as IP or IPX, to route packets from the source to the destination. The logical address is different from the physical address, which is the MAC address of the network interface card (NIC) in the device. The physical address is a 48-bit or 64-bit number that is usually represented in hexadecimal format. The physical address is used by the data link layer protocols, such as Ethernet or Wi-Fi, to deliver frames within a local area network (LAN).

The following diagram illustrates the basic architecture of a network layer with logical addressing:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Application  |       |   Application  |       |   Application  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Transport    |       |   Transport    |       |   Transport    |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Network      |       |   Network      |       |   Network      |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Data Link    |       |   Data Link    |       |   Data Link    |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Physical     |       |   Physical     |       |   Physical     |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
      Device A               Device B               Device C
```

The network layer adds a header to the data received from the transport layer. The header contains the source and destination IP addresses, as well as other information such as the protocol type, the hop count, and the checksum. The network layer uses the logical address to determine the best path to reach the destination device. The network layer may use routing protocols, such as RIP or OSPF, to exchange routing information with other devices on the internetwork. The network layer may also use fragmentation and reassembly techniques to divide and combine packets that are too large or too small for the underlying data link layer.

The data link layer adds a header and a trailer to the data received from the network layer. The header contains the source and destination MAC addresses, as well as other information such as the frame type, the frame length, and the error detection code. The data link layer uses the physical address to deliver the frame to the next hop device on the LAN. The data link layer may use switching protocols, such as STP or VLAN, to forward frames within the LAN. The data link layer may also use error control and flow control techniques to ensure reliable and efficient transmission of frames.

The physical layer converts the data received from the data link layer into electrical signals, optical signals, or radio waves, depending on the type of medium used. The physical layer also defines the characteristics of the medium, such as the voltage, the frequency, the modulation, and the encoding. The physical layer transmits and receives the signals over the medium, such as a copper wire, a fiber optic cable, or a wireless channel. The physical layer may use multiplexing and demultiplexing techniques to combine and separate multiple signals on the same medium. The physical layer may also use synchronization and timing techniques to coordinate the transmission and reception of signals.



### Basic internetworking in network layer

Internetworking is the process of connecting different networks using routers and other devices. Internetworking allows data to be transmitted across networks that use different technologies, protocols, and architectures. Internetworking is implemented in the network layer of the OSI-ISO model, which is responsible for routing, addressing, and fragmentation of packets. The most notable example of internetworking is the Internet, which is a global network of networks.

The following diagram illustrates the basic architecture of a network layer internetwork:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Network A      |     |  Network B      |     |  Network C      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Data link      |     |  Data link      |     |  Data link      |
|  layer          |     |  layer          |     |  layer          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Physical       |     |  Physical       |     |  Physical       |
|  layer          |     |  layer          |     |  layer          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                     |                     |
       |                     |                     |
       +----------+----------+----------+----------+
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  |                     |
                  +----------+----------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |

```




An IP diagram is a visual representation of the IP datagram, which is the basic unit of data transmission over the Internet Protocol (IP). An IP datagram consists of a header and a payload. The header contains information such as the source and destination IP addresses, the protocol type, the length of the datagram, and other fields that help to route the datagram. The payload contains the actual data to be sent, such as a part of a webpage, an email, or a file.

The following diagram illustrates the basic format of an IP datagram header using ASCII characters:

#### IP
```
+-----------------------------------------------------------------+
|Version|  IHL  |Type of Service|          Total Length           |
+-----------------------------------------------------------------+
|         Identification        |Flags|       Fragment Offset     |
+-----------------------------------------------------------------+
|  Time to Live |    Protocol   |         Header Checksum         |
+-----------------------------------------------------------------+
|                       Source IP Address                         |
+-----------------------------------------------------------------+
|                     Destination IP Address                      |
+-----------------------------------------------------------------+
|                    Options                    |    Padding    |
+-----------------------------------------------------------------+
```



CIDR stands for Classless Inter-Domain Routing, a method for allocating IP addresses and for IP routing. It replaces the previous classful network addressing architecture on the Internet, which was based on fixed-length network prefixes. CIDR allows variable-length network prefixes, which enables more efficient use of the IP address space and reduces the size of routing tables.

CIDR notation is a compact representation of an IP address and its associated network prefix. It consists of an IP address followed by a slash (/) and a number, which indicates the number of bits in the network prefix. For example, 192.168.1.0/24 represents the network prefix 192.168.1.0 with a 24-bit length, which covers the IP addresses from 192.168.1.0 to 192.168.1.255.

The following diagram illustrates the basic structure of a CIDR notation:

```
+-----------------+-----------------+-----------------+-----------------+
|   Network ID    |   Network ID    |   Network ID    |    Host ID      |
+-----------------+-----------------+-----------------+-----------------+
| 8 bits          | 8 bits          | 8 bits          | 8 bits          |
+-----------------+-----------------+-----------------+-----------------+
| 192             | 168             | 1               | 0               |
+-----------------+-----------------+-----------------+-----------------+
|<-------------------------- 24 bits -------------------------->|<----->|
|                           Network prefix                       | Host  |
|<---------------------------- 32 bits ------------------------------->|
|                           IP address                             |
+--------------------------------------------------------------------+
| 192.168.1.0/24                                                     |
+--------------------------------------------------------------------+
| CIDR notation                                                      |
+--------------------------------------------------------------------+
```



Address Resolution Protocol (ARP) is a protocol that maps an Internet Protocol (IP) address to a Media Access Control (MAC) address in a local area network (LAN). ARP is used when a device wants to communicate with another device on the same network, but does not know its MAC address. ARP operates by sending a broadcast message to all devices on the network, asking for the MAC address of the device with a specific IP address. The device with that IP address replies with its MAC address, and the communication can proceed.

#### ARP

The following diagram illustrates the basic process of ARP using ASCII art:

```
+--------+    ARP request    +--------+
| Device |------------------>| Router |
|  A     |                   |        |
| IP: X  |<------------------| IP: Y  |
| MAC: ? |    ARP reply     | MAC: Z |
+--------+                   +--------+
```

In this example, device A wants to communicate with the router, but does not know its MAC address. Device A sends an ARP request to the broadcast address, asking for the MAC address of the device with IP address Y. The router, which has IP address Y, responds with an ARP reply, containing its MAC address Z. Device A can then use the MAC address Z to send packets to the router.



RARP stands for Reverse Address Resolution Protocol, which is a protocol that allows a device to request its IP address from a gateway server based on its MAC address. RARP operates on the network access layer of the TCP/IP protocol stack and uses a specialized RARP server that listens for RARP requests on the same LAN. RARP was used for address assignment in the early years of 1980, but was later replaced by BOOTP.

#### RARP

The following diagram illustrates the basic architecture of a RARP:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   RARP Client   |    |   RARP Server   |    |   Other Hosts   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   MAC Address   |    |   MAC to IP     |    |   MAC Address   |
|                 |    |   Mapping       |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   IP Address    |    |   IP Address    |    |   IP Address    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   RARP Module   |    |   RARP Module   |    |   RARP Module   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Ethernet      |    |   Ethernet      |    |   Ethernet      |
|   Interface     |    |   Interface     |    |   Interface     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Ethernet      |    |   Ethernet      |    |   Ethernet      |
|   Cable         |    |   Cable         |    |   Cable         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The RARP process involves the following steps:

1. The RARP client broadcasts a RARP request packet to the LAN, containing its MAC address and a request for its IP address.
2. The RARP server receives the RARP request packet and looks up its MAC to IP mapping table to find the corresponding IP address for the RARP client.
3. The RARP server sends a RARP reply packet to the RARP client, containing its MAC address and the IP address assigned to it.
4. The RARP client receives the RARP reply packet and configures its IP address accordingly.



DHCP stands for Dynamic Host Configuration Protocol. It is a network management protocol that automatically assigns IP addresses and other communication parameters to devices connected to a network using a client-server architecture   .

#### DHCP

The following diagram illustrates the basic architecture of a DHCP network using ASCII art:

```
+-----------------+       +-----------------+       +-----------------+
| DHCP Server     |       | DHCP Relay      |       | DHCP Client     |
|                 |       |                 |       |                 |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | IP Address  | |       | | IP Address  | |       | | IP Address  | |
| | Pool        | |       | | Forwarding  | |       | | Request     | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
|                 |       |                 |       |                 |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | DHCP Offer  | |       | | DHCP Offer  | |       | | DHCP Offer  | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
|                 |       |                 |       |                 |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | DHCP Ack    | |       | | DHCP Ack    | |       | | DHCP Ack    | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       +-------------------------+-------------------------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |

```




ICMP stands for Internet Control Message Protocol. It is a network layer protocol used for error handling and diagnostic purposes. ICMP messages are encapsulated inside IP datagrams and have a specific format that includes a type, a code, a checksum, and optional data fields. The type and code fields indicate the purpose and the nature of the ICMP message, such as echo request, echo reply, destination unreachable, time exceeded, etc. The checksum field is used to verify the integrity of the ICMP message. The data field may contain additional information relevant to the ICMP message, such as the original IP header, the timestamp, the identifier, etc.

#### ICMP

```
+-----------------+-----------------+-----------------+-----------------+
|     Type (8)    |     Code (8)    |   Checksum (16) |      Data       |
+-----------------+-----------------+-----------------+-----------------+
|                                                               |
|                            Data (variable)                    |
|                                                               |
+---------------------------------------------------------------+
```



Routing is the process of finding the best path for a packet to reach its destination in a network. Routing is performed by a special device known as a router, which works at the network layer in the OSI model and internet layer in TCP/IP model. A router is a networking device that forwards the packet based on the information available in the packet header and forwarding table. The routing algorithms are used for routing the packets .

The following diagram illustrates the basic architecture of a router and how it performs routing in the network layer:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Application   |    |   Application   |    |   Application   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Transport     |    |   Transport     |    |   Transport     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Network       |    |   Network       |    |   Network       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Link     |    |   Data Link     |    |   Data Link     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Physical      |    |   Physical      |    |   Physical      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Physical      |    |   Physical      |    |   Physical      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Link     |    |   Data Link     |    |   Data Link     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Network       |    |   Network       |    |   Network       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Routing       |    |   Routing       |    |   Routing       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Link     |    |   Data Link     |    |   Data Link     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Physical      |    |   Physical      |    |   Physical      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |

```




Forwarding and delivery in network layer are two important functions that enable the transmission of packets across multiple networks. Forwarding is the local action of a router to transfer a packet from an input link to the appropriate output link based on the destination address and the routing table. Delivery is the end-to-end process of sending a packet from the source host to the destination host.

The following diagram illustrates the basic architecture of forwarding and delivery in network layer using ASCII characters:

```
    +----+       +----+       +----+       +----+       +----+
    | H1 |-------| R1 |-------| R2 |-------| R3 |-------| H2 |
    +----+       +----+       +----+       +----+       +----+
Source host   Router 1    Router 2    Router 3    Destination host

H1 wants to send a packet to H2. The packet has a network layer header that contains the source and destination addresses.

H1 sends the packet to R1, which is the first hop router on the path to H2. R1 looks up the destination address in its routing table and finds the next hop router, which is R2. R1 forwards the packet to R2.

R2 receives the packet and repeats the same process. It looks up the destination address in its routing table and finds the next hop router, which is R3. R2 forwards the packet to R3.

R3 receives the packet and checks the destination address. It finds that the destination host, H2, is on the same network as itself. R3 delivers the packet to H2.

H2 receives the packet and processes the network layer header. It finds that the packet is intended for itself and passes the packet to the upper layer protocol.
```



Static and dynamic routing are two methods used to determine how to send a packet toward its destination. Static routes are configured in advance of any network communication by a network administrator. Dynamic routes are learned by routers using routing protocols that exchange information with other routers.

The following diagram illustrates the basic architecture of a static and dynamic routing in cn using ASCII characters:

```
+-----+     +-----+     +-----+     +-----+
| R1  |     | R2  |     | R3  |     | R4  |
+-----+     +-----+     +-----+     +-----+
|     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |
+-----+     +-----+     +-----+     +-----+
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
+-----+     +-----+     +-----+     +-----+
| PC1 |     | PC2 |     | PC3 |     | PC4 |
+-----+     +-----+     +-----+     +-----+

Static routing:

R1 has a static route to PC4 via R2 and R4
R2 has a static route to PC3 via R3
R3 has a static route to PC1 via R2 and R1
R4 has a static route to PC2 via R3 and R2

Dynamic routing:

R1, R2, R3 and R4 are running a dynamic routing protocol such as OSPF or EIGRP
They exchange routing information with each other and learn the best paths to all destinations
They update their routing tables accordingly and forward packets based on the dynamic routes
```



Routing algorithms and protocols in cn are the methods and rules that determine how data packets are forwarded from a source node to a destination node in a computer network. There are different types and classifications of routing algorithms and protocols, depending on various factors such as the network topology, the routing metric, the adaptability, the optimality, the complexity, and the scalability.

The following diagram illustrates the basic architecture of a routing algorithm in cn, using the example of a distance vector algorithm, which is a type of dynamic routing protocol that uses the hop count as the routing metric. The diagram shows how each node in the network maintains a routing table that contains the distance and the next hop to each destination, and how the nodes exchange their routing tables periodically or when there is a change in the network topology. The diagram also shows how the nodes use the Bellman-Ford algorithm to update their routing tables based on the information received from their neighbors, and how they avoid the problem of loops by using techniques such as split horizon, poison reverse, or hold-down timers.

The diagram is drawn in ASCII art, using the symbols +, -, |, /, \, <, >, ^, v, o, and x to represent the nodes, the links, the directions, the packets, and the destinations, respectively. The numbers in the parentheses indicate the hop count to each destination.

### Routing algorithms and protocols in cn

```
    o (0)     o (1)     o (2)     o (3)     o (4)     o (5)     o (6)     o (7)     o (8)     o (9)     o (10)    o (11)    o (12)    o (13)    o (14)    o (15)    o (16)    o (17)    o (18)    o (19)    o (20)    o (21)    o (22)    o (23)    o (24)    o (25)    o (26)    o (27)    o (28)    o (29)    o (30)    o (31)    o (32)    o (33)    o (34)    o (35)    o (36)    o (37)    o (38)    o (39)    o (40)    o (41)    o (42)    o (43)    o (44)    o (45)    o (46)    o (47)    o (48)    o (49)    o (50)    o (51)    o (52)    o (53)    o (54)    o (55)    o (56)    o (57)    o (58)    o (59)    o (60)    o (61)    o (62)    o (63)    o (64)    o (65)    o (66)    o (67)    o (68)    o (69)    o (70)    o (71)    o (72)    o (73)    o (74)    o (75)    o (76)    o (77)    o (78)    o (79)    o (80)    o (81)    o (82)    o (83)    o (84)    o (85)    o (86)    o (87)    o (88)    o (89)    o (90)    o (91)    o (92)    o (93)    o (94)    o (95)    o (96)    o (97)    o (98)    o (99)    o (100)   o (101)   o (102)   o (103)   o (104)   o (105)   o (106)   o (107)   o (108)   o (109)   o (110)   o (111)   o (112)   o (113)   o (114)   o (115)   o (116)   o (117)   o (118)   o (119)   o (120)   o (121)   o (122)   o (123)   o (124)   o (125)   o (126)   o (127)   o (128)   o (129)   o (130)   o (131)   o

```




Congestion control algorithms are mechanisms that control the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse. Congestive-Avoidance Algorithms (CAA) are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network.

There are different types of congestion control algorithms, such as:

- Leaky Bucket: This algorithm discovers its use in the context of network traffic shaping or rate-limiting. The algorithm allows controlling the rate at which a record is injected into a network and managing burstiness in the data rate. It works like a leaky bucket with a constant hole at the bottom. The bucket can hold a fixed amount of water, and any excess water will overflow and be lost. Similarly, the algorithm can accept a fixed amount of data, and any excess data will be discarded and lost.
- Token Bucket: This algorithm is similar to the leaky bucket, but it allows some burstiness in the data rate. It works like a leaky bucket with tokens instead of water. The bucket can hold a fixed number of tokens, and tokens are generated at a constant rate. A packet can be sent only if there is a token available in the bucket. If the bucket is full, any new tokens will be discarded. This algorithm allows sending data at a higher rate than the token generation rate, as long as there are enough tokens in the bucket.
- Additive Increase Multiplicative Decrease (AIMD): This algorithm is used by TCP to adjust the congestion window (CWND), which is the amount of data that can be sent without waiting for an acknowledgment. The algorithm works by increasing the CWND by one segment for every acknowledgment received (additive increase), and decreasing the CWND by half for every packet loss detected (multiplicative decrease). This algorithm ensures that the CWND grows slowly when the network is close to congestion, and shrinks quickly when congestion occurs.
- Slow Start: This algorithm is used by TCP to initialize the CWND at the beginning of a connection or after a packet loss. The algorithm works by setting the CWND to one segment, and doubling it for every acknowledgment received. This algorithm allows the CWND to grow exponentially until it reaches a threshold value, or a packet loss occurs. The threshold value is then set to half of the CWND before the packet loss. This algorithm ensures that the CWND grows rapidly when the network is underutilized, and avoids sending too much data too quickly.

The following diagram illustrates the basic architecture of a TCP congestion control algorithm:

```
+-----------------+        +-----------------+
|   Application   |        |   Application   |
+-----------------+        +-----------------+
|      TCP        |        |      TCP        |
+-----------------+        +-----------------+
|  Congestion     |        |  Congestion     |
|  Control        |        |  Control        |
+-----------------+        +-----------------+
|  CWND           |        |  CWND           |
+-----------------+        +-----------------+
|  ACK            |<------>|  ACK            |
+-----------------+        +-----------------+
|  Packet Loss    |<------>|  Packet Loss    |
+-----------------+        +-----------------+
|  IP             |        |  IP             |
+-----------------+        +-----------------+
|  Network        |<-----> |  Network        |
+-----------------+        +-----------------+
```



IPv6 is the latest version of the Internet Protocol, which provides an identification and location system for computers and other devices on networks. IPv6 uses 128-bit addresses, which allows for a much larger address space than IPv4, the previous version. IPv6 also introduces some new features and improvements, such as simplified header format, stateless address autoconfiguration, enhanced security, and support for multicast and anycast communication.

In China, IPv6 deployment and adoption have been increasing in recent years, following the government's plan and policies to promote the transition from IPv4 to IPv6. According to a notice issued by the Central Cyberspace Affairs Commission and Cyberspace Administration in July 2021, China aims to have 700 million active IPv6 users by 2023, and to run a single-stack IPv6 network by 2030. Some of the major IPv6 service providers and users in China include China Telecom, China Mobile, China Unicom, China Broadcasting Network Corporation, China Petroleum & Chemical Corporation, Alibaba, Tencent, Baidu, and Huawei .

The following diagram illustrates the basic architecture of IPv6 in China:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  IPv6 Service  |       |  IPv6 Service  |       |  IPv6 Service  |
|  Provider 1    |       |  Provider 2    |       |  Provider 3    |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  IPv6 User 1   |       |  IPv6 User 2   |       |  IPv6 User 3   |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```



## Unit 4 - Transport Layer in Computer Networks

The transport layer is a conceptual division of methods in the layered architecture of protocols in the network stack in the Internet protocol suite and the OSI model. The protocols of this layer provide end-to-end communication services for applications.

The transport layer takes data from the upper layer (i.e. application layer) and then breaks it into smaller size segments, numbers each byte, and hands over to the lower layer (network layer) for delivery.

The transport layer also provides the user address which is specified as a station or port. The port variable represents a specific process within a host machine that is the source or destination of the data.

The transport layer is responsible for the following functions :

- Service-point addressing: The transport layer provides the user address which is specified as a station or port. The port variable represents a specific process within a host machine that is the source or destination of the data.
- Segmentation and reassembly: The transport layer divides the data received from the application layer into smaller units called segments, and adds a header to each segment. The header contains information such as source and destination port numbers, sequence numbers, checksums, etc. The transport layer also reassembles the segments at the destination and checks for errors.
- Connection control: The transport layer can establish, maintain, and terminate a logical connection between the source and destination hosts. The connection can be either connection-oriented or connectionless, depending on the protocol used. Connection-oriented protocols, such as TCP, use a three-way handshake to establish a connection, and a four-way handshake to terminate a connection. Connectionless protocols, such as UDP, do not use any handshaking mechanism, and simply send the segments without any acknowledgment.
- Flow control: The transport layer regulates the flow of data between the source and destination hosts, to avoid congestion and buffer overflow. Flow control can be either end-to-end or hop-by-hop, depending on the protocol used. End-to-end flow control, such as TCP, uses a sliding window mechanism to control the amount of data that can be sent by the sender before receiving an acknowledgment from the receiver. Hop-by-hop flow control, such as X.25, uses a credit-based mechanism to control the amount of data that can be sent by the sender before receiving a permission from the next hop.
- Error control: The transport layer detects and corrects errors that may occur during the transmission of data. Error control can be either end-to-end or hop-by-hop, depending on the protocol used. End-to-end error control, such as TCP, uses checksums, sequence numbers, acknowledgments, and timers to detect and correct errors. Hop-by-hop error control, such as X.25, uses cyclic redundancy checks (CRC), acknowledgments, and retransmissions to detect and correct errors.

The following diagram illustrates the basic architecture of the transport layer in computer networks:

```
+-----------------+     +-----------------+
| Application     |     | Application     |
| Layer           |     | Layer           |
+-----------------+     +-----------------+
| Transport       |     | Transport       |
| Layer           |     | Layer           |
+-----------------+     +-----------------+
| Network         |     | Network         |
| Layer           |     | Layer           |
+-----------------+     +-----------------+
| Data Link       |     | Data Link       |
| Layer           |     | Layer           |
+-----------------+     +-----------------+
| Physical        |     | Physical        |
| Layer           |     | Layer           |
+-----------------+     +-----------------+
|                 |     |                 |
|      Host A     |     |      Host B     |
|                 |     |                 |
+-----------------+     +-----------------+
```

The transport layer header contains the following fields:

```
+-----------------+-----------------+-----------------+-----------------+
| Source Port     | Destination Port| Sequence Number | Acknowledgment  |
| (16 bits)       | (16 bits)       | (32 bits)       | Number (32 bits)|
+-----------------+-----------------+-----------------+-----------------+
| Data Offset     | Reserved        | Control Bits    | Window Size     |
| (4 bits)        | (6 bits)        | (6 bits)        | (16 bits)       |
+-----------------+-----------------+-----------------+-----------------+
| Checksum        | Urgent Pointer  | Options         | Padding         |
| (16 bits)       | (16 bits

```




The transport layer is responsible for process-to-process delivery, which means the delivery of a packet, part of a message, from one process to another. A process is an entity of the application layer that uses the services of the transport layer. Two processes can communicate using the client/server paradigm, where one process acts as a client and requests services from another process that acts as a server.

The transport layer uses two protocols to perform process-to-process delivery: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). TCP is a connection-oriented protocol that provides reliable, ordered, and error-free delivery of data. UDP is a connectionless protocol that provides unreliable, unordered, and error-free delivery of data.

The transport layer uses port numbers to identify the processes on the source and destination hosts. A port number is a 16-bit integer that is added to the header of the transport layer segment. The source port number identifies the process that sends the data, and the destination port number identifies the process that receives the data.

The following diagram illustrates the process-to-process delivery in the transport layer using ASCII art:

```
+-----------------+       +-----------------+
| Application     |       | Application     |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Transport       |       | Transport       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Network         |       | Network         |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Data Link       |       | Data Link       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Physical        |       | Physical        |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
|                 |       |                 |
|      Host A     |       |      Host B     |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
+-----------------+       +-----------------+
| Data Link       |       | Data Link       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Physical        |       | Physical        |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
|                 |       |                 |
|      Node X     |       |      Node Y     |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
+-----------------+       +-----------------+
| Data Link       |       | Data Link       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Physical        |       | Physical        |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
|                 |       |                 |
|      Node Z     |       |      Node W     |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
+-----------------+       +-----------------+
| Data Link       |       | Data Link       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Physical        |       | Physical        |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
|                 |       |                 |
|      Host C     |       |      Host D     |
|                 |       |                 |
+-----------------+       +-----------------+
| Application     |       | Application     |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Transport       |       | Transport       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Network         |       | Network         |
| Layer           |       | Layer

```




Transport layer protocols are the protocols that provide end-to-end communication services for applications. They lie between the user applications and the network layer. The most common transport layer protocols are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP). TCP provides reliable, connection-oriented, and stream-oriented communication, while UDP provides unreliable, connectionless, and datagram-oriented communication. Other transport layer protocols that have been defined and implemented include the Datagram Congestion Control Protocol (DCCP) and the Stream Control Transmission Protocol (SCTP).

### Transport layer protocols

The following diagram shows the basic structure of a transport layer protocol header. The header contains information such as the source and destination port numbers, the sequence and acknowledgment numbers, the checksum, and the flags. The header is followed by the payload, which is the data that the protocol is carrying.

```
+---------------------+---------------------+
|  Source Port        |  Destination Port   |
+---------------------+---------------------+
|  Sequence Number    |  Acknowledgment No. |
+---------------------+---------------------+
|  Data Offset |Flags |  Window Size        |
+---------------------+---------------------+
|  Checksum           |  Urgent Pointer     |
+---------------------+---------------------+
|  Options (if any)   |  Padding (if any)   |
+---------------------+---------------------+
|                     |                     |
|        Payload      |                     |
|                     |                     |
+---------------------+---------------------+
```



#### UDP Transport layer protocol

UDP is a transport layer protocol that provides a simple and unreliable way of sending and receiving data over the internet. UDP does not establish a connection before sending data, nor does it guarantee that the data will arrive in order or without errors. UDP is useful for applications that require fast and efficient transmission, such as streaming media, online games, or voice over IP.

The basic structure of a UDP packet consists of a header and a payload. The header contains four fields: source port, destination port, length, and checksum. The source and destination ports identify the endpoints of the communication, the length specifies the size of the packet in bytes, and the checksum is used to detect errors in the packet. The payload contains the actual data that is being transmitted.

The following diagram illustrates the basic architecture of a UDP packet using ASCII characters:

```
+---------------------+---------------------+
|    Source Port      |  Destination Port   |
+---------------------+---------------------+
|        Length       |      Checksum       |
+---------------------+---------------------+
|                                              
|                                              
|                                              
|                  Payload                    |
|                                              
|                                              
|                                              
+---------------------------------------------+
```

The UDP protocol does not provide any mechanisms for flow control, congestion control, error recovery, or retransmission. Therefore, the application layer that uses UDP must handle these issues if they are required. UDP is often used in conjunction with other protocols, such as IP, to provide additional features and functionalities. For example, UDP can use IP addresses to route packets to different hosts on the network.



TCP Transport layer protocol
####

TCP Transport layer protocol is a standard that defines how to establish and maintain a network conversation through which application programs can exchange data. It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network . TCP is a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data.

The following diagram illustrates the basic architecture of a TCP Transport layer protocol using ASCII characters:

```
+-----------------+          +-----------------+
| Application     |          | Application     |
| Layer           |          | Layer           |
+-----------------+          +-----------------+
| TCP             |          | TCP             |
| Transport Layer |          | Transport Layer |
+-----------------+          +-----------------+
| IP              |          | IP              |
| Network Layer   |          | Network Layer   |
+-----------------+          +-----------------+
| Data Link Layer |          | Data Link Layer |
+-----------------+          +-----------------+
| Physical Layer  |          | Physical Layer  |
+-----------------+          +-----------------+
|                 |          |                 |
|      Host A     |          |      Host B     |
|                 |          |                 |
+-----------------+          +-----------------+
```

The TCP Transport layer protocol works as follows:

- Step 1: Establish connection
  - When two computers want to send data to each other over TCP, they first need to establish a connection using a three-way handshake.
  - The sender initiates the connection by sending a SYN (synchronize) segment to the receiver, which contains the initial sequence number and other parameters.
  - The receiver responds with a SYN-ACK (synchronize-acknowledge) segment, which contains the acknowledgment number (one more than the received sequence number) and its own initial sequence number and parameters.
  - The sender confirms the connection by sending an ACK (acknowledge) segment, which contains the acknowledgment number (one more than the received sequence number) and other parameters.
  - The connection is now established and ready for data transfer.

- Step 2: Send packets of data
  - When a packet of data is sent over TCP, the recipient must always acknowledge what they received by sending an ACK segment back to the sender.
  - The sender assigns a sequence number to each byte of data and sends it in a TCP segment, which also contains the source and destination port numbers, the checksum, and other flags and options.
  - The receiver checks the checksum and the sequence number of the received segment and sends an ACK segment back to the sender, which contains the acknowledgment number (one more than the last received sequence number) and other parameters.
  - The sender keeps track of the segments that have been sent but not acknowledged and retransmits them if they are lost or corrupted in the network.
  - The receiver also keeps track of the segments that have been received and reorders them if they are out of order.
  - The sender and the receiver use the sliding window mechanism to control the flow of data and avoid congestion in the network.

- Step 3: Close the connection
  - When the data transfer is complete, the sender and the receiver need to close the connection using a four-way handshake.
  - The sender initiates the connection termination by sending a FIN (finish) segment to the receiver, which indicates that it has no more data to send.
  - The receiver acknowledges the FIN segment by sending an ACK segment back to the sender, which indicates that it has received the FIN segment.
  - The receiver also sends a FIN segment to the sender, which indicates that it has no more data to receive.
  - The sender acknowledges the FIN segment by sending an ACK segment back to the receiver, which indicates that it has received the FIN segment.
  - The connection is now closed and the resources are freed.



Multiplexing in transport layer is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver . The transport layer uses port numbers to identify the source and destination processes of the data. The port numbers are added to the transport layer header along with other information such as sequence number, acknowledgement number, checksum, etc. The transport layer header is then encapsulated with the network layer header and sent to the network layer for transmission.

Demultiplexing in transport layer is the reverse process of multiplexing. It is the process of delivering the data to the correct application process at the receiver side . The transport layer uses the port numbers in the transport layer header to identify the destination process of the data. The transport layer removes the transport layer header and passes the data to the corresponding socket.

The following diagram illustrates the basic architecture of multiplexing and demultiplexing in transport layer:

```
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 1       |       | Process 1       |
    +-----------------+       +-----------------+
    | Socket 1        |       | Socket 1        |
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 2       |       | Process 2       |
    +-----------------+       +-----------------+
    | Socket 2        |       | Socket 2        |
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 3       |       | Process 3       |
    +-----------------+       +-----------------+
    | Socket 3        |       | Socket 3        |
    +-----------------+       +-----------------+
    | Transport Layer |       | Transport Layer |
    +-----------------+       +-----------------+
    | Network Layer   |       | Network Layer   |
    +-----------------+       +-----------------+
    | Link Layer      |       | Link Layer      |
    +-----------------+       +-----------------+
    | Physical Layer  |       | Physical Layer  |
    +-----------------+       +-----------------+
    |                 |       |                 |
    |     Sender      |       |    Receiver     |
    |                 |       |                 |
    +-----------------+       +-----------------+
```

The transport layer at the sender side performs multiplexing by collecting the data from different sockets and adding port numbers and other information to the transport layer header. The transport layer at the receiver side performs demultiplexing by extracting the port numbers from the transport layer header and delivering the data to the appropriate socket.

### Multiplexing in transport layer

```
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 1       |       | Process 1       |
    +-----------------+       +-----------------+
    | Socket 1        |       | Socket 1        |
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 2       |       | Process 2       |
    +-----------------+       +-----------------+
    | Socket 2        |       | Socket 2        |
    +-----------------+       +-----------------+
    | Application     |       | Application     |
    | Process 3       |       | Process 3       |
    +-----------------+       +-----------------+
    | Socket 3        |       | Socket 3        |
    +-----------------+       +-----------------+
    | Transport Layer |       | Transport Layer |
    +-----------------+       +-----------------+
    | Network Layer   |       | Network Layer   |
    +-----------------+       +-----------------+
    | Link Layer      |       | Link Layer      |
    +-----------------+       +-----------------+
    | Physical Layer  |       | Physical Layer  |
    +-----------------+       +-----------------+
    |                 |       |                 |
    |     Sender      |       |    Receiver     |
    |                 |       |                 |
    +-----------------+       +-----------------+
          |  |  |                   |  |  |
          |  |  |                   |  |  |
          |  |  |                   |  |  |
          |  |  |                   |

```




Connection management in transport layer is the process of establishing, maintaining and terminating a logical connection between two service access points (SAPs) that communicate using a transport layer protocol such as TCP or UDP. Connection management involves the exchange of messages between the two SAPs to negotiate the parameters and state of the connection, such as the sequence numbers, window sizes, port numbers, and connection identifiers. Connection management also handles the detection and recovery of errors, such as lost, duplicated, or reordered messages, that may occur in the underlying network layer.

The following diagram illustrates the basic architecture of a connection management service in transport layer using ASCII art:

```
+----------------+                        +----------------+
|                |                        |                |
|    User A      |                        |    User B      |
|                |                        |                |
+----------------+                        +----------------+
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
+----------------+                        +----------------+
|                |                        |                |
|    SAP A       |                        |    SAP B       |
|                |                        |                |
+----------------+                        +----------------+
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
+----------------+                        +----------------+
|                |                        |                |
|    TCP A       |                        |    TCP B       |
|                |                        |                |
+----------------+                        +----------------+
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
+----------------+                        +----------------+
|                |                        |                |
|    IP A        |                        |    IP B        |
|                |                        |                |
+----------------+                        +----------------+
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
+----------------+                        +----------------+
|                |                        |                |
|    NIC A       |                        |    NIC B       |
|                |                        |                |
+----------------+                        +----------------+
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
       |                                        |
+----------------+                        +----------------+
|                |                        |                |
|    Link A      |<---------------------->|    Link B      |
|                |                        |                |
+----------------+                        +----------------+
```

The diagram shows the different layers involved in connection management, from the user level to the link level. The user level is where the application programs interact with the transport layer through the service access points (SAPs). The SAPs are the logical endpoints of the connection, and they have unique identifiers such as port numbers. The transport layer is where the connection management protocol, such as TCP, operates. The transport layer is responsible for ensuring reliable and ordered delivery of messages between the SAPs, using mechanisms such as sequence numbers, acknowledgments, timers, and retransmissions. The transport layer also provides flow control and congestion control to regulate the rate of data transmission. The transport layer encapsulates the user data into segments, which are then passed to the network layer. The network layer is where the routing and forwarding of packets takes place, using protocols such as IP. The network layer adds source and destination addresses to the segments, and may fragment or reassemble them if necessary. The network layer delivers the packets to the appropriate link layer. The link layer is where the physical transmission of bits over the medium occurs, using protocols such as Ethernet. The link layer adds headers and trailers to the packets, and may perform error detection and correction using techniques such as checksums and CRCs. The link layer also handles the access and arbitration of the shared medium, using methods such as CSMA/CD or CSMA/CA. The link layer sends and receives the frames to and from the network interface cards (NICs), which are the hardware devices that connect the hosts to the network. The NICs convert the frames into electrical or optical signals, and vice versa, and transmit them over the link, which is the physical medium that connects the NICs. The link may be wired or wireless, and may have different characteristics such as bandwidth, latency, and reliability.

This is a simplified overview of the connection management service in transport layer, and there may be variations and details depending on the specific protocols and implementations used. I hope this helps you understand



Flow control in transport layer is a mechanism that regulates the amount of data that can be sent by a sender to a receiver, to avoid congestion and data loss. It is performed end-to-end, meaning that the sender and receiver communicate with each other using feedback messages, such as acknowledgments and window sizes, to adjust the rate of data transmission.

### Flow control in transport layer

The following diagram illustrates the basic architecture of flow control in transport layer using the TCP protocol:

```
    Sender                          Receiver
+------------+                  +------------+
| Application|                  | Application|
+------------+                  +------------+
|    TCP     |                  |    TCP     |
+------------+                  +------------+
|    IP      |                  |    IP      |
+------------+                  +------------+
|  Network   |                  |  Network   |
+------------+                  +------------+
|            |                  |            |
|            |                  |            |
|            |                  |            |
|            |                  |            |
|            |                  |            |
|            |                  |            |
|            |                  |            |
|            |                  |            |
+------------+                  +------------+
|    Data    |                  |    Data    |
+------------+                  +------------+
|    ACK     |<-----------------|    ACK     |
+------------+                  +------------+
|    Win     |----------------->|    Win     |
+------------+                  +------------+
```

The sender and receiver have a buffer to store the data that is sent or received. The sender maintains a variable called the **congestion window** (Win), which indicates the maximum amount of data that can be sent without receiving an acknowledgment (ACK) from the receiver. The receiver maintains a variable called the **receive window** (RWin), which indicates the amount of free space in the buffer that can receive more data. The sender adjusts the congestion window based on the feedback from the receiver, such as the ACKs and the receive window.

The sender sends data in segments, each with a sequence number, and waits for an ACK from the receiver. The receiver sends an ACK for each segment that it receives and stores in the buffer. The ACK also contains the receive window size, which informs the sender how much more data can be sent. The sender updates the congestion window based on the receive window size and the number of ACKs received. The sender can send more data if the congestion window is larger than the amount of data in transit, or wait if the congestion window is smaller.

The receiver can also use a technique called **flow control by discarding** to signal the sender to slow down. This technique involves dropping some segments that arrive when the buffer is full, and sending a smaller receive window size or a zero window to the sender. The sender will then reduce the congestion window and retransmit the dropped segments.

Flow control in transport layer ensures that the sender and receiver are synchronized and that the data is delivered reliably and efficiently. It is different from flow control in data link layer, which is performed locally between two physically connected nodes, and uses techniques such as stop-and-wait, sliding window, or backpressure.



The transport layer is responsible for providing reliable and efficient communication between end-to-end applications. One of the functions of the transport layer is to ensure that the data is transmitted without any error, loss, duplication or corruption. This is achieved by using error control mechanisms such as retransmission, segmentation, acknowledgement and checksum  .

Etransmission is a term that refers to the process of retransmitting a packet that was lost, delayed or corrupted during the transmission. The transport layer uses a retransmission timer to determine when to resend a packet. The retransmission timer is set based on the round-trip time (RTT) of the packet, which is the time it takes for a packet to travel from the sender to the receiver and back. The retransmission timer is usually a multiple of the RTT, such as 2*RTT or 3*RTT. If the sender does not receive an acknowledgement (ACK) from the receiver before the retransmission timer expires, it assumes that the packet was lost and resends it.

The following diagram illustrates the basic process of etransmission in the transport layer using the Transmission Control Protocol (TCP) as an example :

```
Sender                          Receiver
|                               |
|  Segment 1 (Seq=1, ACK=0)     |
|------------------------------>|  Segment 1 received, checksum OK
|                               |  ACK 1 (Seq=0, ACK=1)
|<------------------------------|  ACK 1 sent
|  ACK 1 received               |
|                               |
|  Segment 2 (Seq=2, ACK=1)     |
|------------------------------>|  Segment 2 received, checksum OK
|                               |  ACK 2 (Seq=1, ACK=2)
|<------------------------------|  ACK 2 sent
|  ACK 2 received               |
|                               |
|  Segment 3 (Seq=3, ACK=2)     |
|------------------------------>|  Segment 3 lost or corrupted
|                               |  No ACK 3 sent
|  Segment 4 (Seq=4, ACK=2)     |
|------------------------------>|  Segment 4 received, checksum OK
|                               |  ACK 2 (Seq=2, ACK=2)
|<------------------------------|  ACK 2 resent (duplicate ACK)
|  ACK 2 received (duplicate)   |
|                               |
|  Segment 5 (Seq=5, ACK=2)     |
|------------------------------>|  Segment 5 received, checksum OK
|                               |  ACK 2 (Seq=3, ACK=2)
|<------------------------------|  ACK 2 resent (duplicate ACK)
|  ACK 2 received (duplicate)   |
|                               |
|  Segment 6 (Seq=6, ACK=2)     |
|------------------------------>|  Segment 6 received, checksum OK
|                               |  ACK 2 (Seq=4, ACK=2)
|<------------------------------|  ACK 2 resent (duplicate ACK)
|  ACK 2 received (duplicate)   |
|                               |
|  Retransmission timer expires |
|                               |
|  Segment 3 (Seq=3, ACK=2)     |
|------------------------------>|  Segment 3 received, checksum OK
|                               |  ACK 6 (Seq=5, ACK=6)
|<------------------------------|  ACK 6 sent (cumulative ACK)
|  ACK 6 received               |
|                               |
|  Segment 7 (Seq=7, ACK=6)     |
|------------------------------>|  Segment 7 received, checksum OK
|                               |  ACK 7 (Seq=6, ACK=7)
|<------------------------------|  ACK 7 sent
|  ACK 7 received               |
|                               |
```



Window management in transport layer is a technique used by protocols such as TCP to control the flow of data packets between two network hosts. It involves maintaining a window size for each connection, which is the number of packets that can be sent or received before an acknowledgment is required. The window size can vary depending on the network conditions and the feedback from the receiver. The sender and the receiver use sliding window algorithms to keep track of the sequence numbers of the packets and to avoid sending or receiving duplicate or out-of-order packets.

The following diagram illustrates the basic architecture of a window management in transport layer using ASCII characters:

### Window management in transport layer

```
    Sender                              Receiver
+------------+                      +------------+
| Application|                      | Application|
+------------+                      +------------+
|    TCP     |                      |    TCP     |
+------------+                      +------------+
|    IP      |                      |    IP      |
+------------+                      +------------+
|  Network   |                      |  Network   |
+------------+                      +------------+
|            |                      |            |
|            |                      |            |
|            |                      |            |
|            |                      |            |
|            |                      |            |
|            |                      |            |
|            |                      |            |
|            |                      |            |
|            |                      |            |
|            |                      |            |
|            |                      |            |
+------------+                      +------------+
|    Data    |                      |    Data    |
+------------+                      +------------+
|    ACK     |                      |    ACK     |
+------------+                      +------------+
|    SEQ     |                      |    SEQ     |
+------------+                      +------------+
|    WIN     |                      |    WIN     |
+------------+                      +------------+
|    RTO     |                      |    RTO     |
+------------+                      +------------+
```

The sender and the receiver exchange the following information:

- Data: The actual data packets that are transmitted or received.
- ACK: The acknowledgment number that indicates the next expected packet from the sender or the receiver.
- SEQ: The sequence number that identifies the order of the packets in the data stream.
- WIN: The window size that indicates the number of packets that can be sent or received before an acknowledgment is required.
- RTO: The retransmission timeout that specifies how long the sender or the receiver waits for an acknowledgment before retransmitting a packet.



TCP congestion control is a mechanism that aims to avoid network congestion by regulating the amount of data that a sender can transmit over a TCP connection. TCP congestion control consists of three phases: slow start, congestion avoidance, and congestion detection.

### TCP Congestion Control in Transport Layer

The following diagram illustrates the basic architecture of TCP congestion control in the transport layer:

```
+-----------------+    +-----------------+
| Application     |    | Application     |
| Layer           |    | Layer           |
+-----------------+    +-----------------+
| Transport       |    | Transport       |
| Layer           |    | Layer           |
| +-------------+ |    | +-------------+ |
| | TCP Header  | |    | | TCP Header  | |
| | +---------+ | |    | | +---------+ | |
| | | Seq No. | | |    | | | Ack No. | | |
| | +---------+ | |    | | +---------+ | |
| | | Ack No. | | |    | | | Seq No. | | |
| | +---------+ | |    | | +---------+ | |
| | | Window  | | |    | | | Window  | | |
| | +---------+ | |    | | +---------+ | |
| | | Options | | |    | | | Options | | |
| | +---------+ | |    | | +---------+ | |
| +-------------+ |    | +-------------+ |
+-----------------+    +-----------------+
| Network         |    | Network         |
| Layer           |    | Layer           |
+-----------------+    +-----------------+
| Data Link       |    | Data Link       |
| Layer           |    | Layer           |
+-----------------+    +-----------------+
| Physical        |    | Physical        |
| Layer           |    | Layer           |
+-----------------+    +-----------------+
```

The sender and the receiver exchange TCP segments that contain a header and a payload. The TCP header contains several fields that are relevant for congestion control, such as:

- Sequence number (Seq No.): the number of the first byte in the segment's payload.
- Acknowledgment number (Ack No.): the number of the next expected byte from the other end of the connection.
- Window size (Window): the number of bytes that the sender or the receiver can accept at a time.
- Options: additional information that can be used for various purposes, such as specifying the maximum segment size (MSS), the congestion window (CWND), the slow start threshold (SSTHRESH), or the selective acknowledgment (SACK) option.

The sender maintains two variables that control the amount of data that it can send: the congestion window (CWND) and the receiver's advertised window (RWND). The sender can send up to min(CWND, RWND) bytes at a time, and it updates these variables based on the feedback from the receiver and the network conditions.

The receiver maintains a variable that indicates the amount of data that it can receive: the receiver's advertised window (RWND). The receiver sends this value to the sender in the window field of the TCP header, and it updates this value based on the amount of buffer space that it has available.

The sender and the receiver use the sequence number and the acknowledgment number fields to keep track of the data that has been sent and received. The sender expects to receive an acknowledgment (ACK) from the receiver for each segment that it sends, and the receiver expects to receive a segment with the next expected sequence number from the sender. If the sender does not receive an ACK within a certain time, it assumes that the segment has been lost or corrupted, and it retransmits the segment. If the receiver receives a segment with an out-of-order sequence number, it discards the segment and sends a duplicate ACK to the sender, indicating the next expected sequence number.

The sender and the receiver use the options field to exchange additional information that can improve the performance and reliability of the TCP connection. For example, the sender and the receiver can negotiate the maximum segment size (MSS) that they can use, which is the largest amount of data that can be sent in a single TCP segment. The sender and the receiver can also use the selective acknowledgment (SACK) option, which allows the receiver to acknowledge non-contiguous segments that it has received, and the sender to retransmit only the missing segments.

The sender uses the congestion window (CWND) and the slow start threshold (SSTHRESH) variables to adjust the rate



Quality of service (QoS) in transport layer is the use of mechanisms or technologies that work on a network to control traffic and ensure the performance of critical applications with limited network capacity. It enables organizations to adjust their overall network traffic by prioritizing specific high-performance applications.

The transport layer establishes the transport connection by sending a request. For establishing a link, it uses the T-CONNECT service primitives. The transport entity provides the quality of service, requirement, and collect addresses services.

The following diagram illustrates the basic architecture of a QoS-enabled transport layer using the TCP/IP model:

```
+-----------------+-----------------+-----------------+
| Application     | Application     | Application     |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Transport    |    Transport    |    Transport    |
|    (TCP/UDP)    |    (TCP/UDP)    |    (TCP/UDP)    |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Internet     |    Internet     |    Internet     |
|    (IP)         |    (IP)         |    (IP)         |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Network      |    Network      |    Network      |
|    Access       |    Access       |    Access       |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Physical     |    Physical     |    Physical     |
+-----------------+-----------------+-----------------+
```

The transport layer can provide QoS by using different protocols, such as TCP or UDP, or by using different mechanisms, such as congestion control, rate control, or reliable data transport. The transport layer can also use QoS parameters, such as delay, jitter, throughput, or packet loss, to measure and adjust the performance of the network .



## Unit 5 - Application Layer in Computer Networks

The application layer is the topmost layer of the Open Systems Interconnection (OSI) model and the Internet Protocol Suite (TCP/IP) model. It is responsible for providing services and protocols that enable applications to communicate with other applications on different computer systems and networks. The application layer is not an application itself, but an abstraction layer that specifies the shared communications protocols and interface methods used by hosts in a communications network .

Some of the common application layer protocols are:

- **Hypertext Transfer Protocol (HTTP)**: It is a protocol for transferring web pages and other resources over the internet. It uses a client-server model, where the client requests a resource from the server and the server responds with the resource or an error message. HTTP uses Uniform Resource Locators (URLs) to identify and locate resources on the web.
- **File Transfer Protocol (FTP)**: It is a protocol for transferring files between hosts on a network. It also allows users to access, retrieve and manage files on a remote computer. FTP uses a control connection and a data connection to exchange commands and data between the client and the server.
- **Simple Mail Transfer Protocol (SMTP)**: It is a protocol for sending and receiving email messages over the internet. It uses a store-and-forward model, where the sender transfers the message to a mail server, which then forwards it to the recipient's mail server. SMTP also supports attachments, encryption and authentication.
- **Domain Name System (DNS)**: It is a protocol for resolving domain names into IP addresses and vice versa. It uses a hierarchical and distributed database of name servers, which store and update the mappings between domain names and IP addresses. DNS also supports caching, load balancing and security features.
- **Telnet**: It is a protocol for providing remote access to a host computer over a network. It allows users to log on as a remote host and execute commands on the host. Telnet uses a virtual terminal emulation, where the client and the server exchange keystrokes and screen updates.
- **Hypertext Transfer Protocol Secure (HTTPS)**: It is a protocol for secure communication over the internet. It uses HTTP as the application layer protocol and Transport Layer Security (TLS) or Secure Sockets Layer (SSL) as the encryption layer protocol. HTTPS ensures the confidentiality, integrity and authenticity of the data exchanged between the client and the server.

The following diagram illustrates the basic architecture of the application layer in computer networks using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
| Application     |    | Application     |    | Application     |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Transport       |    | Transport       |    | Transport       |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Network         |    | Network         |    | Network         |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Data Link       |    | Data Link       |    | Data Link       |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Physical        |    | Physical        |    | Physical        |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      +-------------------------+-------------------------+
                         Network
```



The Domain Name System (DNS) is a service that translates domain names into IP addresses. Domain names are human-readable names that identify websites or other resources on the internet, such as google.com or wikipedia.org. IP addresses are numerical identifiers that computers use to communicate with each other over the network, such as 142.250.64.78 or 208.80.154.224.

DNS works by using a hierarchical and distributed database of domain names and IP addresses, organized into zones. Each zone corresponds to a domain or a subdomain, and contains records that map names to IP addresses or other types of data. For example, the zone for google.com contains records that map www.google.com to 142.250.64.78, mail.google.com to 142.250.64.101, and so on.

DNS also uses a network of servers that store and query the DNS database. These servers are called name servers, and they can be classified into different types according to their role and function. The main types of name servers are:

- Root name servers: These are the authoritative servers for the root zone, which is the top-level zone of the DNS hierarchy. The root zone contains records that point to the name servers for the top-level domains (TLDs), such as .com, .org, .net, and so on. There are 13 root name servers in the world, identified by letters from A to M, and they are distributed across various locations and organizations.
- TLD name servers: These are the authoritative servers for the TLD zones, such as .com, .org, .net, and so on. They contain records that point to the name servers for the second-level domains (SLDs), such as google.com, wikipedia.org, amazon.com, and so on.
- SLD name servers: These are the authoritative servers for the SLD zones, such as google.com, wikipedia.org, amazon.com, and so on. They contain records that point to the name servers for the subdomains or the hostnames, such as www.google.com, en.wikipedia.org, www.amazon.com, and so on. They also contain records that map the hostnames to the IP addresses or other types of data, such as mail servers, name servers, or text records.
- Recursive name servers: These are the servers that receive DNS queries from clients, such as web browsers or applications, and resolve them by contacting the authoritative name servers in the DNS hierarchy. They can also cache the results of the queries to improve the performance and reduce the load on the authoritative name servers. Recursive name servers are usually provided by internet service providers (ISPs), network administrators, or public DNS services, such as Google Public DNS or Cloudflare DNS.

The following diagram illustrates the basic architecture of a DNS system using ASCII art:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Root name      |       |  TLD name       |       |  SLD name       |
|  server         |       |  server         |       |  server         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       +-------------------------+-------------------------+
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |

```




The World Wide Web is an information system that enables documents and other web resources to be accessed over the Internet. It was proposed by Tim Berners-Lee and his colleagues at CERN in 1989. It uses a protocol called HyperText Transfer Protocol (HTTP) to standardize communication between servers and clients. It also uses a markup language called HyperText Markup Language (HTML) to structure and format the content of web pages. Web pages can also contain links to other web pages or resources, which are identified by Uniform Resource Locators (URLs).

The following diagram illustrates the basic architecture of the World Wide Web using ASCII characters:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|    Web User    |       |    Web Server  |       |    Web Page    |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |---------------------->|                       |
       |   HTTP Request       |                       |
       |                       |                       |
       |                       |---------------------->|
       |                       |   Fetch Web Page     |
       |                       |                       |
       |                       |<----------------------|
       |                       |   HTTP Response      |
       |                       |                       |
       |<----------------------|                       |
       |   Display Web Page   |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       V                       V                       V
```



Hyper Text Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML, between web browsers and web servers. HTTP defines how messages are formatted and transmitted, and what actions web servers and browsers should take in response to various commands. HTTP is the foundation of data communication for the World Wide Web, where hypertext documents include hyperlinks to other resources that the user can easily access.

### Hyper Text Transfer Protocol

The following diagram illustrates the basic architecture of HTTP:

```
    +-----------------+                      +-----------------+
    |                 |                      |                 |
    |    Web Browser  |                      |    Web Server   |
    |                 |                      |                 |
    +-----------------+                      +-----------------+
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |<--------HTTP Request Message------|   |
          |   |                                    |   |
          |   |--------HTTP Response Message------>|   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |<--------HTTP Request Message------|   |
          |   |                                    |   |
          |   |--------HTTP Response Message------>|   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          |   |                                    |   |
          V   V                                    V   V
```

An HTTP request message consists of a request line, header fields, and an optional message body. The request line contains the HTTP method, the request URI, and the HTTP version. For example:

```
GET /index.html HTTP/1.1
```

An HTTP response message consists of a status line, header fields, and an optional message body. The status line contains the HTTP version, the status code, and the reason phrase. For example:

```
HTTP/1.1 200 OK
```

HTTP supports different methods for different purposes. Some of the common methods are:

- GET: Requests a representation of the specified resource.
- POST: Submits data to be processed by the specified resource.
- PUT: Replaces the representation of the specified resource with the request payload.
- DELETE: Deletes the specified resource.
- HEAD: Requests only the header fields of the specified resource.
- OPTIONS: Requests the available methods and options for the specified resource.
- TRACE: Echoes back the received request for testing purposes.
- CONNECT: Establishes a tunnel to the specified server for proxying purposes.

HTTP also supports different status codes to indicate the outcome of a request. Some of the common status codes are:

- 200 OK: The request was successful and the response contains the requested resource.
- 301 Moved Permanently: The requested resource has been permanently moved to a new location, which is given by the Location header field.
- 400 Bad Request: The request was malformed or invalid and could not be processed by the server.
- 401 Unauthorized: The request requires authentication and the client did not provide valid credentials.
- 403 Forbidden: The server understood the request but refused to authorize it due to insufficient permissions.
- 404 Not Found: The requested resource was not found on the server.
- 500 Internal Server Error: The server encountered an unexpected error while processing the request and could not fulfill it.
- 503 Service Unavailable: The server is temporarily unable to handle the request due to overload or maintenance.



Electronic mail is an application layer service in which a user can transfer messages and information with another user. Electronic mail is the most popular service of the internet. It uses several protocols to perform different functions, such as SMTP, POP3, IMAP, MIME, etc.   

The following diagram illustrates the basic architecture of electronic mail in application layer using ASCII art:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    User Agent   |        |    Mail Server  |        |    Mail Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    SMTP Client  |        |    SMTP Server  |        |    SMTP Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    POP3 Client  |        |    POP3 Server  |        |    POP3 Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    IMAP Client  |        |    IMAP Server  |        |    IMAP Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    MIME Client  |        |    MIME Server  |        |    MIME Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    TCP Client   |        |    TCP Server   |        |    TCP Server   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    IP Client    |        |    IP Server    |        |    IP Server    |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    NIC Client   |        |    NIC Server   |        |    NIC Server   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```

The user agent is the software that the user uses to read, compose, and organize email. The mail server is the server that interacts with user agents and other mail servers to deliver email. SMTP (Simple Mail Transfer Protocol) is the protocol that transfers email from the sender's mail server to the receiver's mail server. POP3 (Post Office Protocol version 3) and IMAP (Internet Message Access Protocol) are the protocols that allow the user agent to retrieve email from the mail server. MIME (Multipurpose Internet Mail Extensions) is the protocol that allows the user agent and the mail server to handle different types of email content, such as text, images, audio, video, etc. TCP (Transmission Control Protocol) and IP (Internet Protocol) are the protocols that provide reliable and routable data transmission between the user agent and the mail server. NIC (Network Interface Card) is the hardware device that connects the user agent and the mail server to the physical network.   

: https://www.tutorialandexample.com/e-mail-in-computer-network
: https://www.slideshare.net/AmishaSahu3/application-layer-protocol-electronic-mail
: https://www.studocu.com/en-us/document/embry-riddle-aeronautical-university/computer-and-network-technologies/application-layer-unit5/48720165
: https://en.wikipedia.org/wiki/Application_layer
: https://www.geeksforgeeks.org/email-protocols/
: https://www.geeksforgeeks.org/application-layer-in-osi-model/



File Transfer Protocol (FTP) is an application layer protocol that is used to transfer files between a local device and a server over the Internet. It uses two TCP connections in parallel: a control connection and a data connection. The control connection is used to send commands and receive responses, while the data connection is used to transfer the actual files.

The following ASCII diagram illustrates the basic architecture of FTP:

```
+----------------+              +----------------+
|                |              |                |
|    Local       |              |    Remote      |
|    Device      |              |    Server      |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|    FTP         |              |    FTP         |
|    Client      |              |    Server      |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|    TCP         |              |    TCP         |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|    IP          |              |    IP          |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|    Ethernet    |              |    Ethernet    |
|                |              |                |
+----------------+              +----------------+
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |<----------------------->|   |
     |   | Control connection     |   |
     |   | (port 21)              |   |
     |   |                         |   |
     |<---------------------------->|   |
     | Data connection            |   |
     | (port 20)                  |   |
     |                             |   |
```



Remote login is a service that allows a user to log in to a remote computer and run applications as if the user were physically at the host computer. Remote login is an example of an application layer service, which is the highest layer in the OSI model and the TCP/IP model. The application layer provides the interface between the user and the network.

There are different protocols that can implement remote login, such as Telnet and SSH. Telnet is an older and insecure protocol that sends data in plain text over the network. SSH is a newer and secure protocol that encrypts data and provides authentication and integrity. Both protocols use a client-server model, where the client initiates a connection request to the server and the server responds with a login prompt. The client then sends the username and password to the server and the server verifies them. If the login is successful, the server creates a virtual terminal for the client and allows the client to execute commands on the remote computer.

The following diagram illustrates the basic architecture of a remote login service using SSH:

```
+----------------+           +----------------+
|                |           |                |
|     User       |           |    Remote      |
|                |           |    Computer    |
+----------------+           +----------------+
|                |           |                |
| Application    |           | Application    |
| Layer          |           | Layer          |
| (SSH Client)   |           | (SSH Server)   |
|                |           |                |
+----------------+           +----------------+
|                |           |                |
| Transport      |           | Transport      |
| Layer          |           | Layer          |
| (TCP)          |           | (TCP)          |
|                |           |                |
+----------------+           +----------------+
|                |           |                |
| Network        |           | Network        |
| Layer          |           | Layer          |
| (IP)           |           | (IP)           |
|                |           |                |
+----------------+           +----------------+
|                |           |                |
| Data Link      |           | Data Link      |
| Layer          |           | Layer          |
|                |           |                |
+----------------+           +----------------+
|                |           |                |
| Physical       |           | Physical       |
| Layer          |           | Layer          |
|                |           |                |
+----------------+           +----------------+
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       +-----------------------------+
               Network
```



Network management in application layer is the process of monitoring, configuring, and controlling the network resources and services using various protocols and tools. The application layer is the topmost layer of the OSI model that provides the interface between the user applications and the network. Some of the protocols used for network management in application layer are:

- Simple Network Management Protocol (SNMP): A protocol that uses UDP port number 161/162 to collect and manipulate information about network devices and their status. SNMP consists of a manager, an agent, and a management information base (MIB). The manager sends requests to the agent, which responds with the data from the MIB. The MIB is a database that stores the information about the network device and its configuration.
- File Transfer Protocol (FTP): A protocol that uses TCP port number 21 to transfer files between hosts. FTP allows the user to log in to a remote host, browse the directory structure, and upload or download files. FTP can also be used to transfer configuration files or firmware updates to network devices.
- Telnet: A protocol that uses TCP port number 23 to provide remote access to a network device or a host. Telnet allows the user to log in to a network device and execute commands on its command-line interface. Telnet can also be used to configure or troubleshoot network devices.
- Trivial File Transfer Protocol (TFTP): A protocol that uses UDP port number 69 to transfer files between hosts. TFTP is a simplified version of FTP that does not require authentication or directory browsing. TFTP is mainly used to transfer configuration files or firmware updates to network devices.

The following diagram illustrates the basic architecture of a network management system in application layer using SNMP as an example:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Application   |       |   Application   |       |   Application   |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Transport     |       |   Transport     |       |   Transport     |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Network       |       |   Network       |       |   Network       |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Data Link     |       |   Data Link     |       |   Data Link     |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Physical      |       |   Physical      |       |   Physical      |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       +---------------------+-------------------------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |

```




Data compression is the function of presentation layer in OSI reference model. Compression is often used to maximize the use of bandwidth across a network or to optimize disk space when saving data. Data compression reduces the number of bits that need to be transmitted or stored by using algorithms that eliminate redundancy or irrelevant information.

### Data compression in application layer

The application layer is the topmost layer of the OSI model that provides the interface between the user and the network. The application layer also identifies constraints at the application level such as those associated with authentication, privacy, quality of service, networking devices, and data syntax. Some common application layer protocols that use data compression are:

- File Transfer Protocol (FTP): FTP is a protocol that allows users to transfer files between computers over a network. FTP can use data compression to reduce the size of the files before sending them, which can improve the transfer speed and save bandwidth. FTP can use different compression methods, such as ZIP, GZIP, or BZIP2, depending on the type and format of the files.
- Simple Mail Transfer Protocol (SMTP): SMTP is a protocol that enables the sending and receiving of email messages over a network. SMTP can use data compression to reduce the size of the email messages and attachments before sending them, which can improve the delivery speed and save bandwidth. SMTP can use different compression methods, such as MIME, Base64, or Quoted-Printable, depending on the type and format of the messages and attachments.
- Domain Name System (DNS): DNS is a protocol that translates domain names into IP addresses and vice versa. DNS can use data compression to reduce the size of the DNS messages and responses, which can improve the query speed and save bandwidth. DNS can use a compression method called name compression, which eliminates the repetition of domain name labels in the DNS messages and responses.

The following diagram illustrates the basic architecture of a data compression in application layer using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Application   |    |   Application   |    |   Application   |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Presentation  |    |   Presentation  |    |   Presentation  |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Session       |    |   Session       |    |   Session       |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Transport     |    |   Transport     |    |   Transport     |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Network       |    |   Network       |    |   Network       |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Link     |    |   Data Link     |    |   Data Link     |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Physical      |    |   Physical      |    |   Physical      |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |

```




Cryptography in application layer is a data-security solution that encrypts nearly any type of data passing through an application. When encryption occurs at this level, data is encrypted across multiple (including disk, file, and database) layers. This application layer encryption approach increases security by reducing the number of potential attack vectors.

Application-layer encryption, or shift-left cryptography, means giving developers more control over what gets encrypted and who gets the keys for decryption. In some cases, the users themselves may be the only parties with the keys. End-to-end encryption is an increasingly popular type of application-layer cryptography. This type of encryption lets organizations enforce access control using key management as well as policy.

The following diagram illustrates the basic architecture of a typical application-layer encryption scheme:

### Cryptography in application layer

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Application  |     |    Application  |     |    Application  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Encryption   |     |    Encryption   |     |    Encryption   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Transport    |     |    Transport    |     |    Transport    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Network      |     |    Network      |     |    Network      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Physical     |     |    Physical     |     |    Physical     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       User A                 Server                  User B
```

In this diagram, User A and User B are the only parties who have the keys to encrypt and decrypt the data. The server acts as a relay for the data, but cannot access its content. The data is encrypted at the application layer, before it is sent to the transport layer. The data remains encrypted across the network and physical layers, until it reaches the application layer of the other user. This way, the data is protected from any unauthorized access or modification.



Cryptography is the study and practice of techniques for secure communication in the presence of third parties called adversaries. It involves the use of terms like plain text, cipher text, algorithm, key, encryption, and decryption. Encryption is the process of transforming plain text into cipher text using an algorithm and a key. Decryption is the reverse process of transforming cipher text back into plain text using the same or a different key.

Cryptography can be applied at different layers of the network stack, such as the physical layer, the data link layer, the network layer, the transport layer, and the application layer. The application layer is the layer where the user interacts with the software applications, such as web browsers, email clients, instant messaging, etc. Cryptography in the application layer is used to provide end-to-end security and privacy for the data and messages exchanged by the applications.

The following diagram illustrates the basic concepts of cryptography in the application layer using ASCII art:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Application  |      |   Application  |      |   Application  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Encryption   |      |   Transport    |      |   Decryption   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Plain       |      |    Cipher      |      |    Plain       |
|    Text        |      |    Text        |      |    Text        |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|     Key        |      |     Key        |      |     Key        |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Sender      |----->|   Adversary    |----->|    Receiver    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The sender and the receiver are the two parties who want to communicate securely. The adversary is the third party who wants to intercept, modify, or tamper with the communication. The sender uses an encryption algorithm and a key to transform the plain text into cipher text. The cipher text is then sent over the network to the receiver. The adversary can see the cipher text but cannot read or understand it without the key. The receiver uses the same or a different key and a decryption algorithm to transform the cipher text back into plain text. The plain text is then processed by the application layer of the receiver.

There are two main types of cryptography in the application layer: symmetric key cryptography and asymmetric key cryptography. Symmetric key cryptography uses the same key for both encryption and decryption. The key must be shared securely between the sender and the receiver before the communication. Asymmetric key cryptography uses a pair of keys: a public key and a private key. The public key can be shared openly and used for encryption. The private key is kept secret and used for decryption. The sender encrypts the plain text with the receiver's public key. The receiver decrypts the cipher text with their own private key.

Some examples of cryptographic algorithms used in the application layer are:

- AES (Advanced Encryption Standard) - a symmetric key algorithm that uses a fixed-length key (128, 192, or 256 bits) and operates on blocks of 128 bits of data. It is widely used for encrypting data at rest and in transit.
- RSA (Rivest-Shamir-Adleman) - an asymmetric key algorithm that uses variable-length keys (typically 1024, 2048, or 4096 bits) and operates on blocks of data that are smaller than the key length. It is widely used for encrypting and signing data and for key exchange.
- SHA (Secure Hash Algorithm) - a family of hash functions that produce a fixed-length output (160, 224, 256, 384, or 512 bits) from any input. A hash function is a one-way function that maps any input to a unique output. It is widely used for verifying the integrity and authenticity of data and for generating keys and signatures.
- TLS (Transport Layer

