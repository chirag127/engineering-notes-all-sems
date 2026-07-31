### Packet filtering firewall

- A packet filtering firewall is the most basic type of firewall that controls data flow to and from a network .
- It is a network security solution that allows network packets to move across between networks and controls their flow using a set of user-defined rules, IP addresses, ports, and protocols .
- A packet filtering firewall can be implemented as a router that operates in the low levels of a network protocol stack.
- A packet filtering firewall can provide the following benefits :
  - It can block unwanted traffic based on the source and destination addresses, ports, and protocols.
  - It can improve network performance by reducing the amount of traffic that reaches the internal network.
  - It can prevent network scanning and reconnaissance by hiding the internal network topology and services.
  - It can be easily configured and maintained with simple rules and filters.
- A packet filtering firewall can also have some limitations :
  - It cannot inspect the content or the application layer data of the packets, which may contain malicious code or commands.
  - It cannot prevent attacks that use valid addresses, ports, and protocols, such as denial-of-service (DoS) attacks or spoofing attacks.
  - It cannot provide stateful inspection, which means it cannot keep track of the connection state and context of the packets.
  - It cannot provide user authentication or encryption, which means it cannot verify the identity or the integrity of the packets.
- A packet filtering firewall can be classified into two types:
  - Stateless packet filtering firewall: This type of firewall only examines each packet individually and does not store any information about the previous packets or the connection state. It is faster and simpler, but less secure and more prone to errors.
  - Stateful packet filtering firewall: This type of firewall examines each packet in relation to the previous packets and the connection state. It can keep track of the sessions and the sequence numbers of the packets. It is more secure and accurate, but slower and more complex.