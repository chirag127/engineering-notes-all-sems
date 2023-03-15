# ARP

- ARP stands for Address Resolution Protocol.
- It is a network layer protocol that maps an IP address to a physical address (MAC address) of a device on the same network segment.
- It is used when a device wants to communicate with another device on the same network, but does not know its MAC address.
- ARP operates in two phases: request and reply.
- In the request phase, the sender broadcasts an ARP request packet to all devices on the network, asking for the MAC address of the device with a specific IP address.
- In the reply phase, the device with the matching IP address responds with an ARP reply packet, containing its MAC address.
- The sender then updates its ARP cache, which is a table that stores the IP-MAC mappings of known devices on the network, and uses the MAC address to send data packets to the destination.
- ARP is a stateless protocol, meaning it does not keep track of the status or validity of the ARP cache entries.
- ARP cache entries can expire or be overwritten by new mappings, depending on the implementation and configuration of the device.
- ARP can also be used to detect duplicate IP addresses on the network, by sending an ARP request for its own IP address and checking if any other device responds.
- ARP can also be exploited by malicious devices to perform ARP spoofing or poisoning, which is a technique of sending fake ARP replies to trick other devices into sending data to the wrong destination. This can result in data theft, interception, or modification.