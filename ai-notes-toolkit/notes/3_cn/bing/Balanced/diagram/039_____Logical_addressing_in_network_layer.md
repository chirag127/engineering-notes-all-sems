Logical addressing is the process of assigning a unique identifier to each device on a network. Logical addresses are created and used by network layer protocols, such as IP or IPX. The network layer protocol translates logical addresses to MAC addresses, which are the physical addresses of the devices.

A logical address consists of two parts: a network ID and a host ID. The network ID identifies the network to which the device belongs, and the host ID identifies the device within that network. The format and length of the logical address depend on the network layer protocol used. For example, IP uses a 32-bit logical address, while IPX uses a 80-bit logical address.

A logical address can be represented in different ways, such as binary, decimal, hexadecimal, or dotted decimal notation. For example, the IP address 192.168.1.100 can be written as:

- Binary: 11000000.10101000.00000001.01100100
- Decimal: 3232235876
- Hexadecimal: C0.A8.01.64
- Dotted decimal: 192.168.1.100

The following diagram shows an example of logical addressing in the network layer:

### Logical addressing in network layer

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Device A      |    |  Router R      |    |  Device B      |
|                |    |                |    |                |
|  MAC: 00:11:22 |    |  MAC: 11:22:33 |    |  MAC: 22:33:44 |
|  IP: 10.0.0.1  |    |  IP: 10.0.0.2  |    |  IP: 20.0.0.1  |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
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
       +----------------------+----------------------+
                      Network Layer
```

In this diagram, device A and device B are on different networks, and router R is the gateway between them. Device A wants to send a packet to device B, so it uses its network layer protocol (IP) to create a logical address for device B, which is 20.0.0.1. Device A also uses its network layer protocol to find out the logical address of router R, which is 10.0.0.2. Device A then encapsulates the packet with the source and destination logical addresses, which are 10.0.0.1 and 20.0.0.1, respectively.

Device A then sends the packet to router R, using its data link layer protocol (Ethernet) to create a MAC address for router R, which is 11:22:33. Device A also uses its data link layer protocol to find out its own MAC address, which is 00:11:22. Device A then encapsulates the packet with the source and destination MAC addresses, which are 00:11:22 and 11:22:33, respectively.

Router R receives the packet and checks the destination MAC address, which matches its own MAC address. Router R then decapsulates the packet and checks the destination logical address, which does not match its own logical address. Router R then uses its network layer protocol to find out the logical address of device B, which is 20.0.0.1. Router R then encapsulates the packet with the source and destination logical addresses, which are 10.0.0.1 and 20.0.0.1, respectively.

Router R then sends the packet to device B, using its data link layer protocol (Ethernet) to create a MAC address for device B, which is 22:33:44. Router R also uses its data link layer protocol to find out its own MAC address, which is 11:22:33. Router R then encapsulates the packet with the source and destination MAC addresses, which are 11:22:33 and 22:33:44, respectively.

Device B receives the packet and checks the destination MAC address