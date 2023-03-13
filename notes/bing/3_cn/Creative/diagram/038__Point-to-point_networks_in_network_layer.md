### Point-to-point networks in network layer

A point-to-point network is a network that connects two devices directly without any intermediate devices or networks. In the network layer, a point-to-point network can use different protocols to encapsulate and transmit data packets over the link. One of the most common protocols is the Point-to-Point Protocol (PPP), which is a data link layer protocol that can provide authentication, encryption, and compression features. PPP can also support multiple network layer protocols, such as IP, IPX, or AppleTalk.

The following diagram illustrates the basic architecture of a point-to-point network using PPP in the network layer:

```
+----------------+    +----------------+
|                |    |                |
|  Network Layer |    |  Network Layer |
|                |    |                |
+----------------+    +----------------+
|                |    |                |
|   PPP Header   |    |   PPP Header   |
|                |    |                |
+----------------+    +----------------+
|                |    |                |
|   Data Link    |    |   Data Link    |
|    Layer       |    |    Layer       |
|                |    |                |
+----------------+    +----------------+
|                |    |                |
|   Physical     |    |   Physical     |
|    Layer       |    |    Layer       |
|                |    |                |
+----------------+    +----------------+
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
       +----------------------+
              Point-to-point
                Link
```