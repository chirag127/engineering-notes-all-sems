Routing is the process of finding the best path for a packet to reach its destination in a network. Routing is performed by a special device known as a router, which works at the network layer in the OSI model and internet layer in TCP/IP model. A router is a networking device that forwards the packet based on the information available in the packet header and forwarding table. The routing algorithms are used for routing the packets .

The following diagram illustrates the basic architecture of a router and how it performs routing in the network layer:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Application   |    |   Application   |    |   Application   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Transport     |    |   Transport     |    |   Transport     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Network       |    |   Network       |    |   Network       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Link     |    |   Data Link     |    |   Data Link     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Physical      |    |   Physical      |    |   Physical      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Physical      |    |   Physical      |    |   Physical      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Link     |    |   Data Link     |    |   Data Link     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Network       |    |   Network       |    |   Network       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Routing       |    |   Routing       |    |   Routing       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Link     |    |   Data Link     |    |   Data Link     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Physical      |    |   Physical      |    |   Physical      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |