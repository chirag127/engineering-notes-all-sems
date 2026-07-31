### Static and dynamic routing

Static and dynamic routing are two methods used to determine how to send a packet toward its destination. They differ in the following aspects:

- **Configuration**: Static routes are configured in advance of any network communication. Dynamic routes are learned by routers through communication with other routers using routing protocols.
- **Routing table**: Static routing has a smaller routing table with only one entry for each destination, while dynamic routing requires routers to send out their entire routing tables to identify route availability.
- **Adaptability**: Static routing is non-adaptive, meaning it does not react to network changes, such as link failures or congestion. Dynamic routing is adaptive, meaning it can adjust to network changes and find the best path for each packet.
- **Protocols and algorithms**: Static routing does not use protocols or complex routing algorithms. Dynamic routing uses various protocols and algorithms, such as OSPF, EIGRP, RIP, IS-IS, BGP, etc., to exchange routing information and calculate the optimal routes.
- **Overhead**: Static routing has low overhead, as it does not consume bandwidth or CPU resources for routing updates. Dynamic routing has high overhead, as it requires frequent routing updates and computations, which consume bandwidth and CPU resources.
- **Security**: Static routing is more secure, as it does not expose the network topology or routing information to other routers. Dynamic routing is less secure, as it requires routers to share their routing information with other routers, which may be compromised or malicious.
- **Scalability**: Static routing is less scalable, as it requires manual configuration and maintenance for each router and network change. Dynamic routing is more scalable, as it can handle large and complex networks with minimal configuration and maintenance.
- **Reliability**: Static routing is less reliable, as it does not provide redundancy or load balancing for network traffic. Dynamic routing is more reliable, as it can provide redundancy and load balancing for network traffic by using multiple paths and metrics.
- **Suitability**: Static routing is suitable for small and simple networks with stable and predictable traffic patterns. Dynamic routing is suitable for large and complex networks with dynamic and unpredictable traffic patterns.