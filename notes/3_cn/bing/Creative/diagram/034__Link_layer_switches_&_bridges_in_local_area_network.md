#### Link layer switches & bridges in local area network

A link layer switch or a bridge is a network device that connects multiple LANs (local area networks) together to form a larger LAN. It operates at the data link layer of the OSI model and uses MAC addresses to forward Ethernet frames from one device to another device in the same LAN or a different LAN. A switch or a bridge can also filter frames based on their MAC addresses and avoid propagating unnecessary or unwanted traffic to other segments of the network. A switch or a bridge can also isolate collision domains and extend broadcast domains in a LAN.

The following diagram illustrates the basic architecture of a link layer switch or a bridge in a local area network:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  LAN Segment 1  |-----|  Switch/Bridge  |-----|  LAN Segment 2  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

In this diagram, the switch or the bridge has two ports, one for each LAN segment. It stores the MAC addresses of the devices connected to each port in a table and uses this table to forward frames to the appropriate port. For example, if a device A in LAN segment 1 wants to send a frame to device B in LAN segment 2, it will send the frame to the switch or the bridge with the MAC address of device B as the destination address. The switch or the bridge will look up the MAC address of device B in its table and find that it is associated with port 2. It will then forward the frame to port 2 and device B will receive it. If the switch or the bridge does not have the MAC address of the destination device in its table, it will broadcast the frame to all ports except the one it received the frame from. This way, it can learn the MAC addresses of new devices and update its table accordingly. If the switch or the bridge receives a frame with a destination MAC address that is in the same LAN segment as the source MAC address, it will drop the frame and not forward it to the other port. This way, it can filter out local traffic and reduce the network congestion.