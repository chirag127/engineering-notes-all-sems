## Unit 3 - Network Layer in Computer Networks

The network layer is the third layer of the OSI reference model. The network layer controls the operation of the subnet, which is a collection of networks interconnected by routers. The main aim of this layer is to deliver packets from source to destination across multiple links (networks)  . The network layer is involved both at the source host and the destination host, as well as at the intermediate routers.

The network layer provides the following services :

- Packetizing: The network layer receives data from the transport layer and divides it into smaller units called packets. Each packet has a header that contains information such as source and destination addresses, sequence number, and protocol type.
- Routing: The network layer determines the best path for each packet to reach its destination, based on factors such as network topology, traffic load, and routing algorithms. The network layer maintains routing tables that store information about the available routes and their costs.
- Forwarding: The network layer forwards each packet from one link to another, based on the routing decision. The network layer uses the address in the packet header to find the next hop (the next router or the destination host) and sends the packet to it.

The following diagram illustrates the basic architecture of the network layer:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Transport     |      |  Transport     |      |  Transport     |
|    Layer       |      |    Layer       |      |    Layer       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Network       |      |  Network       |      |  Network       |
|    Layer       |      |    Layer       |      |    Layer       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Data Link     |      |  Data Link     |      |  Data Link     |
|    Layer       |      |    Layer       |      |    Layer       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Physical      |      |  Physical      |      |  Physical      |
|    Layer       |      |    Layer       |      |    Layer       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
     Source             Intermediate            Destination
      Host                Router                  Host
```

The network layer is also responsible for error control, congestion control, and quality of service at the subnet level . The network layer can use different protocols to perform its functions, such as IP, ICMP, ARP, RARP, etc.  .