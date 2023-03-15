### Packet filtering firewall

- A packet filtering firewall is the most basic type of firewall that controls data flow to and from a network .
- It is a network security solution that allows network packets to move across between networks and controls their flow using a set of user-defined rules, IP addresses, ports, and protocols .
- A packet filtering firewall can be implemented as a router that operates in the low levels of a network protocol stack.
- A packet filtering firewall can provide the following benefits:
  - It can prevent unauthorized access to a network by blocking packets from untrusted sources or destinations.
  - It can improve network performance by reducing the amount of traffic that reaches the internal network.
  - It can enhance network transparency by allowing legitimate packets to pass through without modification or delay.
- A packet filtering firewall can also have some limitations :
  - It cannot inspect the content or payload of the packets, so it cannot detect malicious code or data that may be embedded in them.
  - It cannot prevent attacks that use spoofed or forged IP addresses or ports, as it relies on the header information of the packets.
  - It cannot handle complex or dynamic protocols that use multiple ports or change ports during a session, such as FTP or VoIP.
  - It cannot provide stateful inspection, which means it cannot keep track of the state or context of a connection, such as whether it is initiated by an internal or external host, or whether it is part of an ongoing or new session.