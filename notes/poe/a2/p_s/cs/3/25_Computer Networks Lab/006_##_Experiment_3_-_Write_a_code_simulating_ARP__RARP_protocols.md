 Here is the content in markdown format for ## Experiment 3 - Write a code simulating ARP /RARP protocols:

## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP (Address Resolution Protocol) is a protocol used to map IP addresses to MAC addresses. It is used when a device needs to send a packet to another device on the same network. The device will first check its ARP cache for the MAC address corresponding to the IP address. If not found, it will broadcast an ARP request to all devices on the network asking for the MAC address of the IP address. The device with that IP address will reply with its MAC address. The original device will store this address in its ARP cache and then use it to send the packet.
- RARP (Reverse Address Resolution Protocol) is almost similar to ARP but works in the reverse direction. A device will broadcast a RARP request asking for its own IP address if it only knows its MAC address. The server which maintains the IP to MAC address mapping will reply with the IP address corresponding to the MAC address. This is often used by diskless workstations while booting up to obtain their IP address.
- We can write code to simulate the working of ARP and RARP by implementing the following:
    - ARP:
        - Create an ARP cache (dictionary/hash map) to store IP-MAC address mappings
        - Listen for ARP requests (broadcasts)
        - Check own ARP cache for mapping, if not present, reply with own MAC address for the requested IP address
        - Update own ARP cache with IP-MAC address mapping received in ARP replies
    - RARP:
        - Listen for RARP requests (broadcasts) containing a MAC address
        - Look up the MAC address in the IP-MAC address mapping and reply with the corresponding IP address
- The code can be written in languages like Python/C/C++ and can simulate scenarios like multiple devices sending ARP/RARP requests and updating their cache, devices going offline/coming back online, etc. to demonstrate the working of these protocols.
- Advantages: Resolves IP addresses to MAC addresses efficiently. Disadvantages: Vulnerable to ARP spoofing attacks.
- Applications: Critical for communication in Ethernet networks. Enables translation between layer 3 and layer 2 addresses.