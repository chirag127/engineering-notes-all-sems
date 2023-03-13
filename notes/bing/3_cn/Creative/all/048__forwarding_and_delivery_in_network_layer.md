### Forwarding and delivery in network layer

- Forwarding is the process of moving packets from an input interface to an output interface on a router based on the destination address and routing table.
- Delivery is the process of delivering packets to the final destination host or network.
- Forwarding and delivery are two main functions of the network layer in the TCP/IP model or the internet layer in the OSI model.
- Forwarding can be classified into two types: static and dynamic.
  - Static forwarding is when the routing table is manually configured by the network administrator and does not change unless updated manually.
  - Dynamic forwarding is when the routing table is automatically updated by routing protocols that exchange information with other routers and adapt to network changes.
- Delivery can be classified into two types: direct and indirect.
  - Direct delivery is when the source and destination hosts are on the same network and the packet is delivered directly to the destination host without passing through any routers.
  - Indirect delivery is when the source and destination hosts are on different networks and the packet is delivered through one or more routers until it reaches the destination network and then the destination host.
- A mnemonic to remember the difference between forwarding and delivery is: **F**orwarding is **F**rom input to output, **D**elivery is **D**estination host or network.
- A mnemonic to remember the difference between static and dynamic forwarding is: **S**tatic is **S**et by hand, **D**ynamic is **D**one by protocol.
- A mnemonic to remember the difference between direct and indirect delivery is: **D**irect is **D**one without router, **I**ndirect is **I**nvolving router.
- An example of forwarding and delivery in network layer is shown below:

```
  Source host A (192.168.1.10/24) wants to send a packet to destination host B (10.0.0.20/8).

  +-----------------+      +-----------------+      +-----------------+
  |  Host A         |      |  Router R1      |      |  Host B         |
  |  IP: 192.168.1.10/24   |  IP: 192.168.1.1/24    |  IP: 10.0.0.20/8 |
  |                 |      |      10.0.0.1/8 |      |                 |
  +-----------------+      +-----------------+      +-----------------+
       |                          |                          |
       |                          |                          |
       +--------------------------+--------------------------+
                        Network N (10.0.0.0/8)

  - Host A performs direct delivery to router R1, since they are on the same network (192.168.1.0/24).
  - Host A sets the destination IP address as 10.0.0.20 and the destination MAC address as the MAC address of router R1.
  - Host A sends the packet to router R1 using the data link layer protocol (e.g. Ethernet).

  - Router R1 performs forwarding to host B, since it has an interface on the destination network (10.0.0.0/8).
  - Router R1 looks up the destination IP address in its routing table and finds the output interface as 10.0.0.1/8.
  - Router R1 sets the source IP address as 10.0.0.1 and the source MAC address as its own MAC address on the 10.0.0.1/8 interface.
  - Router R1 sets the destination IP address as 10.0.0.20 and the destination MAC address as the MAC address of host B.
  - Router R1 sends the packet to host B using the data link layer protocol (e.g. Ethernet).

  - Host B performs direct delivery to itself, since it is the final destination host.
  - Host B receives the packet and checks the destination IP address and MAC address.
  - Host B processes the packet at the network layer and above.
```