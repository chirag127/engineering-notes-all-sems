A point-to-point network is a network topology that connects two nodes directly using a single link. In the network layer, point-to-point networks can use different protocols to encapsulate and transmit data over the link, such as Point-to-Point Protocol (PPP) or Point-to-Point Tunneling Protocol (PPTP). A point-to-point network can provide authentication, encryption, and compression of data.

A possible ASCII diagram for a point-to-point network in the network layer is:

```
+--------+    +--------+
| Node A |----| Node B |
+--------+    +--------+
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
+--------+    +--------+
| PPP    |----| PPP    |
+--------+    +--------+
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
   |             |
+--------+    +--------+
| Link   |----| Link   |
+--------+    +--------+
```

The diagram shows that Node A and Node B are connected by a single link, and they use PPP as the network layer protocol to encapsulate and transmit data over the link. The PPP layer can provide authentication, encryption, and compression of data. The link layer can be any physical medium that supports point-to-point communication, such as a serial cable, a phone line, or a wireless connection.