Basic internetworking in network layer is the process of connecting different networks using routers or gateways that operate at the network layer of the OSI-ISO model. The routers or gateways use the Internet Protocol (IP) to forward packets across different physical networks. The most notable example of internetworking is the Internet, which is a global network of networks.

The following diagram illustrates the basic architecture of an internetwork:

### Basic internetworking in network layer

```
    +----+    +----+    +----+    +----+
    | H1 |----| R1 |----| R2 |----| H2 |
    +----+    +----+    +----+    +----+
       |         |         |         |
       |         |         |         |
    +----+    +----+    +----+    +----+
    | H3 |----| R3 |----| R4 |----| H4 |
    +----+    +----+    +----+    +----+

H: Host
R: Router
```

In this diagram, there are four physical networks: two Ethernets, one wireless network, and one point-to-point link. Each network has two hosts (H1 to H4) and two routers (R1 to R4) connected to it. The routers are responsible for forwarding packets from one network to another, using IP addresses to determine the best path. The hosts are the end devices that send and receive packets over the internetwork.