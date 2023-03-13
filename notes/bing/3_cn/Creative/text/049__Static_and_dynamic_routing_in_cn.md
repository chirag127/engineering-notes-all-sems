### Static and dynamic routing in computer networks

- Static routing and dynamic routing are two methods used to determine how to send a packet toward its destination.
- Static routes are configured in advance of any network communication. Static routing is often used for small networks or as a backup for dynamic routing.
- Dynamic routing, on the other hand, requires routers to exchange information with other routers to learn about paths through the network. Dynamic routing is often used for large networks or to adapt to changing network conditions.
- Some of the key differences between static and dynamic routing are  :
  - Path selection: Static routing uses a single preconfigured route to send traffic to its destination, while dynamic routing uses complex routing algorithms to select the best route based on various factors such as hop count, bandwidth, load, etc.
  - Ability to update routes: Network administrators must manually reconfigure static routes in order to adjust routes or add new destinations, while dynamic routing automatically updates routes based on the information received from other routers.
  - Routing overhead: Static routing does not generate any routing overhead, as no routing messages are exchanged between routers, while dynamic routing consumes some network bandwidth and router resources to exchange routing information and maintain routing tables.
  - Security: Static routing provides more security, as the routes are not exposed to other routers or potential attackers, while dynamic routing provides less security, as the routing information can be intercepted or manipulated by malicious actors.
  - Scalability: Static routing is not scalable, as it becomes difficult and error-prone to manage static routes for large networks, while dynamic routing is scalable, as it can handle network growth and changes without manual intervention.