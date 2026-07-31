### Forwarding and Delivery for the Notes of the Unit 5 - Network Layer in the Subject of Computer Networks

- The network layer is responsible for the delivery of packets from the source host to the destination host across one or more networks.
- The network layer provides two main functions: forwarding and routing.
- Forwarding is the process of moving a packet from an input interface to an output interface of a router based on the destination address of the packet.
- Routing is the process of finding the best path from the source to the destination in the network.
- Forwarding and routing are closely related, but they are not the same. Forwarding is a local action, while routing is a global process.
- Forwarding can be done in two ways: datagram approach and virtual circuit approach.
- In the datagram approach, each packet is treated independently and forwarded based on its destination address. The packets may take different paths and arrive out of order at the destination. This approach is used by the Internet Protocol (IP).
- In the virtual circuit approach, a connection is established between the source and the destination before any data is sent. The packets are forwarded along the same path and arrive in order at the destination. This approach is used by some network layer protocols such as X.25 and Frame Relay.
- Routing can be done in two ways: static routing and dynamic routing.
- In static routing, the routes are fixed and do not change unless the network topology changes. The routes are manually configured by the network administrator or by a routing protocol. Static routing is simple and reliable, but it cannot adapt to network failures or traffic variations.
- In dynamic routing, the routes are updated periodically based on the current network conditions. The routes are automatically learned by the routers using routing algorithms or protocols. Dynamic routing is more flexible and scalable, but it requires more computation and communication overhead.