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