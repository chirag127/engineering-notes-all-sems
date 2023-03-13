#### RARP

RARP stands for Reverse Address Resolution Protocol. It is a protocol used to map a known physical address (MAC address) to an unknown IP address. RARP is the opposite of ARP (Address Resolution Protocol), which maps an IP address to a MAC address.

Here are some key points to remember about RARP:

- RARP is an obsolete protocol that is no longer widely used. It has been replaced by DHCP (Dynamic Host Configuration Protocol), which is more flexible and easier to manage.
- RARP is used primarily in legacy systems that do not support DHCP. It was commonly used in Unix-based systems in the 1980s and 1990s.
- RARP works by broadcasting a request for an IP address, along with the MAC address of the requesting device. A RARP server on the network responds with the corresponding IP address, which is then assigned to the requesting device.
- RARP has several disadvantages compared to DHCP. First, it requires a separate server to manage IP address assignments. Second, it does not support dynamic IP address assignments, which can lead to conflicts if two devices on the network request the same IP address. Finally, it is vulnerable to security attacks, as it does not include any authentication mechanisms.
- Although RARP is no longer widely used, it is still important to understand its basic principles, as it provides a historical perspective on the evolution of networking protocols. 

Mnemonics and learning tricks for RARP are not widely used or necessary, as it is a relatively simple protocol with only a few key concepts to remember.