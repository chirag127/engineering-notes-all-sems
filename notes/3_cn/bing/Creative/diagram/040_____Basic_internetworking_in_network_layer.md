Basic internetworking in network layer is the process of connecting different networks using routers and protocols. Internetworking allows communication between hosts that belong to different networks. The most common example of internetworking is the Internet, which is a network of networks.

A basic diagram of internetworking in network layer is shown below:

### Basic internetworking in network layer

```
    +--------+     +--------+     +--------+
    | Host A |-----| Router |-----| Router |-----+ Internet
    +--------+     +--------+     +--------+     |
                                                 |
    +--------+     +--------+     +--------+     |
    | Host B |-----| Router |-----| Router |-----+
    +--------+     +--------+     +--------+
```

In this diagram, Host A and Host B belong to different networks, such as Ethernet, wireless, or point-to-point link. They communicate with each other through routers, which are devices that forward packets based on their network-layer addresses. The routers are connected to the Internet, which is an internetwork that uses the Internet Protocol (IP) to route packets across different networks. The network layer is responsible for providing logical addressing, routing, and fragmentation of packets for internetworking.