#### RARP

Reverse Address Resolution Protocol (RARP) is a protocol used to resolve a network device's physical address (MAC address) from its IP address. RARP is the opposite of Address Resolution Protocol (ARP), which resolves a device's IP address from its MAC address.

RARP operates by broadcasting a RARP request packet on a network to obtain the MAC address of a device with a given IP address. The device with the matching IP address responds with its MAC address, allowing the requesting device to establish a link with the other device.

Here are some key points to remember about RARP:

- RARP is typically used in legacy environments where devices do not have the capability to store their MAC addresses in non-volatile memory.
- RARP requires a dedicated RARP server, which maintains a table of IP addresses and their corresponding MAC addresses.
- RARP operates at the data link layer (Layer 2) of the OSI model.
- RARP packets consist of a header and a payload. The header contains information such as the source and destination MAC addresses, while the payload contains the IP address being queried.
- RARP has largely been replaced by DHCP (Dynamic Host Configuration Protocol), which provides a more flexible and scalable solution for assigning IP addresses and other network configuration information to devices.

While RARP is no longer widely used, it is still important to understand its principles and how it operates, particularly in legacy environments. Remembering the key points listed above can help you understand and remember the basics of RARP.