Static and dynamic routing are two methods used to determine how to send a packet toward its destination. Static routes are configured in advance of any network communication by a network administrator  . Dynamic routes are learned by routers through exchanging information with other routers using routing protocols  .

### Static and dynamic routing in cn

The following diagram shows an example of static and dynamic routing in a computer network. The network consists of four routers (R1, R2, R3, and R4) and four subnets (A, B, C, and D). The routers are connected by links with different costs.

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
   6
   |
   |
   D
   |
   | 7
   |
   R4
```

In static routing, the network administrator manually configures the routes for each router. For example, the administrator can configure the following static routes for R1:

- To reach subnet A, use the interface connected to A
- To reach subnet B, use the interface connected to B
- To reach subnet C, use the interface connected to C
- To reach subnet D, use the interface connected to R3

The static routes for the other routers can be configured similarly. The advantage of static routing is that it provides more security and control over the network traffic . The disadvantage is that it requires manual intervention and is not scalable for large networks .

In dynamic routing, the routers use routing protocols to exchange information about the network topology and the best routes to reach different destinations. For example, the routers can use the Open Shortest Path First (OSPF) protocol, which is a link-state protocol that calculates the shortest path to each destination based on the link costs. The routers periodically send and receive updates about the network state and adjust their routing tables accordingly. The advantage of dynamic routing is that it adapts to network changes and failures automatically and is more efficient for large networks . The disadvantage is that it consumes more bandwidth and CPU resources and may be less secure .