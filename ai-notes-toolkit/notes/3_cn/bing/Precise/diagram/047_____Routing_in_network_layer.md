### Routing in network layer

```
+--------+       +--------+       +--------+
|        |       |        |       |        |
| Router |-------| Router |-------| Router |
|   A    |       |   B    |       |   C    |
|        |       |        |       |        |
+--------+       +--------+       +--------+
   |  |             |  |             |  |
   |  |             |  |             |  |
+----+----+     +----+----+     +----+----+
|         |     |         |     |         |
| Network |     | Network |     | Network |
|    1    |     |    2    |     |    3    |
|         |     |         |     |         |
+---------+     +---------+     +---------+
```

In the network layer, routers are responsible for routing packets from one network to another. In the diagram above, there are three routers, A, B, and C, connected to each other. Each router is also connected to a network, 1, 2, and 3 respectively. When a packet is sent from a device in network 1 to a device in network 3, the packet will first be sent to router A. Router A will then forward the packet to router B, which will then forward the packet to router C. Finally, router C will forward the packet to the destination device in network 3. This process is known as routing.