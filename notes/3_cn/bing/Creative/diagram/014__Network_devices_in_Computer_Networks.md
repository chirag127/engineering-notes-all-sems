Network devices are physical devices that enable communication and interaction between hardware on a computer network. Each networking device operates in a distinct computer network segment and performs distinct functions. A network may require hundreds or thousands of different network devices to maintain and build out various LAN and WAN.

Some of the common types of network devices are:

- Repeater: A device that regenerates the signal over the same network before the signal becomes too weak or corrupted. It operates at the physical layer (Layer 1) of the OSI model.
- Hub: A device that connects multiple wires coming from different branches of a network. It acts as a multi-port repeater and broadcasts the data to all connected devices. It operates at the physical layer (Layer 1) of the OSI model.
- Bridge: A device that interconnects two or more LANs, creating a single domain from separate LANs. It filters the data by reading the MAC addresses of the source and destination. It operates at the data link layer (Layer 2) of the OSI model.
- Switch: A device that connects multiple devices on a network and forwards data frames to the intended device based on the MAC address. It operates at the data link layer (Layer 2) of the OSI model.
- Router: A device that connects different networks and forwards data packets based on the IP address. It operates at the network layer (Layer 3) of the OSI model.
- Gateway: A device that connects discrete networks or systems that use different protocols, enabling data to flow between the networks. It operates at the application layer (Layer 7) of the OSI model.
- Access point: A device that sends and receives data wirelessly over radio frequencies, using 2.4 GHz or 5 GHz bands. It enables clients to join the wireless LAN created by the access point. It operates at the data link layer (Layer 2) of the OSI model.
- NIC: A device that enables a computer to communicate with other devices on a network. It provides a physical interface for the network cable and converts the data into electrical signals. It operates at the physical layer (Layer 1) and the data link layer (Layer 2) of the OSI model.

#### Network devices in Computer Networks

The following diagram illustrates the basic architecture of a network with some of the network devices mentioned above.

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|    Computer    |        |    Computer    |        |    Computer    |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
       | NIC                   | NIC                   | NIC
       |                       |                       |
       +-----------------------+-----------------------+
                               |
                               | Hub
                               |
                               +-----------------------+
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
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               +-----------------------+
                               |
                               | Bridge
                               |
                               +-----------------------+
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
                               |
                               | Switch
                               |
                               +-----------------------+
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
                               |
                               | Router
                               |
                               +-----------------------+
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
                               |
                               | Gateway
                               |
                               +-----------------------+
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