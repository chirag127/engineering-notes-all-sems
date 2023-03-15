### Packet filtering firewall

- A packet filtering firewall is the most basic type of firewall that controls data flow to and from a network .
- It is a network security solution that allows network packets to move across between networks and controls their flow using a set of user-defined rules, IP addresses, ports, and protocols .
- A packet filtering firewall can be implemented as a router that operates in the low levels of a network protocol stack.
- A packet filtering firewall can provide the following benefits:
  - It can block unwanted traffic based on source and destination addresses, ports, and protocols.
  - It can improve network performance by reducing the amount of traffic that reaches the internal network.
  - It can be transparent to the end users and applications, as it does not modify the packets or require any configuration on the client side.
- A packet filtering firewall can also have some limitations :
  - It cannot inspect the content or the state of the packets, so it cannot detect malicious or malformed packets that may exploit application vulnerabilities or bypass the rules.
  - It cannot prevent attacks that use spoofed or encrypted packets, as it cannot verify the identity or the integrity of the packets.
  - It cannot provide granular control over the network traffic, as it cannot distinguish between different types of applications or services that use the same port or protocol.
  - It can be vulnerable to denial-of-service (DoS) attacks, as it can be overwhelmed by a large number of packets that match the rules.