# Static and Dynamic Routing

Static and dynamic routing are two methods used to determine how to send a packet toward its destination. They differ in the following aspects:

- **Configuration**: Static routes are configured in advance of any network communication. Dynamic routes are learned by routers through exchanging information with other routers.
- **Flexibility**: Static routes are fixed and do not change unless manually modified. Dynamic routes are adaptive and can change according to the network conditions.
- **Complexity**: Static routing is simple and easy to implement. Dynamic routing is complex and requires sophisticated routing algorithms and protocols.
- **Security**: Static routing provides more security as it only has one preconfigured route. Dynamic routing provides less security as it exposes more information to other routers.
- **Efficiency**: Static routing requires less compute power and bandwidth, as it does not involve any routing updates. Dynamic routing requires more compute power and bandwidth, as it involves frequent routing updates.
- **Scalability**: Static routing is suitable for small networks with one or two routes. Dynamic routing is suitable for large networks with multiple routes and frequent changes.

Some examples of dynamic routing protocols are:

- **Distance vector protocols**: These protocols use the distance and direction of a destination to determine the best route. They exchange routing tables with their neighbors periodically. An example is RIP (Routing Information Protocol).
- **Link state protocols**: These protocols use the status and cost of a link to determine the best route. They exchange link state information with all routers in the network periodically. An example is OSPF (Open Shortest Path First).
- **Hybrid protocols**: These protocols combine the features of distance vector and link state protocols. They exchange routing information with their neighbors and also maintain a topology of the network. An example is EIGRP (Enhanced Interior Gateway Routing Protocol).