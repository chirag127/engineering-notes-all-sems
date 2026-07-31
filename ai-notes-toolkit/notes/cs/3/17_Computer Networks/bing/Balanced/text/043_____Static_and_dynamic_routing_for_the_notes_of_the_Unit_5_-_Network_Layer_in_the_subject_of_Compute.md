### Static and dynamic routing

- Static routing and dynamic routing are two methods used to determine how to send a packet toward its destination.
- Static routes are configured in advance of any network communication.
- Dynamic routing requires routers to exchange information with other routers to learn about paths through the network.
- Static routing is often used for small networks or as a backup for dynamic routing.
- Dynamic routing is often used for large networks or to adapt to changing network conditions.

#### Advantages and disadvantages of static and dynamic routing

- Static routing provides more security, less computation and bandwidth requirements, and more control over the routing decisions .
- Static routing also has some drawbacks, such as manual configuration, lack of scalability, and difficulty in handling network failures .
- Dynamic routing provides more flexibility, adaptability, and scalability, and can handle network failures automatically .
- Dynamic routing also has some drawbacks, such as less security, more computation and bandwidth requirements, and dependence on routing protocols .

#### Types of dynamic routing protocols

- Dynamic routing protocols can be classified into two types: distance vector protocols and link state protocols .
- Distance vector protocols use the distance and direction of the destination to determine the best route. They exchange routing information with their immediate neighbors only .
- Examples of distance vector protocols are RIP and IGRP.
- Link state protocols use the state and cost of each link to determine the best route. They exchange routing information with all the routers in the network .
- Examples of link state protocols are OSPF and IS-IS.