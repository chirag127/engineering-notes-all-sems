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