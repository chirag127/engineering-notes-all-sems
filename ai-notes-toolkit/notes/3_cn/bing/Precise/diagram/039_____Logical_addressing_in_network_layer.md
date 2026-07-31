### Logical addressing in network layer

Logical addressing is used to provide a universal addressing scheme for identifying hosts on a network. The network layer uses logical addresses to identify the source and destination hosts in a packet. These addresses are used by routers to forward packets to their destination.

Here is an ASCII diagram that illustrates the concept of logical addressing in the network layer:

```
+------------+       +------------+
|            |       |            |
|   Host A   |       |   Host B   |
|            |       |            |
+-----+------+       +------+-----+
      |                     |
      |                     |
+-----+------+       +------+-----+
|            |       |            |
|   Router   |       |   Router   |
|            |       |            |
+------------+       +------------+
```

In this diagram, Host A and Host B are two devices on a network. Each host has a unique logical address assigned to it. When Host A wants to send a packet to Host B, it includes the logical address of Host B in the packet. The packet is then sent to the nearest router, which uses the logical address to determine the next hop for the packet. The packet is forwarded from router to router until it reaches the router connected to Host B. The router then delivers the packet to Host B using its logical address.
