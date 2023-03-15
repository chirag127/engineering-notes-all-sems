Logical addressing in network layer is the process of assigning a unique and universal identifier to each device on an internetwork. The network layer uses protocols such as IP or IPX to create and translate logical addresses to MAC addresses. Logical addresses are also known as network addresses or layer 3 addresses. They are placed in the header of the packets by the network layer.

A possible ASCII diagram for logical addressing in network layer is:

```
+-----------------+       +-----------------+       +-----------------+
|  Device A       |       |  Router         |       |  Device B       |
|  IP: 192.168.1.1|       |  IP: 10.0.0.1   |       |  IP: 10.0.0.2   |
|  MAC: AA:AA:AA  |       |  MAC: BB:BB:BB  |       |  MAC: CC:CC:CC  |
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
+-----+-----+             +-----+-----+             +-----+-----+
|  Packet  |             |  Packet  |             |  Packet  |
|  IP src: |             |  IP src: |             |  IP src: |
|  192.168.|             |  192.168.|             |  192.168.|
|  1.1     |             |  1.1     |             |  1.1     |
|  IP dst: |             |  IP dst: |             |  IP dst: |
|  10.0.0.2|             |  10.0.0.2|             |  10.0.0.2|
|  MAC src:|             |  MAC src:|             |  MAC src:|
|  AA:AA:AA|             |  BB:BB:BB|             |  BB:BB:BB|
|  MAC dst:|             |  MAC dst:|             |  MAC dst:|
|  BB:BB:BB|             |  CC:CC:CC|             |  CC:CC:CC|
+----------+             +----------+             +----------+
```

The diagram shows how device A sends a packet to device B through a router. The packet has the IP address of device A as the source and the IP address of device B as the destination. The packet also has the MAC address of device A as the source and the MAC address of the router as the destination. The router then forwards the packet to device B by changing the MAC address of the source to its own and the MAC address of the destination to device B's. The IP address of the packet remains unchanged throughout the process. This is how logical addressing in network layer works.