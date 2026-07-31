# Mobile IP

Mobile IP is a communication protocol that allows mobile device users to move from one network to another while maintaining the same permanent IP address. Mobile IP is an extension of the Internet Protocol (IP) and is defined by the Internet Engineering Task Force (IETF) in RFC 2002 and RFC 5944.

## Overview of Mobile IP

Mobile IP enables seamless and continuous Internet connectivity for mobile devices. Mobile IP is useful for roaming between overlapping wireless systems, such as WLAN, WiMAX, and cellular networks. Mobile IP can also support mobility across different types of networks, such as wired and wireless LANs.

Mobile IP works by using two types of IP addresses: a home address and a care-of address. The home address is the permanent IP address of the mobile device, which belongs to its home network. The care-of address is the temporary IP address of the mobile device, which belongs to the current network that the device is visiting. The care-of address changes as the device moves from one network to another.

Mobile IP also uses three types of entities: a home agent, a foreign agent, and a mobile node. The home agent is a router on the home network that maintains a binding between the home address and the care-of address of the mobile device. The foreign agent is a router on the visited network that provides routing services to the mobile device. The mobile node is the mobile device that uses Mobile IP to communicate with other nodes on the Internet.

The basic operation of Mobile IP is as follows:

- When the mobile node is on its home network, it communicates with other nodes using its home address as the source and destination IP address.
- When the mobile node moves to a foreign network, it obtains a care-of address from the foreign agent or by using DHCP. The mobile node then registers its care-of address with its home agent, which creates a binding entry in its binding cache.
- The home agent intercepts any packets destined to the home address of the mobile node and tunnels them to the care-of address of the mobile node. The foreign agent decapsulates the packets and delivers them to the mobile node.
- The mobile node can also send packets to other nodes using its home address as the source IP address. The foreign agent encapsulates the packets and tunnels them to the home agent, which decapsulates the packets and forwards them to the destination node.

## Advantages and Disadvantages of Mobile IP

Some of the advantages of Mobile IP are:

- It supports transparent mobility for mobile devices across different networks and subnets.
- It preserves the existing IP applications and security mechanisms without requiring any modifications.
- It is scalable and compatible with the Internet infrastructure and standards.

Some of the disadvantages of Mobile IP are:

- It introduces additional overhead and latency due to the tunneling and encapsulation processes.
- It may cause suboptimal routing and increased network congestion due to the triangular routing problem.
- It may suffer from security issues such as spoofing, replay, and denial-of-service attacks.

## References

: Mobile IP | What is Mobile IP - javatpoint. https://www.javatpoint.com/what-is-mobile-ip
: Mobile IP - Wikipedia. https://en.wikipedia.org/wiki/Mobile_IP
: Introduction to Mobile IP - Cisco. https://www.cisco.com/c/en/us/td/docs/ios/solutions_docs/mobile_ip/mobil_ip.html
: How to Find Your Phone's IP Address on Android or iPhone - MUO. https://www.makeuseof.com/tag/find-ip-address-mobile-smartphone/