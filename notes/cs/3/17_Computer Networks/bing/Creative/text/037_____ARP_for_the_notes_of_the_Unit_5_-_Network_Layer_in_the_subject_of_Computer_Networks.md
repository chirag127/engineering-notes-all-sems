### ARP

- ARP stands for Address Resolution Protocol   .
- It is a communication protocol used for discovering the link layer address, such as a MAC address, associated with a given internet layer address, typically an IPv4 address   .
- It is a critical function in the Internet protocol suite, as it enables devices to communicate within a local area network (LAN)   .
- ARP was defined in 1982 by RFC 826, which is Internet Standard STD 37.
- ARP operates by sending broadcast messages to all devices in the LAN, asking for the MAC address of the device that has a specific IP address.
- The device that has the requested IP address replies with its MAC address, and the sender stores this information in a cache for future use.
- ARP can also be used to update or delete entries in the cache, or to resolve conflicts between IP and MAC addresses.
- ARP has some limitations and vulnerabilities, such as the lack of authentication, the possibility of ARP spoofing or poisoning, and the scalability issues in large networks   .
- To overcome some of these problems, various extensions and modifications of ARP have been proposed, such as Reverse ARP (RARP), Proxy ARP, Gratuitous ARP, Inverse ARP (InARP), and Neighbor Discovery Protocol (NDP)   .