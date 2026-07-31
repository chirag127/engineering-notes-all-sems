Forwarding and delivery are two important functions of the network layer. Forwarding is the process of moving a packet from an input link to an appropriate output link at a router. Delivery is the process of sending the packet to the final destination.

A diagram for forwarding and delivery in network layer is shown below. It uses ASCII characters to represent the network elements and the packet flow.

### Forwarding and delivery in network layer

```
    +----+      +----+      +----+      +----+
    | H1 |------| R1 |------| R2 |------| H2 |
    +----+      +----+      +----+      +----+
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       |           |           |           |
       V           V           V           V
    +----+      +----+      +----+      +----+
    | H3 |------| R3 |------| R4 |------| H4 |
    +----+      +----+      +----+      +----+

    H1, H2, H3, H4 are hosts
    R1, R2, R3, R4 are routers
    The arrows indicate the direction of packet flow

    Example: H1 wants to send a packet to H4

    1. H1 creates a packet with the destination address of H4 and sends it to R1
    2. R1 looks up the destination address in its routing table and forwards the packet to R2
    3. R2 looks up the destination address in its routing table and forwards the packet to R4
    4. R4 looks up the destination address in its routing table and forwards the packet to H4
    5. H4 receives the packet and processes it
```