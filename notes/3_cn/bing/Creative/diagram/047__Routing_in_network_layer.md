Routing is the process of selecting a path across one or more networks for data packets to travel from their origin to their destination. Routing is performed by a special device known as a router, which works at the network layer in the OSI model and internet layer in TCP/IP model. A router is a networking device that forwards the packet based on the information available in the packet header and forwarding table. The routing algorithms are used for routing the packets.

Forwarding is the process of moving a packet from one interface to another within a router. Forwarding is based on the destination address in the packet header and the forwarding table in the router. Forwarding is a local action, while routing is a global process.

The following diagram illustrates the basic architecture of routing and forwarding in the network layer:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Source Host   |       |     Router 1    |       | Destination Host|
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Network Layer |       |   Network Layer |       |   Network Layer |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Data Link     |       |   Data Link     |       |   Data Link     |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Physical      |       |   Physical      |       |   Physical      |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+------+--------------------+ | +--------------------+------+
|                           | | |                           |
|                           | | |                           |
|                           | | |                           |
|                           | | |                           |
|                           | | |                           |
|                           | | |                           |
|                           | | |                           |
|                           | | |                           |
|                           | | |                           |
|                           | | |                           |
|                           | | |                           |
|                           | | |                           |
+------+--------------------+ | +--------------------+------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Network Layer |       |   Network Layer |       |   Network Layer |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Data Link     |       |   Data Link     |       |   Data Link     |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Physical      |       |   Physical      |       |   Physical      |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |