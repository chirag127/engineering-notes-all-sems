A point-to-point network is a network topology in which two nodes are directly connected by a link, without any intermediate devices or hosts. A point-to-point network can use different protocols at the data link layer, such as High-level Data Link Control (HDLC), Point-to-Point Protocol (PPP), or Point-to-Point Tunneling Protocol (PPTP). These protocols provide a way to encapsulate multiprotocol data, establish and configure the link, authenticate the users, and compress or encrypt the data.

A point-to-point network in the network layer can be used to connect two routers or two hosts over a WAN link, such as a leased line, a dial-up modem, or a wireless connection. The network layer protocol, such as IP, can use the point-to-point link as a logical interface to send and receive packets.

A possible ASCII diagram for a point-to-point network in the network layer is:

```
    +--------+      +--------+
    | Router |------| Router |
    +--------+      +--------+
       |                |
       |                |
    +--------+      +--------+
    | Host A |      | Host B |
    +--------+      +--------+
```

In this diagram, the two routers are connected by a point-to-point link, which can use any of the data link layer protocols mentioned above. The routers can use IP as the network layer protocol to exchange packets over the link. The hosts A and B are connected to the routers by other network interfaces, such as Ethernet or Wi-Fi. The hosts can also use IP as the network layer protocol to communicate with each other through the routers.