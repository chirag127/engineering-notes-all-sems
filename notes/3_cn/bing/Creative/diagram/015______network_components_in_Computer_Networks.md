A network component is a device or a software that enables communication and data transfer between different devices in a computer network. Some of the major network components are:

- Network Interface Card (NIC): A hardware device that connects a computer to a network and allows it to send and receive data.
- Hub: A device that connects multiple computers or other network devices and broadcasts data to all of them.
- Switch: A device that connects multiple computers or other network devices and forwards data only to the intended recipient.
- Cables and connectors: The physical media and devices that link the network devices and transmit data signals.
- Router: A device that connects two or more networks and routes data packets based on their destination address.
- Modem: A device that modulates and demodulates data signals between analog and digital formats, such as between a telephone line and a computer.
- Server: A computer that provides services or resources to other computers or clients in a network.
- Client: A computer that requests and receives services or resources from a server in a network.

A possible ASCII diagram for network components in computer networks is:

```
    +--------+        +--------+        +--------+
    | Server |--------| Router |--------| Modem  |----(Internet)
    +--------+        +--------+        +--------+
         |                |                |
         |                |                |
+--------+--------+ +-----+-----+ +--------+--------+
| Hub/Switch      | | Hub/Switch | | Hub/Switch      |
+--------+--------+ +-----+-----+ +--------+--------+
    | | | |             | | | |             | | | |
    | | | |             | | | |             | | | |
+---+ + + +---+     +---+ + + +---+     +---+ + + +---+
| NIC | | | NIC |   | NIC | | | NIC |   | NIC | | | NIC |
+---+ + + +---+     +---+ + + +---+     +---+ + + +---+
  | | | |               | | | |               | | | |
  | | | |               | | | |               | | | |
+---+ + + +---+     +---+ + + +---+     +---+ + + +---+
| Client    |       | Client    |       | Client    |
+---+ + + +---+     +---+ + + +---+     +---+ + + +---+
```