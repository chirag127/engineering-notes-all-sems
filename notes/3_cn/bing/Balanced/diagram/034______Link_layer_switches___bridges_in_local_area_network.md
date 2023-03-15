A link layer switch or a bridge is a network device that connects multiple LANs (local area networks) together to form a larger LAN. It operates at the data link layer of the OSI model and uses MAC addresses to forward Ethernet frames from one device to another device in the network . A switch or a bridge can also interconnect data link layer domains that have different technologies, such as Ethernet and FDDI.

A possible ASCII diagram for link layer switches and bridges in a local area network is shown below:

```
    +------+     +------+     +------+     +------+
    | Host |-----|      |-----|      |-----| Host |
    +------+     |      |     |      |     +------+
                 |Switch|     |Switch|
    +------+     |      |     |      |     +------+
    | Host |-----|      |-----|      |-----| Host |
    +------+     +------+     +------+     +------+
                 |      |     |      |
                 |Bridge|-----|Bridge|
                 |      |     |      |
    +------+     +------+     +------+     +------+
    | Host |-----|      |-----|      |-----| Host |
    +------+     |      |     |      |     +------+
                 |Switch|     |Switch|
    +------+     |      |     |      |     +------+
    | Host |-----|      |-----|      |-----| Host |
    +------+     +------+     +------+     +------+
```

In this diagram, there are four LANs, each with two hosts and a switch. The switches are connected by two bridges, which allow the LANs to communicate with each other. The bridges can also handle different data link layer technologies, such as Ethernet and FDDI, if needed. The switches and bridges use MAC addresses to forward frames to the appropriate destination.