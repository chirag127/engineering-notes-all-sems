### Forwarding and delivery in network layer

- Forwarding is the process of moving packets from an input interface to an output interface on a router based on the destination address and routing table.
- Delivery is the process of delivering packets to the final destination host or network.
- Forwarding and delivery are two different functions performed by the network layer.
- Forwarding can be done in two ways: datagram-based or virtual-circuit-based.
  - Datagram-based forwarding: each packet is forwarded independently based on its destination address and the current state of the network. No connection is established between the source and destination before sending packets. This is used by IP protocol.
  - Virtual-circuit-based forwarding: a connection or a virtual circuit is established between the source and destination before sending packets. Each packet is forwarded along the same path based on a virtual circuit identifier. This is used by ATM protocol.
- Delivery can be done in two ways: direct or indirect.
  - Direct delivery: the destination host is on the same physical network as the source host or the last router. The network layer delivers the packet directly to the destination host by using its physical address (such as MAC address).
  - Indirect delivery: the destination host is on a different physical network than the source host or the last router. The network layer delivers the packet to the next router that is closer to the destination host by using its physical address. This process is repeated until the packet reaches the final destination.

- A mnemonic to remember the difference between forwarding and delivery is: **F**orwarding is **F**rom input to output, **D**elivery is **D**own to the host.
- A mnemonic to remember the difference between datagram-based and virtual-circuit-based forwarding is: **D**atagram is **D**ynamic, **V**irtual circuit is **V**alidated.