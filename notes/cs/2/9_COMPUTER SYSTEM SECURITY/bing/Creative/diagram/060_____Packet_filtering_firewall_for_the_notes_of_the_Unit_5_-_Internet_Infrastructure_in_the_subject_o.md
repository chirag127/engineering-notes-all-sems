### Packet filtering firewall

- A packet filtering firewall is the most basic type of firewall that controls data flow to and from a network .
- It is a network security solution that allows network packets to move across between networks and controls their flow using a set of user-defined rules, IP addresses, ports, and protocols .
- A packet filtering firewall can be implemented as a router that operates in the low levels of a network protocol stack.
- A packet filtering firewall can provide the following benefits :
  - It can block unwanted traffic based on source and destination addresses, ports, and protocols.
  - It can improve network performance by reducing the amount of traffic that reaches the internal network.
  - It can prevent network scanning and reconnaissance by hiding the internal network topology and services.
  - It can be easily configured and maintained with minimal overhead.
- A packet filtering firewall can also have the following limitations :
  - It cannot inspect the content or context of the packets, only the header information.
  - It cannot prevent application-level attacks, such as viruses, worms, or malware.
  - It cannot distinguish between legitimate and illegitimate requests from the same source or destination.
  - It can be vulnerable to spoofing, fragmentation, and denial-of-service attacks.
- A packet filtering firewall can be classified into two types:
  - Stateless packet filtering firewall: It examines each packet individually and does not keep track of the connection state or history. It is faster but less secure.
  - Stateful packet filtering firewall: It examines each packet in relation to the previous and subsequent packets and maintains a state table of the connection information. It is slower but more secure.