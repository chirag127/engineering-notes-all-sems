 Here is the formal notes on ARP for the Network Layer (Unit 5) in Computer Networks:

### ARP

ARP stands for Address Resolution Protocol. It is a protocol used for discovering the link layer address, such as a MAC address, associated with a given internet layer address, typically an IPv4 address.

- ARP is used when a device needs to send packets to another device on the local network. The sending device needs to resolve the IP address to MAC address.
- The device will broadcast an ARP request containing the IP address of the destination device. The device with that IP address will respond with its MAC address.
- The sending device will then use the MAC address to send packets to the destination device.
- ARP is limited to the local network and uses broadcasts to locate devices.
- The mappings of IP to MAC addresses are stored in the ARP cache to speed up future communications with the same device. The cache entries eventually expire if not used.
- ARP does not work for devices located on other networks or networks separated by routers since broadcasts do not pass through routers.
- ARP has vulnerabilities and can be a target of ARP spoofing attacks where malicious actors send spoofed ARP responses to redirect traffic.

The notes cover the key points about ARP, how it functions to resolve IP addresses to MAC addresses, its limitations, usage, and vulnerabilities. The points are written in a formal tone with no emojis or external links as instructed. Please let me know if you would like me to elaborate on any part or modify the notes.