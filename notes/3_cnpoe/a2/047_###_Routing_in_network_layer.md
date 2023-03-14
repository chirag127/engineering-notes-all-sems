 Here is the content on the topic ### Routing in network layer in markdown format:

### Routing in network layer

The network layer is responsible for routing of packets from source to destination. Routing is the process of selecting paths for traffic in a network based on network conditions, priority, and other routing criteria.

Following are some key points about routing in network layer:

1. Routing tables: Routers maintain routing tables which contain routing information and are used to determine the best path for forwarding packets. The routing tables are updated using routing protocols.
2. Distance vector routing protocols: These protocols (like RIP and IGRP) determine the best route based on hop count. Routers advertise the entire route table periodically to neighbours. Limitation is that they can suffer from routing loops and converge slowly on topology changes.
3. Link state routing protocols: These protocols (like OSPF and IS-IS) determine the best route based on link bandwidth and delay. Routers advertise only local connectivity information and use Dijkstra's algorithm to determine the best routes. They converge faster than distance vector protocols but require more resources.
4. Policy based routing: In this, routes are selected based on configured policies and traffic classification. It provides more control but is complex to configure and manage.
5. Static routing: Simplest form where routes are manually configured and don't change unless explicitly changed. Not adaptive to changes but sufficient for small networks with simple topology.

Advantages of routing: Efficient utilisation of network resources, fault tolerance, load balancing.
Disadvantages: Complexity, resource intensive, possibility of routing loops and blackholes.

Applications: Enterprise networks, ISPs, Internet routing.

[Include diagrams and examples here if required]

Hope this helps! Let me know if you would like me to elaborate on any of the points or add more details.