### Static and Dynamic Routing in Computer Networks

In computer networking, routing refers to the process of forwarding data packets from one network to another. Routing can be classified into two types: static routing and dynamic routing.

#### Static Routing

Static routing is a type of routing where network administrators manually configure the routes in the routing table of a router. In static routing, the network topology is fixed, and the routes do not change unless the administrator manually updates them.

##### Advantages of Static Routing

- Simple to configure and troubleshoot
- Does not have overhead of computing the routes dynamically
- Provides better control over the routing paths

##### Disadvantages of Static Routing

- Not suitable for large networks with frequent topology changes
- Prone to errors due to manual configuration
- Does not adapt to changes in the network topology

#### Dynamic Routing

Dynamic routing is a type of routing where routers exchange information with each other to automatically update the routing table. In dynamic routing, the network topology changes dynamically, and the routes are updated automatically based on the information exchanged between the routers.

##### Advantages of Dynamic Routing

- Suitable for large networks with frequent topology changes
- Automatically adapts to changes in the network topology
- Provides redundancy and load balancing

##### Disadvantages of Dynamic Routing

- More complex to configure and troubleshoot
- Has overhead of computing the routes dynamically
- Provides less control over the routing paths

#### Routing Protocols

Routing protocols are used to facilitate the exchange of routing information between routers. Some of the commonly used routing protocols are:

- Routing Information Protocol (RIP)
- Open Shortest Path First (OSPF)
- Border Gateway Protocol (BGP)

##### RIP

RIP is a distance vector routing protocol that uses hop count as the metric to determine the best path to a destination network. RIP has a limit of 15 hops, and any network beyond that is considered unreachable.

##### OSPF

OSPF is a link-state routing protocol that uses the shortest path first algorithm to determine the best path to a destination network. OSPF calculates the shortest path based on the cost of the links between the routers.

##### BGP

BGP is an exterior gateway protocol that is used to exchange routing information between different autonomous systems (AS). BGP is used by internet service providers (ISP) to exchange routing information between their networks.

#### Conclusion

Static and dynamic routing are two types of routing used in computer networks. Static routing is simple to configure and troubleshoot but does not adapt to changes in the network topology. Dynamic routing is suitable for large networks with frequent topology changes but is more complex to configure and troubleshoot. Routing protocols are used to facilitate the exchange of routing information between routers, and some of the commonly used routing protocols are RIP, OSPF, and BGP.