### Static and dynamic routing

- Static routing and dynamic routing are two methods used to determine how to send a packet toward its destination.
- Static routes are configured in advance of any network communication  .
- Dynamic routing requires routers to exchange information with other routers to learn about paths through the network  .

#### Advantages and disadvantages of static routing

- Static routing is often more efficient because a link is not being wasted by exchanging dynamic routing information.
- Static routing provides high or more security because the administrator can control the traffic flow.
- Static routing is easy to configure and troubleshoot for small networks.
- Static routing requires less compute power and bandwidth, as it only has one preconfigured route.
- Static routing is not suitable for large networks because it is difficult to maintain and update the routing table manually.
- Static routing is not adaptive to network changes, such as link failures or congestion.
- Static routing can cause suboptimal routing, such as longer paths or loops.

#### Advantages and disadvantages of dynamic routing

- Dynamic routing uses complex routing algorithms, such as distance vector protocols (e.g., RIP and IGRP) and link state protocols (e.g., OSPF and IS-IS), to adjust routes .
- Dynamic routing provides less security because the routers share their routing information with other routers.
- Dynamic routing is automated and can adapt to network changes quickly and efficiently.
- Dynamic routing requires more compute power and bandwidth, as it involves periodic or triggered updates of routing information .
- Dynamic routing is suitable for large networks because it can handle complex topologies and scalability.
- Dynamic routing can avoid suboptimal routing, such as shorter paths or loops.
- Dynamic routing can cause routing instability, such as oscillations or flapping, if the routing updates are not synchronized or consistent.