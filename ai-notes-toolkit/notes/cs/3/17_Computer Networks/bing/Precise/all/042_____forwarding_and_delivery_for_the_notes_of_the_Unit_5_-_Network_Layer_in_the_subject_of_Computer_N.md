# Forwarding and Delivery

Forwarding and delivery are two important concepts in the network layer of the OSI model in computer networks.

## Forwarding

- Forwarding refers to the process of moving a packet from an incoming link to the appropriate outgoing link at a router.
- The forwarding decision is made based on the destination address of the packet and the forwarding table of the router.
- The forwarding table contains information about the next hop for each possible destination address.
- The forwarding table is typically populated using routing algorithms, which determine the best path for packets to take through the network.

## Delivery

- Delivery refers to the process of delivering a packet from the source host to the destination host.
- The delivery process involves multiple steps, including forwarding at intermediate routers and transmission over multiple links.
- The delivery process is typically reliable, meaning that packets are guaranteed to be delivered to the destination host, although there may be some delay or packet loss.
- The delivery process is typically transparent to the higher layers of the OSI model, meaning that the higher layers do not need to be aware of the details of the delivery process.
