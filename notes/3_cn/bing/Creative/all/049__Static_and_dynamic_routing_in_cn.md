### Static and dynamic routing in cn

- Static routing and dynamic routing are two methods of configuring routing tables in a network.
- Routing tables are data structures that store information about how to reach different destinations in a network, such as IP addresses, subnet masks, next-hop addresses, and interface names.
- Static routing is the manual configuration of routing tables by a network administrator. Dynamic routing is the automatic configuration of routing tables by routing protocols that exchange information with other routers.
- Static routing has the following advantages and disadvantages:
  - Advantages:
    - It is simple and easy to implement in small networks.
    - It is more secure and predictable than dynamic routing, as it does not depend on external information or updates.
    - It consumes less bandwidth and CPU resources than dynamic routing, as it does not generate routing traffic or updates.
  - Disadvantages:
    - It is difficult and time-consuming to implement and maintain in large or complex networks, as it requires manual intervention for every change or failure in the network topology.
    - It is not scalable or adaptable to network growth or changes, as it does not respond to network conditions or traffic demands.
    - It can cause suboptimal routing or routing loops, as it does not consider the best path or the current state of the network.
- Dynamic routing has the following advantages and disadvantages:
  - Advantages:
    - It is easier and faster to implement and maintain in large or complex networks, as it automatically adapts to network changes or failures.
    - It is more scalable and efficient than static routing, as it responds to network conditions and traffic demands, and selects the best path for each destination.
    - It can avoid suboptimal routing or routing loops, as it considers the current state and metrics of the network, such as hop count, bandwidth, delay, or load.
  - Disadvantages:
    - It is more complex and difficult to implement in small networks, as it requires the configuration and coordination of routing protocols and parameters.
    - It is less secure and predictable than static routing, as it depends on external information or updates, which can be corrupted, delayed, or lost.
    - It consumes more bandwidth and CPU resources than static routing, as it generates routing traffic or updates, which can affect network performance or stability.
- Examples of static routing and dynamic routing are as follows:
  - Static routing: A network administrator manually configures the routing table of each router in the network, specifying the next-hop address or interface for each destination network or host. For example, in the following network diagram, the network administrator configures the routing table of router R1 as follows:

    | Destination | Next-hop |
    |-------------|----------|
    | 10.0.0.0/24 | 192.168.1.2 |
    | 172.16.0.0/16 | 192.168.1.3 |
    | 192.168.2.0/24 | 192.168.1.4 |

    Similarly, the network administrator configures the routing table of router R2, R3, and R4.

  - Dynamic routing: A network administrator enables a routing protocol on each router in the network, such as RIP, OSPF, EIGRP, or BGP. The routing protocol exchanges routing information or updates with other routers, and automatically updates the routing table of each router based on the received information or updates. For example, in the following network diagram, the network administrator enables RIP on each router in the network. RIP uses hop count as the metric to select the best path for each destination. RIP sends routing updates every 30 seconds to its neighbors, and updates the routing table accordingly. For example, router R1 receives the following routing updates from its neighbors:

    | Source | Destination | Metric |
    |--------|-------------|--------|
    | R2 | 10.0.0.0/24 | 1 |
    | R2 | 172.16.0.0/16 | 2 |
    | R2 | 192.168.2.0/24 | 2 |
    | R3 | 10.0.0.0/24 | 2 |
    | R3 | 172.16.0.0/16 | 1 |
    | R3 | 192.168.2.0/24 | 2 |
    | R4 | 10.0.0.0/24 | 2 |
    | R4 | 172.16.0.0/16 | 2 |
    | R4 | 192.168.2.0/24 | 1 |

    Based on the received updates, router R1 updates its routing table as follows: