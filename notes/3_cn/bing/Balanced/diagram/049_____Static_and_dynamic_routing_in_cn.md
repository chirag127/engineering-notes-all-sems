Static and dynamic routing are two methods used to determine how to send a packet toward its destination. Static routing is a form of routing which occurs when a router uses a manual configuration routing entry rather than dynamic entry. Dynamic routing, on the other hand, requires routers to exchange information with other routers to learn about paths through the network. Static routing provides more security and is implemented in small networks, while dynamic routing uses complex routing algorithms and is implemented in large networks.

### Static and dynamic routing in cn

The following diagram shows an example of static and dynamic routing in a computer network. The network consists of four routers (R1, R2, R3, and R4) and four subnets (A, B, C, and D). The routers are connected by links with different costs (represented by numbers).

```
    A
    |
    | 1
    |
   R1
  /  \
 / 2  \ 3
/      \
B       C
|       |
| 4     | 5
|       |
R2-----R3
 \     /
  \ 6 /
   \ /
    R4
    |
    | 7
    |
    D
```

In static routing, the network administrator manually configures the route and makes an entry to the routing table for each router. For example, the routing table for R1 might look like this:

| Destination | Next hop | Interface |
|-------------|----------|-----------|
| A          | -        | eth0      |
| B          | R2       | eth1      |
| C          | R3       | eth2      |
| D          | R2       | eth1      |

In dynamic routing, the router will use a protocol that was assigned by the network administrator to exchange information with other routers and update its routing table automatically. For example, the routing table for R1 might look like this after using a dynamic routing protocol such as OSPF:

| Destination | Next hop | Interface | Cost |
|-------------|----------|-----------|------|
| A          | -        | eth0      | 0    |
| B          | R2       | eth1      | 6    |
| C          | R3       | eth2      | 3    |
| D          | R2       | eth1      | 17   |

The cost is a metric that represents the best path to the destination. The lower the cost, the better the path. The cost can be calculated based on various factors such as hop count, bandwidth, delay, reliability, etc. Dynamic routing protocols use different algorithms to calculate the cost and update the routing table. Some common dynamic routing protocols are OSPF, EIGRP, RIP, IS-IS, and BGP.