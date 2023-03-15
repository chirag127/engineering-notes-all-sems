# Forwarding and Delivery for the Notes of the Unit 5 - Network Layer in the Subject of Computer Networks

- The network layer is responsible for the delivery of packets from the source host to the destination host across one or more networks.
- The network layer provides two main functions: forwarding and routing.
- Forwarding is the process of moving a packet from an input link interface to the appropriate output link interface of a router based on the destination address in the packet header.
- Routing is the process of finding the best path from the source to the destination in the network topology based on some criteria such as distance, cost, or congestion.
- Forwarding and routing are closely related but not the same. Forwarding is a local action performed by each router, while routing is a global process that involves the exchange of information among routers.
- There are two types of delivery in the network layer: direct and indirect.
- Direct delivery occurs when the source and destination hosts are on the same network. In this case, the network layer does not need to do anything, and the packet is delivered directly to the destination by the data link layer.
- Indirect delivery occurs when the source and destination hosts are on different networks. In this case, the network layer needs to use the services of the routers to forward the packet from one network to another until it reaches the destination network.
- There are two types of routing in the network layer: static and dynamic.
- Static routing is when the routes are fixed and do not change over time. Static routing can be configured manually by the network administrator or by using a default route that points to a gateway router.
- Dynamic routing is when the routes are updated periodically based on the current network conditions. Dynamic routing can be implemented by using routing protocols that exchange information among routers and use algorithms to compute the best routes.