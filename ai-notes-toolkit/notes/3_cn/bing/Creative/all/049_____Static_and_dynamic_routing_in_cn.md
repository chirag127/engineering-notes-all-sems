### Static and dynamic routing in computer networks

- Static routing and dynamic routing are two methods used to determine how to send a packet toward its destination.
- Static routes are configured in advance of any network communication by the network administrator  .
- Dynamic routing requires routers to exchange information with other routers to learn about paths through the network .

#### Key differences between static and dynamic routing

- Path selection: Static routing uses a single preconfigured route to send traffic to its destination, while dynamic routing uses complex routing algorithms to select the best route based on network conditions .
- Ability to update routes: Network administrators must manually reconfigure static routes in order to adjust routes, while dynamic routing automatically adapts to network changes .
- Routing overhead: Static routing does not generate any routing overhead, while dynamic routing consumes bandwidth and CPU resources to exchange routing information .
- Security: Static routing provides more security as it does not expose the network topology, while dynamic routing provides less security as it may be vulnerable to attacks or misconfigurations.
- Scalability: Static routing is suitable for small networks with one or two routes, while dynamic routing is suitable for large networks with many routes .
- Reliability: Static routing does not provide any backup or alternative routes in case of link failures, while dynamic routing can provide redundancy and load balancing by using multiple routes .

#### Examples of static and dynamic routing protocols

- Static routing does not use any specific protocol, but rather relies on manual configuration of the routing table.
- Dynamic routing uses various protocols to exchange routing information, such as:
  - Distance vector protocols: These protocols use the hop count as the metric to determine the best route. Examples are RIP and IGRP.
  - Link state protocols: These protocols use the cost of the link as the metric to determine the best route. Examples are OSPF and IS-IS.
  - Path vector protocols: These protocols use the attributes of the path as the metric to determine the best route. Examples are BGP and EIGRP.

#### Advantages and disadvantages of static and dynamic routing

- Static routing has the following advantages:
  - It is simple and easy to configure.
  - It does not consume any bandwidth or CPU resources.
  - It provides more security and control over the network.
- Static routing has the following disadvantages:
  - It is not scalable or adaptable to network changes.
  - It does not provide any redundancy or load balancing.
  - It requires manual intervention and maintenance.
- Dynamic routing has the following advantages:
  - It is scalable and adaptable to network changes.
  - It provides redundancy and load balancing.
  - It does not require manual intervention and maintenance.
- Dynamic routing has the following disadvantages:
  - It is complex and difficult to configure.
  - It consumes bandwidth and CPU resources.
  - It provides less security and control over the network.

#### Mnemonics and learning tricks for static and dynamic routing

- One possible mnemonic to remember the difference between static and dynamic routing is:

  - Static routing is **S**imple, **S**ecure, and **S**tatic.
  - Dynamic routing is **D**ifficult, **D**emanding, and **D**ynamic.

- One possible learning trick to remember the types of dynamic routing protocols is:

  - Distance vector protocols use the **D**istance to the destination as the metric.
  - Link state protocols use the **L**ink cost as the metric.
  - Path vector protocols use the **P**ath attributes as the metric.