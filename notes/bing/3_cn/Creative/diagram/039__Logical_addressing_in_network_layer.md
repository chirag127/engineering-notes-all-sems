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