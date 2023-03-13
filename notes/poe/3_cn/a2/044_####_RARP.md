 Here is the content in markdown format on the topic #### RARP:

#### RARP

RARP stands for Reverse Address Resolution Protocol. It is used to map a physical address (MAC address) to an IP address.

- RARP is the reverse of ARP which maps IP addresses to MAC addresses.
- In RARP, the physical address is known but the corresponding IP address is required. The RARP request is sent as a broadcast and the device with the specified physical address responds with its IP address.
- RARP is used during booting process to obtain the IP address of a booting device. The booting device sends a RARP request with its MAC address. The RARP server responds with the IP address configured for that MAC address. This enables the booting device to participate in IP networking.
- RARP has been deprecated and replaced by BOOTP and DHCP protocols which are more robust and flexible.

**Mnemonics:**
**R**everse **A**ddress **R**esolution **P**rotocol - Maps MAC to IP
**R**equest sent with MAC, **R**esponse contains IP

**Learning Tricks:**
- Remember RARP is reverse of ARP
- Used during booting to get IP address from MAC address
- Replaced by BOOTP and DHCP

**Advantages:**
- Simple protocol to dynamically allocate IP addresses based on MAC addresses

**Disadvantages:**
- Inefficient as it broadcasts requests
- Limited features compared to BOOTP and DHCP

**Examples:**
- A booting device sends RARP request with its MAC address 0000.0000.0001. RARP server responds with IP address 192.168.1.10 which is configured for that MAC address. The booting device can now use this IP address to participate in networking.

**Applications:**
- Mostly used during booting process to obtain IP address
- Legacy protocol, not used nowadays due to limitations and inefficiencies