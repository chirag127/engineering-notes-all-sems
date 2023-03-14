There are various standards for local area networks (LANs) that specify the physical and data link layers of the network. The most common and widely used standard is IEEE 802.3, also known as Ethernet, which defines the format of frames, the addressing scheme, the medium access control (MAC) protocol, and the physical layer characteristics for different types of cables and connectors. Ethernet can operate at different speeds, such as 10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps, and 100 Gbps, depending on the type of cable and equipment used. Ethernet can also support different topologies, such as bus, star, ring, and mesh, using devices such as hubs, switches, routers, and bridges to connect multiple segments of the network.

Another standard for LANs is IEEE 802.11, also known as Wireless LAN (WLAN) or Wi-Fi, which defines the physical and data link layers for wireless communication using radio frequency (RF) signals. WLAN can operate at different frequencies, such as 2.4 GHz, 5 GHz, and 6 GHz, and different modulation schemes, such as OFDM, QAM, and QPSK, to achieve different data rates, such as 11 Mbps, 54 Mbps, 600 Mbps, and 1.3 Gbps. WLAN can also support different modes of operation, such as infrastructure, ad hoc, and mesh, using devices such as access points, wireless routers, wireless adapters, and wireless repeaters to connect multiple stations of the network.

Other standards for LANs include IEEE 802.5, also known as Token Ring, which uses a token-passing mechanism to control the access to the shared medium; IEEE 802.4, also known as Token Bus, which uses a bus topology and a token-passing mechanism to control the access to the shared medium; and IEEE 802.6, also known as Distributed Queue Dual Bus (DQDB), which uses a dual bus topology and a distributed queueing mechanism to provide high-speed communication for metropolitan area networks (MANs).

The following diagram illustrates the basic architecture of a LAN using Ethernet and WLAN standards:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Ethernet      |     |   Ethernet      |     |   Ethernet      |
|   Segment 1     |     |   Segment 2     |     |   Segment 3     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
    |       |             |       |             |       |
    |       |             |       |             |       |
    |       |             |       |             |       |
    |       |             |       |             |       |
    |       |             |       |             |       |
    |       |             |       |             |       |
+---+-------+---+     +---+-------+---+     +---+-------+---+
|               |     |               |     |               |
|    Switch     +-----+    Router     +-----+    Bridge     |
|               |     |               |     |               |
+---+-------+---+     +---+-------+---+     +---+-------+---+
    |       |             |       |             |       |
    |       |             |       |             |       |
    |       |             |       |             |       |
    |       |             |       |             |       |
    |       |             |       |             |       |
    |       |             |       |             |       |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   WLAN          |     |   WLAN          |     |   WLAN          |
|   Segment 1     |     |   Segment 2     |     |   Segment 3     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```