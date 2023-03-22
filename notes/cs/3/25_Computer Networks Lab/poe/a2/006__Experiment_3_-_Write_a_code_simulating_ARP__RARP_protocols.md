 Here is the content in formal tone without emojis and external links:

## Experiment 3 - Write a code simulating ARP /RARP protocols

1. Address Resolution Protocol (ARP):
- ARP is used to map IP addresses to MAC addresses.
- When a machine wants to send an IP packet to another machine on the local network, it first checks its ARP cache for the MAC address corresponding to the IP address. If the entry is not found, it broadcasts an ARP request packet containing the IP address of the target machine. The machine with that IP address responds with its MAC address. The initiating machine caches this IP-MAC mapping and uses it to forward packets in the future.

2. Reverse Address Resolution Protocol (RARP):
- RARP is the reverse of ARP and is used to obtain an IP address from a MAC address.
- A machine broadcasts a RARP request containing its own MAC address. The server that maintains the IP-MAC mappings responds with the IP address corresponding to that MAC address.
- Code the following:
    - ARP request and response packets
    - RARP request and response packets
    - Populating and using ARP/RARP caches to forward packets

3. Learn and understand the following:
    - Ethernet header and trailer formats
    - IP header format
    - Broadcast addressing
    - Caching mechanisms

The above content summarizes the key points about ARP and RARP protocols in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.