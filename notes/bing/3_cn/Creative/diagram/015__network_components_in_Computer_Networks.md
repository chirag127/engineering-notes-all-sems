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