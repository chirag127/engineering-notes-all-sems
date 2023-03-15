### Static and dynamic routing in computer networks

- Static routing and dynamic routing are two methods used to determine how to send a packet toward its destination.
- Static routes are configured in advance of any network communication by the network administrator  .
- Dynamic routes are learned by routers through exchanging information with other routers using complex routing algorithms .

#### Advantages and disadvantages of static routing

- Static routing provides more security as the routes are not advertised to other routers.
- Static routing is more efficient as it does not consume bandwidth or CPU resources for exchanging routing information.
- Static routing is easier to implement and troubleshoot in small networks .
- Static routing is less adaptable to network changes or failures as the routes have to be manually reconfigured .
- Static routing is not scalable for large networks as it requires a lot of manual work and maintenance .

#### Advantages and disadvantages of dynamic routing

- Dynamic routing provides more flexibility and reliability as it can adjust routes automatically based on network conditions or topology changes .
- Dynamic routing is more scalable for large networks as it reduces the administrative burden and complexity of routing configuration .
- Dynamic routing provides less security as the routes are advertised to other routers and may be vulnerable to attacks or misconfigurations.
- Dynamic routing is less efficient as it consumes bandwidth and CPU resources for exchanging routing information and running routing algorithms.
- Dynamic routing is harder to implement and troubleshoot in complex networks as it requires a good understanding of the routing protocols and their parameters.

#### Types of static routes

- Standard static route: a static route that specifies the next-hop address or interface to reach a specific destination network.
- Default static route: a static route that matches all packets that do not have a more specific route in the routing table and sends them to a default gateway.
- Summary static route: a static route that aggregates multiple subnets into a single route and reduces the size of the routing table.
- Floating static route: a static route that has a higher administrative distance than a dynamic route and acts as a backup route in case the dynamic route fails.