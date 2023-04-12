Routing in network layer is the process of finding and selecting the best path for sending data packets from the source host to the destination host in a network. The network layer is the third layer of the OSI model and the internet layer of the TCP/IP model. The network layer is responsible for addressing, routing, fragmentation, and reassembly of data packets. The main protocols used at this layer are IP and ICMP.

A router is a device that works at the network layer and forwards data packets based on the information available in the packet header and the forwarding table. The forwarding table is a data structure that stores the mapping between network addresses and the next hop router or interface. The forwarding table is updated by routing algorithms, which are strategies for finding the best route for each destination. Routing algorithms can be classified into two types: static and dynamic. Static routing algorithms use fixed routes that are manually configured or rarely changed. Dynamic routing algorithms use information from the network topology and traffic conditions to update the routes automatically.

A possible ASCII diagram for routing in network layer is shown below:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Source host  |      |    Router A    |      | Destination    |
|                |      |                |      |    host        |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Router B    |      |    Router C    |      |    Router D    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Router E    |      |    Router F    |      |    Router G    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Router H    |      |    Router I    |      |    Router J    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |

```
