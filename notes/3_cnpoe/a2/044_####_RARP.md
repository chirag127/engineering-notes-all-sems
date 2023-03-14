 Here is the content in markdown format about Reverse Address Resolution Protocol (RARP):

#### RARP

* RARP is a protocol used to learn the IP address of a host from its physical (MAC) address.
* It works in the opposite way as ARP which maps IP addresses to MAC addresses.
* RARP allows a diskless workstation to discover its own IP address by broadcasting its MAC address and receiving its IP address in response.
* The RARP server maintains a database that maps MAC addresses to IP addresses. When it receives a RARP request containing a MAC address, it searches this database and returns the corresponding IP address.
* RARP is not routable and is primarily used in local area networks. It has been superseded by BOOTP and DHCP which also provide additional information such as subnet mask and default gateway.

* **Mnemonic:** Remember RARP maps MAC to IP (opposite of ARP) to help a diskless workstation discover its IP address.
* **Advantages:** Provides a simple mechanism for diskless workstations to acquire IP addresses. No manual IP address configuration required.
* **Disadvantages:** Requires RARP server to maintain MAC-IP address database. Not routable and limited to LANs. Replaced by BOOTP and DHCP which provide additional features.

[Diagrams and examples could be included here if helpful for learning/reading]

The content is written in points in a formal tone with Mnemonics and learning tricks included where easy to remember. Let me know if you would like me to modify or expand the content in any way.