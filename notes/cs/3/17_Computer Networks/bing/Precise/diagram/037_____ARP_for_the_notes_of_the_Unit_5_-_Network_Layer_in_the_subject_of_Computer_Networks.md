### ARP (Address Resolution Protocol)

ARP is a protocol used to map an IP address to a physical (MAC) address on a local network. It is a crucial component of the network layer in the OSI model. Here are some key points to remember about ARP:

1. ARP operates at the Data Link layer of the OSI model.
2. ARP is used to find the MAC address of a device on the local network, given its IP address.
3. ARP maintains a cache of recently resolved IP-to-MAC address mappings to reduce the number of ARP requests.
4. ARP requests are broadcast to all devices on the local network.
5. ARP replies are sent directly to the requesting device.
6. ARP is a stateless protocol, meaning it does not keep track of ongoing communications or previous requests.
7. ARP can be used for both IPv4 and IPv6 addresses.
8. ARP is vulnerable to spoofing attacks, where an attacker can send false ARP replies to redirect traffic to their device.
