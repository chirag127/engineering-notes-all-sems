Forwarding and delivery in network layer are two important functions that enable the transmission of packets across multiple networks. Forwarding is the local action of a router to transfer a packet from an input link to the appropriate output link based on the destination address and the routing table. Delivery is the end-to-end process of sending a packet from the source host to the destination host.

The following diagram illustrates the basic architecture of forwarding and delivery in network layer using ASCII characters:

```
    +----+       +----+       +----+       +----+       +----+
    | H1 |-------| R1 |-------| R2 |-------| R3 |-------| H2 |
    +----+       +----+       +----+       +----+       +----+
Source host   Router 1    Router 2    Router 3    Destination host

H1 wants to send a packet to H2. The packet has a network layer header that contains the source and destination addresses.

H1 sends the packet to R1, which is the first hop router on the path to H2. R1 looks up the destination address in its routing table and finds the next hop router, which is R2. R1 forwards the packet to R2.

R2 receives the packet and repeats the same process. It looks up the destination address in its routing table and finds the next hop router, which is R3. R2 forwards the packet to R3.

R3 receives the packet and checks the destination address. It finds that the destination host, H2, is on the same network as itself. R3 delivers the packet to H2.

H2 receives the packet and processes the network layer header. It finds that the packet is intended for itself and passes the packet to the upper layer protocol.
```