# Static and Dynamic Routing

Static and dynamic routing are two methods used to determine how to send a packet toward its destination. 

## Static Routing

- Static routing is a technique of configuring routes manually in advance of any network communication.
- Static routing is often used for small networks that have one or two routes, or as a backup for dynamic routing.
- Static routing provides more security and less overhead than dynamic routing, but it is less adaptable to network changes and requires more manual intervention .

## Dynamic Routing

- Dynamic routing is a technique of using routing protocols to exchange information with other routers and learn about network paths.
- Dynamic routing is often used for large networks that have multiple routes and frequent changes in topology.
- Dynamic routing provides more flexibility and scalability than static routing, but it also consumes more bandwidth and compute power, and it may be less secure .
- Dynamic routing uses two types of protocols: distance vector protocols and link state protocols.
  - Distance vector protocols, such as RIP and IGRP, calculate the best route based on the distance and direction to the destination.
  - Link state protocols, such as OSPF and IS-IS, maintain a map of the network topology and update it periodically.
